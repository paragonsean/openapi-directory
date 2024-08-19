# VertexAiApi.GoogleCloudAiplatformV1SchemaTrainingjobDefinitionHyperparameterTuningJobSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxFailedTrialCount** | **Number** | The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails. | [optional] 
**maxTrialCount** | **Number** | The desired total number of Trials. | [optional] 
**parallelTrialCount** | **Number** | The desired number of Trials to run in parallel. | [optional] 
**studySpec** | [**GoogleCloudAiplatformV1StudySpec**](GoogleCloudAiplatformV1StudySpec.md) |  | [optional] 
**trialJobSpec** | [**GoogleCloudAiplatformV1CustomJobSpec**](GoogleCloudAiplatformV1CustomJobSpec.md) |  | [optional] 


