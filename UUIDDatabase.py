import uuid

class UUIDDatabase():

    database = {}

    @staticmethod
    def get(purpose):
        while True:
            u = uuid.uuid4().hex[:4]
            if u not in UUIDDatabase.database:
                break
        UUIDDatabase.database[u] = purpose
        return u