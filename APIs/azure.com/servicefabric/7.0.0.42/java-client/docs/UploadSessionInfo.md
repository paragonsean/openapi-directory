

# UploadSessionInfo

Information about an image store upload session. A session is associated with a relative path in the image store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expectedRanges** | [**List&lt;UploadChunkRange&gt;**](UploadChunkRange.md) | List of chunk ranges that image store has not received yet. |  [optional] |
|**fileSize** | **String** | The size in bytes of the uploading file. |  [optional] |
|**modifiedDate** | **OffsetDateTime** | The date and time when the upload session was last modified. |  [optional] |
|**sessionId** | **UUID** | A unique ID of the upload session. A session ID can be reused only if the session was committed or removed. |  [optional] |
|**storeRelativePath** | **String** | The remote location within image store. This path is relative to the image store root. |  [optional] |



