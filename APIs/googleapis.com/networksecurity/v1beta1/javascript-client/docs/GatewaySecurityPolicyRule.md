# NetworkSecurityApi.GatewaySecurityPolicyRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationMatcher** | **String** | Optional. CEL expression for matching on L7/application level criteria. | [optional] 
**basicProfile** | **String** | Required. Profile which tells what the primitive action should be. | [optional] 
**createTime** | **String** | Output only. Time when the rule was created. | [optional] [readonly] 
**description** | **String** | Optional. Free-text description of the resource. | [optional] 
**enabled** | **Boolean** | Required. Whether the rule is enforced. | [optional] 
**name** | **String** | Required. Immutable. Name of the resource. ame is the full resource name so projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}/rules/{rule} rule should match the pattern: (^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). | [optional] 
**priority** | **Number** | Required. Priority of the rule. Lower number corresponds to higher precedence. | [optional] 
**sessionMatcher** | **String** | Required. CEL expression for matching on session criteria. | [optional] 
**tlsInspectionEnabled** | **Boolean** | Optional. Flag to enable TLS inspection of traffic matching on , can only be true if the parent GatewaySecurityPolicy references a TLSInspectionConfig. | [optional] 
**updateTime** | **String** | Output only. Time when the rule was updated. | [optional] [readonly] 



## Enum: BasicProfileEnum


* `BASIC_PROFILE_UNSPECIFIED` (value: `"BASIC_PROFILE_UNSPECIFIED"`)

* `ALLOW` (value: `"ALLOW"`)

* `DENY` (value: `"DENY"`)




