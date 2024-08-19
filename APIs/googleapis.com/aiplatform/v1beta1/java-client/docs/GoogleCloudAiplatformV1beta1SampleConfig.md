

# GoogleCloudAiplatformV1beta1SampleConfig

Active learning data sampling config. For every active learning labeling iteration, it will select a batch of data based on the sampling strategy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**followingBatchSamplePercentage** | **Integer** | The percentage of data needed to be labeled in each following batch (except the first batch). |  [optional] |
|**initialBatchSamplePercentage** | **Integer** | The percentage of data needed to be labeled in the first batch. |  [optional] |
|**sampleStrategy** | [**SampleStrategyEnum**](#SampleStrategyEnum) | Field to choose sampling strategy. Sampling strategy will decide which data should be selected for human labeling in every batch. |  [optional] |



## Enum: SampleStrategyEnum

| Name | Value |
|---- | -----|
| SAMPLE_STRATEGY_UNSPECIFIED | &quot;SAMPLE_STRATEGY_UNSPECIFIED&quot; |
| UNCERTAINTY | &quot;UNCERTAINTY&quot; |



