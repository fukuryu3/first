import argparse
import re

def extract_start_line(filename):
    match = re.search(r'(fe|be)_dump_(.*).bin', filename)
    if match:
        return int(match.group(2), 16)
    return 1

def binary_to_hex_grouped(input_files, group_size=4, group_length=8):
    for input_file in input_files:
        start_line = extract_start_line(input_file)

        with open(input_file, 'rb') as binary_file:
            binary_data = binary_file.read()
            hex_data = ''.join(format(byte, '02X') for byte in binary_data)

        grouped_hex_data = ' '.join(hex_data[i:i+group_length] for i in range(0, len(hex_data), group_length))

        formatted_data = f'{input_file}\n\n'  # ファイル名を1行目に追加
        for i, line in enumerate(range(0, len(grouped_hex_data), group_size * (group_length + 1)), start=start_line):
            formatted_data += f'{i:08X}: '  # 行数を8桁の16進数で表示
            formatted_data += ''.join(grouped_hex_data[line:line + group_size * (group_length + 1)]).rstrip()
            formatted_data += '\n'

        formatted_data += '\n'  # ファイルデータの終わりに空行を追加

        base_name = re.sub(r'\.bin$', '', input_file)
        output_file = f'{base_name}.txt'
        
        with open(output_file, 'w') as hex_output_file:
            hex_output_file.write(formatted_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert binary files to grouped hex representation.')
    parser.add_argument('input_files', nargs='+', help='Input binary file names (multiple files can be provided)')
    parser.add_argument('--group_size', type=int, default=4, help='Number of hex groups per line (default: 4)')
    parser.add_argument('--group_length', type=int, default=8, help='Number of hex characters per group (default: 8)')
    args = parser.parse_args()

    binary_to_hex_grouped(args.input_files, args.group_size, args.group_length)
