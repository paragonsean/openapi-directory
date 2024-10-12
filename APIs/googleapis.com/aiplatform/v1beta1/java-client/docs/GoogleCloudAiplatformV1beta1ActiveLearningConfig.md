

# GoogleCloudAiplatformV1beta1ActiveLearningConfig

Parameters that configure the active learning pipeline. Active learning will label the data incrementally by several iterations. For every iteration, it will select a batch of data based on the sampling strategy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxDataItemCount** | **String** | Max number of human labeled DataItems. |  [optional] |
|**maxDataItemPercentage** | **Integer** | Max percent of total DataItems for human labeling. |  [optional] |
|**sampleConfig** | [**GoogleCloudAiplatformV1beta1SampleConfig**](GoogleCloudAiplatformV1beta1SampleConfig.md) |  |  [optional] |
|**trainingConfig** | [**GoogleCloudAiplatformV1beta1TrainingConfig**](GoogleCloudAiplatformV1beta1TrainingConfig.md) |  |  [optional] |



