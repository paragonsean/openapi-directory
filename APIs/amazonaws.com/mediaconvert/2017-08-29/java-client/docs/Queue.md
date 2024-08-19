

# Queue

You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you don't specify a queue, the service sends all jobs through the default queue. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**lastUpdated** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  |
|**pricingPlan** | [**PricingPlan**](PricingPlan.md) |  |  [optional] |
|**progressingJobsCount** | [**Integer**](Integer.md) |  |  [optional] |
|**reservationPlan** | [**QueueReservationPlan**](QueueReservationPlan.md) |  |  [optional] |
|**status** | [**QueueStatus**](QueueStatus.md) |  |  [optional] |
|**submittedJobsCount** | [**Integer**](Integer.md) |  |  [optional] |
|**type** | [**Type**](Type.md) |  |  [optional] |



