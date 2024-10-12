

# SignalRCreateParameters

Parameters for SignalR service create/update operation.    Keep the same schema as AzSignalR.Models.SignalRResource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | Azure GEO region: e.g. West US | East US | North Central US | South Central US | West Europe | North Europe | East Asia | Southeast Asia | etc.   The geo region of a resource never changes after it is created. |  |
|**properties** | [**SignalRCreateOrUpdateProperties**](SignalRCreateOrUpdateProperties.md) |  |  [optional] |
|**sku** | [**ResourceSku**](ResourceSku.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A list of key value pairs that describe the resource. |  [optional] |



