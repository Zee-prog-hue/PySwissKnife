import speedtest
import time
import itertools
import sys
import threading

# Frames for a triangle-like dot animation
frames = [
    "•     ",
    " •    ",
    "  •   ",
    " •    ",
]

spinner_running = False

def triangle_spinner(delay=0.2):
    for frame in itertools.cycle(frames):
        if not spinner_running:
            break
        sys.stdout.write("\rLoading " + frame)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\rDone!     \n")

def run_with_spinner(func, *args, **kwargs):
    global spinner_running
    spinner_running = True
    spinner_thread = threading.Thread(target=triangle_spinner)
    spinner_thread.start()

    # Run the actual function (blocking)
    result = func(*args, **kwargs)

    # Stop spinner
    spinner_running = False
    spinner_thread.join()
    return result

# --- Usage ---
st = speedtest.Speedtest()

print("Getting best server...")
run_with_spinner(st.get_best_server)

print("Testing download speed...")
download_speed = run_with_spinner(st.download) / 1_000_000
print(f"Download Speed: {download_speed:.2f} Mbps")

print("Testing upload speed...")
upload_speed = run_with_spinner(st.upload) / 1_000_000
print(f"Upload Speed: {upload_speed:.2f} Mbps")

print("Testing ping...")
ping = st.results.ping
print(f"Ping: {ping:.2f} ms")
