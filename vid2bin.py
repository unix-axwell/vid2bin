def binary_to_text(file_path):
    with open(file_path, 'rb') as binary_file:
        binary_data = binary_file.read()

    binary_text = ''.join(format(byte, '08b') for byte in binary_data)

    with open('output.txt', 'w') as text_file:
        text_file.write(binary_text)

# Call the function with the path to your binary file
binary_to_text('input.mp3')
