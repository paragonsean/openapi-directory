# AzureMlCommitmentPlansManagementClient.CatalogSku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**[SkuCapability]**](SkuCapability.md) | The capability information for the specified SKU. | [optional] [readonly] 
**capacity** | [**SkuCapacity**](SkuCapacity.md) |  | [optional] 
**costs** | [**[SkuCost]**](SkuCost.md) | The cost information for the specified SKU. | [optional] [readonly] 
**locations** | **[String]** | Regions where the SKU is available. | [optional] [readonly] 
**name** | **String** | SKU name | [optional] [readonly] 
**resourceType** | **String** | Resource type name | [optional] [readonly] 
**restrictions** | [**[SkuRestrictions]**](SkuRestrictions.md) | Restrictions which would prevent a SKU from being used. This is empty if there are no restrictions. | [optional] [readonly] 
**tier** | **String** | SKU tier | [optional] [readonly] 


