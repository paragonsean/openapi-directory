# DisplayVideo360Api.RateDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventorySourceRateType** | **String** | The rate type. Acceptable values are &#x60;INVENTORY_SOURCE_RATE_TYPE_CPM_FIXED&#x60;, &#x60;INVENTORY_SOURCE_RATE_TYPE_CPM_FLOOR&#x60;, and &#x60;INVENTORY_SOURCE_RATE_TYPE_CPD&#x60;. | [optional] 
**minimumSpend** | [**Money**](Money.md) |  | [optional] 
**rate** | [**Money**](Money.md) |  | [optional] 
**unitsPurchased** | **String** | Required for guaranteed inventory sources. The number of impressions guaranteed by the seller. | [optional] 



## Enum: InventorySourceRateTypeEnum


* `UNSPECIFIED` (value: `"INVENTORY_SOURCE_RATE_TYPE_UNSPECIFIED"`)

* `CPM_FIXED` (value: `"INVENTORY_SOURCE_RATE_TYPE_CPM_FIXED"`)

* `CPM_FLOOR` (value: `"INVENTORY_SOURCE_RATE_TYPE_CPM_FLOOR"`)

* `CPD` (value: `"INVENTORY_SOURCE_RATE_TYPE_CPD"`)

* `FLAT` (value: `"INVENTORY_SOURCE_RATE_TYPE_FLAT"`)




