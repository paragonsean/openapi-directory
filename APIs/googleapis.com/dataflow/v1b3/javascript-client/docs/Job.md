# DataflowApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRequestId** | **String** | The client&#39;s unique identifier of the job, re-used across retried attempts. If this field is set, the service will ensure its uniqueness. The request to create a job will fail if the service has knowledge of a previously submitted job with the same client&#39;s ID and job name. The caller may use this field to ensure idempotence of job creation across retried attempts to create a job. By default, the field is empty and, in that case, the service ignores it. | [optional] 
**createTime** | **String** | The timestamp when the job was initially created. Immutable and set by the Cloud Dataflow service. | [optional] 
**createdFromSnapshotId** | **String** | If this is specified, the job&#39;s initial state is populated from the given snapshot. | [optional] 
**currentState** | **String** | The current state of the job. Jobs are created in the &#x60;JOB_STATE_STOPPED&#x60; state unless otherwise specified. A job in the &#x60;JOB_STATE_RUNNING&#x60; state may asynchronously enter a terminal state. After a job has reached a terminal state, no further state updates may be made. This field might be mutated by the Dataflow service; callers cannot mutate it. | [optional] 
**currentStateTime** | **String** | The timestamp associated with the current state. | [optional] 
**environment** | [**Environment**](Environment.md) |  | [optional] 
**executionInfo** | [**JobExecutionInfo**](JobExecutionInfo.md) |  | [optional] 
**id** | **String** | The unique ID of this job. This field is set by the Dataflow service when the job is created, and is immutable for the life of the job. | [optional] 
**jobMetadata** | [**JobMetadata**](JobMetadata.md) |  | [optional] 
**labels** | **{String: String}** | User-defined labels for this job. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \\p{Ll}\\p{Lo}{0,62} * Values must conform to regexp: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} * Both keys and values are additionally constrained to be &lt;&#x3D; 128 bytes in size. | [optional] 
**location** | **String** | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job. | [optional] 
**name** | **String** | The user-specified Dataflow job name. Only one active job with a given name can exist in a project within one region at any given time. Jobs in different regions can have the same name. If a caller attempts to create a job with the same name as an active job that already exists, the attempt returns the existing job. The name must match the regular expression &#x60;[a-z]([-a-z0-9]{0,1022}[a-z0-9])?&#x60; | [optional] 
**pipelineDescription** | [**PipelineDescription**](PipelineDescription.md) |  | [optional] 
**projectId** | **String** | The ID of the Google Cloud project that the job belongs to. | [optional] 
**replaceJobId** | **String** | If this job is an update of an existing job, this field is the job ID of the job it replaced. When sending a &#x60;CreateJobRequest&#x60;, you can update a job by specifying it here. The job named here is stopped, and its intermediate state is transferred to this job. | [optional] 
**replacedByJobId** | **String** | If another job is an update of this job (and thus, this job is in &#x60;JOB_STATE_UPDATED&#x60;), this field contains the ID of that job. | [optional] 
**requestedState** | **String** | The job&#39;s requested state. Applies to &#x60;UpdateJob&#x60; requests. Set &#x60;requested_state&#x60; with &#x60;UpdateJob&#x60; requests to switch between the states &#x60;JOB_STATE_STOPPED&#x60; and &#x60;JOB_STATE_RUNNING&#x60;. You can also use &#x60;UpdateJob&#x60; requests to change a job&#39;s state from &#x60;JOB_STATE_RUNNING&#x60; to &#x60;JOB_STATE_CANCELLED&#x60;, &#x60;JOB_STATE_DONE&#x60;, or &#x60;JOB_STATE_DRAINED&#x60;. These states irrevocably terminate the job if it hasn&#39;t already reached a terminal state. This field has no effect on &#x60;CreateJob&#x60; requests. | [optional] 
**runtimeUpdatableParams** | [**RuntimeUpdatableParams**](RuntimeUpdatableParams.md) |  | [optional] 
**satisfiesPzi** | **Boolean** | Output only. Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests. | [optional] [readonly] 
**satisfiesPzs** | **Boolean** | Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests. | [optional] 
**stageStates** | [**[ExecutionStageState]**](ExecutionStageState.md) | This field may be mutated by the Cloud Dataflow service; callers cannot mutate it. | [optional] 
**startTime** | **String** | The timestamp when the job was started (transitioned to JOB_STATE_PENDING). Flexible resource scheduling jobs are started with some delay after job creation, so start_time is unset before start and is updated when the job is started by the Cloud Dataflow service. For other jobs, start_time always equals to create_time and is immutable and set by the Cloud Dataflow service. | [optional] 
**steps** | [**[Step]**](Step.md) | Exactly one of step or steps_location should be specified. The top-level steps that constitute the entire job. Only retrieved with JOB_VIEW_ALL. | [optional] 
**stepsLocation** | **String** | The Cloud Storage location where the steps are stored. | [optional] 
**tempFiles** | **[String]** | A set of files the system should be aware of that are used for temporary storage. These temporary files will be removed on job completion. No duplicates are allowed. No file patterns are supported. The supported files are: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} | [optional] 
**transformNameMapping** | **{String: String}** | The map of transform name prefixes of the job to be replaced to the corresponding name prefixes of the new job. | [optional] 
**type** | **String** | The type of Dataflow job. | [optional] 



