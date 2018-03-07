#!/usr/bin/python3


import pyaudio


class AudioIn(pyaudio.PyAudio):

    # Class init function
    def __init__(self):

        # Initialize base
        pyaudio.PyAudio.__init__(self)

        # Constant definitions
        self.BUFFER_SIZE = 1024
        self.SAMPLE_FREQUENCY = 48100
        self.NUMBER_OF_CHANNELS = 1

        # Member variable initialization
        # TODO
        self.timeToRecord = 2 # TODO Remove

    # Function to open and start stream
    def StartStream(self):

        # Initialize the audio input stream
        self.mAudioStream = self.open(format=pyaudio.paInt16, #pyaudio.paInt16,
                                      channels=self.NUMBER_OF_CHANNELS,
                                      rate=self.SAMPLE_FREQUENCY,
                                      input=True,
                                      output=True, # TODO Remove
                                      frames_per_buffer=self.BUFFER_SIZE)

        # ---- TODO Remove all of this
        print("* recording")

        for i in range(0, int(self.SAMPLE_FREQUENCY / self.BUFFER_SIZE * self.timeToRecord)):
            data = self.mAudioStream.read(self.BUFFER_SIZE)
            self.mAudioStream.write(data, self.BUFFER_SIZE)

        print("* done")

        self.mAudioStream.stop_stream()
        self.mAudioStream.close()

        self.terminate()
        # ----
