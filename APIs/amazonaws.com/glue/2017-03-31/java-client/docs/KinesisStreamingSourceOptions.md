

# KinesisStreamingSourceOptions

Additional options for the Amazon Kinesis streaming data source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointUrl** | [**String**](String.md) |  |  [optional] |
|**streamName** | [**String**](String.md) |  |  [optional] |
|**classification** | [**String**](String.md) |  |  [optional] |
|**delimiter** | [**String**](String.md) |  |  [optional] |
|**startingPosition** | [**StartingPosition**](StartingPosition.md) |  |  [optional] |
|**maxFetchTimeInMs** | [**Integer**](Integer.md) |  |  [optional] |
|**maxFetchRecordsPerShard** | [**Integer**](Integer.md) |  |  [optional] |
|**maxRecordPerRead** | [**Integer**](Integer.md) |  |  [optional] |
|**addIdleTimeBetweenReads** | [**Boolean**](Boolean.md) |  |  [optional] |
|**idleTimeBetweenReadsInMs** | [**Integer**](Integer.md) |  |  [optional] |
|**describeShardInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**numRetries** | [**Integer**](Integer.md) |  |  [optional] |
|**retryIntervalMs** | [**Integer**](Integer.md) |  |  [optional] |
|**maxRetryIntervalMs** | [**Integer**](Integer.md) |  |  [optional] |
|**avoidEmptyBatches** | [**Boolean**](Boolean.md) |  |  [optional] |
|**streamArn** | [**String**](String.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**roleSessionName** | [**String**](String.md) |  |  [optional] |
|**addRecordTimestamp** | [**String**](String.md) |  |  [optional] |
|**emitConsumerLagMetrics** | [**String**](String.md) |  |  [optional] |
|**startingTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



