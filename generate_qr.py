#!/usr/bin/env python3
"""
GitHub PagesのURLからQRコードを生成するスクリプト
"""

import qrcode
from PIL import Image

def generate_qr_code(url, output_file='qrcode.png', size=10, border=4):
    """
    URLからQRコードを生成
    
    Args:
        url: QRコードにエンコードするURL
        output_file: 出力ファイル名
        size: QRコードのサイズ（各モジュールのピクセル数）
        border: ボーダーのサイズ
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QRコードを生成しました: {output_file}")
    print(f"URL: {url}")

if __name__ == "__main__":
    # GitHub PagesのURLを入力
    print("GitHub PagesのURLを入力してください")
    print("例: https://username.github.io/repository-name/")
    url = input("URL: ").strip()
    
    if not url:
        print("URLが入力されていません")
        exit(1)
    
    # URLの形式をチェック
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    
    generate_qr_code(url)

