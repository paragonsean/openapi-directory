

# GeneratePresignedPutRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileName** | **String** |  |  |
|**fileSize** | **Integer** | File size should be represented in bytes. |  |
|**metadata** | **CreateMultipartUploadRequestMetadata** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AVATAR | &quot;avatar&quot; |
| PROFILE_BACKGROUND | &quot;profile_background&quot; |
| CARD_BACKGROUND | &quot;card_background&quot; |
| CUSTOM_EMOJI | &quot;custom_emoji&quot; |
| COMPOSER | &quot;composer&quot; |



