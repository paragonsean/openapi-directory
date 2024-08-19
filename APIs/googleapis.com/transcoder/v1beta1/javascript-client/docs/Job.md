# TranscoderApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**JobConfig**](JobConfig.md) |  | [optional] 
**createTime** | **String** | Output only. The time the job was created. | [optional] [readonly] 
**endTime** | **String** | Output only. The time the transcoding finished. | [optional] [readonly] 
**failureDetails** | [**[FailureDetail]**](FailureDetail.md) | Output only. List of failure details. This property may contain additional information about the failure when &#x60;failure_reason&#x60; is present. *Note*: This feature is not yet available. | [optional] [readonly] 
**failureReason** | **String** | Output only. A description of the reason for the failure. This property is always present when &#x60;state&#x60; is &#x60;FAILED&#x60;. | [optional] [readonly] 
**inputUri** | **String** | Input only. Specify the &#x60;input_uri&#x60; to populate empty &#x60;uri&#x60; fields in each element of &#x60;Job.config.inputs&#x60; or &#x60;JobTemplate.config.inputs&#x60; when using template. URI of the media. Input files must be at least 5 seconds in duration and stored in Cloud Storage (for example, &#x60;gs://bucket/inputs/file.mp4&#x60;). | [optional] 
**name** | **String** | The resource name of the job. Format: &#x60;projects/{project}/locations/{location}/jobs/{job}&#x60; | [optional] 
**originUri** | [**OriginUri**](OriginUri.md) |  | [optional] 
**outputUri** | **String** | Input only. Specify the &#x60;output_uri&#x60; to populate an empty &#x60;Job.config.output.uri&#x60; or &#x60;JobTemplate.config.output.uri&#x60; when using template. URI for the output file(s). For example, &#x60;gs://my-bucket/outputs/&#x60;. | [optional] 
**priority** | **Number** | Specify the priority of the job. Enter a value between 0 and 100, where 0 is the lowest priority and 100 is the highest priority. The default is 0. | [optional] 
**progress** | [**Progress**](Progress.md) |  | [optional] 
**startTime** | **String** | Output only. The time the transcoding started. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the job. | [optional] [readonly] 
**templateId** | **String** | Input only. Specify the &#x60;template_id&#x60; to use for populating &#x60;Job.config&#x60;. The default is &#x60;preset/web-hd&#x60;. Preset Transcoder templates: - &#x60;preset/{preset_id}&#x60; - User defined JobTemplate: &#x60;{job_template_id}&#x60; | [optional] 
**ttlAfterCompletionDays** | **Number** | Job time to live value in days, which will be effective after job completion. Job should be deleted automatically after the given TTL. Enter a value between 1 and 90. The default is 30. | [optional] 



## Enum: StateEnum


* `PROCESSING_STATE_UNSPECIFIED` (value: `"PROCESSING_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




