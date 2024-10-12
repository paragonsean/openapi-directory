# CloudTasksApi.RenewLeaseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaseDuration** | **String** | Required. The desired new lease duration, starting from now. The maximum lease duration is 1 week. &#x60;lease_duration&#x60; will be truncated to the nearest second. | [optional] 
**responseView** | **String** | The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires &#x60;cloudtasks.tasks.fullView&#x60; [Google IAM](https://cloud.google.com/iam/) permission on the Task resource. | [optional] 
**scheduleTime** | **String** | Required. The task&#39;s current schedule time, available in the schedule_time returned by LeaseTasks response or RenewLease response. This restriction is to ensure that your worker currently holds the lease. | [optional] 



## Enum: ResponseViewEnum


* `VIEW_UNSPECIFIED` (value: `"VIEW_UNSPECIFIED"`)

* `BASIC` (value: `"BASIC"`)

* `FULL` (value: `"FULL"`)




