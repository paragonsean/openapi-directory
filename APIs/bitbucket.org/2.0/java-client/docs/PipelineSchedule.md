

# PipelineSchedule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdOn** | **OffsetDateTime** | The timestamp when the schedule was created. |  [optional] |
|**cronPattern** | **String** | The cron expression with second precision (7 fields) that the schedule applies. For example, for expression: 0 0 12 * * ? *, will execute at 12pm UTC every day. |  [optional] |
|**enabled** | **Boolean** | Whether the schedule is enabled. |  [optional] |
|**target** | [**PipelineRefTarget**](PipelineRefTarget.md) |  |  [optional] |
|**updatedOn** | **OffsetDateTime** | The timestamp when the schedule was updated. |  [optional] |
|**uuid** | **String** | The UUID identifying the schedule. |  [optional] |



