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