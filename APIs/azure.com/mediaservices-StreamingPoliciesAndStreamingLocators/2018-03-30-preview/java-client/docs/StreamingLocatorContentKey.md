

# StreamingLocatorContentKey

Class for content key in Streaming Locator

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | ID of Content Key |  |
|**label** | **String** | Label of Content Key |  [optional] |
|**policyName** | **String** | ContentKeyPolicy used by Content Key |  [optional] |
|**tracks** | [**List&lt;TrackSelection&gt;**](TrackSelection.md) | Tracks which use this Content Key |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Encryption type of Content Key |  |
|**value** | **String** | Value of Content Key |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMMON_ENCRYPTION_CENC | &quot;CommonEncryptionCenc&quot; |
| COMMON_ENCRYPTION_CBCS | &quot;CommonEncryptionCbcs&quot; |
| ENVELOPE_ENCRYPTION | &quot;EnvelopeEncryption&quot; |



