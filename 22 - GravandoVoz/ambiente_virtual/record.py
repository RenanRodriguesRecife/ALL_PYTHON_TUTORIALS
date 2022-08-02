import sounddevice
from scipy.io.wavfile import write

#tempo de gravação
fs = 44100 #frequencia
second = int(input("Quantos seguntos deseja gravar?"))

print("\nGravando......\n")

#gravação
record_voice=sounddevice.rec(int(second * fs),samplerate=fs, channels=2)
#sounddevice.wait()

#salva arquivo de gravação
write("gravacao.wav",fs,record_voice)
print("gravação finalizada!")