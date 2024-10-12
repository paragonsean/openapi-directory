

# MetricFilterClause

Represents a group of metric filters. Set the operator value to specify how the filters are logically combined.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filters** | [**List&lt;MetricFilter&gt;**](MetricFilter.md) | The repeated set of filters. They are logically combined based on the operator specified. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | The operator for combining multiple metric filters. If unspecified, it is treated as an &#x60;OR&#x60;. |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| OPERATOR_UNSPECIFIED | &quot;OPERATOR_UNSPECIFIED&quot; |
| OR | &quot;OR&quot; |
| AND | &quot;AND&quot; |



