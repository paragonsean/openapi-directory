# CertificateAuthorityApi.PublishingOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encodingFormat** | **String** | Optional. Specifies the encoding format of each CertificateAuthority&#39;s CA certificate and CRLs. If this is omitted, CA certificates and CRLs will be published in PEM. | [optional] 
**publishCaCert** | **Boolean** | Optional. When true, publishes each CertificateAuthority&#39;s CA certificate and includes its URL in the \&quot;Authority Information Access\&quot; X.509 extension in all issued Certificates. If this is false, the CA certificate will not be published and the corresponding X.509 extension will not be written in issued certificates. | [optional] 
**publishCrl** | **Boolean** | Optional. When true, publishes each CertificateAuthority&#39;s CRL and includes its URL in the \&quot;CRL Distribution Points\&quot; X.509 extension in all issued Certificates. If this is false, CRLs will not be published and the corresponding X.509 extension will not be written in issued certificates. CRLs will expire 7 days from their creation. However, we will rebuild daily. CRLs are also rebuilt shortly after a certificate is revoked. | [optional] 



## Enum: EncodingFormatEnum


* `ENCODING_FORMAT_UNSPECIFIED` (value: `"ENCODING_FORMAT_UNSPECIFIED"`)

* `PEM` (value: `"PEM"`)

* `DER` (value: `"DER"`)




