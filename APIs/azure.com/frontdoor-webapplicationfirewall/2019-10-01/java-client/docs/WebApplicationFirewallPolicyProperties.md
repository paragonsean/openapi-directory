

# WebApplicationFirewallPolicyProperties

Defines web application firewall policy properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customRules** | [**CustomRuleList**](CustomRuleList.md) |  |  [optional] |
|**frontendEndpointLinks** | [**List&lt;FrontendEndpointLink&gt;**](FrontendEndpointLink.md) | Describes Frontend Endpoints associated with this Web Application Firewall policy. |  [optional] [readonly] |
|**managedRules** | [**ManagedRuleSetList**](ManagedRuleSetList.md) |  |  [optional] |
|**policySettings** | [**PolicySettings**](PolicySettings.md) |  |  [optional] |
|**provisioningState** | **String** | Provisioning state of the policy. |  [optional] [readonly] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) |  |  [optional] [readonly] |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| ENABLING | &quot;Enabling&quot; |
| ENABLED | &quot;Enabled&quot; |
| DISABLING | &quot;Disabling&quot; |
| DISABLED | &quot;Disabled&quot; |
| DELETING | &quot;Deleting&quot; |



