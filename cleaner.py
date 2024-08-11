import pandas as pd
import os

# Mengganti 'path_to_folder' dengan lokasi folder yang berisi file CSV
folder_path = r'D:'

# Membaca semua file CSV dalam folder dan menggabungkannya menjadi satu DataFrame
all_data = pd.DataFrame()
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # Membaca kolom 'Phone' sebagai string
        df = pd.read_csv(file_path, dtype={'Phone': str})
        all_data = pd.concat([all_data, df], ignore_index=True)

# Menghapus baris yang tidak memiliki nomor telepon
cleaned_data = all_data.dropna(subset=['Phone'])

# Menghapus duplikat data
cleaned_data = cleaned_data.drop_duplicates()

# Membuat kolom 'Operator' berdasarkan prefix nomor telepon
def get_operator(phone_number):
    if not isinstance(phone_number, str):
        return 'Unknown'
    # Menghapus karakter non-digit
    phone_number = ''.join(filter(str.isdigit, phone_number))
    # Memeriksa apakah nomor telepon adalah nomor kantor
    if phone_number.startswith('022'):
        return 'Kantor'
    # Memeriksa prefix untuk operator selain "Kantor"
    prefixes = {
        'Telkomsel': ['0811', '0812', '0813', '0851', '0852', '0853', '0821', '0822', '0823'],
        'Indosat Ooredoo': ['0814', '0815', '0816', '0855', '0856', '0857', '0858'],
        'XL Axiata': ['0817', '0818', '0819', '0859', '0877', '0878', '0831', '0832', '0833', '0838', '0859'],
        'Smartfren': ['0881', '0882', '0883', '0884', '0885', '0886', '0887', '0888', '0889'],
        'Tri': ['0895', '0896', '0897', '0898', '0899'],
        'Ceria': ['0828'],
        'Byru': ['0868'],
        'NTS 3G': ['0838'],
        'Lippo': ['08135']
    }
    for operator, prefixes_list in prefixes.items():
        if any(phone_number.startswith(prefix) for prefix in prefixes_list):
            return operator
    return 'Unknown'
