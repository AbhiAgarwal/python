import feedparser

# Get all the "titles" from the NYULocal RSS Feed
allFeeds = ['http://nyulocal.com/feed']
j = []
for i in allFeeds:
    d = feedparser.parse(i)
    for item in d.entries:
        j.append({"title": item["title"]})
print j
