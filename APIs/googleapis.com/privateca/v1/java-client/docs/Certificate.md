

# Certificate

A Certificate corresponds to a signed X.509 certificate issued by a CertificateAuthority.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateDescription** | [**CertificateDescription**](CertificateDescription.md) |  |  [optional] |
|**certificateTemplate** | **String** | Immutable. The resource name for a CertificateTemplate used to issue this certificate, in the format &#x60;projects/_*_/locations/_*_/certificateTemplates/_*&#x60;. If this is specified, the caller must have the necessary permission to use this template. If this is omitted, no template will be used. This template must be in the same location as the Certificate. |  [optional] |
|**config** | [**CertificateConfig**](CertificateConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which this Certificate was created. |  [optional] [readonly] |
|**issuerCertificateAuthority** | **String** | Output only. The resource name of the issuing CertificateAuthority in the format &#x60;projects/_*_/locations/_*_/caPools/_*_/certificateAuthorities/_*&#x60;. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels with user-defined metadata. |  [optional] |
|**lifetime** | **String** | Required. Immutable. The desired lifetime of a certificate. Used to create the \&quot;not_before_time\&quot; and \&quot;not_after_time\&quot; fields inside an X.509 certificate. Note that the lifetime may be truncated if it would extend past the life of any certificate authority in the issuing chain. |  [optional] |
|**name** | **String** | Output only. The resource name for this Certificate in the format &#x60;projects/_*_/locations/_*_/caPools/_*_/certificates/_*&#x60;. |  [optional] [readonly] |
|**pemCertificate** | **String** | Output only. The pem-encoded, signed X.509 certificate. |  [optional] [readonly] |
|**pemCertificateChain** | **List&lt;String&gt;** | Output only. The chain that may be used to verify the X.509 certificate. Expected to be in issuer-to-root order according to RFC 5246. |  [optional] [readonly] |
|**pemCsr** | **String** | Immutable. A pem-encoded X.509 certificate signing request (CSR). |  [optional] |
|**revocationDetails** | [**RevocationDetails**](RevocationDetails.md) |  |  [optional] |
|**subjectMode** | [**SubjectModeEnum**](#SubjectModeEnum) | Immutable. Specifies how the Certificate&#39;s identity fields are to be decided. If this is omitted, the &#x60;DEFAULT&#x60; subject mode will be used. |  [optional] |
|**updateTime** | **String** | Output only. The time at which this Certificate was updated. |  [optional] [readonly] |



## Enum: SubjectModeEnum

| Name | Value |
|---- | -----|
| SUBJECT_REQUEST_MODE_UNSPECIFIED | &quot;SUBJECT_REQUEST_MODE_UNSPECIFIED&quot; |
| DEFAULT | &quot;DEFAULT&quot; |
| REFLECTED_SPIFFE | &quot;REFLECTED_SPIFFE&quot; |



