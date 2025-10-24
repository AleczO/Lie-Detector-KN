import mne

filename = r'datasets\2D663E30\EEG_ExperimentBlock.DECEITFUL_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)

raw.crop(tmin=0.0, tmax=200.0)
# raw.notch_filter(freqs=[50., 60.], notch_widths=2.0)


def notch_filter_processing():
    eeg_picks = mne.pick_types(raw.info, eeg=True)

    raw.load_data().notch_filter(freqs=[50., 60.], picks=eeg_picks)
    raw.load_data().notch_filter(freqs=[100., 110.], picks=eeg_picks)

    raw._data = raw.get_data() / 1e7

    raw.compute_psd().plot()
    raw.plot(block=True)


def no_processing():
    raw._data = raw.get_data()
    
    raw.compute_psd().plot()
    raw.plot(block=True)


no_processing()

# raw_notch = raw.copy().

#raw_notch._data = raw_notch.get_data() / 1e8

#raw.load_data().filter(l_freq=70., h_freq=120., method='iir', fir_design='firwin')



#raw_notch.plot(block=True)

#raw.plot(block=True)