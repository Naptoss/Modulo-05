import os
import fnmatch
import sys

if sys.platform == "linux":
    comando_ffmpeg = 'ffmpeg'

else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'


codec_video = 'libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = ''
caminho_destino = ''
