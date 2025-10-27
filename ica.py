import mne
import processing as proc

filename = r'datasets\SDF673HF\EEG_ExperimentBlock.HONEST_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)


raw = proc.preprocessing(raw, 1e-8)


ica = mne.preprocessing.ICA(random_state=97, max_iter="auto", n_components=None)
ica.fit(raw)


ica.plot_sources(raw, block=True)


#ica.plot_properties(raw)