import pymongo, pprint

# 1. Define alamat server (mongodb://namaServer:Port/)
dbURL = "mongodb://localhost:27017"

# 2. Define client
myMongo = pymongo.MongoClient(dbURL)

# 3. Show database
dbs = myMongo.list_database_names()

# 4. Untuk melihat collections, kita harus masuk / memilih Database
myDB = myMongo["HRD"].list_collection_names()

# 5. Select collection. Hasil dari .find() adalah object, maka untuk menampilkan harus pakai filter()
# Selain list, untuk menampilkan hasil dari .find() juga bisa di loop terhada col.find() nya.
myCol = list(myMongo["HRD"]["Employee"].find())

# 6. Membuat database baru sama seperti calling collections, hanya saja pastikan nama db tersebut belum ada
newDB = myMongo["Penjualan"]

# 7. Membuat collection baru sama seperti membuat database baru, pastikan nama collcetions belum ada
newCol = newDB["staff"]

# 8. Memasukkan data baru ke dalam collection. Jika satu data maka formatnya dict, kalau banyak list
# data = [{
#     "NIK" : "123AC",
#     "nama" : "Rossi",
#     "kota" : "Bandung",
#     "usia" : 23
# },
# {
#     "NIK" : "647UI",
#     "nama" : "Joko",
#     "kota" : "Malang",
#     "usia" : 32
# }]

# x = newCol.insert_many(data) ## pakai insert_many untuk memasukkan banyak item dan pakai list

# print("Data submitted, with ID : ", x.inserted_id) # ==> inserted_id untuk memunculkan ID ketika data awal baru dimasukkan

# 9. Kondisi
# for x in newCol.find({"nama" : "Rick"}):
#     print(x)
# cons = ["Rossi", "Joko"]
# print(list(myMongo["Penjualan"]["staff"].find({"$or" : [{"nama" : "Rick"}, {"usia" : 23}]}))) ## $or untuk memunculkan item yang memunculkan item yang memenuhi salah satu kondisi (BANYAK ITEM)
# print(list(myMongo["Penjualan"]["staff"].find({"nama" : {"$in" : cons}}))) ## ==> $in untuk memunculkan item yang PROPERTYnya memenuhi salah satu kondisi VALUE

# 10. Menghapus item dalam collection
# newCol.delete_many({"nama" : "Rossi"}) ## pakai delete_many untuk menghapus banyak dengan kondisi yang sama

# print(list(myMongo["Penjualan"]["staff"].find()))

# 11. Update data
# newCol.update_many({"kota" : "Malang"}, {"$set" : {"usia" : 100}}) ## update_one untuk 1 item / 1 kondisi, update_many untuk banyak item / banyak kondisi

# 12. Menghapus property
# newCol.update_one({"kota" : "Jakarta"}, {"$unset" : {"nama" : True}})

# 13. Mengubah nama property
# newCol.update_one({"nama" : "Joko"}, {"$rename" : {"nama" : "panggilan"}})

# 14. Menghapus data
# newCol.delete_one({"kota" : "Bandung"}) ## delete_many untuk menghapus banyak item dengan kondisi tertentu. Pakai {} untuk menghapus semua data

# Mengubah VALUE dari PROPERTY terkait
# newCol.update_one({"kota" : "Bandung"}, {"$set" : {"nama" : "Valentino"}})

print(pprint.pprint(list(newCol.find())))