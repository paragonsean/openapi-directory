# KeyVaultClient.DeletedSecretItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletedDate** | **Number** | The time when the secret was deleted, in UTC | [optional] [readonly] 
**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted secret. | [optional] 
**scheduledPurgeDate** | **Number** | The time when the secret is scheduled to be purged, in UTC | [optional] [readonly] 
**attributes** | [**SecretAttributes**](SecretAttributes.md) |  | [optional] 
**contentType** | **String** | Type of the secret value such as a password. | [optional] 
**id** | **String** | Secret identifier. | [optional] 
**managed** | **Boolean** | True if the secret&#39;s lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true. | [optional] [readonly] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 


