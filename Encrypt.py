import cv2
import os

def encrypt_image(image_path, msg, password):
    img = cv2.imread(image_path)

    d = {}
    for i in range(256):
        d[chr(i)] = i

    n = 0
    m = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        z = (z + 1) % 3
        if z == 0:
            m = (m + 1) % img.shape[1]
            if m == 0:
                n = (n + 1) % img.shape[0]

    encrypted_image_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_image_path, img)
    os.system("start " + encrypted_image_path)

    

if __name__ == "__main__":
    image_path = "mypic.jpg"  # Replace with the correct image path
    msg = input("Enter secret message:")
    with open("message.txt", "w") as f:
        f.write(msg)
    password = input("Enter a passcode:")
    encrypt_image(image_path, msg, password)
