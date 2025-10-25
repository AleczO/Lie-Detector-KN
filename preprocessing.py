import mne
import matplotlib.pyplot as plt

#filename = r'datasets\SDF673HF\EEG_ExperimentBlock.DECEITFUL_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
filename = r'datasets\SDF673HF\EEG_ExperimentBlock.HONEST_RESPONSE_TO_TRUE_IDENTITY_raw.fif'
raw = mne.io.read_raw_fif(fname=filename)



def notch_filter_processing():
    eeg_picks = mne.pick_types(raw.info, eeg=True)


    raw.load_data().filter(l_freq=1.0, h_freq=None)
    raw.load_data().filter(l_freq=0.5, h_freq=45, fir_design='firwin')


    raw.load_data().notch_filter(freqs=[50.], picks=eeg_picks)

    raw.load_data()
    raw.apply_function(lambda v: v * 1e-8)


    raw.compute_psd().plot()
    raw.compute_psd(fmax=125).plot(average=True, amplitude=False, picks="data", exclude="bads")

    raw.plot(block=True)

    

def no_processing():
    raw.load_data()
    raw.apply_function(lambda v: v )
    
    raw.compute_psd().plot()
    raw.plot(block=True)


notch_filter_processing()


