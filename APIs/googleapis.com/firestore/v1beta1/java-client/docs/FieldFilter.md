

# FieldFilter

A filter on a specific field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldReference**](FieldReference.md) |  |  [optional] |
|**op** | [**OpEnum**](#OpEnum) | The operator to filter by. |  [optional] |
|**value** | [**Value**](Value.md) |  |  [optional] |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| OPERATOR_UNSPECIFIED | &quot;OPERATOR_UNSPECIFIED&quot; |
| LESS_THAN | &quot;LESS_THAN&quot; |
| LESS_THAN_OR_EQUAL | &quot;LESS_THAN_OR_EQUAL&quot; |
| GREATER_THAN | &quot;GREATER_THAN&quot; |
| GREATER_THAN_OR_EQUAL | &quot;GREATER_THAN_OR_EQUAL&quot; |
| EQUAL | &quot;EQUAL&quot; |
| NOT_EQUAL | &quot;NOT_EQUAL&quot; |
| ARRAY_CONTAINS | &quot;ARRAY_CONTAINS&quot; |
| IN | &quot;IN&quot; |
| ARRAY_CONTAINS_ANY | &quot;ARRAY_CONTAINS_ANY&quot; |
| NOT_IN | &quot;NOT_IN&quot; |



