

# AzureFirewallApplicationRuleCollectionPropertiesFormat

Properties of the application rule collection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**AzureFirewallRCAction**](AzureFirewallRCAction.md) |  |  [optional] |
|**priority** | **Integer** | Priority of the application rule collection resource. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**rules** | [**List&lt;AzureFirewallApplicationRule&gt;**](AzureFirewallApplicationRule.md) | Collection of rules used by a application rule collection. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



