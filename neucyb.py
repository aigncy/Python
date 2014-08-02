import neuron
from neuron import h


# most NEURON specific commands start with `neuron.h.`

# Creating the morphology
# =======================
soma = h.Section()
soma.Ra = 1
soma.L = 40 # um; stored as a float number
soma.diam = 20 # um
soma.nseg = 10 # stored as an integer

# contralateral dendrite
dend_contra = h.Section()
dend_contra.Ra = 1
dend_contra.L = 150
dend_contra.diam = 3
dend_contra.nseg = int(dend_contra.L/10)

# ipsi lateral dendrite
dend_ipsi = h.Section()
dend_ipsi.Ra = 1
dend_ipsi.L = 150
dend_ipsi.diam = 3
dend_ipsi.nseg = int(dend_ipsi.L/10)

dend_contra.connect(soma, 1, 0) # connect soma(1) with dend_contra(0)
dend_ipsi.connect(soma, 0, 0) # connect soma(0) with dend_ipsi(0)

# Implementing a current clamp electrode
# ======================================

# Locate the electrode at the center of the soma
stim = h.IClamp(soma(0.5))

# Setting recording paradigm
stim.delay = 1
stim.amp = 1
stim.dur = 3


# You can play with the NEURON-gui by typing
# >>> from neuron import gui
# For an overview (gui menu bar): Tools -> Model View -> 1 real cell -> root...

# Record Time from NEURON (neuron.h._ref_t)
rec_t = h.Vector()
rec_t.record(h._ref_t)
# Record Voltage from the center of the soma
rec_v = h.Vector()
rec_v.record(soma(0.5)._ref_v)

h.finitialize(-60)

neuron.init()
neuron.run(5)

# Plot the recordings with matplotlib
# ===================================

import matplotlib.pyplot as plt

# get values from NEURON-vector format into Python format
times = [] # Use list to add another trace later.
voltages = []
times.append(list(rec_t)) # alternativ to `list(rec_t)`: `numpy.array(rec_t)`
voltages.append(list(rec_v))

# Do for each section (here: soma, dend_contra, dend_ipsi):
for sec in h.allsec():
  # Do with the present `sec`
  sec.insert('pas')
  sec.Ra = 200
  # Do for each segment within `sec`:
  for seg in sec:
    # Do with the segment `seg`:
    seg.pas.g = 0.002
    seg.pas.e = -60

h.finitialize(-60)
neuron.init()
neuron.run(5)

times.append(list(rec_t))
voltages.append(list(rec_v))
fig = plt.figure()
for time, voltage in zip(times, voltages):
  plt.plot(time, voltage)
plt.title("Hello World")
plt.xlabel("Time [ms]")
plt.ylabel("Voltage [mV]")
plt.axis(ymin=-70, ymax=0)
traces = ['no channels', 'passive channels']
plt.legend(traces, loc='best')
plt.show()
