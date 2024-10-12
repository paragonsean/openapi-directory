

# CertificateAttributes

Stores information about a certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateTemplate** | [**CertificateTemplate**](CertificateTemplate.md) |  |  [optional] |
|**fingerprint** | **String** | The encoded certificate fingerprint. |  [optional] |
|**issuer** | **String** | The name of the issuer of this certificate. |  [optional] |
|**serialNumber** | **String** | Serial number of the certificate, Example: \&quot;123456789\&quot;. |  [optional] |
|**subject** | **String** | The subject name of this certificate. |  [optional] |
|**thumbprint** | **String** | The certificate thumbprint. |  [optional] |
|**validationState** | [**ValidationStateEnum**](#ValidationStateEnum) | Validation state of this certificate. |  [optional] |
|**validityExpirationTime** | **String** | Certificate not valid at or after this timestamp. |  [optional] |
|**validityStartTime** | **String** | Certificate not valid before this timestamp. |  [optional] |



## Enum: ValidationStateEnum

| Name | Value |
|---- | -----|
| CERTIFICATE_VALIDATION_STATE_UNSPECIFIED | &quot;CERTIFICATE_VALIDATION_STATE_UNSPECIFIED&quot; |
| VALIDATION_SUCCESSFUL | &quot;VALIDATION_SUCCESSFUL&quot; |
| VALIDATION_FAILED | &quot;VALIDATION_FAILED&quot; |



