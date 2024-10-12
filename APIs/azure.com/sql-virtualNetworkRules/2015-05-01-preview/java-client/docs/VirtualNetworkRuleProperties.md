

# VirtualNetworkRuleProperties

Properties of a virtual network rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ignoreMissingVnetServiceEndpoint** | **Boolean** | Create firewall rule before the virtual network has vnet service endpoint enabled. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Virtual Network Rule State |  [optional] [readonly] |
|**virtualNetworkSubnetId** | **String** | The ARM resource id of the virtual network subnet. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| INITIALIZING | &quot;Initializing&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| READY | &quot;Ready&quot; |
| DELETING | &quot;Deleting&quot; |
| UNKNOWN | &quot;Unknown&quot; |



