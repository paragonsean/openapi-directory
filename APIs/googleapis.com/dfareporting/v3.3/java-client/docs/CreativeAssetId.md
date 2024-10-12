

# CreativeAssetId

Creative Asset ID.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the creative asset. This is a required field while inserting an asset. After insertion, this assetIdentifier is used to identify the uploaded asset. Characters in the name must be alphanumeric or one of the following: \&quot;.-_ \&quot;. Spaces are allowed. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of asset to upload. This is a required field. FLASH and IMAGE are no longer supported for new uploads. All image assets should use HTML_IMAGE. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;IMAGE&quot; |
| FLASH | &quot;FLASH&quot; |
| VIDEO | &quot;VIDEO&quot; |
| HTML | &quot;HTML&quot; |
| HTML_IMAGE | &quot;HTML_IMAGE&quot; |
| AUDIO | &quot;AUDIO&quot; |



