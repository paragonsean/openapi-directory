

# JobResource

Job Resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Id of the object. |  [optional] [readonly] |
|**name** | **String** | Name of the object. |  [optional] [readonly] |
|**properties** | [**JobProperties**](JobProperties.md) |  |  |
|**type** | **String** | Type of the object. |  [optional] [readonly] |
|**location** | **String** | The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. |  |
|**sku** | [**Sku**](Sku.md) |  |  |
|**tags** | **Map&lt;String, String&gt;** | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). |  [optional] |



