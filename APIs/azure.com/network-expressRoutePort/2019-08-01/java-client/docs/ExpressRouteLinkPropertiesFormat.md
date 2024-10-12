

# ExpressRouteLinkPropertiesFormat

Properties specific to ExpressRouteLink resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminState** | [**AdminStateEnum**](#AdminStateEnum) | Administrative state of the physical port. |  [optional] |
|**connectorType** | [**ConnectorTypeEnum**](#ConnectorTypeEnum) | Physical fiber port type. |  [optional] [readonly] |
|**interfaceName** | **String** | Name of Azure router interface. |  [optional] [readonly] |
|**macSecConfig** | [**ExpressRouteLinkMacSecConfig**](ExpressRouteLinkMacSecConfig.md) |  |  [optional] |
|**patchPanelId** | **String** | Mapping between physical port to patch panel port. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**rackId** | **String** | Mapping of physical patch panel to rack. |  [optional] [readonly] |
|**routerName** | **String** | Name of Azure router associated with physical port. |  [optional] [readonly] |



## Enum: AdminStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: ConnectorTypeEnum

| Name | Value |
|---- | -----|
| LC | &quot;LC&quot; |
| SC | &quot;SC&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



