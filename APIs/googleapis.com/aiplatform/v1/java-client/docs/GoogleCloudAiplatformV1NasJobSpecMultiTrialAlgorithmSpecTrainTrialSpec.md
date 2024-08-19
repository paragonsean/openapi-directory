

# GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecTrainTrialSpec

Represent spec for train trials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frequency** | **Integer** | Required. Frequency of search trials to start train stage. Top N [TrainTrialSpec.max_parallel_trial_count] search trials will be trained for every M [TrainTrialSpec.frequency] trials searched. |  [optional] |
|**maxParallelTrialCount** | **Integer** | Required. The maximum number of trials to run in parallel. |  [optional] |
|**trainTrialJobSpec** | [**GoogleCloudAiplatformV1CustomJobSpec**](GoogleCloudAiplatformV1CustomJobSpec.md) |  |  [optional] |



