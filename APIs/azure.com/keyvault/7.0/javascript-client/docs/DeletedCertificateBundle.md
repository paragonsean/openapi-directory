# KeyVaultClient.DeletedCertificateBundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletedDate** | **Number** | The time when the certificate was deleted, in UTC | [optional] [readonly] 
**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted certificate. | [optional] 
**scheduledPurgeDate** | **Number** | The time when the certificate is scheduled to be purged, in UTC | [optional] [readonly] 
**attributes** | [**CertificateAttributes**](CertificateAttributes.md) |  | [optional] 
**cer** | **Blob** | CER contents of x509 certificate. | [optional] 
**contentType** | **String** | The content type of the secret. | [optional] 
**id** | **String** | The certificate id. | [optional] [readonly] 
**kid** | **String** | The key id. | [optional] [readonly] 
**policy** | [**CertificatePolicy**](CertificatePolicy.md) |  | [optional] 
**sid** | **String** | The secret id. | [optional] [readonly] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs | [optional] 
**x5t** | **String** | Thumbprint of the certificate. | [optional] [readonly] 


