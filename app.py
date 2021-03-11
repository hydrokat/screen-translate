from dearpygui import core, simple
from vidgear.gears import ScreenGear
from dearpygui import core, simple
import cv2
import pyautogui

def stop_stream(sender, data):
    # close output window
    cv2.destroyAllWindows()

    # safely close video stream
    stream.stop()

    #close preview window
    delete_item("Stream Feed")

# open video stream with default parameters

def start_stream():
    stream = ScreenGear(monitor=1, logging=True).start()

    image = None
    with simple.window("Stream Feed"):
        core.add_button("Stop Stream", callback=stop_stream)

        # loop over
        while True:

            # read frames from stream
            frame = stream.read()

            # check for frame if Nonetype
            if frame is None:
                break

            # {do something with the frame here}

            # Show output window
            # cv2.imshow("Output Frame", frame)
            image = pyautogui.screenshot("img_cap.png")
            core.add_image("canvas", "img_cap.png")

            # check for 'q' key if pressed
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                stop_stream
                break

with simple.window("Controls"):
    core.add_button("Start", callback=start_stream)
    core.add_button("Stop", callback=stop_stream)

core.start_dearpygui()
