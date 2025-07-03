import subprocess
import os

def run_stellarium(script_path, image_name):
    """
    Runs Stellarium with a given .ssc script and assumes it generates the screenshot.

    Args:
        script_path (str): Path to the .ssc file
        image_name (str): Name of the expected image output (e.g., 'moon.png')

    Returns:
        str: Full path to the saved image (no validation)
    """
    stellarium_exe = "D:/New folder (3)/New folder/Stellarium/stellarium.exe"
    output_dir = os.path.abspath("D:/Stellarium project/output")
    image_path = os.path.join(output_dir, image_name)

    # Remove previous file if it exists
    if os.path.exists(image_path):
        os.remove(image_path)

    print(f"[run_stellarium] Running: {script_path}")
    subprocess.run([
        stellarium_exe,
        f"--startup-script={os.path.abspath(script_path)}"
    ], check=True)

    return image_path
