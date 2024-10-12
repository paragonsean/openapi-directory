

# ResourceSkusListSkus200ResponseValueInnerRestrictionsInner

Describes scaling information of a SKU.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reasonCode** | [**ReasonCodeEnum**](#ReasonCodeEnum) | The reason code for restriction. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of restrictions. |  [optional] [readonly] |
|**values** | **List&lt;String&gt;** | The value of restrictions. If the restriction type is set to location. This would be different locations where the SKU is restricted. |  [optional] [readonly] |



## Enum: ReasonCodeEnum

| Name | Value |
|---- | -----|
| QUOTA_ID | &quot;QuotaId&quot; |
| NOT_AVAILABLE_FOR_SUBSCRIPTION | &quot;NotAvailableForSubscription&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LOCATION | &quot;location&quot; |



