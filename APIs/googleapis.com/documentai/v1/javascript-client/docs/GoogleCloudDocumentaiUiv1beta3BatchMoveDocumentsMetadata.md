# CloudDocumentAiApi.GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonMetadata** | [**GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata**](GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata.md) |  | [optional] 
**destDatasetType** | **String** | The destination dataset split type. | [optional] 
**destSplitType** | **String** | The destination dataset split type. | [optional] 
**individualBatchMoveStatuses** | [**[GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatus]**](GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatus.md) | The list of response details of each document. | [optional] 



## Enum: DestDatasetTypeEnum


* `TYPE_UNSPECIFIED` (value: `"DATASET_SPLIT_TYPE_UNSPECIFIED"`)

* `TRAIN` (value: `"DATASET_SPLIT_TRAIN"`)

* `TEST` (value: `"DATASET_SPLIT_TEST"`)

* `UNASSIGNED` (value: `"DATASET_SPLIT_UNASSIGNED"`)





## Enum: DestSplitTypeEnum


* `TYPE_UNSPECIFIED` (value: `"DATASET_SPLIT_TYPE_UNSPECIFIED"`)

* `TRAIN` (value: `"DATASET_SPLIT_TRAIN"`)

* `TEST` (value: `"DATASET_SPLIT_TEST"`)

* `UNASSIGNED` (value: `"DATASET_SPLIT_UNASSIGNED"`)




