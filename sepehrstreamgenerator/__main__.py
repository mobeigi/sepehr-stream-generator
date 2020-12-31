from .browser import Browser
from .m3u_writer import M3UWriter

import os
import sys
import json

# Set CWD to script directory
os.chdir(sys.path[0])

# Open channel data file
channel_data = None
with open('data/channel_data.json', 'r') as f:
    channel_data = json.load(f)

# Fetch links
browser = Browser()

for channel in channel_data["channels"]:
    id = channel["id"]

    if id.lower().startswith('jjtvn'):
        # Use JJTVN method
        frame = browser.get_jjtvn_sepehr_frame(id)
        channel["link"] = browser.get_jjtvn_link_for_frame(id, frame)
    else:
        # Use generic Sepehr method
        channel["link"] = browser.get_sepehr_link(id)

# Dump final channel data file
with open('out/channel_data_with_links.json', 'w') as outfile:
    json.dump(channel_data, outfile)

# Create M3U output file
m3u_str = M3UWriter.create_from_channel_data(channel_data)
with open('out/sepehr.m3u', 'w') as outfile:
    outfile.write(m3u_str)
