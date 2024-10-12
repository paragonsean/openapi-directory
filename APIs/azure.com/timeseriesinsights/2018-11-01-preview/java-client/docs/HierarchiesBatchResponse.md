

# HierarchiesBatchResponse

Response of a single operation on a batch of time series hierarchies. Only one of \"get\", \"put\" or \"delete\" will be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delete** | **List&lt;TsiErrorBody&gt;** | List of error objects corresponding by position to the \&quot;delete\&quot; array in the request - null when the operation is successful. |  [optional] [readonly] |
|**get** | [**List&lt;TimeSeriesHierarchyOrError&gt;**](TimeSeriesHierarchyOrError.md) | List of hierarchy or error objects corresponding by position to the \&quot;get\&quot; array in the request. Hierarchy object is set when operation is successful and error object is set when operation is unsuccessful. |  [optional] [readonly] |
|**put** | [**List&lt;TimeSeriesHierarchyOrError&gt;**](TimeSeriesHierarchyOrError.md) | List of hierarchy or error object corresponding by position to the \&quot;put\&quot; array in the request. Hierarchy object is set when operation is successful and error object is set when operation is unsuccessful. |  [optional] [readonly] |



