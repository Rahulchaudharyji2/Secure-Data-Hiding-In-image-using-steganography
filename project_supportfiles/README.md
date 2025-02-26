# Secure Data Hiding in Images Using Steganography

## 📌 Project Overview
This project implements **image steganography**, a technique used to hide secret messages inside images securely. By leveraging **OpenCV, Tkinter, and NumPy**, the system allows users to encode and decode messages within an image while ensuring **password protection** for additional security.

## 🚀 Features
- **Password-Protected Steganography** – Ensures only authorized users can decrypt the hidden message.
- **User-Friendly GUI** – Simplifies message encoding and decoding using an interactive interface.
- **Pixel-Level Encoding** – Hides the message in image pixels while maintaining quality.
- **Efficient Data Hiding** – Supports dynamic message length without corrupting the image.
- **Cross-Platform Compatibility** – Works on Windows, Linux, and macOS.
- **Real-Time Encryption & Decryption** – Ensures fast and secure message hiding and retrieval.

## 🔧 Technologies Used
- **Python** – Core programming language.
- **OpenCV (cv2)** – Image processing and manipulation.
- **Tkinter** – GUI design for better usability.
- **NumPy** – Efficient handling of image data.
- **OS Module** – File handling operations.

## 🛠 Installation & Setup
### Prerequisites
Ensure you have Python installed. Install the required dependencies using:
```sh
pip install numpy opencv-python tkinter
```

### Running the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/Rahulchaudharyji2/Secure-Data-Hiding-In-image-using-steganography.git
   cd steganography-project
   ```
2. Run the script:
   ```sh
   python stego.py
   ```

## 🎯 How It Works
1. **Encryption (Hiding Message):**
   - Upload an image.
   - Enter the secret message and set a passcode.
   - Click **Encrypt** to hide the message inside the image.
   - Save the encrypted image.

2. **Decryption (Retrieving Message):**
   - Open the encrypted image.
   - Enter the correct passcode.
   - Click **Decrypt** to retrieve the hidden message.

## 🎯 End Users
- **Cybersecurity Professionals** – Secure data transmission.
- **Journalists & Whistleblowers** – Confidential communication.
- **Government & Defense Agencies** – Secure intelligence sharing.
- **Corporate Organizations** – Protection of confidential information.
- **Forensic Experts** – Investigating hidden messages in images.

## 📌 Future Enhancements
- Implement **AES encryption** for extra security.
- Support **multiple image formats** (PNG, BMP, GIF, etc.).
- Develop a **web-based** version for remote access.
- Improve **steganographic algorithms** for better invisibility.

## 📜 Conclusion
This project demonstrates an effective approach to **hiding sensitive messages inside images using steganography**. With added **password protection and an intuitive GUI**, it ensures **data security and confidentiality**. Future improvements will make it even more robust and versatile for real-world applications.

---
💡 **Contributions & Feedback are Welcome!** Feel free to fork this repository and enhance it. 🚀

