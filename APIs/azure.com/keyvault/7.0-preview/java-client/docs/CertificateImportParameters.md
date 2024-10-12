

# CertificateImportParameters

The certificate import parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**CertificateAttributes**](CertificateAttributes.md) |  |  [optional] |
|**policy** | [**CertificatePolicy**](CertificatePolicy.md) |  |  [optional] |
|**pwd** | **String** | If the private key in base64EncodedCertificate is encrypted, the password used for encryption. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] |
|**value** | **String** | Base64 encoded representation of the certificate object to import. This certificate needs to contain the private key. |  |



