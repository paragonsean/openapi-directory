

# GoogleCloudAiplatformV1beta1MigratableResource

Represents one resource that exists in automl.googleapis.com, datalabeling.googleapis.com or ml.googleapis.com.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automlDataset** | [**GoogleCloudAiplatformV1beta1MigratableResourceAutomlDataset**](GoogleCloudAiplatformV1beta1MigratableResourceAutomlDataset.md) |  |  [optional] |
|**automlModel** | [**GoogleCloudAiplatformV1beta1MigratableResourceAutomlModel**](GoogleCloudAiplatformV1beta1MigratableResourceAutomlModel.md) |  |  [optional] |
|**dataLabelingDataset** | [**GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDataset**](GoogleCloudAiplatformV1beta1MigratableResourceDataLabelingDataset.md) |  |  [optional] |
|**lastMigrateTime** | **String** | Output only. Timestamp when the last migration attempt on this MigratableResource started. Will not be set if there&#39;s no migration attempt on this MigratableResource. |  [optional] [readonly] |
|**lastUpdateTime** | **String** | Output only. Timestamp when this MigratableResource was last updated. |  [optional] [readonly] |
|**mlEngineModelVersion** | [**GoogleCloudAiplatformV1beta1MigratableResourceMlEngineModelVersion**](GoogleCloudAiplatformV1beta1MigratableResourceMlEngineModelVersion.md) |  |  [optional] |



