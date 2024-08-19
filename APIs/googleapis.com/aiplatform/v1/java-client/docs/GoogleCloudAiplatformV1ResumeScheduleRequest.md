

# GoogleCloudAiplatformV1ResumeScheduleRequest

Request message for ScheduleService.ResumeSchedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catchUp** | **Boolean** | Optional. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. This will also update Schedule.catch_up field. Default to false. |  [optional] |



