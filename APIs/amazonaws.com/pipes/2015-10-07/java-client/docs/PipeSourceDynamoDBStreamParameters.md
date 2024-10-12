

# PipeSourceDynamoDBStreamParameters

The parameters for using a DynamoDB stream as a source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchSize** | [**Integer**](Integer.md) |  |  [optional] |
|**deadLetterConfig** | [**PipeSourceDynamoDBStreamParametersDeadLetterConfig**](PipeSourceDynamoDBStreamParametersDeadLetterConfig.md) |  |  [optional] |
|**maximumBatchingWindowInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**maximumRecordAgeInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**maximumRetryAttempts** | [**Integer**](Integer.md) |  |  [optional] |
|**onPartialBatchItemFailure** | [**OnPartialBatchItemFailureStreams**](OnPartialBatchItemFailureStreams.md) |  |  [optional] |
|**parallelizationFactor** | [**Integer**](Integer.md) |  |  [optional] |
|**startingPosition** | [**DynamoDBStreamStartPosition**](DynamoDBStreamStartPosition.md) |  |  |



