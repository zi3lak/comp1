from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Updated computer parts data with image URLs
    computer_parts = [
        {'name': 'IPS', 'description': 'Asrock 27" Challenger Gaming Monitor', 'specs': 'IPS, 1920 x 1080, 1ms (MPRT), 100Hz, sRGB 99%, Eye Care, FreeSync, VESA', 'image': 'https://www.spire.co.uk/images/product/TFT27ARCL27FF_2.jpg'},
        {'name': 'CIT', 'description': 'Galaxy Gaming Case w/ Glass Side', 'specs': 'Front LED Strip, Rear RGB Fan, LED Button - 13 Modes, White', 'image': 'https://www.spire.co.uk/images/product/CAA-SPIMT038.jpg'},
        {'name': 'CPU', 'description': 'Intel Core i3', 'specs': '4-core, 3.3 GHz', 'image': 'https://www.spire.co.uk/images/product/I3-12100.jpg'},
        {'name': 'ATX', 'description': 'Asrock H610M-HVS', 'specs': 'Intel H610, 1700, Micro ATX, 2 DDR4, VGA, HDMI, PCIe4', 'image': 'https://www.spire.co.uk/images/product/ASMBH610MHVS_4.jpg'},
        {'name': 'GPU', 'description': 'Asus RTX 4060', 'specs': '8GB GDDR6X', 'image': 'https://www.spire.co.uk/images/product/NVRTX4060X8ASDUALOCW_14.jpg'},
        {'name': 'K&M', 'description': 'Logitech MK120', 'specs': 'Wired Keyboard and Mouse Desktop Kit, USB, Low Profile', 'image': 'https://www.spire.co.uk/images/product/KBDESK-LOMK120.jpg'},
        {'name': 'RAM', 'description': 'Kingston Fury', 'specs': '32GB (2x16GB) DDR4', 'image': 'https://www.spire.co.uk/images/product/D432G32KFBB16K2R_1.jpg'},
        {'name': 'SSD', 'description': 'Netac 480GB', 'specs': 'SSD, 2.5", SATA3, 3D NAND, R/W 520/450 MB/s, 7mm', 'image': 'https://www.spire.co.uk/images/product/SSD-480NESA500.jpg'},
        {'name': 'PSU', 'description': '500W ATX', 'specs': '80+ Bronze, Fluid Dynamic Ultra-Quiet Fan', 'image': 'https://www.spire.co.uk/images/product/PSU-500VID80BRONZE.jpg'},
        {'name': 'MSW', 'description': 'Microsoft Windows', 'specs': 'Windows 11 Home 64-bit, OEM DVD, Single Copy', 'image': 'https://www.spire.co.uk/images/product/MSW1164_2.jpg'},
        # Add more parts as needed
    ]
    return render_template('index.html', parts=computer_parts)

@app.route('/buy')
def buy():
    return render_template('buy.html')

if __name__ == '__main__':
    app.run(debug=True)

