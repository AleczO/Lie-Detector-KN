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



filename = r'.\datasets\SDF673HF\EEG_ExperimentBlock.HONEST_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)


proc = DataPreprocessor()
proc.process(raw, 1e-8)


ica = mne.preprocessing.ICA(random_state=97, max_iter="auto", n_components=None)
ica.fit(raw)

ica.plot_sources(raw)
raw.plot(block=True)

events, event_dict = mne.events_from_annotations(raw)


ica.plot_components()

#ica.plot_properties(raw)