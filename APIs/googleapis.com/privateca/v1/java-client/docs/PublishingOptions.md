

# PublishingOptions

Options relating to the publication of each CertificateAuthority's CA certificate and CRLs and their inclusion as extensions in issued Certificates. The options set here apply to certificates issued by any CertificateAuthority in the CaPool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encodingFormat** | [**EncodingFormatEnum**](#EncodingFormatEnum) | Optional. Specifies the encoding format of each CertificateAuthority&#39;s CA certificate and CRLs. If this is omitted, CA certificates and CRLs will be published in PEM. |  [optional] |
|**publishCaCert** | **Boolean** | Optional. When true, publishes each CertificateAuthority&#39;s CA certificate and includes its URL in the \&quot;Authority Information Access\&quot; X.509 extension in all issued Certificates. If this is false, the CA certificate will not be published and the corresponding X.509 extension will not be written in issued certificates. |  [optional] |
|**publishCrl** | **Boolean** | Optional. When true, publishes each CertificateAuthority&#39;s CRL and includes its URL in the \&quot;CRL Distribution Points\&quot; X.509 extension in all issued Certificates. If this is false, CRLs will not be published and the corresponding X.509 extension will not be written in issued certificates. CRLs will expire 7 days from their creation. However, we will rebuild daily. CRLs are also rebuilt shortly after a certificate is revoked. |  [optional] |



## Enum: EncodingFormatEnum

| Name | Value |
|---- | -----|
| ENCODING_FORMAT_UNSPECIFIED | &quot;ENCODING_FORMAT_UNSPECIFIED&quot; |
| PEM | &quot;PEM&quot; |
| DER | &quot;DER&quot; |



