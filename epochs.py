import mne
import matplotlib.pyplot as plt

filename = r'datasets\02F6BC66\EEG_ExperimentBlock.HONEST_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)

print(raw.info)
print(raw.ch_names)

raw.crop(tmin=0.0, tmax=1.0)


def evoked():
    eeg_evoked = mne.preprocessing.create_eog_epochs(raw).average()
    eeg_evoked.plot_joint()


def epochs_find():
    data, times = raw.get_data(return_times=True)
    
    data = data * 1e6

    events = mne.find_events(raw, stim_channel='Digital')

    print(events)

    stim_picks = mne.pick_types(raw.info, stim=True)
    stim_names = [raw.info['ch_names'][i] for i in stim_picks]
    print("Stim channels:", stim_names)

    print(stim_picks)

    print(events)



evoked()