def map(doc):
    if doc.get("type","") == "case":
        yield [doc.get('subject'),
               doc.get('history',[{}])[-1].get("at","")
               ], 1
