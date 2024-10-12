# CloudIdentityApi.InboundSsoAssignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | **String** | Immutable. The customer. For example: &#x60;customers/C0123abc&#x60;. | [optional] 
**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Inbound SSO Assignment. | [optional] [readonly] 
**rank** | **Number** | Must be zero (which is the default value so it can be omitted) for assignments with &#x60;target_org_unit&#x60; set and must be greater-than-or-equal-to one for assignments with &#x60;target_group&#x60; set. | [optional] 
**samlSsoInfo** | [**SamlSsoInfo**](SamlSsoInfo.md) |  | [optional] 
**signInBehavior** | [**SignInBehavior**](SignInBehavior.md) |  | [optional] 
**ssoMode** | **String** | Inbound SSO behavior. | [optional] 
**targetGroup** | **String** | Immutable. Must be of the form &#x60;groups/{group}&#x60;. | [optional] 
**targetOrgUnit** | **String** | Immutable. Must be of the form &#x60;orgUnits/{org_unit}&#x60;. | [optional] 



## Enum: SsoModeEnum


* `SSO_MODE_UNSPECIFIED` (value: `"SSO_MODE_UNSPECIFIED"`)

* `SSO_OFF` (value: `"SSO_OFF"`)

* `SAML_SSO` (value: `"SAML_SSO"`)

* `DOMAIN_WIDE_SAML_IF_ENABLED` (value: `"DOMAIN_WIDE_SAML_IF_ENABLED"`)




