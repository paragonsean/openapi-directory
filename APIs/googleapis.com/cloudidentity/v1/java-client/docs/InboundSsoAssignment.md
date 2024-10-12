

# InboundSsoAssignment

Targets with \"set\" SSO assignments and their respective assignments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | **String** | Immutable. The customer. For example: &#x60;customers/C0123abc&#x60;. |  [optional] |
|**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Inbound SSO Assignment. |  [optional] [readonly] |
|**rank** | **Integer** | Must be zero (which is the default value so it can be omitted) for assignments with &#x60;target_org_unit&#x60; set and must be greater-than-or-equal-to one for assignments with &#x60;target_group&#x60; set. |  [optional] |
|**samlSsoInfo** | [**SamlSsoInfo**](SamlSsoInfo.md) |  |  [optional] |
|**signInBehavior** | [**SignInBehavior**](SignInBehavior.md) |  |  [optional] |
|**ssoMode** | [**SsoModeEnum**](#SsoModeEnum) | Inbound SSO behavior. |  [optional] |
|**targetGroup** | **String** | Immutable. Must be of the form &#x60;groups/{group}&#x60;. |  [optional] |
|**targetOrgUnit** | **String** | Immutable. Must be of the form &#x60;orgUnits/{org_unit}&#x60;. |  [optional] |



## Enum: SsoModeEnum

| Name | Value |
|---- | -----|
| SSO_MODE_UNSPECIFIED | &quot;SSO_MODE_UNSPECIFIED&quot; |
| SSO_OFF | &quot;SSO_OFF&quot; |
| SAML_SSO | &quot;SAML_SSO&quot; |
| DOMAIN_WIDE_SAML_IF_ENABLED | &quot;DOMAIN_WIDE_SAML_IF_ENABLED&quot; |



