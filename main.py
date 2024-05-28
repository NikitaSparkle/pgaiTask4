import qrcode
import os

def create_qr_code(url):
    # Створення QR-коду
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Шлях до папки завантажень
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Перевірка, що папка завантажень існує
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)

    # Ім'я файлу
    filename = os.path.join(downloads_folder, "qr_code.png")

    # Збереження зображення
    img.save(filename)

    print(f"QR-код збережено у {filename}")

# Отримання лінку
url = input("Введіть URL для створення QR-коду: ")
create_qr_code(url)
