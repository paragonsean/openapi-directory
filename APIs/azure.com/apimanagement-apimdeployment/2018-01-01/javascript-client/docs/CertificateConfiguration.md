# ApiManagementClient.CertificateConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | [**CertificateInformation**](CertificateInformation.md) |  | [optional] 
**certificatePassword** | **String** | Certificate Password. | [optional] 
**encodedCertificate** | **String** | Base64 Encoded certificate. | [optional] 
**storeName** | **String** | The System.Security.Cryptography.x509certificates.StoreName certificate store location. Only Root and CertificateAuthority are valid locations. | 



## Enum: StoreNameEnum


* `CertificateAuthority` (value: `"CertificateAuthority"`)

* `Root` (value: `"Root"`)




