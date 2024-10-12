# PeerTube.VideoStreamingPlaylists

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**[VideoFile]**](VideoFile.md) | Video files associated to this playlist.  The difference with the root &#x60;files&#x60; property is that these files are fragmented, so they can be used in this streaming playlist (HLS, etc.)  | [optional] 
**playlistUrl** | **String** |  | [optional] 
**redundancies** | [**[VideoStreamingPlaylistsHLSRedundanciesInner]**](VideoStreamingPlaylistsHLSRedundanciesInner.md) |  | [optional] 
**segmentsSha256Url** | **String** |  | [optional] 
**id** | **Number** |  | [optional] 
**type** | **Number** | Playlist type: - &#x60;1&#x60;: HLS  | [optional] 



## Enum: TypeEnum


* `1` (value: `1`)




