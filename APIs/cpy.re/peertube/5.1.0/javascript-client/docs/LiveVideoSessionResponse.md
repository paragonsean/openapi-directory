# PeerTube.LiveVideoSessionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endDate** | **Date** | End date of the live session | [optional] 
**error** | **Number** | Error type if an error occurred during the live session:   - &#x60;1&#x60;: Bad socket health (transcoding is too slow)   - &#x60;2&#x60;: Max duration exceeded   - &#x60;3&#x60;: Quota exceeded   - &#x60;4&#x60;: Quota FFmpeg error   - &#x60;5&#x60;: Video has been blacklisted during the live  | [optional] 
**id** | **Number** |  | [optional] 
**replayVideo** | [**LiveVideoSessionResponseReplayVideo**](LiveVideoSessionResponseReplayVideo.md) |  | [optional] 
**startDate** | **Date** | Start date of the live session | [optional] 



## Enum: ErrorEnum


* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)




