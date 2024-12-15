from PIL import Image

def main():
    # Perguntar o nome do ficheiro
    input_filename = input("file to reduce ( .bmp, .png ou .jpg): ").strip()
    
    try:
        # Abrir a imagem
        img = Image.open(input_filename)
        print(f"Imagem carregada: {input_filename} ({img.size[0]}x{img.size[1]})")
    except FileNotFoundError:
        print("File not find.")
        return
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return

    # Perguntar o novo comprimento e a nova largura
    try:
        new_width = int(input("w (px): ").strip())
        new_height = int(input("h (px) ").strip())
    except ValueError:
        print("integer only.")
        return

    if new_width <= 0 or new_height <= 0:
        print(">0.")
        return

    # Redimensionar a imagem
    try:
        resized_img = img.resize((new_width, new_height))
    except Exception as e:
        print(f"Error on riseze image: {e}")
        return

    # Criar o novo nome do ficheiro
    output_filename = "new_" + input_filename

    # Salvar a nova imagem
    try:
        resized_img.save(output_filename)
        print(f"new imagem save as: {output_filename}")
    except Exception as e:
        print(f"Error save new image: {e}")

if __name__ == "__main__":
    main()

