import cv2
from skimage import io

# Get rectangles
def detectFaces(url):

    # Create a cascadeClassifier Object
    face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

    image = io.imread(url)
    height, width = image.shape[0:2]
    print(height, width)

    # Color correction from BGR2RBG: scikit-image and opencv difference
    cc_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reading the image as gray scale image
    gray_image = cv2.cvtColor(cc_image, cv2.COLOR_BGR2GRAY)

    # Search the co-ordinates of the image
    faces = face_cascade.detectMultiScale(
        gray_image, scaleFactor=1.05, minNeighbors=5)

    faceRectangles = convertToRatio(height, width, faces)
    # print(faceRectangles)
    return faceRectangles
    
    # print(type(faces))
    # print(faces)

    # for x, y, w, h in faces[0:1]:
    #     cc_image = cv2.rectangle(
    #         cc_image, (x, y), (x+w, y+h), (255, 150, 100), 4)

    # resized = cv2.resize(cc_image, (650, 500))
    # cv2.imshow("Gray", resized)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# Convert to percentages
def convertToRatio(height, width, faces):
    faceRectangles = []
    for x, y, w, h in faces:
        faceRectangles.append({
            'left_col': (x) / width,
            'right_col': (x + w) / width,
            'top_row': (y) / height,
            'bottom_row': (y + h) / height,
        })
    return faceRectangles


# imgUrl = "https://www.sciencenewsforstudents.org/wp-content/uploads/2019/11/860_main_beauty.png"
# detectFaces(imgUrl)