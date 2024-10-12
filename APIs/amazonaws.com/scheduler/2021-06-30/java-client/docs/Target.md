

# Target

The schedule's target. EventBridge Scheduler supports templated target that invoke common API operations, as well as universal targets that you can customize to invoke over 6,000 API operations across more than 270 services. You can only specify one templated or universal target for a schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  |
|**deadLetterConfig** | [**UpdateScheduleRequestTargetDeadLetterConfig**](UpdateScheduleRequestTargetDeadLetterConfig.md) |  |  [optional] |
|**ecsParameters** | [**UpdateScheduleRequestTargetEcsParameters**](UpdateScheduleRequestTargetEcsParameters.md) |  |  [optional] |
|**eventBridgeParameters** | [**UpdateScheduleRequestTargetEventBridgeParameters**](UpdateScheduleRequestTargetEventBridgeParameters.md) |  |  [optional] |
|**input** | [**String**](String.md) |  |  [optional] |
|**kinesisParameters** | [**UpdateScheduleRequestTargetKinesisParameters**](UpdateScheduleRequestTargetKinesisParameters.md) |  |  [optional] |
|**retryPolicy** | [**UpdateScheduleRequestTargetRetryPolicy**](UpdateScheduleRequestTargetRetryPolicy.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  |
|**sageMakerPipelineParameters** | [**UpdateScheduleRequestTargetSageMakerPipelineParameters**](UpdateScheduleRequestTargetSageMakerPipelineParameters.md) |  |  [optional] |
|**sqsParameters** | [**UpdateScheduleRequestTargetSqsParameters**](UpdateScheduleRequestTargetSqsParameters.md) |  |  [optional] |



