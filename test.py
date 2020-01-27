import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["new_db"]

print(my_client.list_database_names())

my_coll = my_db["notes"]
print(my_db.list_collection_names())

new_rec = {"note_head":"tssting from pymongo", "note_content": "testinnnnnnng"}

new_rec2 = {"note_head":"2__tssting from pymongo", "note_content": "2_testinnnnnnng"}
new_rec3 = {"note_head":"3__tssting from pymongo", "note_content": "3_testinnnnnnng"}

rec_list = [new_rec2, new_rec3]
my_coll.insert_one(new_rec)
my_coll.insert_many(rec_list)
for x in my_coll.find({},{"_id":0}):
	print(x)
