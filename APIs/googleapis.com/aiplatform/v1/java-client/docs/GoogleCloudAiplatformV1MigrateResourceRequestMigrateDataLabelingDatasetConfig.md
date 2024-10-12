

# GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfig

Config for migrating Dataset in datalabeling.googleapis.com to Vertex AI's Dataset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataset** | **String** | Required. Full resource name of data labeling Dataset. Format: &#x60;projects/{project}/datasets/{dataset}&#x60;. |  [optional] |
|**datasetDisplayName** | **String** | Optional. Display name of the Dataset in Vertex AI. System will pick a display name if unspecified. |  [optional] |
|**migrateDataLabelingAnnotatedDatasetConfigs** | [**List&lt;GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig&gt;**](GoogleCloudAiplatformV1MigrateResourceRequestMigrateDataLabelingDatasetConfigMigrateDataLabelingAnnotatedDatasetConfig.md) | Optional. Configs for migrating AnnotatedDataset in datalabeling.googleapis.com to Vertex AI&#39;s SavedQuery. The specified AnnotatedDatasets have to belong to the datalabeling Dataset. |  [optional] |



