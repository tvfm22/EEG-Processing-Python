import mne 
from mne.preprocessing import ICA
import matplotlib.pyplot as plt

raw = mne.io.read_raw_edf('/home/vfm22/Project/EEG-Processing-Python/Dataset/Emotiv_30s_EDF/S001/S001E04.edf', preload=True)

raw.plot(block=True, duration=10.0)

raw_filtered = raw.filter(.1, 30)

raw_filtered.plot(block=True, duration=10.0)

raw_filtered.save('/home/vfm22/Project/EEG-Processing-Python/Prepocessing/S001/raw4.fif',overwrite=True)

raw4 = mne.io.read_raw_fif('/home/vfm22/Project/EEG-Processing-Python/Prepocessing/S001/raw4.fif', preload=True)

montage = mne.channels.make_standard_montage('standard_1005')

raw4.set_montage(montage)

ica = ICA(14)

ica.fit(raw4)

raw4.plot(block=True, duration=10.0)

ica.plot_components()