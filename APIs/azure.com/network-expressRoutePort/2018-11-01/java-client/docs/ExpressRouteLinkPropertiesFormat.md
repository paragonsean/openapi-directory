

# ExpressRouteLinkPropertiesFormat

Properties specific to ExpressRouteLink resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminState** | [**AdminStateEnum**](#AdminStateEnum) | Administrative state of the physical port |  [optional] |
|**connectorType** | [**ConnectorTypeEnum**](#ConnectorTypeEnum) | Physical fiber port type. |  [optional] [readonly] |
|**interfaceName** | **String** | Name of Azure router interface. |  [optional] [readonly] |
|**patchPanelId** | **String** | Mapping between physical port to patch panel port. |  [optional] [readonly] |
|**provisioningState** | **String** | The provisioning state of the ExpressRouteLink resource. Possible values are: &#39;Succeeded&#39;, &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] [readonly] |
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



