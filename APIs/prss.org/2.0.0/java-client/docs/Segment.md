

# Segment

An audio segment in an episode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channels** | **Integer** | The number of audio channels in the segment. Generated at creation. |  [optional] |
|**createdDate** | **OffsetDateTime** | The date the segment was created. Generated at creation. |  [optional] |
|**episodeId** | **Long** | The ID of the episode that owns the segment. |  |
|**fileName** | **String** | The name of the audio content file. Generated at creation. |  [optional] |
|**fileSize** | **Long** | The size of the audio content file in bytes. Generated at creation. |  [optional] |
|**id** | **Long** | The unique ID of the segment. Generated at creation. |  [optional] |
|**inCue** | **String** | The in-cue copy that signals the start of the segment to a board operator. |  [optional] |
|**lastModifiedDate** | **OffsetDateTime** | The date the segment was last modified/updated. Automatically updated on any write operation. |  [optional] |
|**length** | **Integer** | The length (duration) of the segment in seconds. |  [optional] |
|**originalFileName** | **String** | The original name of the audio content file. |  [optional] |
|**outCue** | **String** | The out-cue copy that signals the end of the segment to a board operator. |  [optional] |
|**segmentNumber** | **Integer** | The number of the segment in the episode, starting with 1. |  |



