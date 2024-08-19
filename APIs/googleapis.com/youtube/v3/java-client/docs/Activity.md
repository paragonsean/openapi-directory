

# Activity

An *activity* resource contains information about an action that a particular channel, or user, has taken on YouTube.The actions reported in activity feeds include rating a video, sharing a video, marking a video as a favorite, commenting on a video, uploading a video, and so forth. Each activity resource identifies the type of action, the channel associated with the action, and the resource(s) associated with the action, such as the video that was rated or uploaded.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentDetails** | [**ActivityContentDetails**](ActivityContentDetails.md) |  |  [optional] |
|**etag** | **String** | Etag of this resource |  [optional] |
|**id** | **String** | The ID that YouTube uses to uniquely identify the activity. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;youtube#activity\&quot;. |  [optional] |
|**snippet** | [**ActivitySnippet**](ActivitySnippet.md) |  |  [optional] |



