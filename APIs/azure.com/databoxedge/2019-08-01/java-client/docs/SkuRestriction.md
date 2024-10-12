

# SkuRestriction

The restrictions because of which SKU cannot be used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reasonCode** | [**ReasonCodeEnum**](#ReasonCodeEnum) | The SKU restriction reason. |  [optional] [readonly] |
|**restrictionInfo** | [**SkuRestrictionInfo**](SkuRestrictionInfo.md) |  |  [optional] |
|**type** | **String** | The type of the restriction. |  [optional] [readonly] |
|**values** | **List&lt;String&gt;** | The locations where sku is restricted. |  [optional] [readonly] |



## Enum: ReasonCodeEnum

| Name | Value |
|---- | -----|
| NOT_AVAILABLE_FOR_SUBSCRIPTION | &quot;NotAvailableForSubscription&quot; |
| QUOTA_ID | &quot;QuotaId&quot; |



