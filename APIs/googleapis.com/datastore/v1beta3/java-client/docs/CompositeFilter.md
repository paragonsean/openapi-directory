

# CompositeFilter

A filter that merges multiple other filters using the given operator.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filters** | [**List&lt;Filter&gt;**](Filter.md) | The list of filters to combine. Requires: * At least one filter is present. |  [optional] |
|**op** | [**OpEnum**](#OpEnum) | The operator for combining multiple filters. |  [optional] |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| OPERATOR_UNSPECIFIED | &quot;OPERATOR_UNSPECIFIED&quot; |
| AND | &quot;AND&quot; |
| OR | &quot;OR&quot; |



