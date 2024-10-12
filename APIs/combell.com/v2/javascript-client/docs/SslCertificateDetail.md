# PublicApi.SslCertificateDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonName** | **String** | The common name (e.g. domain.com) of the certificate. | [optional] 
**expiresAfter** | **Date** | The exact time the certificate will expire. | [optional] 
**sha1Fingerprint** | **String** | The SHA-1 fingerprint of the certificate.&lt;br /&gt;  The fingerprint is a cryptographic hash which is a short unique identification of the certificate. | [optional] 
**subjectAltNames** | [**[SslSubjectAltName]**](SslSubjectAltName.md) | The list of all supported dns names in the certificate. | [optional] 
**type** | [**SslCertificateType**](SslCertificateType.md) |  | [optional] 
**validationLevel** | [**SslCertificateValidationLevel**](SslCertificateValidationLevel.md) |  | [optional] 


