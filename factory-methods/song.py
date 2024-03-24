
# python3 song.py

from serializer_demo import Song, SongSerializer

song = Song('1', 'Water of Love', 'Dire Straits')
serializer = SongSerializer()

song_in_json_format = serializer.serialize(song, 'JSON')
print(song_in_json_format)

song_in_xml_format = serializer.serialize(song, 'XML')
print(song_in_xml_format)

song_in_yaml_format = serializer.serialize(song, 'YAML')
print(song_in_yaml_format)
