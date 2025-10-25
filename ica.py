import mne

filename = r'datasets\SDF673HF\EEG_ExperimentBlock.HONEST_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)

def notch_filter_processing():
    

    #raw.load_data().filter(l_freq=1.0, h_freq=None)
    raw.load_data().filter(l_freq=1.5, h_freq=100.0, fir_design='firwin')

    eeg_picks = mne.pick_types(raw.info, eeg=True)
    raw.load_data().notch_filter(freqs=[50, 100], picks=eeg_picks)

    raw.load_data()
    raw.apply_function(lambda v: v * 1e-7)


    #raw.compute_psd().plot()
    raw.compute_psd(fmax=125).plot(average=True, amplitude=False, picks="data", exclude="bads")

    raw.plot(block=True)


notch_filter_processing()

ica = mne.preprocessing.ICA(random_state=97, max_iter="auto", n_components=16)
ica.fit(raw)




ica.plot_properties(raw)