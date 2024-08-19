

# CreateQueueRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. A description of the queue that you are creating. |  [optional] |
|**name** | **String** | The name of the queue that you are creating. |  |
|**pricingPlan** | [**PricingPlanEnum**](#PricingPlanEnum) | Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. |  [optional] |
|**reservationPlanSettings** | [**CreateQueueRequestReservationPlanSettings**](CreateQueueRequestReservationPlanSettings.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Queues can be ACTIVE or PAUSED. If you pause a queue, jobs in that queue won&#39;t begin. Jobs that are running when you pause a queue continue to run until they finish or result in an error. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. |  [optional] |



## Enum: PricingPlanEnum

| Name | Value |
|---- | -----|
| ON_DEMAND | &quot;ON_DEMAND&quot; |
| RESERVED | &quot;RESERVED&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PAUSED | &quot;PAUSED&quot; |



