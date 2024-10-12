

# GoogleCloudDocumentaiV1beta3DocumentMetadata

Metadata about a document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetType** | [**DatasetTypeEnum**](#DatasetTypeEnum) | Type of the dataset split to which the document belongs. |  [optional] |
|**displayName** | **String** | The display name of the document. |  [optional] |
|**documentId** | [**GoogleCloudDocumentaiV1beta3DocumentId**](GoogleCloudDocumentaiV1beta3DocumentId.md) |  |  [optional] |
|**labelingState** | [**LabelingStateEnum**](#LabelingStateEnum) | Labeling state of the document. |  [optional] |
|**pageCount** | **Integer** | Number of pages in the document. |  [optional] |



## Enum: DatasetTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;DATASET_SPLIT_TYPE_UNSPECIFIED&quot; |
| TRAIN | &quot;DATASET_SPLIT_TRAIN&quot; |
| TEST | &quot;DATASET_SPLIT_TEST&quot; |
| UNASSIGNED | &quot;DATASET_SPLIT_UNASSIGNED&quot; |



## Enum: LabelingStateEnum

| Name | Value |
|---- | -----|
| LABELING_STATE_UNSPECIFIED | &quot;DOCUMENT_LABELING_STATE_UNSPECIFIED&quot; |
| LABELED | &quot;DOCUMENT_LABELED&quot; |
| UNLABELED | &quot;DOCUMENT_UNLABELED&quot; |
| AUTO_LABELED | &quot;DOCUMENT_AUTO_LABELED&quot; |



