

# GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause

A clause for defining a filter. A filter may be inclusive (events satisfying the filter clause are included in the subproperty's data) or exclusive (events satisfying the filter clause are excluded from the subproperty's data).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterClauseType** | [**FilterClauseTypeEnum**](#FilterClauseTypeEnum) | Required. The type for the filter clause. |  [optional] |
|**filterExpression** | [**GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression**](GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression.md) |  |  [optional] |



## Enum: FilterClauseTypeEnum

| Name | Value |
|---- | -----|
| FILTER_CLAUSE_TYPE_UNSPECIFIED | &quot;FILTER_CLAUSE_TYPE_UNSPECIFIED&quot; |
| INCLUDE | &quot;INCLUDE&quot; |
| EXCLUDE | &quot;EXCLUDE&quot; |



