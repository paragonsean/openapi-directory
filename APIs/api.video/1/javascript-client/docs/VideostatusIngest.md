# ApiVideo.VideostatusIngest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filesize** | **Number** | The size of your file in bytes. | [optional] 
**receivedBytes** | [**[BytesRange]**](BytesRange.md) | The total number of bytes received, listed for each chunk of the upload. | [optional] 
**status** | **String** | There are three possible ingest statuses. missing - you are missing information required to ingest the video. uploading - the video is in the process of being uploaded. uploaded - the video is ready for use. | [optional] 



## Enum: StatusEnum


* `missing` (value: `"missing"`)

* `uploading` (value: `"uploading"`)

* `uploaded` (value: `"uploaded"`)




