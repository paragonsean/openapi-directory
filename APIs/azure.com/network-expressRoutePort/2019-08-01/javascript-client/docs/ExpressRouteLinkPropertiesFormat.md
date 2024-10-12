# NetworkManagementClient.ExpressRouteLinkPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminState** | **String** | Administrative state of the physical port. | [optional] 
**connectorType** | **String** | Physical fiber port type. | [optional] [readonly] 
**interfaceName** | **String** | Name of Azure router interface. | [optional] [readonly] 
**macSecConfig** | [**ExpressRouteLinkMacSecConfig**](ExpressRouteLinkMacSecConfig.md) |  | [optional] 
**patchPanelId** | **String** | Mapping between physical port to patch panel port. | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**rackId** | **String** | Mapping of physical patch panel to rack. | [optional] [readonly] 
**routerName** | **String** | Name of Azure router associated with physical port. | [optional] [readonly] 



## Enum: AdminStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ConnectorTypeEnum


* `LC` (value: `"LC"`)

* `SC` (value: `"SC"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




