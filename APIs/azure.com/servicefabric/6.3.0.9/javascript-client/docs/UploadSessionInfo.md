# ServiceFabricClientApis.UploadSessionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectedRanges** | [**[UploadChunkRange]**](UploadChunkRange.md) | List of chunk ranges that image store has not received yet. | [optional] 
**fileSize** | **String** | The size in bytes of the uploading file. | [optional] 
**modifiedDate** | **Date** | The date and time when the upload session was last modified. | [optional] 
**sessionId** | **String** | A unique ID of the upload session. A session ID can be reused only if the session was committed or removed. | [optional] 
**storeRelativePath** | **String** | The remote location within image store. This path is relative to the image store root. | [optional] 


