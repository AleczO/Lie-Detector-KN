import mne
import matplotlib.pyplot as plt

def filter_data(raw):
    raw.load_data().filter(l_freq=1.0, h_freq=90, fir_design='firwin')

    eeg_picks = mne.pick_types(raw.info, eeg=True)
    raw.load_data().notch_filter(freqs=[50.], picks=eeg_picks)

    return raw


def scale_data(raw, c):
    raw.load_data()
    raw.apply_function(lambda v: v * c)
    
    return raw



def plot_data(raw):
    raw.compute_psd().plot()
    raw.compute_psd(fmax=125).plot(average=True, amplitude=False, picks="data", exclude="bads")

    raw.plot(block=True)



filename = r'datasets\SDF673HF\EEG_ExperimentBlock.HONEST_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)


raw = filter_data(raw)
raw = scale_data(raw, 1e-8)


plot_data(raw)