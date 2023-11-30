import argparse

def binary_to_hex_grouped(input_file, output_file, group_size=4, group_length=8):
    with open(input_file, 'rb') as binary_file:
        binary_data = binary_file.read()
        hex_data = ''.join(format(byte, '02X') for byte in binary_data)

    grouped_hex_data = ' '.join(hex_data[i:i+group_length] for i in range(0, len(hex_data), group_length))

    formatted_data = ''
    for i in range(0, len(grouped_hex_data), group_size * (group_length + 1)):
        formatted_data += ''.join(grouped_hex_data[i:i + group_size * (group_length + 1)]).rstrip()
        formatted_data += '\n'

    with open(output_file, 'w') as hex_output_file:
        hex_output_file.write(formatted_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert binary file to grouped hex representation.')
    parser.add_argument('input_file', help='Input binary file name')
    parser.add_argument('output_file', help='Output file name for grouped hex representation')
    parser.add_argument('--group_size', type=int, default=4, help='Number of hex groups per line (default: 4)')
    parser.add_argument('--group_length', type=int, default=8, help='Number of hex characters per group (default: 8)')
    args = parser.parse_args()

    binary_to_hex_grouped(args.input_file, args.output_file, args.group_size, args.group_length)
