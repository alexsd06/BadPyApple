import cv2
import os
def extract_frames():
    source = cv2.VideoCapture(os.path.join('video', 'bad_apple.mp4'))
    length = 0
    if os.path.exists('frames') == False:
        os.mkdir('frames')
    while True:
        try:
            length += 1
            ret, img = source.read()
            if ret == False:
                break
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join("frames", str(int(length)) + ".png"), gray)
            cv2.imshow("Live", gray)
            key = cv2.waitKey(1)
        except:
            pass
        if key == ord("q"):
            break
    # closing the window
    cv2.destroyAllWindows()
    source.release()
if __name__=="__main__":
    extract_frames()