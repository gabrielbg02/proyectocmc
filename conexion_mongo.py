from pymongo import MongoClient
from bson.objectid import ObjectId 


client = MongoClient ('localhost', 27017)

database = client.prueba

persona = database.persona 

#persona.insert_one ({"nombre" : "jesus", "edad" : 33})

actualizacion = {'$set' : {"nombre" : "esther"}}

persona.update_one({"_id": ObjectId ("67af8c14e49cc3f2a98dec61")}, {"$set" : {"nombre" : "esther"}})

for persona in persona.find() :
    print (persona)



