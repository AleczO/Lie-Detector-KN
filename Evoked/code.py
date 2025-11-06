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


class EpochsProcessor:
    def create(self, raw):
        events, event_dict = mne.events_from_annotations(raw)

        picked = mne.pick_events(events, exclude=[1,2])
        epochs = mne.Epochs(raw, picked, tmin=-0.05, tmax=2.5)

        return epochs
    
    #def plot_epochs(raw):
    #   epochs.plot()
    #   mne.viz.plot_events(picked, sfreq=raw.info["sfreq"])



def extra_info():
    raw.plot_sensors(show_names=True)
    fig = raw.plot_sensors("3d", block=True)



filename = r'.\datasets\SDF673HF\EEG_ExperimentBlock.HONEST_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)

proc = DataPreprocessor()
proc.process(raw, 1e-8)


eproc = EpochsProcessor()
epochs = eproc.create(raw)


evoked = epochs.average()

evoked.plot_topomap(times=[0.741], average=0.05)
evoked.plot(spatial_colors=True)


evoked.plot(gfp=True)