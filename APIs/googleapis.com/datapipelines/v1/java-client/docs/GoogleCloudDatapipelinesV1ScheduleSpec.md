

# GoogleCloudDatapipelinesV1ScheduleSpec

Details of the schedule the pipeline runs on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextJobTime** | **String** | Output only. When the next Scheduler job is going to run. |  [optional] [readonly] |
|**schedule** | **String** | Unix-cron format of the schedule. This information is retrieved from the linked Cloud Scheduler. |  [optional] |
|**timeZone** | **String** | Timezone ID. This matches the timezone IDs used by the Cloud Scheduler API. If empty, UTC time is assumed. |  [optional] |



