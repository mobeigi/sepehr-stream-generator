class M3UWriter:

    @staticmethod
    def create_from_channel_data(channel_data):
        out_str = '#EXTM3U\n'

        for channel in channel_data["channels"]:
            out_str += f'#EXTINF:-1 tvg-id="{channel["tvg-id"]}" tvg-name="{channel["tvg-name"]}" tvg-language="{channel["tvg-language"]}" tvg-logo="{channel["tvg-logo"]}" tvg-country="{channel["tvg-country"]}" tvg-url="{channel["tvg-url"]}" group-title="{channel["group-title"]}",{channel["tvg-name"]}\n'
            out_str += f'{channel["link"]}\n'
        return out_str
