

# AcknowledgeTaskRequest

Request message for acknowledging a task using AcknowledgeTask.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scheduleTime** | **String** | Required. The task&#39;s current schedule time, available in the schedule_time returned by LeaseTasks response or RenewLease response. This restriction is to ensure that your worker currently holds the lease. |  [optional] |



