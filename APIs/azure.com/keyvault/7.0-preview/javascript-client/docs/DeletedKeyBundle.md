# KeyVaultClient.DeletedKeyBundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletedDate** | **Number** | The time when the key was deleted, in UTC | [optional] [readonly] 
**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted key. | [optional] 
**scheduledPurgeDate** | **Number** | The time when the key is scheduled to be purged, in UTC | [optional] [readonly] 
**attributes** | [**KeyAttributes**](KeyAttributes.md) |  | [optional] 
**key** | [**JsonWebKey**](JsonWebKey.md) |  | [optional] 
**managed** | **Boolean** | True if the key&#39;s lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true. | [optional] [readonly] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 


