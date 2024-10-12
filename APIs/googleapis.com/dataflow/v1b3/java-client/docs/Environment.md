

# Environment

Describes the environment in which a Dataflow Job runs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterManagerApiService** | **String** | The type of cluster manager API to use. If unknown or unspecified, the service will attempt to choose a reasonable default. This should be in the form of the API service name, e.g. \&quot;compute.googleapis.com\&quot;. |  [optional] |
|**dataset** | **String** | The dataset for the current project where various workflow related tables are stored. The supported resource type is: Google BigQuery: bigquery.googleapis.com/{dataset} |  [optional] |
|**debugOptions** | [**DebugOptions**](DebugOptions.md) |  |  [optional] |
|**experiments** | **List&lt;String&gt;** | The list of experiments to enable. This field should be used for SDK related experiments and not for service related experiments. The proper field for service related experiments is service_options. |  [optional] |
|**flexResourceSchedulingGoal** | [**FlexResourceSchedulingGoalEnum**](#FlexResourceSchedulingGoalEnum) | Which Flexible Resource Scheduling mode to run in. |  [optional] |
|**internalExperiments** | **Map&lt;String, Object&gt;** | Experimental settings. |  [optional] |
|**sdkPipelineOptions** | **Map&lt;String, Object&gt;** | The Cloud Dataflow SDK pipeline options specified by the user. These options are passed through the service and are used to recreate the SDK pipeline options on the worker in a language agnostic and platform independent way. |  [optional] |
|**serviceAccountEmail** | **String** | Identity to run virtual machines as. Defaults to the default account. |  [optional] |
|**serviceKmsKeyName** | **String** | If set, contains the Cloud KMS key identifier used to encrypt data at rest, AKA a Customer Managed Encryption Key (CMEK). Format: projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY |  [optional] |
|**serviceOptions** | **List&lt;String&gt;** | The list of service options to enable. This field should be used for service related experiments only. These experiments, when graduating to GA, should be replaced by dedicated fields or become default (i.e. always on). |  [optional] |
|**shuffleMode** | [**ShuffleModeEnum**](#ShuffleModeEnum) | Output only. The shuffle mode used for the job. |  [optional] [readonly] |
|**streamingMode** | [**StreamingModeEnum**](#StreamingModeEnum) | Optional. Specifies the Streaming Engine message processing guarantees. Reduces cost and latency but might result in duplicate messages committed to storage. Designed to run simple mapping streaming ETL jobs at the lowest cost. For example, Change Data Capture (CDC) to BigQuery is a canonical use case. |  [optional] |
|**tempStoragePrefix** | **String** | The prefix of the resources the system should use for temporary storage. The system will append the suffix \&quot;/temp-{JOBNAME} to this resource prefix, where {JOBNAME} is the value of the job_name field. The resulting bucket and object prefix is used as the prefix of the resources used to store temporary data needed during the job execution. NOTE: This will override the value in taskrunner_settings. The supported resource type is: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} |  [optional] |
|**useStreamingEngineResourceBasedBilling** | **Boolean** | Output only. Whether the job uses the Streaming Engine resource-based billing model. |  [optional] [readonly] |
|**userAgent** | **Map&lt;String, Object&gt;** | A description of the process that generated the request. |  [optional] |
|**version** | **Map&lt;String, Object&gt;** | A structure describing which components and their versions of the service are required in order to run the job. |  [optional] |
|**workerPools** | [**List&lt;WorkerPool&gt;**](WorkerPool.md) | The worker pools. At least one \&quot;harness\&quot; worker pool must be specified in order for the job to have workers. |  [optional] |
|**workerRegion** | **String** | The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. \&quot;us-west1\&quot;. Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane&#39;s region. |  [optional] |
|**workerZone** | **String** | The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. \&quot;us-west1-a\&quot;. Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane&#39;s region is chosen based on available capacity. |  [optional] |



## Enum: FlexResourceSchedulingGoalEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;FLEXRS_UNSPECIFIED&quot; |
| SPEED_OPTIMIZED | &quot;FLEXRS_SPEED_OPTIMIZED&quot; |
| COST_OPTIMIZED | &quot;FLEXRS_COST_OPTIMIZED&quot; |



## Enum: ShuffleModeEnum

| Name | Value |
|---- | -----|
| SHUFFLE_MODE_UNSPECIFIED | &quot;SHUFFLE_MODE_UNSPECIFIED&quot; |
| VM_BASED | &quot;VM_BASED&quot; |
| SERVICE_BASED | &quot;SERVICE_BASED&quot; |



## Enum: StreamingModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STREAMING_MODE_UNSPECIFIED&quot; |
| EXACTLY_ONCE | &quot;STREAMING_MODE_EXACTLY_ONCE&quot; |
| AT_LEAST_ONCE | &quot;STREAMING_MODE_AT_LEAST_ONCE&quot; |



