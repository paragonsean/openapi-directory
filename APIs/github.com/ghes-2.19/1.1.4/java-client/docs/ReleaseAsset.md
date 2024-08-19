

# ReleaseAsset

Data related to a release.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**browserDownloadUrl** | **URI** |  |  |
|**contentType** | **String** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**downloadCount** | **Integer** |  |  |
|**id** | **Integer** |  |  |
|**label** | **String** |  |  |
|**name** | **String** | The file name of the asset. |  |
|**nodeId** | **String** |  |  |
|**size** | **Integer** |  |  |
|**state** | [**StateEnum**](#StateEnum) | State of the release asset. |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**uploader** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**url** | **URI** |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UPLOADED | &quot;uploaded&quot; |
| OPEN | &quot;open&quot; |



