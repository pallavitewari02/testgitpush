import pymongo
client = pymongo.MongoClient("mongodb+srv://pallavi02:Alld1234@cluster0.kaete.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {

    "name":"Sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname":"kumar"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)