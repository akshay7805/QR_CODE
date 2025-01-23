import qrcode
import PIL
input_url="https://www.youtube.com/watch?v=xcfFv3GldUs"
qr= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
    )
qr.add_data(input_url)

qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("backbone_qr.png")
print(qr.data_list)

