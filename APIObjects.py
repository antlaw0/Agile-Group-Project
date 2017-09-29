import Wikipedia

API_DICT = {
    'flickr': 0,
    'wikipedia': 1,
    'twitter': 2
}


class API():
    api_ind = None
    def __init__(self,API_NAME):
        global api_ind
        try:
            api_ind = API_DICT[API_NAME.lower()]
        except KeyError:
            print("API error: " + API_NAME.lower + " is not in the list of APIs.")
            return

    def getResults(self,searchTerm):
        global api_ind
        result_current = None
        # Method for creating the overall format of the returned value
        if api_ind == 1:
            # Wikipedia
            result_current = Wikipedia.summary(searchTerm)
        if len(str(result_current)) < 1:
            print("API error: Wikipedia could not find " + searchTerm)
        else:
            print(result_current)

def main(searchterm):
    wiki = API("wikipedia")
    wiki.getResults(searchterm)