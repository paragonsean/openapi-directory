

# RateDetails

The rate related settings of the inventory source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inventorySourceRateType** | [**InventorySourceRateTypeEnum**](#InventorySourceRateTypeEnum) | The rate type. Acceptable values are &#x60;INVENTORY_SOURCE_RATE_TYPE_CPM_FIXED&#x60;, &#x60;INVENTORY_SOURCE_RATE_TYPE_CPM_FLOOR&#x60;, and &#x60;INVENTORY_SOURCE_RATE_TYPE_CPD&#x60;. |  [optional] |
|**minimumSpend** | [**Money**](Money.md) |  |  [optional] |
|**rate** | [**Money**](Money.md) |  |  [optional] |
|**unitsPurchased** | **String** | Required for guaranteed inventory sources. The number of impressions guaranteed by the seller. |  [optional] |



## Enum: InventorySourceRateTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INVENTORY_SOURCE_RATE_TYPE_UNSPECIFIED&quot; |
| CPM_FIXED | &quot;INVENTORY_SOURCE_RATE_TYPE_CPM_FIXED&quot; |
| CPM_FLOOR | &quot;INVENTORY_SOURCE_RATE_TYPE_CPM_FLOOR&quot; |
| CPD | &quot;INVENTORY_SOURCE_RATE_TYPE_CPD&quot; |
| FLAT | &quot;INVENTORY_SOURCE_RATE_TYPE_FLAT&quot; |



