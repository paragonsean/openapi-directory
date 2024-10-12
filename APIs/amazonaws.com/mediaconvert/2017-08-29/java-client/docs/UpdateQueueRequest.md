

# UpdateQueueRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The new description for the queue, if you are changing it. |  [optional] |
|**reservationPlanSettings** | [**CreateQueueRequestReservationPlanSettings**](CreateQueueRequestReservationPlanSettings.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Queues can be ACTIVE or PAUSED. If you pause a queue, jobs in that queue won&#39;t begin. Jobs that are running when you pause a queue continue to run until they finish or result in an error. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |



