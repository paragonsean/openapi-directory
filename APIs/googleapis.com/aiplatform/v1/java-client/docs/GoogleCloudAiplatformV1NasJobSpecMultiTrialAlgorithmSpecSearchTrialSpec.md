

# GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec

Represent spec for search trials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxFailedTrialCount** | **Integer** | The number of failed trials that need to be seen before failing the NasJob. If set to 0, Vertex AI decides how many trials must fail before the whole job fails. |  [optional] |
|**maxParallelTrialCount** | **Integer** | Required. The maximum number of trials to run in parallel. |  [optional] |
|**maxTrialCount** | **Integer** | Required. The maximum number of Neural Architecture Search (NAS) trials to run. |  [optional] |
|**searchTrialJobSpec** | [**GoogleCloudAiplatformV1CustomJobSpec**](GoogleCloudAiplatformV1CustomJobSpec.md) |  |  [optional] |



