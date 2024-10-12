

# CertificatePolicy

Management policy for a certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**CertificateAttributes**](CertificateAttributes.md) |  |  [optional] |
|**id** | **String** | The certificate id. |  [optional] [readonly] |
|**issuer** | [**IssuerParameters**](IssuerParameters.md) |  |  [optional] |
|**keyProps** | [**KeyProperties**](KeyProperties.md) |  |  [optional] |
|**lifetimeActions** | [**List&lt;LifetimeAction&gt;**](LifetimeAction.md) | Actions that will be performed by Key Vault over the lifetime of a certificate. |  [optional] |
|**secretProps** | [**SecretProperties**](SecretProperties.md) |  |  [optional] |
|**x509Props** | [**X509CertificateProperties**](X509CertificateProperties.md) |  |  [optional] |



