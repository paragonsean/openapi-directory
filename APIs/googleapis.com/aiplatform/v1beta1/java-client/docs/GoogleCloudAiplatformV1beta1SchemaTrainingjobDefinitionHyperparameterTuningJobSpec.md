

# GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxFailedTrialCount** | **Integer** | The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails. |  [optional] |
|**maxTrialCount** | **Integer** | The desired total number of Trials. |  [optional] |
|**parallelTrialCount** | **Integer** | The desired number of Trials to run in parallel. |  [optional] |
|**studySpec** | [**GoogleCloudAiplatformV1beta1StudySpec**](GoogleCloudAiplatformV1beta1StudySpec.md) |  |  [optional] |
|**trialJobSpec** | [**GoogleCloudAiplatformV1beta1CustomJobSpec**](GoogleCloudAiplatformV1beta1CustomJobSpec.md) |  |  [optional] |



