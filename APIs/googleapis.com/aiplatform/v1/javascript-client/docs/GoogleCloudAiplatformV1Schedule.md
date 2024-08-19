# VertexAiApi.GoogleCloudAiplatformV1Schedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowQueueing** | **Boolean** | Optional. Whether new scheduled runs can be queued when max_concurrent_runs limit is reached. If set to true, new runs will be queued instead of skipped. Default to false. | [optional] 
**catchUp** | **Boolean** | Output only. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. Default to false. | [optional] [readonly] 
**createPipelineJobRequest** | [**GoogleCloudAiplatformV1CreatePipelineJobRequest**](GoogleCloudAiplatformV1CreatePipelineJobRequest.md) |  | [optional] 
**createTime** | **String** | Output only. Timestamp when this Schedule was created. | [optional] [readonly] 
**cron** | **String** | Cron schedule (https://en.wikipedia.org/wiki/Cron) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: \&quot;CRON_TZ&#x3D;${IANA_TIME_ZONE}\&quot; or \&quot;TZ&#x3D;${IANA_TIME_ZONE}\&quot;. The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, \&quot;CRON_TZ&#x3D;America/New_York 1 * * * *\&quot;, or \&quot;TZ&#x3D;America/New_York 1 * * * *\&quot;. | [optional] 
**displayName** | **String** | Required. User provided name of the Schedule. The name can be up to 128 characters long and can consist of any UTF-8 characters. | [optional] 
**endTime** | **String** | Optional. Timestamp after which no new runs can be scheduled. If specified, The schedule will be completed when either end_time is reached or when scheduled_run_count &gt;&#x3D; max_run_count. If not specified, new runs will keep getting scheduled until this Schedule is paused or deleted. Already scheduled runs will be allowed to complete. Unset if not specified. | [optional] 
**lastPauseTime** | **String** | Output only. Timestamp when this Schedule was last paused. Unset if never paused. | [optional] [readonly] 
**lastResumeTime** | **String** | Output only. Timestamp when this Schedule was last resumed. Unset if never resumed from pause. | [optional] [readonly] 
**lastScheduledRunResponse** | [**GoogleCloudAiplatformV1ScheduleRunResponse**](GoogleCloudAiplatformV1ScheduleRunResponse.md) |  | [optional] 
**maxConcurrentRunCount** | **String** | Required. Maximum number of runs that can be started concurrently for this Schedule. This is the limit for starting the scheduled requests and not the execution of the operations/jobs created by the requests (if applicable). | [optional] 
**maxRunCount** | **String** | Optional. Maximum run count of the schedule. If specified, The schedule will be completed when either started_run_count &gt;&#x3D; max_run_count or when end_time is reached. If not specified, new runs will keep getting scheduled until this Schedule is paused or deleted. Already scheduled runs will be allowed to complete. Unset if not specified. | [optional] 
**name** | **String** | Immutable. The resource name of the Schedule. | [optional] 
**nextRunTime** | **String** | Output only. Timestamp when this Schedule should schedule the next run. Having a next_run_time in the past means the runs are being started behind schedule. | [optional] [readonly] 
**startTime** | **String** | Optional. Timestamp after which the first run can be scheduled. Default to Schedule create time if not specified. | [optional] 
**startedRunCount** | **String** | Output only. The number of runs started by this schedule. | [optional] [readonly] 
**state** | **String** | Output only. The state of this Schedule. | [optional] [readonly] 
**updateTime** | **String** | Output only. Timestamp when this Schedule was updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `PAUSED` (value: `"PAUSED"`)

* `COMPLETED` (value: `"COMPLETED"`)




