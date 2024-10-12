# PeerTube.VideoFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileDownloadUrl** | **String** | URL endpoint that transfers the video file as an attachment (so that the browser opens a download dialog) | [optional] 
**fileUrl** | **String** | Direct URL of the video | [optional] 
**fps** | **Number** | Frames per second of the video file | [optional] 
**id** | **Number** |  | [optional] 
**magnetUri** | **String** | magnet URI allowing to resolve the video via BitTorrent without a metainfo file | [optional] 
**metadataUrl** | **String** | URL dereferencing the output of ffprobe on the file | [optional] 
**resolution** | [**VideoResolutionConstant**](VideoResolutionConstant.md) |  | [optional] 
**size** | **Number** | Video file size in bytes | [optional] 
**torrentDownloadUrl** | **String** | URL endpoint that transfers the torrent file as an attachment (so that the browser opens a download dialog) | [optional] 
**torrentUrl** | **String** | Direct URL of the torrent file | [optional] 


