

# StreamingLocatorContentKey

Class for content key in Streaming Locator

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | ID of Content Key |  |
|**labelReferenceInStreamingPolicy** | **String** | Label of Content Key as specified in the Streaming Policy |  [optional] |
|**policyName** | **String** | ContentKeyPolicy used by Content Key |  [optional] [readonly] |
|**tracks** | [**List&lt;TrackSelection&gt;**](TrackSelection.md) | Tracks which use this Content Key |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Encryption type of Content Key |  [optional] [readonly] |
|**value** | **String** | Value of Content Key |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMMON_ENCRYPTION_CENC | &quot;CommonEncryptionCenc&quot; |
| COMMON_ENCRYPTION_CBCS | &quot;CommonEncryptionCbcs&quot; |
| ENVELOPE_ENCRYPTION | &quot;EnvelopeEncryption&quot; |



