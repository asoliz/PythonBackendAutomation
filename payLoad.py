import utilities.configurations


def addBookPayload(isbn, aisle):
    body = {
        "name": "This is how we do it",
        "isbn": isbn,
        "aisle": aisle,
        "author": "montell jordan"
    }
    return body



def buildBookPayloadFromCSV():
    addBody = {}
    pl = utilities.configurations.getCsv('files/books.csv')
    addBody['name'] = pl.get("name")[0]
    addBody['isbn'] = pl.get('isbn')[0]
    addBody['aisle'] = str(pl.get('aisle')[0])
    addBody['author'] = pl.get('author')[0]
    return addBody

# print(type(buildBookPayloadFromCSV()))
# print(type(addBookPayload("oij")))
# print(buildBookPayloadFromCSV())
