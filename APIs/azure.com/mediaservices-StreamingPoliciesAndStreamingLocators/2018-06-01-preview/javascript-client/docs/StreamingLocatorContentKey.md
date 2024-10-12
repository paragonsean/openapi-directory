# AzureMediaServices.StreamingLocatorContentKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | ID of Content Key | 
**label** | **String** | Label of Content Key | [optional] 
**policyName** | **String** | ContentKeyPolicy used by Content Key | [optional] [readonly] 
**tracks** | [**[TrackSelection]**](TrackSelection.md) | Tracks which use this Content Key | [optional] 
**type** | **String** | Encryption type of Content Key | [optional] [readonly] 
**value** | **String** | Value of Content Key | [optional] 



## Enum: TypeEnum


* `CommonEncryptionCenc` (value: `"CommonEncryptionCenc"`)

* `CommonEncryptionCbcs` (value: `"CommonEncryptionCbcs"`)

* `EnvelopeEncryption` (value: `"EnvelopeEncryption"`)




