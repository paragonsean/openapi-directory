

# VirtualNetworkRule

Virtual Network rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The action of virtual network rule. |  [optional] |
|**id** | **String** | Resource ID of a subnet, for example: /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}. |  |
|**state** | [**StateEnum**](#StateEnum) | Gets the state of virtual network rule. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PROVISIONING | &quot;provisioning&quot; |
| DEPROVISIONING | &quot;deprovisioning&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |
| NETWORK_SOURCE_DELETED | &quot;networkSourceDeleted&quot; |



