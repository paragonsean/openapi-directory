# AmazonEventBridgePipes.CreatePipeRequestSourceParametersKinesisStreamParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchSize** | **Number** |  | [optional] 
**deadLetterConfig** | [**PipeSourceDynamoDBStreamParametersDeadLetterConfig**](PipeSourceDynamoDBStreamParametersDeadLetterConfig.md) |  | [optional] 
**maximumBatchingWindowInSeconds** | **Number** |  | [optional] 
**maximumRecordAgeInSeconds** | **Number** |  | [optional] 
**maximumRetryAttempts** | **Number** |  | [optional] 
**onPartialBatchItemFailure** | [**OnPartialBatchItemFailureStreams**](OnPartialBatchItemFailureStreams.md) |  | [optional] 
**parallelizationFactor** | **Number** |  | [optional] 
**startingPosition** | [**KinesisStreamStartPosition**](KinesisStreamStartPosition.md) |  | 
**startingPositionTimestamp** | **Date** |  | [optional] 


