# KeyVaultClient.DeletedSecretBundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletedDate** | **Number** | The time when the secret was deleted, in UTC | [optional] [readonly] 
**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted secret. | [optional] 
**scheduledPurgeDate** | **Number** | The time when the secret is scheduled to be purged, in UTC | [optional] [readonly] 
**attributes** | [**SecretAttributes**](SecretAttributes.md) |  | [optional] 
**contentType** | **String** | The content type of the secret. | [optional] 
**id** | **String** | The secret id. | [optional] 
**kid** | **String** | If this is a secret backing a KV certificate, then this field specifies the corresponding key backing the KV certificate. | [optional] [readonly] 
**managed** | **Boolean** | True if the secret&#39;s lifetime is managed by key vault. If this is a secret backing a certificate, then managed will be true. | [optional] [readonly] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 
**value** | **String** | The secret value. | [optional] 


