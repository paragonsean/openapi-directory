

# LiveVideoSessionResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endDate** | **OffsetDateTime** | End date of the live session |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) | Error type if an error occurred during the live session:   - &#x60;1&#x60;: Bad socket health (transcoding is too slow)   - &#x60;2&#x60;: Max duration exceeded   - &#x60;3&#x60;: Quota exceeded   - &#x60;4&#x60;: Quota FFmpeg error   - &#x60;5&#x60;: Video has been blacklisted during the live  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**replayVideo** | [**LiveVideoSessionResponseReplayVideo**](LiveVideoSessionResponseReplayVideo.md) |  |  [optional] |
|**startDate** | **OffsetDateTime** | Start date of the live session |  [optional] |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |



