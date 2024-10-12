

# WorkspaceSku

Describes Workspace Sku details and features

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**List&lt;SKUCapability&gt;**](SKUCapability.md) | List of features/user capabilities associated with the sku |  [optional] [readonly] |
|**locationInfo** | [**List&lt;ResourceSkuLocationInfo&gt;**](ResourceSkuLocationInfo.md) | A list of locations and availability zones in those locations where the SKU is available. |  [optional] [readonly] |
|**locations** | **List&lt;String&gt;** | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). |  [optional] [readonly] |
|**name** | **String** |  |  [optional] [readonly] |
|**resourceType** | **String** |  |  [optional] [readonly] |
|**restrictions** | [**List&lt;Restriction&gt;**](Restriction.md) | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |  [optional] |
|**tier** | **String** | Sku Tier like Basic or Enterprise |  [optional] [readonly] |



