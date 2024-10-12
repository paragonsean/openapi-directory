# VertexAiApi.GoogleCloudAiplatformV1PipelineJobRuntimeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failurePolicy** | **String** | Represents the failure policy of a pipeline. Currently, the default of a pipeline is that the pipeline will continue to run until no more tasks can be executed, also known as PIPELINE_FAILURE_POLICY_FAIL_SLOW. However, if a pipeline is set to PIPELINE_FAILURE_POLICY_FAIL_FAST, it will stop scheduling any new tasks when a task has failed. Any scheduled tasks will continue to completion. | [optional] 
**gcsOutputDirectory** | **String** | Required. A path in a Cloud Storage bucket, which will be treated as the root output directory of the pipeline. It is used by the system to generate the paths of output artifacts. The artifact paths are generated with a sub-path pattern &#x60;{job_id}/{task_id}/{output_key}&#x60; under the specified output directory. The service account specified in this pipeline must have the &#x60;storage.objects.get&#x60; and &#x60;storage.objects.create&#x60; permissions for this bucket. | [optional] 
**inputArtifacts** | [**{String: GoogleCloudAiplatformV1PipelineJobRuntimeConfigInputArtifact}**](GoogleCloudAiplatformV1PipelineJobRuntimeConfigInputArtifact.md) | The runtime artifacts of the PipelineJob. The key will be the input artifact name and the value would be one of the InputArtifact. | [optional] 
**parameterValues** | **{String: Object}** | The runtime parameters of the PipelineJob. The parameters will be passed into PipelineJob.pipeline_spec to replace the placeholders at runtime. This field is used by pipelines built using &#x60;PipelineJob.pipeline_spec.schema_version&#x60; 2.1.0, such as pipelines built using Kubeflow Pipelines SDK 1.9 or higher and the v2 DSL. | [optional] 
**parameters** | [**{String: GoogleCloudAiplatformV1Value}**](GoogleCloudAiplatformV1Value.md) | Deprecated. Use RuntimeConfig.parameter_values instead. The runtime parameters of the PipelineJob. The parameters will be passed into PipelineJob.pipeline_spec to replace the placeholders at runtime. This field is used by pipelines built using &#x60;PipelineJob.pipeline_spec.schema_version&#x60; 2.0.0 or lower, such as pipelines built using Kubeflow Pipelines SDK 1.8 or lower. | [optional] 



## Enum: FailurePolicyEnum


* `UNSPECIFIED` (value: `"PIPELINE_FAILURE_POLICY_UNSPECIFIED"`)

* `FAIL_SLOW` (value: `"PIPELINE_FAILURE_POLICY_FAIL_SLOW"`)

* `FAIL_FAST` (value: `"PIPELINE_FAILURE_POLICY_FAIL_FAST"`)




