# AzureMediaServices.Image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **String** | The position in the input video at which to stop generating thumbnails. The value can be in absolute timestamp (ISO 8601, e.g: PT5M30S to stop at 5 minutes and 30 seconds), or a frame count (For example, 300 to stop at the 300th frame), or a relative value (For example, 100%). | [optional] 
**start** | **String** | The position in the input video from where to start generating thumbnails. The value can be in absolute timestamp (ISO 8601, e.g: PT05S), or a frame count (For example, 10 for the 10th frame), or a relative value (For example, 1%). Also supports a macro {Best}, which tells the encoder to select the best thumbnail from the first few seconds of the video. | [optional] 
**step** | **String** | The intervals at which thumbnails are generated. The value can be in absolute timestamp (ISO 8601, e.g: PT05S for one image every 5 seconds), or a frame count (For example, 30 for every 30 frames), or a relative value (For example, 1%). | [optional] 


