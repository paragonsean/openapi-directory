

# BuildAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationDate** | **OffsetDateTime** |  |  [optional] |
|**expired** | **Boolean** |  |  [optional] |
|**iconAssetToken** | [**ImageAsset**](ImageAsset.md) |  |  [optional] |
|**minOsVersion** | **String** |  |  [optional] |
|**processingState** | [**ProcessingStateEnum**](#ProcessingStateEnum) |  |  [optional] |
|**uploadedDate** | **OffsetDateTime** |  |  [optional] |
|**usesNonExemptEncryption** | **Boolean** |  |  [optional] |
|**version** | **String** |  |  [optional] |



## Enum: ProcessingStateEnum

| Name | Value |
|---- | -----|
| PROCESSING | &quot;PROCESSING&quot; |
| FAILED | &quot;FAILED&quot; |
| INVALID | &quot;INVALID&quot; |
| VALID | &quot;VALID&quot; |



