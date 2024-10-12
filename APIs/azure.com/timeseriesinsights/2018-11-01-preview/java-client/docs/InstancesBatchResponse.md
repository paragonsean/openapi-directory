

# InstancesBatchResponse

Response of a single operation on a batch of instances. Only one of \"get\", \"put\", \"update\" or \"delete\" will be set based on the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delete** | **List&lt;TsiErrorBody&gt;** | List of error objects corresponding by position to the \&quot;delete\&quot; array in the request. Null means the instance has been deleted, or did not exist. Error object is set when operation is unsuccessful (e.g. when there are events associated with this time series instance). |  [optional] [readonly] |
|**get** | [**List&lt;InstanceOrError&gt;**](InstanceOrError.md) | List of instance or error objects corresponding by position to the \&quot;get\&quot; array in the request. Instance object is set when operation is successful and error object is set when operation is unsuccessful. |  [optional] [readonly] |
|**put** | [**List&lt;InstanceOrError&gt;**](InstanceOrError.md) | List of error objects corresponding by position to the \&quot;put\&quot; array in the request. Error object is set when operation is unsuccessful. |  [optional] [readonly] |
|**update** | [**List&lt;InstanceOrError&gt;**](InstanceOrError.md) | List of error objects corresponding by position to the \&quot;update\&quot; array in the request. Instance object is set when operation is successful and error object is set when operation is unsuccessful. |  [optional] [readonly] |



