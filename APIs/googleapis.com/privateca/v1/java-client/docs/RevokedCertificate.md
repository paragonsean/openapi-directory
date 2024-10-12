

# RevokedCertificate

Describes a revoked Certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificate** | **String** | The resource name for the Certificate in the format &#x60;projects/_*_/locations/_*_/caPools/_*_/certificates/_*&#x60;. |  [optional] |
|**hexSerialNumber** | **String** | The serial number of the Certificate. |  [optional] |
|**revocationReason** | [**RevocationReasonEnum**](#RevocationReasonEnum) | The reason the Certificate was revoked. |  [optional] |



## Enum: RevocationReasonEnum

| Name | Value |
|---- | -----|
| REVOCATION_REASON_UNSPECIFIED | &quot;REVOCATION_REASON_UNSPECIFIED&quot; |
| KEY_COMPROMISE | &quot;KEY_COMPROMISE&quot; |
| CERTIFICATE_AUTHORITY_COMPROMISE | &quot;CERTIFICATE_AUTHORITY_COMPROMISE&quot; |
| AFFILIATION_CHANGED | &quot;AFFILIATION_CHANGED&quot; |
| SUPERSEDED | &quot;SUPERSEDED&quot; |
| CESSATION_OF_OPERATION | &quot;CESSATION_OF_OPERATION&quot; |
| CERTIFICATE_HOLD | &quot;CERTIFICATE_HOLD&quot; |
| PRIVILEGE_WITHDRAWN | &quot;PRIVILEGE_WITHDRAWN&quot; |
| ATTRIBUTE_AUTHORITY_COMPROMISE | &quot;ATTRIBUTE_AUTHORITY_COMPROMISE&quot; |



