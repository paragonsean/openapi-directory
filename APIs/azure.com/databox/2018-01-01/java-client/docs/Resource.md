

# Resource

Model of the Resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed. |  |
|**sku** | [**Sku**](Sku.md) |  |  |
|**tags** | **Map&lt;String, String&gt;** | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). |  [optional] |



