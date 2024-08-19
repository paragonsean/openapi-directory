

# DimensionOrderBy

Sorts by dimension values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensionName** | **String** | A dimension name in the request to order by. |  [optional] |
|**orderType** | [**OrderTypeEnum**](#OrderTypeEnum) | Controls the rule for dimension value ordering. |  [optional] |



## Enum: OrderTypeEnum

| Name | Value |
|---- | -----|
| ORDER_TYPE_UNSPECIFIED | &quot;ORDER_TYPE_UNSPECIFIED&quot; |
| ALPHANUMERIC | &quot;ALPHANUMERIC&quot; |
| CASE_INSENSITIVE_ALPHANUMERIC | &quot;CASE_INSENSITIVE_ALPHANUMERIC&quot; |
| NUMERIC | &quot;NUMERIC&quot; |



