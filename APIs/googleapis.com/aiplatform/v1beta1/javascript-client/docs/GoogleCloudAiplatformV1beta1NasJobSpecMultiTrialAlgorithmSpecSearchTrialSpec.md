# VertexAiApi.GoogleCloudAiplatformV1beta1NasJobSpecMultiTrialAlgorithmSpecSearchTrialSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxFailedTrialCount** | **Number** | The number of failed trials that need to be seen before failing the NasJob. If set to 0, Vertex AI decides how many trials must fail before the whole job fails. | [optional] 
**maxParallelTrialCount** | **Number** | Required. The maximum number of trials to run in parallel. | [optional] 
**maxTrialCount** | **Number** | Required. The maximum number of Neural Architecture Search (NAS) trials to run. | [optional] 
**searchTrialJobSpec** | [**GoogleCloudAiplatformV1beta1CustomJobSpec**](GoogleCloudAiplatformV1beta1CustomJobSpec.md) |  | [optional] 


