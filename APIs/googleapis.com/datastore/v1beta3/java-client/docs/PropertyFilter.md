

# PropertyFilter

A filter on a specific property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**op** | [**OpEnum**](#OpEnum) | The operator to filter by. |  [optional] |
|**property** | [**PropertyReference**](PropertyReference.md) |  |  [optional] |
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
| IN | &quot;IN&quot; |
| NOT_EQUAL | &quot;NOT_EQUAL&quot; |
| HAS_ANCESTOR | &quot;HAS_ANCESTOR&quot; |
| NOT_IN | &quot;NOT_IN&quot; |



