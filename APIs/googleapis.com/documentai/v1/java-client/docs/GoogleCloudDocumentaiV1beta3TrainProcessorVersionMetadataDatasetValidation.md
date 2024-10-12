

# GoogleCloudDocumentaiV1beta3TrainProcessorVersionMetadataDatasetValidation

The dataset validation information. This includes any and all errors with documents and the dataset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetErrorCount** | **Integer** | The total number of dataset errors. |  [optional] |
|**datasetErrors** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | Error information for the dataset as a whole. A maximum of 10 dataset errors will be returned. A single dataset error is terminal for training. |  [optional] |
|**documentErrorCount** | **Integer** | The total number of document errors. |  [optional] |
|**documentErrors** | [**List&lt;GoogleRpcStatus&gt;**](GoogleRpcStatus.md) | Error information pertaining to specific documents. A maximum of 10 document errors will be returned. Any document with errors will not be used throughout training. |  [optional] |



