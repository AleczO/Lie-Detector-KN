import mne


class DataPreprocessor:
    def filter(self, raw):
        raw.load_data().filter(l_freq=1.0, h_freq=90, fir_design='firwin')

        eeg_picks = mne.pick_types(raw.info, eeg=True)
        raw.load_data().notch_filter(freqs=[50.], picks=eeg_picks)

        return raw
    

    def scale(self, raw, c):
        raw.load_data()
        raw.apply_function(lambda v: v * c)
        
        return raw
    

    def process(self, raw, c):
        self.filter(raw)
        self.scale(raw, c)



def epochs(raw):

    events, event_dict = mne.events_from_annotations(raw)

    picked = mne.pick_events(events, exclude=[1,2])
    epochs = mne.Epochs(raw, picked, tmin=-0.05, tmax=2.5)

    epochs.plot()
    mne.viz.plot_events(picked, sfreq=raw.info["sfreq"])


    evoked = epochs.average()
    evoked.plot()


filename = r'datasets\SDF673HF\EEG_ExperimentBlock.DECEITFUL_RESPONSE_TO_TRUE_IDENTITY_raw.fif'

raw = mne.io.read_raw_fif(fname=filename)
# raw.crop(tmin=0.0, tmax=100.0)