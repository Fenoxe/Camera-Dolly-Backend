import uuid

class UUIDDatabase():

    database = {}

    @staticmethod
    def get(purpose):
        u = uuid.uuid4().hex
        UUIDDatabase.database[purpose] = u
        return u