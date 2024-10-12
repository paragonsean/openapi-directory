

# ConnectableResource

Describes the allowed inbound and outbound traffic of an Azure resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The Azure resource id |  [optional] [readonly] |
|**inboundConnectedResources** | [**List&lt;ConnectedResource&gt;**](ConnectedResource.md) | The list of Azure resources that the resource has inbound allowed connection from |  [optional] [readonly] |
|**outboundConnectedResources** | [**List&lt;ConnectedResource&gt;**](ConnectedResource.md) | The list of Azure resources that the resource has outbound allowed connection to |  [optional] [readonly] |



