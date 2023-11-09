def convertToDict(posts):
    postList = []
    if str(type(posts)) == "<class 'sqlalchemy.engine.row.Row'>":
        postList = posts._asdict()
    else:
        for post in posts:
            postList.append(post._asdict())
    return postList
