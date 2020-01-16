import settings, feedparser, csv
from os.path import join

for filename, feed in settings.feeds.items():
	output = join(settings.output,filename)
	feed.parsed = feedparser.parse(feed.url)
	items = feed.filter(feed.parsed["items"])
	# sort by date descending
	items.sort(key=lambda x: x[0],reverse=True)
	with open(output,"w") as f:
		w = csv.writer(f,delimiter="\t")
		w.writerows(items)
