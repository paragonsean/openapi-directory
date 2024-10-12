

# InboundSamlSsoProfile

A [SAML 2.0](https://www.oasis-open.org/standards#samlv2.0) federation between a Google enterprise customer and a SAML identity provider.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | **String** | Immutable. The customer. For example: &#x60;customers/C0123abc&#x60;. |  [optional] |
|**displayName** | **String** | Human-readable name of the SAML SSO profile. |  [optional] |
|**idpConfig** | [**SamlIdpConfig**](SamlIdpConfig.md) |  |  [optional] |
|**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the SAML SSO profile. |  [optional] [readonly] |
|**spConfig** | [**SamlSpConfig**](SamlSpConfig.md) |  |  [optional] |



