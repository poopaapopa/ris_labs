from DataBase.connection import DBConnection

def select_from_db(db_config, request):
    with DBConnection(db_config) as cursor:
        cursor.execute(request)
        if cursor.description is not None:
            result = cursor.fetchall()
            output = []
            schema = [column[0] for column in cursor.description]
            for row in result:
                dict_row = dict(zip(schema, row))
                output.append(dict_row)
            cursor.close()
            return output
        else:
            cursor.close()
            return []
