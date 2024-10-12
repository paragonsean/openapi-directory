

# CompleteUploadRequest

The body must be empty if public upload token is used.  The `resolutionStrategy` in that case will be always `autorename`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileKey** | [**FileKey**](FileKey.md) |  |  [optional] |
|**fileName** | **String** | New file name to store with |  [optional] |
|**keepShareLinks** | **Boolean** | Preserve Download Share Links and point them to the new node. |  [optional] |
|**resolutionStrategy** | [**ResolutionStrategyEnum**](#ResolutionStrategyEnum) | Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60; |  [optional] |
|**userFileKeyList** | [**UserFileKeyList**](UserFileKeyList.md) |  |  [optional] |



## Enum: ResolutionStrategyEnum

| Name | Value |
|---- | -----|
| AUTORENAME | &quot;autorename&quot; |
| OVERWRITE | &quot;overwrite&quot; |
| FAIL | &quot;fail&quot; |



