

# VideoStreamingPlaylistsHLS


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**files** | [**List&lt;VideoFile&gt;**](VideoFile.md) | Video files associated to this playlist.  The difference with the root &#x60;files&#x60; property is that these files are fragmented, so they can be used in this streaming playlist (HLS, etc.)  |  [optional] |
|**playlistUrl** | **String** |  |  [optional] |
|**redundancies** | [**List&lt;VideoStreamingPlaylistsHLSRedundanciesInner&gt;**](VideoStreamingPlaylistsHLSRedundanciesInner.md) |  |  [optional] |
|**segmentsSha256Url** | **String** |  |  [optional] |



