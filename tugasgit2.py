user = [
    {'nama': 'arsene lupin', 'nik': 1234, 'jenis_kelamin': 'male', 'tanggal_lahir': '1902-03-23'},
    {'nama': 'sherlock holmes', 'nik': 4321, 'jenis_kelamin': 'male', 'tanggal_lahir': '1876-08-16'},
    {'nama': 'irene adler', 'nik': 6789, 'jenis_kelamin': 'female', 'tanggal_lahir': '1884-10-07'}
]


user_input = input("Masukkan nama yang hendak dicari:")

# jika apa yang diinout user ada maka tampilkan seluruh data. jika tidak ada maka "data kosong"

if user_input in user :
    print ("nama yang dicari adalah",user[user_input])
else :
    print ((user), 'nama tidak ada')


