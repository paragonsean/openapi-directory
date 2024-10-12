# VertexAiApi.GoogleCloudAiplatformV1beta1SampleConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**followingBatchSamplePercentage** | **Number** | The percentage of data needed to be labeled in each following batch (except the first batch). | [optional] 
**initialBatchSamplePercentage** | **Number** | The percentage of data needed to be labeled in the first batch. | [optional] 
**sampleStrategy** | **String** | Field to choose sampling strategy. Sampling strategy will decide which data should be selected for human labeling in every batch. | [optional] 



## Enum: SampleStrategyEnum


* `SAMPLE_STRATEGY_UNSPECIFIED` (value: `"SAMPLE_STRATEGY_UNSPECIFIED"`)

* `UNCERTAINTY` (value: `"UNCERTAINTY"`)




