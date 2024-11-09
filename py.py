import random
import string
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import messagebox

def generate_captcha_text(length=5):
    """Gera um texto aleatório para o CAPTCHA."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_captcha_image(text):
    """Gera uma imagem CAPTCHA a partir do texto dado."""
    width, height = 200, 80
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Fonte e posição do texto
    font = ImageFont.truetype("arial.ttf", 40)
    text_position = (30, 15)
    
    # Adiciona o texto à imagem
    draw.text(text_position, text, font=font, fill='black')

    # Adiciona ruído (linhas)
    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line(((x1, y1), (x2, y2)), fill="gray", width=2)

    # Salva a imagem CAPTCHA
    image.save("captcha.png")

def verify_captcha():
    """Verifica se o texto digitado corresponde ao texto do CAPTCHA."""
    user_input = entry.get()
    if user_input == captcha_text:
        messagebox.showinfo("Sucesso", "CAPTCHA verificado com sucesso!")
    else:
        messagebox.showerror("Erro", "Texto incorreto. Tente novamente.")

# Gera o texto e a imagem do CAPTCHA
captcha_text = generate_captcha_text()
generate_captcha_image(captcha_text)

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("CAPTCHA com Imagem")
root.geometry("300x200")

# Instrução
instruction_label = tk.Label(root, text="Digite o texto do CAPTCHA:")
instruction_label.pack(pady=10)

# Exibe a imagem do CAPTCHA
captcha_image = tk.PhotoImage(file="captcha.png")
captcha_label = tk.Label(root, image=captcha_image)
captcha_label.pack()

# Campo de entrada do usuário
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

# Botão para verificar o CAPTCHA
verify_button = tk.Button(root, text="Verificar", command=verify_captcha)
verify_button.pack(pady=10)

# Executa a GUI
root.mainloop()
