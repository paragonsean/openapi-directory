# StorageCacheMgmtClient.ResourceSku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**[ResourceSkuCapabilities]**](ResourceSkuCapabilities.md) | A list of capabilities of this SKU, such as throughput or ops/sec. | [optional] 
**locationInfo** | [**[ResourceSkuLocationInfo]**](ResourceSkuLocationInfo.md) | The set of locations that the SKU is available. | [optional] 
**locations** | **[String]** | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g., West US, East US, Southeast Asia, etc.). | [optional] [readonly] 
**name** | **String** | The name of this SKU. | [optional] 
**resourceType** | **String** | The type of resource the SKU applies to. | [optional] [readonly] 
**restrictions** | [**[Restriction]**](Restriction.md) | The restrictions preventing this SKU from being used. This is empty if there are no restrictions. | [optional] 


