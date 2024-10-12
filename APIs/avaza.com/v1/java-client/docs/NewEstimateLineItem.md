

# NewEstimateLineItem

Line item to be added to new Estimate

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Plain UTF8 text. (no HTML) |  [optional] |
|**discount** | **Double** | Enter 10.5 to give a 10.5% discount |  [optional] |
|**inventoryItemIDFK** | **Integer** | If not specified then Inventory Item Name must be specified. |  [optional] |
|**inventoryItemName** | **String** | If not specified then Inventory item ID must be specified. If specified and not matched to any existing inventory items then a new inventory item will be created. Max 200 characters. |  [optional] |
|**quantity** | **Double** | The quantity for the line item |  |
|**taxIDFK** | **Integer** | If specified then it must match an existing Tax ID. If not specified then Tax Name and Tax Percent must be specified. |  [optional] |
|**taxName** | **String** | Must be specified if the Tax ID is blank. If the Tax Name is specified it will be matched to an existing Tax Name or else a new Tax will be created. |  [optional] |
|**taxPercent** | **Double** | The Tax Percent will only be used if a new tax is being created. |  [optional] |
|**unitPrice** | **Double** | The unit price for the lineitem. |  |



