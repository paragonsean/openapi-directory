

# CertificateConfiguration

Certificate configuration which consist of non-trusted intermediates and root certificates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificate** | [**CertificateInformation**](CertificateInformation.md) |  |  [optional] |
|**certificatePassword** | **String** | Certificate Password. |  [optional] |
|**encodedCertificate** | **String** | Base64 Encoded certificate. |  [optional] |
|**storeName** | [**StoreNameEnum**](#StoreNameEnum) | The local certificate store location. Only Root and CertificateAuthority are valid locations. |  |



## Enum: StoreNameEnum

| Name | Value |
|---- | -----|
| CERTIFICATE_AUTHORITY | &quot;CertificateAuthority&quot; |
| ROOT | &quot;Root&quot; |



