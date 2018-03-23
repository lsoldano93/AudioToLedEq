# AudioToLEDEq

## Goal

Obtain input audio in real-time in order to illuminate a responsive LED system in a variety of customizable patterns, which correlate to the frequencies band-passed from the input source. This goal will be achieved in Python in order to be runnable on a Raspberry Pi, which will use its output pins to light external LED strips.

### Requirements

1. This system should read in live audio with minimal latency
   i. This will allow for an LED system, which appears to respond to live audio in "real-time"
2. Quickly convert the audio to the frequency-domain and pass the converted stream through a customizable number of bandpass filters which will encompass the entire audible spectrum
   i. This will allow for "real-time" lighting in a way that allows for different lighting detail so as not to hamstring the system with a limited number of "visible" bands
3. Pass the filtered information to a customizable, LED manager which can determine the proper lighting arrangement according to the input
   i. This manager will be aware of the available lights and will allow for different reactions to the audio so as not to limit the creativity of response methods
4. Abstract the detail of how power should be distributed to the used LEDs such that said LEDs can be switched out with different models so long as new APIs are written for these models
   i. This will allow for any LED models to be used without the hacking of other pieces of the code

## Getting Started

### Items to Install Before Running:

PyAudio
https://people.csail.mit.edu/hubert/pyaudio/

NumPy
http://www.numpy.org/

OSX Installation:

brew install portaudio

pip install pyaudio

pip install numpy

## Setting Up Your System

TODO

## Configuring the Code for Your System

TODO

## Running the Code

TODO

## Demo

TODO

## Thanks To:

https://www.swharden.com/wp/2013-05-09-realtime-fft-audio-visualization-with-python/
