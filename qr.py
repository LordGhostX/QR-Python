import sys
from requests import get

def generate_qr(link, size="", path=""):
    try:
        if path == "":
            path = link + ".png"
        if size == "":
            size = 200

        link = "https://" + link

        img_data = get("http://chart.apis.google.com/chart?cht=qr&chl={link}&chs={size}x{size}".format(link=link, size=size)).content

        with open(path, "wb") as f:
            f.write(img_data)

        return True
    except:
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        link = sys.argv[1]

        if len(sys.argv) > 2:
            size = sys.argv[2]
        else:
            size = ""

        if len(sys.argv) > 3:
            path = sys.argv[3]
        else:
            path = ""
    else:
        link = input("Enter Destination URL: ")
        size = input("Enter image size in px (Leave empty for 200px): ")
        path = input("Enter Filename (Leave empty for site name): ")

    if generate_qr(link, size, path):
        print("QR generated successfully!")
    else:
        print("Error generating QR!")
