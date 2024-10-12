# CloudDocumentAiApi.GoogleCloudDocumentaiUiv1beta3TrainProcessorVersionMetadataDatasetValidation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasetErrorCount** | **Number** | The total number of dataset errors. | [optional] 
**datasetErrors** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | Error information for the dataset as a whole. A maximum of 10 dataset errors will be returned. A single dataset error is terminal for training. | [optional] 
**documentErrorCount** | **Number** | The total number of document errors. | [optional] 
**documentErrors** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | Error information pertaining to specific documents. A maximum of 10 document errors will be returned. Any document with errors will not be used throughout training. | [optional] 


