

# GoogleCloudAiplatformV1beta1InputDataConfig

Specifies Vertex AI owned input data to be used for training, and possibly evaluating, the Model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSchemaUri** | **String** | Applicable only to custom training with Datasets that have DataItems and Annotations. Cloud Storage URI that points to a YAML file describing the annotation schema. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/ , note that the chosen schema must be consistent with metadata of the Dataset specified by dataset_id. Only Annotations that both match this schema and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on. When used in conjunction with annotations_filter, the Annotations used for training are filtered by both annotations_filter and annotation_schema_uri. |  [optional] |
|**annotationsFilter** | **String** | Applicable only to Datasets that have DataItems and Annotations. A filter on Annotations of the Dataset. Only Annotations that both match this filter and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on (for the auto-assigned that role is decided by Vertex AI). A filter with same syntax as the one used in ListAnnotations may be used, but note here it filters across all Annotations of the Dataset, and not just within a single DataItem. |  [optional] |
|**bigqueryDestination** | [**GoogleCloudAiplatformV1beta1BigQueryDestination**](GoogleCloudAiplatformV1beta1BigQueryDestination.md) |  |  [optional] |
|**datasetId** | **String** | Required. The ID of the Dataset in the same Project and Location which data will be used to train the Model. The Dataset must use schema compatible with Model being trained, and what is compatible should be described in the used TrainingPipeline&#39;s training_task_definition. For tabular Datasets, all their data is exported to training, to pick and choose from. |  [optional] |
|**filterSplit** | [**GoogleCloudAiplatformV1beta1FilterSplit**](GoogleCloudAiplatformV1beta1FilterSplit.md) |  |  [optional] |
|**fractionSplit** | [**GoogleCloudAiplatformV1beta1FractionSplit**](GoogleCloudAiplatformV1beta1FractionSplit.md) |  |  [optional] |
|**gcsDestination** | [**GoogleCloudAiplatformV1beta1GcsDestination**](GoogleCloudAiplatformV1beta1GcsDestination.md) |  |  [optional] |
|**persistMlUseAssignment** | **Boolean** | Whether to persist the ML use assignment to data item system labels. |  [optional] |
|**predefinedSplit** | [**GoogleCloudAiplatformV1beta1PredefinedSplit**](GoogleCloudAiplatformV1beta1PredefinedSplit.md) |  |  [optional] |
|**savedQueryId** | **String** | Only applicable to Datasets that have SavedQueries. The ID of a SavedQuery (annotation set) under the Dataset specified by dataset_id used for filtering Annotations for training. Only Annotations that are associated with this SavedQuery are used in respectively training. When used in conjunction with annotations_filter, the Annotations used for training are filtered by both saved_query_id and annotations_filter. Only one of saved_query_id and annotation_schema_uri should be specified as both of them represent the same thing: problem type. |  [optional] |
|**stratifiedSplit** | [**GoogleCloudAiplatformV1beta1StratifiedSplit**](GoogleCloudAiplatformV1beta1StratifiedSplit.md) |  |  [optional] |
|**timestampSplit** | [**GoogleCloudAiplatformV1beta1TimestampSplit**](GoogleCloudAiplatformV1beta1TimestampSplit.md) |  |  [optional] |



