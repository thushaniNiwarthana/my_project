import cv2

def decrypt_image(image_path, password, entered_password):
    if password != entered_password:
        print("YOU ARE NOT auth")
        return

    img = cv2.imread(image_path)

    c = {}
    for i in range(256):
        c[i] = chr(i)

    with open("message.txt", "r") as f:
        msg = f.read()

    

    print("Decryption message:", msg)

if __name__ == "__main__":
    image_path = "encryptedImage.jpg"  # Replace with the correct image path
    password = input("Enter the original passcode:")
    entered_password = input("Enter passcode for Decryption:")
    decrypt_image(image_path, password, entered_password)
