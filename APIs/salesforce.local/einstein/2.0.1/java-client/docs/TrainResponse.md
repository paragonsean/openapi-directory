

# TrainResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | **String** | Algorithm used to create the model. Returned only when the modelType is image-detection. |  [optional] |
|**createdAt** | **OffsetDateTime** | Date and time that the model was created. |  [optional] |
|**datasetId** | **Long** | ID of the dataset trained to create the model. |  |
|**datasetVersionId** | **Long** | Not available yet |  |
|**epochs** | **Integer** | Number of epochs used during training. |  [optional] |
|**failureMsg** | **String** | Reason the dataset training failed. Returned only if the training status is FAILED. |  [optional] |
|**language** | **String** | Model language inherited from the dataset language. For image datasets, default is N/A. For text datasets, default is en_US. |  |
|**learningRate** | **Double** | Learning rate used during training. |  [optional] |
|**modelId** | **String** | ID of the model. Contains letters and numbers. |  |
|**modelType** | **String** | Type of data from which the model was created. |  [optional] |
|**name** | **String** | Name of the model. |  |
|**_object** | **String** | Object returned; in this case, training. |  [optional] |
|**progress** | **BigDecimal** | How far the dataset training has progressed. Values are between 0�1. |  |
|**queuePosition** | **Integer** | Where the training job is in the queue. This field appears in the response only if the status is QUEUED. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the model. |  |
|**trainParams** | **String** | Training parameters passed into the request. |  [optional] |
|**trainStats** | **String** | Returns null when you train a dataset. Training statistics are returned when the status is SUCCEEDED or FAILED. |  [optional] |
|**updatedAt** | **OffsetDateTime** | Date and time that the model was last updated. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;QUEUED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| KILLED | &quot;KILLED&quot; |
| FAILED_WITH_RETRIES | &quot;FAILED_WITH_RETRIES&quot; |



