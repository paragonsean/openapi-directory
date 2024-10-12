

# Region

Represents a geographic region that you can use as a target with both the `RegionalInventory` and `ShippingSettings` services. You can define regions as collections of either postal codes or, in some countries, using predefined geotargets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The display name of the region. |  [optional] |
|**geotargetArea** | [**RegionGeoTargetArea**](RegionGeoTargetArea.md) |  |  [optional] |
|**merchantId** | **String** | Output only. Immutable. Merchant that owns the region. |  [optional] [readonly] |
|**postalCodeArea** | [**RegionPostalCodeArea**](RegionPostalCodeArea.md) |  |  [optional] |
|**regionId** | **String** | Output only. Immutable. The ID uniquely identifying each region. |  [optional] [readonly] |
|**regionalInventoryEligible** | **Boolean** | Output only. Indicates if the region is eligible to use in the Regional Inventory configuration. |  [optional] [readonly] |
|**shippingEligible** | **Boolean** | Output only. Indicates if the region is eligible to use in the Shipping Services configuration. |  [optional] [readonly] |



