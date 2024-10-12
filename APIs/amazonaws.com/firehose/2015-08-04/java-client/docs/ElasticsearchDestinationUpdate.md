

# ElasticsearchDestinationUpdate

Describes an update for a destination in Amazon ES.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  [optional] |
|**domainARN** | [**String**](String.md) |  |  [optional] |
|**clusterEndpoint** | [**String**](String.md) |  |  [optional] |
|**indexName** | [**String**](String.md) |  |  [optional] |
|**typeName** | [**String**](String.md) |  |  [optional] |
|**indexRotationPeriod** | [**ElasticsearchIndexRotationPeriod**](ElasticsearchIndexRotationPeriod.md) |  |  [optional] |
|**bufferingHints** | [**ElasticsearchDestinationUpdateBufferingHints**](ElasticsearchDestinationUpdateBufferingHints.md) |  |  [optional] |
|**retryOptions** | [**ElasticsearchDestinationConfigurationRetryOptions**](ElasticsearchDestinationConfigurationRetryOptions.md) |  |  [optional] |
|**s3Update** | [**ElasticsearchDestinationUpdateS3Update**](ElasticsearchDestinationUpdateS3Update.md) |  |  [optional] |
|**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**S3DestinationConfigurationCloudWatchLoggingOptions**](S3DestinationConfigurationCloudWatchLoggingOptions.md) |  |  [optional] |



