

# CompleteS3FileUploadRequest

Request model for completing a S3 file upload

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileKey** | [**FileKey**](FileKey.md) |  |  [optional] |
|**fileName** | **String** | New file name to store with |  [optional] |
|**keepShareLinks** | **Boolean** | Preserve Download Share Links and point them to the new node. |  [optional] |
|**parts** | [**List&lt;S3FileUploadPart&gt;**](S3FileUploadPart.md) | List of S3 file upload parts |  |
|**resolutionStrategy** | [**ResolutionStrategyEnum**](#ResolutionStrategyEnum) | Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60; |  [optional] |



## Enum: ResolutionStrategyEnum

| Name | Value |
|---- | -----|
| AUTORENAME | &quot;autorename&quot; |
| OVERWRITE | &quot;overwrite&quot; |
| FAIL | &quot;fail&quot; |



