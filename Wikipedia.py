import wikipedia

def summary(searchTerm):
    output = ""
    try:
        output = wikipedia.summary(searchTerm)
    except wikipedia.PageError:
        return "No page by name " + searchTerm.lower()
        if len(wikipedia.suggest(searchTerm)) > 0:
            errStr = "Wikipedia has the following pages on " + searchTerm + ": "
            for rslt in wikipedia.suggest(searchTerm):
                errStr += "\n-" + rslt
            output = errStr
        else:
            output = "Unexpected error..."
    return output