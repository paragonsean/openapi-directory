

# GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadata


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonMetadata** | [**GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata**](GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata.md) |  |  [optional] |
|**destDatasetType** | [**DestDatasetTypeEnum**](#DestDatasetTypeEnum) | The destination dataset split type. |  [optional] |
|**destSplitType** | [**DestSplitTypeEnum**](#DestSplitTypeEnum) | The destination dataset split type. |  [optional] |
|**individualBatchMoveStatuses** | [**List&lt;GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatus&gt;**](GoogleCloudDocumentaiUiv1beta3BatchMoveDocumentsMetadataIndividualBatchMoveStatus.md) | The list of response details of each document. |  [optional] |



## Enum: DestDatasetTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;DATASET_SPLIT_TYPE_UNSPECIFIED&quot; |
| TRAIN | &quot;DATASET_SPLIT_TRAIN&quot; |
| TEST | &quot;DATASET_SPLIT_TEST&quot; |
| UNASSIGNED | &quot;DATASET_SPLIT_UNASSIGNED&quot; |



## Enum: DestSplitTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;DATASET_SPLIT_TYPE_UNSPECIFIED&quot; |
| TRAIN | &quot;DATASET_SPLIT_TRAIN&quot; |
| TEST | &quot;DATASET_SPLIT_TEST&quot; |
| UNASSIGNED | &quot;DATASET_SPLIT_UNASSIGNED&quot; |



