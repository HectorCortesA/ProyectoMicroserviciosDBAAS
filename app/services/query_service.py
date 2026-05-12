# app/services/query_service.py

from app.database.connection import client


def count_documents(
    user_id: str,
    db_name: str,
    table_name: str,
    filters: dict = {}
):

    database_name = f"{user_id}_{db_name}"

    db = client[database_name]

    collection = db[table_name]

    total = collection.count_documents(filters)

    return {
        "count": total
    }


def sort_documents(
    user_id: str,
    db_name: str,
    table_name: str,
    field: str,
    order: int = 1
):

    database_name = f"{user_id}_{db_name}"

    db = client[database_name]

    collection = db[table_name]

    documents = list(
        collection.find().sort(field, order)
    )

    for doc in documents:
        doc["_id"] = str(doc["_id"])

    return {
        "data": documents
    }


def limit_documents(
    user_id: str,
    db_name: str,
    table_name: str,
    limit: int
):

    database_name = f"{user_id}_{db_name}"

    db = client[database_name]

    collection = db[table_name]

    documents = list(
        collection.find().limit(limit)
    )

    for doc in documents:
        doc["_id"] = str(doc["_id"])

    return {
        "data": documents
    }


def aggregate_group_by(
    user_id: str,
    db_name: str,
    table_name: str,
    field: str
):

    database_name = f"{user_id}_{db_name}"

    db = client[database_name]

    collection = db[table_name]

    pipeline = [
        {
            "$group": {
                "_id": f"${field}",
                "total": {
                    "$sum": 1
                }
            }
        }
    ]

    result = list(
        collection.aggregate(pipeline)
    )

    return {
        "data": result
    }


def aggregate_sum(
    user_id: str,
    db_name: str,
    table_name: str,
    field: str
):

    database_name = f"{user_id}_{db_name}"

    db = client[database_name]

    collection = db[table_name]

    pipeline = [
        {
            "$group": {
                "_id": None,
                "total": {
                    "$sum": f"${field}"
                }
            }
        }
    ]

    result = list(
        collection.aggregate(pipeline)
    )

    return {
        "data": result
    }


def aggregate_avg(
    user_id: str,
    db_name: str,
    table_name: str,
    field: str
):

    database_name = f"{user_id}_{db_name}"

    db = client[database_name]

    collection = db[table_name]

    pipeline = [
        {
            "$group": {
                "_id": None,
                "average": {
                    "$avg": f"${field}"
                }
            }
        }
    ]

    result = list(
        collection.aggregate(pipeline)
    )

    return {
        "data": result
    }
# Añadir al final de app/services/query_service.py

def aggregate_distinct(
    user_id: str,
    db_name: str,
    table_name: str,
    field: str
):
    database_name = f"{user_id}_{db_name}"
    db = client[database_name]
    collection = db[table_name]

    # MongoDB tiene una función nativa para distinct
    result = collection.distinct(field)

    return {
        "data": result
    }

def aggregate_inner_join(
    user_id: str,
    db_name: str,
    table_name: str,
    from_table: str,      # La tabla con la que se va a cruzar
    local_field: str,     # El campo en la tabla principal
    foreign_field: str,   # El campo en la tabla secundaria
    as_name: str          # El nombre del nuevo campo combinado
):
    database_name = f"{user_id}_{db_name}"
    db = client[database_name]
    collection = db[table_name]

    pipeline = [
        {
            "$lookup": {
                "from": from_table,
                "localField": local_field,
                "foreignField": foreign_field,
                "as": as_name
            }
        },
        {
            # $unwind descarta los documentos que no tuvieron coincidencia,
            # emulando exactamente el comportamiento de un INNER JOIN en SQL
            "$unwind": f"${as_name}"
        }
    ]

    documents = list(collection.aggregate(pipeline))

    # Parsear los ObjectIDs a string para evitar errores de serialización JSON
    for doc in documents:
        if "_id" in doc:
            doc["_id"] = str(doc["_id"])
        if as_name in doc and "_id" in doc[as_name]:
            doc[as_name]["_id"] = str(doc[as_name]["_id"])

    return {
        "data": documents
    }

# Añadir al final de app/services/query_service.py
from bson import ObjectId

def filter_documents(db_name: str, collection_name: str, filters: dict, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    
    if "_id" in filters and isinstance(filters["_id"], str):
        filters["_id"] = ObjectId(filters["_id"])
        
    documents = list(db[collection_name].find(filters))
    for doc in documents:
        doc["_id"] = str(doc["_id"])
    return {"data": documents}

def aggregate_documents(db_name: str, collection_name: str, pipeline: list, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    documents = list(db[collection_name].aggregate(pipeline))
    for doc in documents:
        if "_id" in doc:
            doc["_id"] = str(doc["_id"])
    return {"data": documents}