# TranscoderApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchModePriority** | **Number** | The processing priority of a batch job. This field can only be set for batch mode jobs. The default value is 0. This value cannot be negative. Higher values correspond to higher priorities for the job. | [optional] 
**config** | [**JobConfig**](JobConfig.md) |  | [optional] 
**createTime** | **String** | Output only. The time the job was created. | [optional] [readonly] 
**endTime** | **String** | Output only. The time the transcoding finished. | [optional] [readonly] 
**error** | [**Status**](Status.md) |  | [optional] 
**inputUri** | **String** | Input only. Specify the &#x60;input_uri&#x60; to populate empty &#x60;uri&#x60; fields in each element of &#x60;Job.config.inputs&#x60; or &#x60;JobTemplate.config.inputs&#x60; when using template. URI of the media. Input files must be at least 5 seconds in duration and stored in Cloud Storage (for example, &#x60;gs://bucket/inputs/file.mp4&#x60;). See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). | [optional] 
**labels** | **{String: String}** | The labels associated with this job. You can use these to organize and group your jobs. | [optional] 
**mode** | **String** | The processing mode of the job. The default is &#x60;PROCESSING_MODE_INTERACTIVE&#x60;. | [optional] 
**name** | **String** | The resource name of the job. Format: &#x60;projects/{project_number}/locations/{location}/jobs/{job}&#x60; | [optional] 
**optimization** | **String** | Optional. The optimization strategy of the job. The default is &#x60;AUTODETECT&#x60;. | [optional] 
**outputUri** | **String** | Input only. Specify the &#x60;output_uri&#x60; to populate an empty &#x60;Job.config.output.uri&#x60; or &#x60;JobTemplate.config.output.uri&#x60; when using template. URI for the output file(s). For example, &#x60;gs://my-bucket/outputs/&#x60;. See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). | [optional] 
**startTime** | **String** | Output only. The time the transcoding started. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the job. | [optional] [readonly] 
**templateId** | **String** | Input only. Specify the &#x60;template_id&#x60; to use for populating &#x60;Job.config&#x60;. The default is &#x60;preset/web-hd&#x60;, which is the only supported preset. User defined JobTemplate: &#x60;{job_template_id}&#x60; | [optional] 
**ttlAfterCompletionDays** | **Number** | Job time to live value in days, which will be effective after job completion. Job should be deleted automatically after the given TTL. Enter a value between 1 and 90. The default is 30. | [optional] 



## Enum: ModeEnum


* `UNSPECIFIED` (value: `"PROCESSING_MODE_UNSPECIFIED"`)

* `INTERACTIVE` (value: `"PROCESSING_MODE_INTERACTIVE"`)

* `BATCH` (value: `"PROCESSING_MODE_BATCH"`)





## Enum: OptimizationEnum


* `OPTIMIZATION_STRATEGY_UNSPECIFIED` (value: `"OPTIMIZATION_STRATEGY_UNSPECIFIED"`)

* `AUTODETECT` (value: `"AUTODETECT"`)

* `DISABLED` (value: `"DISABLED"`)





## Enum: StateEnum


* `PROCESSING_STATE_UNSPECIFIED` (value: `"PROCESSING_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




