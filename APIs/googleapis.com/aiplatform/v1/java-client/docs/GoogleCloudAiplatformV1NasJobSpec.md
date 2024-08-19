

# GoogleCloudAiplatformV1NasJobSpec

Represents the spec of a NasJob.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**multiTrialAlgorithmSpec** | [**GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpec**](GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpec.md) |  |  [optional] |
|**resumeNasJobId** | **String** | The ID of the existing NasJob in the same Project and Location which will be used to resume search. search_space_spec and nas_algorithm_spec are obtained from previous NasJob hence should not provide them again for this NasJob. |  [optional] |
|**searchSpaceSpec** | **String** | It defines the search space for Neural Architecture Search (NAS). |  [optional] |



