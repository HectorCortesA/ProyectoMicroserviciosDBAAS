# app/services/database_service.py

from app.database.connection import client


def create_database(user_id: str, db_name: str):

    database_name = f"{user_id}_{db_name}"

    db = client[database_name]

    db["init_collection"].insert_one({
        "initialized": True
    })

    return {
        "message": f"Base de datos '{db_name}' creada correctamente"
    }


def list_databases(user_id: str):

    databases = client.list_database_names()

    user_databases = []

    prefix = f"{user_id}_"

    for db in databases:

        if db.startswith(prefix):

            clean_name = db.replace(prefix, "")

            user_databases.append(clean_name)

    return {
        "databases": user_databases
    }


def delete_database(user_id: str, db_name: str):

    database_name = f"{user_id}_{db_name}"

    client.drop_database(database_name)

    return {
        "message": f"Base de datos '{db_name}' eliminada"
    }