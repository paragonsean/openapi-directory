

# TrainResult

Response of the Train API call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;FormOperationError&gt;**](FormOperationError.md) | Errors returned during the training operation. |  [optional] |
|**modelId** | **UUID** | Identifier of the model. |  [optional] |
|**trainingDocuments** | [**List&lt;FormDocumentReport&gt;**](FormDocumentReport.md) | List of documents used to train the model and the  train operation error reported by each. |  [optional] |



