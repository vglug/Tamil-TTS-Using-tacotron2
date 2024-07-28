# Tamil TTS Using Tacotron 2
The main goal of this project is building the Tamil TTS using Tacotron 2.


## Pre-requisites
1. NVIDIA GPU + CUDA cuDNN

## Setup
1. Download and extract the [Common Voice Dataset] https://commonvoice.mozilla.org/ta/datasets
2. Clone this repo: `git clone https://github.com/vglug/Tamil-TTS-Using-tacotron2.git`
3. Create a input text file with the path of the audio files and the sentence of the audio
4. Install [PyTorch 1.0]
5. Install [Apex]
6. Install python requirements or build docker image 
    - Install python requirements: `pip install -r requirements.txt`

## Training
1. `python train.py --output_directory=outdir --log_directory=logdir`
2. (OPTIONAL) `tensorboard --logdir=outdir/logdir`

## Inference demo
1. Give your tained model 
2. Download [WaveGlow] model
3. `jupyter notebook --ip=127.0.0.1 --port=31337`
4. Load inference_for_tamil_language.ipynb
5. Execute the steps one by one in the final step you will the audio of the given text


## Related repos
[WaveGlow](https://github.com/NVIDIA/WaveGlow) Faster than real time Flow-based
Generative Network for Speech Synthesis

[nv-wavenet](https://github.com/NVIDIA/nv-wavenet/) Faster than real time
WaveNet.

## Acknowledgements
This implementation uses code from the following repos: [Keith
Ito](https://github.com/keithito/tacotron/), [Prem
Seetharaman](https://github.com/pseeth/pytorch-stft) as described in our code.

We are inspired by [Ryuchi Yamamoto's](https://github.com/r9y9/tacotron_pytorch)
Tacotron PyTorch implementation.

We are thankful to the Tacotron 2 paper authors, specially Jonathan Shen, Yuxuan
Wang and Zongheng Yang.


[WaveGlow]: https://drive.google.com/open?id=1rpK8CzAAirq9sWZhe9nlfvxMF1dRgFbF
[Tacotron 2]: https://drive.google.com/file/d/1c5ZTuT7J08wLUoVZ2KkUs_VdZuJ86ZqA/view?usp=sharing
[pytorch 1.0]: https://github.com/pytorch/pytorch#installation
[website]: https://nv-adlr.github.io/WaveGlow
[ignored]: https://github.com/NVIDIA/tacotron2/blob/master/hparams.py#L22
[Apex]: https://github.com/nvidia/apex
[AMP]: https://github.com/NVIDIA/apex/tree/master/apex/amp
