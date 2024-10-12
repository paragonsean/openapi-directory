

# Node

The node

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codeVersion** | **String** |  |  [optional] |
|**configVersion** | **String** |  |  [optional] |
|**faultDomain** | **String** |  |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |
|**id** | [**ClusterHealthNodeHealthStatesInnerId**](ClusterHealthNodeHealthStatesInnerId.md) |  |  [optional] |
|**instanceId** | **String** |  |  [optional] |
|**ipAddressOrFQDN** | **String** |  |  [optional] |
|**isSeedNode** | **Boolean** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**nodeDeactivationInfo** | [**NodeNodeDeactivationInfo**](NodeNodeDeactivationInfo.md) |  |  [optional] |
|**nodeStatus** | [**NodeStatusEnum**](#NodeStatusEnum) |  |  [optional] |
|**nodeUpTimeInSeconds** | **String** |  |  [optional] |
|**type** | **String** |  |  [optional] |
|**upgradeDomain** | **String** |  |  [optional] |



## Enum: NodeStatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| UP | &quot;Up&quot; |
| DOWN | &quot;Down&quot; |
| ENABLING | &quot;Enabling&quot; |
| DISABLING | &quot;Disabling&quot; |
| DISABLED | &quot;Disabled&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| REMOVED | &quot;Removed&quot; |