## Enum: CurrentStateEnum


* `UNKNOWN` (value: `"JOB_STATE_UNKNOWN"`)

* `STOPPED` (value: `"JOB_STATE_STOPPED"`)

* `RUNNING` (value: `"JOB_STATE_RUNNING"`)

* `DONE` (value: `"JOB_STATE_DONE"`)

* `FAILED` (value: `"JOB_STATE_FAILED"`)

* `CANCELLED` (value: `"JOB_STATE_CANCELLED"`)

* `UPDATED` (value: `"JOB_STATE_UPDATED"`)

* `DRAINING` (value: `"JOB_STATE_DRAINING"`)

* `DRAINED` (value: `"JOB_STATE_DRAINED"`)

* `PENDING` (value: `"JOB_STATE_PENDING"`)

* `CANCELLING` (value: `"JOB_STATE_CANCELLING"`)

* `QUEUED` (value: `"JOB_STATE_QUEUED"`)

* `RESOURCE_CLEANING_UP` (value: `"JOB_STATE_RESOURCE_CLEANING_UP"`)





## Enum: RequestedStateEnum


* `UNKNOWN` (value: `"JOB_STATE_UNKNOWN"`)

* `STOPPED` (value: `"JOB_STATE_STOPPED"`)

* `RUNNING` (value: `"JOB_STATE_RUNNING"`)

* `DONE` (value: `"JOB_STATE_DONE"`)

* `FAILED` (value: `"JOB_STATE_FAILED"`)

* `CANCELLED` (value: `"JOB_STATE_CANCELLED"`)

* `UPDATED` (value: `"JOB_STATE_UPDATED"`)

* `DRAINING` (value: `"JOB_STATE_DRAINING"`)

* `DRAINED` (value: `"JOB_STATE_DRAINED"`)

* `PENDING` (value: `"JOB_STATE_PENDING"`)

* `CANCELLING` (value: `"JOB_STATE_CANCELLING"`)

* `QUEUED` (value: `"JOB_STATE_QUEUED"`)

* `RESOURCE_CLEANING_UP` (value: `"JOB_STATE_RESOURCE_CLEANING_UP"`)





## Enum: TypeEnum


* `UNKNOWN` (value: `"JOB_TYPE_UNKNOWN"`)

* `BATCH` (value: `"JOB_TYPE_BATCH"`)

* `STREAMING` (value: `"JOB_TYPE_STREAMING"`)




