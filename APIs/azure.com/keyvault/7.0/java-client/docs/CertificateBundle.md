

# CertificateBundle

A certificate bundle consists of a certificate (X509) plus its attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**CertificateAttributes**](CertificateAttributes.md) |  |  [optional] |
|**cer** | **byte[]** | CER contents of x509 certificate. |  [optional] |
|**contentType** | **String** | The content type of the secret. |  [optional] |
|**id** | **String** | The certificate id. |  [optional] [readonly] |
|**kid** | **String** | The key id. |  [optional] [readonly] |
|**policy** | [**CertificatePolicy**](CertificatePolicy.md) |  |  [optional] |
|**sid** | **String** | The secret id. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs |  [optional] |
|**x5t** | **String** | Thumbprint of the certificate. |  [optional] [readonly] |



