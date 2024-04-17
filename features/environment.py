import requests
from utilities.configurations import *
from utilities.resources import *


def after_scenario(context, scenario):  # this will run after each scenario
    if "cleanup" in scenario.tags:

        # DELETE /DeleteBook.php
        # to delete, referencing `configuration.py`, `properties.ini` and `resources.py`
        deleteBookUrl = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        # use delete api and pass the stored variable 'bookId'
        deleteBook_response = requests.post(
            deleteBookUrl,
            json={"ID": context.bookId},  # using the stored bookID from addBookUrl
            headers=context.header, )

        # print status response and verify
        print(deleteBook_response)
        assert deleteBook_response.status_code == 200

        # print then store the response
        print(deleteBook_response.json())
        deleteResponse_json = deleteBook_response.json()
        # Validate the response
        assert deleteResponse_json['msg'] == "book is successfully deleted"

