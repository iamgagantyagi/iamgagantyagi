import xml.etree.ElementTree as ET
import requests

# Replace with your actual feed URL
feed_url = "https://medium.com/feed/@iamgagantyagi"

# Fetch the feed
response = requests.get(feed_url)

# Parse the XML feed
root = ET.fromstring(response.content)

# Extract the latest blog post
latest_post = root.find('channel/item')
if latest_post is not None:
    title = latest_post.find('title').text
    link = latest_post.find('link').text
    content = latest_post.find('content:encoded').text
    print(f"Title: {title}")
    print(f"Link: {link}")
else:
    print("No blog posts found in the feed.")
