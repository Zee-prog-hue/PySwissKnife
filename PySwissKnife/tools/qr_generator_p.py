import qrcode
from qrcode.exceptions import DataOverflowError

def generate_qr(data: str, file_path: str = "qr_code.png", box_size: int = 10, border: int = 5):
    """
    Generates a QR code image from the given data.

    :param data: The text or URL to encode in the QR code.
    :param filename: Output file name (PNG format recommended).
    :param box_size: Size of each QR code box (pixels).
    :param border: Border thickness (boxes).
    """
    try:
        if not data.strip():
            raise ValueError("Data for Qr Code cannot be empty.")
        
        # generate qr object
        qr = qrcode.QRCode(
            version=None, # automatic version
            error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # create qr image and save it
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)
        print(f"QR code generated and saved to {file_path}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except TypeError as te:
        print(f"Type Error: {te}")
    except DataOverflowError:
        print("Error: The provided data is too large to fit in a QR code.")
    except Exception as e:
        print(f"An error occurred: {e}") 

