from urllib.parse import urlparse
import base64
from io import BytesIO
import streamlit as st
import qrcode

def generate_qr_code(input_data):
    """Generates a QR code
    in: Youtube link
    out: PIL image
    """
    qr = qrcode.QRCode(version=1,box_size=5,border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img
    
def get_image_download_link(img):
    """Generates a link allowing the PIL image to be downloaded
    in:  PIL image
    out: href string
    """
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}" download="qrcode.jpg" >Download QR Code</a>'
    return href

def is_url(url):
    """
    Checks if a given string is a url
    in: sring
    out: url status (boolean)
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def main():
    st.sidebar.title("3 easy steps:")
    st.sidebar.markdown("1. Enter the Youtube link in the box")
    st.sidebar.markdown("2. Click press to get QR code")
    st.sidebar.markdown("3. Download and print the QR Code")
    st.title("Youtube QR link Generation")
    input_data = st.text_input("Enter Youtube link here")
    if is_url(input_data):
        if st.button("Press to get QR code"):
            img = generate_qr_code(input_data)
            st.markdown(get_image_download_link(img), unsafe_allow_html=True)
            st.info("QR Code Generated")
        
if __name__ == "__main__":
    main()