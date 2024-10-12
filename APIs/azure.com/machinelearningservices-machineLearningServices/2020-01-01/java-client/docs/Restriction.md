

# Restriction

The restriction because of which SKU cannot be used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reasonCode** | [**ReasonCodeEnum**](#ReasonCodeEnum) | The reason for the restriction. |  [optional] |
|**type** | **String** | The type of restrictions. As of now only possible value for this is location. |  [optional] [readonly] |
|**values** | **List&lt;String&gt;** | The value of restrictions. If the restriction type is set to location. This would be different locations where the SKU is restricted. |  [optional] [readonly] |



## Enum: ReasonCodeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| NOT_AVAILABLE_FOR_REGION | &quot;NotAvailableForRegion&quot; |
| NOT_AVAILABLE_FOR_SUBSCRIPTION | &quot;NotAvailableForSubscription&quot; |



