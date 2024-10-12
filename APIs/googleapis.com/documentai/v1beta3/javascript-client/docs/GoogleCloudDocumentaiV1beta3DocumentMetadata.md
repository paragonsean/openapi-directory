# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasetType** | **String** | Type of the dataset split to which the document belongs. | [optional] 
**displayName** | **String** | The display name of the document. | [optional] 
**documentId** | [**GoogleCloudDocumentaiV1beta3DocumentId**](GoogleCloudDocumentaiV1beta3DocumentId.md) |  | [optional] 
**labelingState** | **String** | Labeling state of the document. | [optional] 
**pageCount** | **Number** | Number of pages in the document. | [optional] 



## Enum: DatasetTypeEnum


* `TYPE_UNSPECIFIED` (value: `"DATASET_SPLIT_TYPE_UNSPECIFIED"`)

* `TRAIN` (value: `"DATASET_SPLIT_TRAIN"`)

* `TEST` (value: `"DATASET_SPLIT_TEST"`)

* `UNASSIGNED` (value: `"DATASET_SPLIT_UNASSIGNED"`)





## Enum: LabelingStateEnum


* `LABELING_STATE_UNSPECIFIED` (value: `"DOCUMENT_LABELING_STATE_UNSPECIFIED"`)

* `LABELED` (value: `"DOCUMENT_LABELED"`)

* `UNLABELED` (value: `"DOCUMENT_UNLABELED"`)

* `AUTO_LABELED` (value: `"DOCUMENT_AUTO_LABELED"`)




