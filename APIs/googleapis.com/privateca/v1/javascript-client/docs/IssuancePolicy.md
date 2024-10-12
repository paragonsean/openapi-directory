# CertificateAuthorityApi.IssuancePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedIssuanceModes** | [**IssuanceModes**](IssuanceModes.md) |  | [optional] 
**allowedKeyTypes** | [**[AllowedKeyType]**](AllowedKeyType.md) | Optional. If any AllowedKeyType is specified, then the certificate request&#39;s public key must match one of the key types listed here. Otherwise, any key may be used. | [optional] 
**baselineValues** | [**X509Parameters**](X509Parameters.md) |  | [optional] 
**identityConstraints** | [**CertificateIdentityConstraints**](CertificateIdentityConstraints.md) |  | [optional] 
**maximumLifetime** | **String** | Optional. The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate&#39;s requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it. | [optional] 
**passthroughExtensions** | [**CertificateExtensionConstraints**](CertificateExtensionConstraints.md) |  | [optional] 


