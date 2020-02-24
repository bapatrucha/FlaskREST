from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.findByName(name)
        if store:
            return store.json()
        return {'Message': 'Store {} not found'.format(name)}, 404

    def post(self, name):
        store = StoreModel.findByName(name)
        if store:
            return {'Message': 'Store {} already exists'.format(name)}, 400
        store = StoreModel(name)
        try:
            store.save()
        except:
            return {'Error': 'Store {} could not be created'.format(name)}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.findByName(name)
        if store:
            store.delete()
        else:
            return {'Message': 'Store {} does not exist'.format(name)}, 404
        return {'Message': 'Store {} deleted'.format(name)}, 200

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
