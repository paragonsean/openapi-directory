

# GoogleCloudDatapipelinesV1Pipeline

The main pipeline entity and all the necessary metadata for launching and managing linked jobs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Immutable. The timestamp when the pipeline was initially created. Set by the Data Pipelines service. |  [optional] [readonly] |
|**displayName** | **String** | Required. The display name of the pipeline. It can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), and underscores (_). |  [optional] |
|**jobCount** | **Integer** | Output only. Number of jobs. |  [optional] [readonly] |
|**lastUpdateTime** | **String** | Output only. Immutable. The timestamp when the pipeline was last modified. Set by the Data Pipelines service. |  [optional] [readonly] |
|**name** | **String** | The pipeline name. For example: &#x60;projects/PROJECT_ID/locations/LOCATION_ID/pipelines/PIPELINE_ID&#x60;. * &#x60;PROJECT_ID&#x60; can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), and periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). * &#x60;LOCATION_ID&#x60; is the canonical ID for the pipeline&#39;s location. The list of available locations can be obtained by calling &#x60;google.cloud.location.Locations.ListLocations&#x60;. Note that the Data Pipelines service is not available in all regions. It depends on Cloud Scheduler, an App Engine application, so it&#39;s only available in [App Engine regions](https://cloud.google.com/about/locations#region). * &#x60;PIPELINE_ID&#x60; is the ID of the pipeline. Must be unique for the selected project and location. |  [optional] |
|**pipelineSources** | **Map&lt;String, String&gt;** | Immutable. The sources of the pipeline (for example, Dataplex). The keys and values are set by the corresponding sources during pipeline creation. |  [optional] |
|**scheduleInfo** | [**GoogleCloudDatapipelinesV1ScheduleSpec**](GoogleCloudDatapipelinesV1ScheduleSpec.md) |  |  [optional] |
|**schedulerServiceAccountEmail** | **String** | Optional. A service account email to be used with the Cloud Scheduler job. If not specified, the default compute engine service account will be used. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Required. The state of the pipeline. When the pipeline is created, the state is set to &#39;PIPELINE_STATE_ACTIVE&#39; by default. State changes can be requested by setting the state to stopping, paused, or resuming. State cannot be changed through UpdatePipeline requests. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the pipeline. This field affects the scheduling of the pipeline and the type of metrics to show for the pipeline. |  [optional] |
|**workload** | [**GoogleCloudDatapipelinesV1Workload**](GoogleCloudDatapipelinesV1Workload.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RESUMING | &quot;STATE_RESUMING&quot; |
| ACTIVE | &quot;STATE_ACTIVE&quot; |
| STOPPING | &quot;STATE_STOPPING&quot; |
| ARCHIVED | &quot;STATE_ARCHIVED&quot; |
| PAUSED | &quot;STATE_PAUSED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PIPELINE_TYPE_UNSPECIFIED&quot; |
| BATCH | &quot;PIPELINE_TYPE_BATCH&quot; |
| STREAMING | &quot;PIPELINE_TYPE_STREAMING&quot; |



