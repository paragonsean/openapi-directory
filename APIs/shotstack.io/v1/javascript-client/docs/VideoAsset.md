# Shotstack.VideoAsset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crop** | [**Crop**](Crop.md) |  | [optional] 
**src** | **String** | The video source URL. The URL must be publicly accessible or include credentials. | 
**trim** | **Number** | The start trim point of the video clip, in seconds (defaults to 0). Videos will start from the in trim point. The video will play until the file ends or the Clip length is reached. | [optional] 
**type** | **String** | The type of asset - set to &#x60;video&#x60; for videos. | [default to &#39;video&#39;]
**volume** | **Number** | Set the volume for the video clip between 0 and 1 where 0 is muted and 1 is full volume (defaults to 0). | [optional] 


