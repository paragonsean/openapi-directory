# AzureMediaServices.StreamingLocatorContentKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | ID of Content Key | 
**labelReferenceInStreamingPolicy** | **String** | Label of Content Key as specified in the Streaming Policy | [optional] 
**policyName** | **String** | ContentKeyPolicy used by Content Key | [optional] [readonly] 
**tracks** | [**[TrackSelection]**](TrackSelection.md) | Tracks which use this Content Key | [optional] [readonly] 
**type** | **String** | Encryption type of Content Key | [optional] [readonly] 
**value** | **String** | Value of Content Key | [optional] 



## Enum: TypeEnum


* `CommonEncryptionCenc` (value: `"CommonEncryptionCenc"`)

* `CommonEncryptionCbcs` (value: `"CommonEncryptionCbcs"`)

* `EnvelopeEncryption` (value: `"EnvelopeEncryption"`)




