
import subprocess
import os
import sys

def generate_pdf():
    # Dosya isimleri
    input_file = "OSA_Growth_Intelligence_Overview.md"
    output_pdf = "OSA_Growth_Intelligence_Overview.pdf"

    print(f"📄 İşleniyor: {input_file}...")

    # 1. PDF Üretimi (LaTeX motoru kullanarak)
    # Bu komut arka planda LaTeX kullanır, size profesyonel çıktı verir.
    # Markdown (Basit Metin) -> PDF (Profesyonel Görünüm)
    cmd_pdf = [
        "pandoc",
        input_file,
        "-o", output_pdf,
        "--pdf-engine=pdflatex",
        "--highlight-style=tango",
        "-V", "geometry:a4paper,portrait,margin=2cm",
        "-V", "lang=tr"
    ]

    try:
        print("⚙️  PDF oluşturuluyor... (OSA Overview)")
        subprocess.run(cmd_pdf, check=True)
        print(f"✅ Başarılı: {output_pdf}")

    except subprocess.CalledProcessError as e:
        print("❌ Hata oluştu!")
        print(e)
    except FileNotFoundError:
        print("❌ Hata: 'pandoc' komutu bulunamadı. Lütfen Pandoc yüklü olduğundan emin olun.")

if __name__ == "__main__":
    generate_pdf()
