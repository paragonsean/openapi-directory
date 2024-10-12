# CertificateAuthorityApi.RevokedCertificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **String** | The resource name for the Certificate in the format &#x60;projects/_*_/locations/_*_/caPools/_*_/certificates/_*&#x60;. | [optional] 
**hexSerialNumber** | **String** | The serial number of the Certificate. | [optional] 
**revocationReason** | **String** | The reason the Certificate was revoked. | [optional] 



## Enum: RevocationReasonEnum


* `REVOCATION_REASON_UNSPECIFIED` (value: `"REVOCATION_REASON_UNSPECIFIED"`)

* `KEY_COMPROMISE` (value: `"KEY_COMPROMISE"`)

* `CERTIFICATE_AUTHORITY_COMPROMISE` (value: `"CERTIFICATE_AUTHORITY_COMPROMISE"`)

* `AFFILIATION_CHANGED` (value: `"AFFILIATION_CHANGED"`)

* `SUPERSEDED` (value: `"SUPERSEDED"`)

* `CESSATION_OF_OPERATION` (value: `"CESSATION_OF_OPERATION"`)

* `CERTIFICATE_HOLD` (value: `"CERTIFICATE_HOLD"`)

* `PRIVILEGE_WITHDRAWN` (value: `"PRIVILEGE_WITHDRAWN"`)

* `ATTRIBUTE_AUTHORITY_COMPROMISE` (value: `"ATTRIBUTE_AUTHORITY_COMPROMISE"`)




