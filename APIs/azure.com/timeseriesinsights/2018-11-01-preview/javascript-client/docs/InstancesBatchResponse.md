# TimeSeriesInsightsClient.InstancesBatchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_delete** | [**[TsiErrorBody]**](TsiErrorBody.md) | List of error objects corresponding by position to the \&quot;delete\&quot; array in the request. Null means the instance has been deleted, or did not exist. Error object is set when operation is unsuccessful (e.g. when there are events associated with this time series instance). | [optional] [readonly] 
**get** | [**[InstanceOrError]**](InstanceOrError.md) | List of instance or error objects corresponding by position to the \&quot;get\&quot; array in the request. Instance object is set when operation is successful and error object is set when operation is unsuccessful. | [optional] [readonly] 
**put** | [**[InstanceOrError]**](InstanceOrError.md) | List of error objects corresponding by position to the \&quot;put\&quot; array in the request. Error object is set when operation is unsuccessful. | [optional] [readonly] 
**update** | [**[InstanceOrError]**](InstanceOrError.md) | List of error objects corresponding by position to the \&quot;update\&quot; array in the request. Instance object is set when operation is successful and error object is set when operation is unsuccessful. | [optional] [readonly] 


