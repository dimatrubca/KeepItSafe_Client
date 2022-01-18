import pyotp
import qrcode
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

secret = pyotp.random_base32()

totp = pyotp.TOTP(secret)

uri = totp.provisioning_uri(name='dimatrubca@google.com', issuer_name='Keep it safe')

print('Uri:', uri)
print("Current OTP:", totp.now())

def generate_otp(secret):
    totp = pyotp.TOTP(secret)

    return totp.now()


def get_random_secret():
    return pyotp.random_base32()


def generate_qr_image(secret, name):
    totp = pyotp.TOTP(secret)

    uri = totp.provisioning_uri(name=name, issuer_name='KeepItSafe')

    pil_image = generate_qr_code(uri)

    return pil_image

    # # Link for website
    # input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"
    # #Creating an instance of qrcode



def generate_qr_code(uri):
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(uri)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    #data = img.tobytes("raw", "RGB")
    #print(data)
    print(type(img))
    img.save('qrcode001.png')

    return img