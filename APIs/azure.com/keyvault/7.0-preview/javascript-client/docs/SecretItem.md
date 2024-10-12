# KeyVaultClient.SecretItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SecretAttributes**](SecretAttributes.md) |  | [optional] 
**contentType** | **String** | Type of the secret value such as a password. | [optional] 
**id** | **String** | Secret identifier. | [optional] 
**managed** | **Boolean** | True if the secret&#39;s lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true. | [optional] [readonly] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 


