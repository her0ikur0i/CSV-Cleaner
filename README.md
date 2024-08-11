# CSV-Cleaner
Cleaner for gmap


# Menghapus tanda petik satu di depan nomor telepon
cleaned_data['Phone'] = cleaned_data['Phone'].str.replace("'", "")

# Menambahkan karakter tab di depan nomor telepon agar Excel membacanya sebagai teks
cleaned_data['Phone'] = cleaned_data['Phone'].apply(lambda x: f"'{x}")

# Memanggil fungsi get_operator untuk setiap nomor telepon
cleaned_data['Operator'] = cleaned_data['Phone'].apply(lambda x: get_operator(x[1:]))

# Menyusun ulang kolom sesuai urutan yang diinginkan
column_order = ['Name', 'Phone', 'Operator', 'Website', 'Address', 'Zona', 'Category', 'Rating', 'Verified', 'Map URL']
cleaned_data = cleaned_data[column_order]

# Menyimpan hasil akhir ke dalam file CSV di folder yang sama dengan script ini dijalankan
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, 'Cleaned_Data_Bakery.csv')
cleaned_data.to_csv(output_file, index=False)

print("Pembersihan data telah selesai. Hasilnya disimpan dalam file:", output_file)


Kode ini memastikan kolom-kolom dihasilkan dalam urutan yang Anda inginkan dan menyimpan hasilnya dalam file CSV dengan nama Cleaned_Data_Bakery.csv.
