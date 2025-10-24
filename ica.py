import mne

filename = r'datasets\02F6BC66\EEG_ExperimentBlock.HONEST_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)

ica = mne.preprocessing.ICA(random_state=97, max_iter=200)
ica.fit(raw)

ica.plot_properties(raw)