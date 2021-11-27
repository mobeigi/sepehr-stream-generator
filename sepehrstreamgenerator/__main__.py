from .browser import Browser
from .m3u_writer import M3UWriter

import os
import sys
import json

# Set CWD to script directory
os.chdir(sys.path[0])

# Init browser
browser = Browser()

# Load channel name mappings
channel_name_mappings = None
with open('data/channel_name_mappings.json', 'r') as f:
    channel_name_mappings = json.load(f)

# Get all channels
all_sepehr_channels = browser.get_all_sepehr_channels()
channel_data_list = []

for channel in all_sepehr_channels:

    # Filter non-TV channels
    if channel.type != 'TV':
        continue

    # Determine desired tvg name
    # Format will be uid or mapped name first, then Persian name in brackets after
    tvg_name = f'IRIB {channel.uid} ({channel.name})'
    if channel.uid in channel_name_mappings['mappings']:
        mapped_name = channel_name_mappings['mappings'][channel.uid]
        tvg_name = f'{mapped_name} ({channel.name})'

    # Create channel data entry for each channel
    channel_data_entry = {
        'id': channel.id,
        'uid': channel.uid,
        'tvg-id': f'{channel.uid} IR',
        'tvg-name': f'{tvg_name}',
        'tvg-language': 'Persian',
        'tvg-logo': f'{channel.icon}',
        'tvg-country': 'IR',
        'tvg-url': '',
        'group-title': 'General',
        'stream-url': channel.stream_url
    }
    channel_data_list.append(channel_data_entry)

# Dump final channel data file
channel_data = { 'channels': channel_data_list }
with open('out/channel_data.json', 'w') as outfile:
    json.dump(channel_data, outfile)

# Create M3U output file
m3u_str = M3UWriter.create_from_channel_data(channel_data)
with open('out/sepehr.m3u', 'w', encoding='utf-8') as outfile:
    outfile.write(m3u_str)
