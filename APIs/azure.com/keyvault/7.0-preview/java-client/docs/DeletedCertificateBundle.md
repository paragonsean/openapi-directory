

# DeletedCertificateBundle

A Deleted Certificate consisting of its previous id, attributes and its tags, as well as information on when it will be purged.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletedDate** | **Integer** | The time when the certificate was deleted, in UTC |  [optional] [readonly] |
|**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted certificate. |  [optional] |
|**scheduledPurgeDate** | **Integer** | The time when the certificate is scheduled to be purged, in UTC |  [optional] [readonly] |
|**attributes** | [**CertificateAttributes**](CertificateAttributes.md) |  |  [optional] |
|**cer** | **byte[]** | CER contents of x509 certificate. |  [optional] |
|**contentType** | **String** | The content type of the secret. |  [optional] |
|**id** | **String** | The certificate id. |  [optional] [readonly] |
|**kid** | **String** | The key id. |  [optional] [readonly] |
|**policy** | [**CertificatePolicy**](CertificatePolicy.md) |  |  [optional] |
|**sid** | **String** | The secret id. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs |  [optional] |
|**x5t** | **String** | Thumbprint of the certificate. |  [optional] [readonly] |



