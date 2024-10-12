

# PostNamespacesDeleteImagesResponseErrorErrinfoAllOfDetailsErrorsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digest** | **String** | Digest of the image that caused the error. |  [optional] |
|**error** | [**ErrorEnum**](#ErrorEnum) | Error type. |  [optional] |
|**repository** | **String** | Name of the repository of the image that caused the error. |  [optional] |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| NOT_FOUND | &quot;not_found&quot; |
| UNAUTHORIZED | &quot;unauthorized&quot; |
| CHILD_MANIFEST | &quot;child_manifest&quot; |



