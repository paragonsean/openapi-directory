# ComputeManagementClient.ResourceSku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersions** | **[String]** | The api versions that support this SKU. | [optional] [readonly] 
**capabilities** | [**[ResourceSkuCapabilities]**](ResourceSkuCapabilities.md) | A name value pair to describe the capability. | [optional] [readonly] 
**capacity** | [**ResourceSkuCapacity**](ResourceSkuCapacity.md) |  | [optional] 
**costs** | [**[ResourceSkuCosts]**](ResourceSkuCosts.md) | Metadata for retrieving price info. | [optional] [readonly] 
**family** | **String** | The Family of this particular SKU. | [optional] [readonly] 
**kind** | **String** | The Kind of resources that are supported in this SKU. | [optional] [readonly] 
**locationInfo** | [**[ResourceSkuLocationInfo]**](ResourceSkuLocationInfo.md) | A list of locations and availability zones in those locations where the SKU is available. | [optional] [readonly] 
**locations** | **[String]** | The set of locations that the SKU is available. | [optional] [readonly] 
**name** | **String** | The name of SKU. | [optional] [readonly] 
**resourceType** | **String** | The type of resource the SKU applies to. | [optional] [readonly] 
**restrictions** | [**[ResourceSkuRestrictions]**](ResourceSkuRestrictions.md) | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. | [optional] [readonly] 
**size** | **String** | The Size of the SKU. | [optional] [readonly] 
**tier** | **String** | Specifies the tier of virtual machines in a scale set.&lt;br /&gt;&lt;br /&gt; Possible Values:&lt;br /&gt;&lt;br /&gt; **Standard**&lt;br /&gt;&lt;br /&gt; **Basic** | [optional] [readonly] 


