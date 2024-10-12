# TimeSeriesInsightsClient.HierarchiesBatchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_delete** | [**[TsiErrorBody]**](TsiErrorBody.md) | List of error objects corresponding by position to the \&quot;delete\&quot; array in the request - null when the operation is successful. | [optional] [readonly] 
**get** | [**[TimeSeriesHierarchyOrError]**](TimeSeriesHierarchyOrError.md) | List of hierarchy or error objects corresponding by position to the \&quot;get\&quot; array in the request. Hierarchy object is set when operation is successful and error object is set when operation is unsuccessful. | [optional] [readonly] 
**put** | [**[TimeSeriesHierarchyOrError]**](TimeSeriesHierarchyOrError.md) | List of hierarchy or error object corresponding by position to the \&quot;put\&quot; array in the request. Hierarchy object is set when operation is successful and error object is set when operation is unsuccessful. | [optional] [readonly] 


