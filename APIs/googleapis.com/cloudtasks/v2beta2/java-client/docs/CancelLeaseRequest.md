

# CancelLeaseRequest

Request message for canceling a lease using CancelLease.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**responseView** | [**ResponseViewEnum**](#ResponseViewEnum) | The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires &#x60;cloudtasks.tasks.fullView&#x60; [Google IAM](https://cloud.google.com/iam/) permission on the Task resource. |  [optional] |
|**scheduleTime** | **String** | Required. The task&#39;s current schedule time, available in the schedule_time returned by LeaseTasks response or RenewLease response. This restriction is to ensure that your worker currently holds the lease. |  [optional] |



## Enum: ResponseViewEnum

| Name | Value |
|---- | -----|
| VIEW_UNSPECIFIED | &quot;VIEW_UNSPECIFIED&quot; |
| BASIC | &quot;BASIC&quot; |
| FULL | &quot;FULL&quot; |



