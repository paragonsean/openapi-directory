

# TrainResult

Custom model training result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averageModelAccuracy** | **BigDecimal** | Average accuracy. |  [optional] |
|**errors** | [**List&lt;ErrorInformation&gt;**](ErrorInformation.md) | Errors returned during the training operation. |  [optional] |
|**fields** | [**List&lt;FormFieldsReport&gt;**](FormFieldsReport.md) | List of fields used to train the model and the train operation error reported by each. |  [optional] |
|**trainingDocuments** | [**List&lt;TrainingDocumentInfo&gt;**](TrainingDocumentInfo.md) | List of the documents used to train the model and any errors reported in each document. |  |



