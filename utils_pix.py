import qrcode
import io

def generar_qr_pix(chave_pix: str, valor: float, desc: str = "Diario Elite"):
    # Genera un QR code básico con la clave Pix
    data = f"PIX:{chave_pix}|VALOR:{valor:.2f}|DESC:{desc}"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer
  
