

# CertificateTemplate

A CertificateTemplate refers to a managed template for certificate issuance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time at which this CertificateTemplate was created. |  [optional] [readonly] |
|**description** | **String** | Optional. A human-readable description of scenarios this template is intended for. |  [optional] |
|**identityConstraints** | [**CertificateIdentityConstraints**](CertificateIdentityConstraints.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels with user-defined metadata. |  [optional] |
|**maximumLifetime** | **String** | Optional. The maximum lifetime allowed for issued Certificates that use this template. If the issuing CaPool&#39;s IssuancePolicy specifies a maximum_lifetime the minimum of the two durations will be the maximum lifetime for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate&#39;s requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it. |  [optional] |
|**name** | **String** | Output only. The resource name for this CertificateTemplate in the format &#x60;projects/_*_/locations/_*_/certificateTemplates/_*&#x60;. |  [optional] [readonly] |
|**passthroughExtensions** | [**CertificateExtensionConstraints**](CertificateExtensionConstraints.md) |  |  [optional] |
|**predefinedValues** | [**X509Parameters**](X509Parameters.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The time at which this CertificateTemplate was updated. |  [optional] [readonly] |



