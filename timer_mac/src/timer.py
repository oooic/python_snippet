import time
import subprocess
from pathlib import Path
fdir = Path(__file__)
sound_path = fdir.parent.resolve().parent / "data" / "Onmtp-Ding05-1.mp3"
sound_command = [
    f"afplay {sound_path}",
]
subprocess.run("clear", shell=True)
input("Press ⏎")
subprocess.run("clear", shell=True)
start_time = time.time()
flags = [True, True]
beeptimes = [60 * 6, 60 * 7]
while True:
    diff = time.time() - start_time
    for i in range(len(beeptimes)):
        if flags[i] and diff > beeptimes[i]:
            subprocess.Popen(sound_command, shell=True)
            flags[i] = False
    print(f"\r{int(diff//60)}:{int(diff%60):0>2}", end="")
