

# GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfig

Config for importing documents. Each batch can have its own dataset split type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoSplitConfig** | [**GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfigAutoSplitConfig**](GoogleCloudDocumentaiV1beta3ImportDocumentsRequestBatchDocumentsImportConfigAutoSplitConfig.md) |  |  [optional] |
|**batchInputConfig** | [**GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig**](GoogleCloudDocumentaiV1beta3BatchDocumentsInputConfig.md) |  |  [optional] |
|**datasetSplit** | [**DatasetSplitEnum**](#DatasetSplitEnum) | Target dataset split where the documents must be stored. |  [optional] |



## Enum: DatasetSplitEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;DATASET_SPLIT_TYPE_UNSPECIFIED&quot; |
| TRAIN | &quot;DATASET_SPLIT_TRAIN&quot; |
| TEST | &quot;DATASET_SPLIT_TEST&quot; |
| UNASSIGNED | &quot;DATASET_SPLIT_UNASSIGNED&quot; |



