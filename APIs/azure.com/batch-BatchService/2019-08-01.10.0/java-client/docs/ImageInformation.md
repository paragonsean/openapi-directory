

# ImageInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchSupportEndOfLife** | **OffsetDateTime** |  |  [optional] |
|**capabilities** | **List&lt;String&gt;** | Not every capability of the Image is listed. Capabilities in this list are considered of special interest and are generally related to integration with other features in the Azure Batch service. |  [optional] |
|**imageReference** | [**ImageReference**](ImageReference.md) |  |  |
|**nodeAgentSKUId** | **String** |  |  |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) |  |  |
|**verificationType** | [**VerificationTypeEnum**](#VerificationTypeEnum) |  |  |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;linux&quot; |
| WINDOWS | &quot;windows&quot; |



## Enum: VerificationTypeEnum

| Name | Value |
|---- | -----|
| VERIFIED | &quot;verified&quot; |
| UNVERIFIED | &quot;unverified&quot; |



