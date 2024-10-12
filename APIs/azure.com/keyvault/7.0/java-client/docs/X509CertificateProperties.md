

# X509CertificateProperties

Properties of the X509 component of a certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ekus** | **List&lt;String&gt;** | The enhanced key usage. |  [optional] |
|**keyUsage** | [**List&lt;KeyUsageEnum&gt;**](#List&lt;KeyUsageEnum&gt;) | List of key usages. |  [optional] |
|**sans** | [**SubjectAlternativeNames**](SubjectAlternativeNames.md) |  |  [optional] |
|**subject** | **String** | The subject name. Should be a valid X509 distinguished Name. |  [optional] |
|**validityMonths** | **Integer** | The duration that the certificate is valid in months. |  [optional] |



## Enum: List&lt;KeyUsageEnum&gt;

| Name | Value |
|---- | -----|
| DIGITAL_SIGNATURE | &quot;digitalSignature&quot; |
| NON_REPUDIATION | &quot;nonRepudiation&quot; |
| KEY_ENCIPHERMENT | &quot;keyEncipherment&quot; |
| DATA_ENCIPHERMENT | &quot;dataEncipherment&quot; |
| KEY_AGREEMENT | &quot;keyAgreement&quot; |
| KEY_CERT_SIGN | &quot;keyCertSign&quot; |
| C_RL_SIGN | &quot;cRLSign&quot; |
| ENCIPHER_ONLY | &quot;encipherOnly&quot; |
| DECIPHER_ONLY | &quot;decipherOnly&quot; |



