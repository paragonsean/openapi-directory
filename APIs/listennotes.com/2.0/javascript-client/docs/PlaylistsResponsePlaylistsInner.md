# ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistsResponsePlaylistsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Playlist description. | [optional] 
**episodeCount** | **Number** | The number of episodes (including custom audio) in this playlist. | [optional] 
**id** | **String** | A 11-character playlist id, which can be used to further fetch detailed playlist metadata via &#x60;GET /playlists/{id}&#x60;. | [optional] 
**image** | **String** | High resolution image url of the playlist. | [optional] 
**lastTimestampMs** | **Number** | Passed to the **last_timestamp_ms** parameter of &#x60;GET /playlists/{id}&#x60; to paginate through items of that playlist.  | [optional] 
**listennotesUrl** | **String** | The url of this playlist on ListenNotes.com. | [optional] 
**name** | **String** | Playlist name. | [optional] 
**podcastCount** | **Number** | The number of podcasts in this playlist. | [optional] 
**thumbnail** | **String** | Low resolution image url of the playlist. | [optional] 
**totalAudioLengthSec** | **Number** | Total audio length of all episodes in this playlist, in seconds. | [optional] 
**visibility** | [**PlaylistVisibilityField**](PlaylistVisibilityField.md) |  | [optional] 


