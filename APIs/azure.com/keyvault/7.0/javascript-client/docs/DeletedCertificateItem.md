# KeyVaultClient.DeletedCertificateItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletedDate** | **Number** | The time when the certificate was deleted, in UTC | [optional] [readonly] 
**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted certificate. | [optional] 
**scheduledPurgeDate** | **Number** | The time when the certificate is scheduled to be purged, in UTC | [optional] [readonly] 
**attributes** | [**CertificateAttributes**](CertificateAttributes.md) |  | [optional] 
**id** | **String** | Certificate identifier. | [optional] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 
**x5t** | **String** | Thumbprint of the certificate. | [optional] 


