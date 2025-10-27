import mne
import matplotlib.pyplot as plt

filename = r'datasets\SDF673HF\EEG_ExperimentBlock.DECEITFUL_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)


raw.crop(tmin=0.0, tmax=100.0)

def notch_filter_processing():
    
    raw.load_data().filter(l_freq=1.5, h_freq=100.0, fir_design='firwin')

    eeg_picks = mne.pick_types(raw.info, eeg=True)
    raw.load_data().notch_filter(freqs=[50, 100], picks=eeg_picks)

    raw.load_data()
    raw.apply_function(lambda v: v * 1e-8)





def epochs_evoked_construct():

    events, event_dict = mne.events_from_annotations(raw)

    picked = mne.pick_events(events, exclude=[1,2])

    epochs = mne.Epochs(raw, picked, tmin=-0.01, tmax=1.0)

    epochs.plot()
    mne.viz.plot_events(picked, sfreq=raw.info["sfreq"])


    evoked = epochs.average()
    evoked.plot()



notch_filter_processing()

epochs_evoked_construct()
