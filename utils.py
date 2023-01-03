from PIL import Image


def adjust_images(path1, path2):

    img1 = Image.open(path1)
    img2 = Image.open(path2)

    width1, height1 = img1.size
    width2, height2 = img2.size

    dim1 = width1 + height1
    dim2 = width2 + height2

    if (dim1 >= dim2):
        img2_resized = img2.resize((width1, height1))
        img2_resized.save(path2)
    else:
        img1_resized = img1.resize((width2, height2))
        img1_resized.save(path1)
