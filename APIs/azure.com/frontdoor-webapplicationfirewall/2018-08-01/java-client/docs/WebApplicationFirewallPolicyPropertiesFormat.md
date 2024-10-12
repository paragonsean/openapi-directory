

# WebApplicationFirewallPolicyPropertiesFormat

Defines web application firewall policy properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customRules** | [**CustomRules**](CustomRules.md) |  |  [optional] |
|**managedRules** | [**ManagedRuleSets**](ManagedRuleSets.md) |  |  [optional] |
|**policySettings** | [**PolicySettings**](PolicySettings.md) |  |  [optional] |
|**provisioningState** | **String** | Provisioning state of the WebApplicationFirewallPolicy. |  [optional] [readonly] |
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



