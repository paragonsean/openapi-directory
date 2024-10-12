# WebApplicationFirewallManagement.WebApplicationFirewallPolicyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customRules** | [**CustomRuleList**](CustomRuleList.md) |  | [optional] 
**frontendEndpointLinks** | [**[FrontendEndpointLink]**](FrontendEndpointLink.md) | Describes Frontend Endpoints associated with this Web Application Firewall policy. | [optional] [readonly] 
**managedRules** | [**ManagedRuleSetList**](ManagedRuleSetList.md) |  | [optional] 
**policySettings** | [**PolicySettings**](PolicySettings.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the policy. | [optional] [readonly] 
**resourceState** | **String** |  | [optional] [readonly] 



## Enum: ResourceStateEnum


* `Creating` (value: `"Creating"`)

* `Enabling` (value: `"Enabling"`)

* `Enabled` (value: `"Enabled"`)

* `Disabling` (value: `"Disabling"`)

* `Disabled` (value: `"Disabled"`)

* `Deleting` (value: `"Deleting"`)




