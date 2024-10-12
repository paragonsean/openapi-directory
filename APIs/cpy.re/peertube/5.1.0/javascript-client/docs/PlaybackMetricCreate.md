# PeerTube.PlaybackMetricCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downloadedBytesHTTP** | **Number** | How many bytes were downloaded with HTTP since the last metric creation | 
**downloadedBytesP2P** | **Number** | How many bytes were downloaded with P2P since the last metric creation | 
**errors** | **Number** | How many errors occured since the last metric creation | 
**fps** | **Number** | Current player video fps | [optional] 
**playerMode** | **String** |  | 
**resolution** | **Number** | Current player video resolution | [optional] 
**resolutionChanges** | **Number** | How many resolution changes occured since the last metric creation | 
**uploadedBytesP2P** | **Number** | How many bytes were uploaded with P2P since the last metric creation | 
**videoId** | [**GetLiveIdIdParameter**](GetLiveIdIdParameter.md) |  | 



## Enum: PlayerModeEnum


* `p2p-media-loader` (value: `"p2p-media-loader"`)

* `webtorrent` (value: `"webtorrent"`)




