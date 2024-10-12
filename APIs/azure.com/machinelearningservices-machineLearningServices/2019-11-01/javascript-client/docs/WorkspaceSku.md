# AzureMachineLearningWorkspaces.WorkspaceSku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**[SKUCapability]**](SKUCapability.md) | List of features/user capabilities associated with the sku | [optional] [readonly] 
**locationInfo** | [**[ResourceSkuLocationInfo]**](ResourceSkuLocationInfo.md) | A list of locations and availability zones in those locations where the SKU is available. | [optional] [readonly] 
**locations** | **[String]** | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). | [optional] [readonly] 
**name** | **String** |  | [optional] [readonly] 
**resourceType** | **String** |  | [optional] [readonly] 
**restrictions** | [**[Restriction]**](Restriction.md) | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. | [optional] 
**tier** | **String** | Sku Tier like Basic or Enterprise | [optional] [readonly] 


