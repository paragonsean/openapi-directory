

# ElasticsearchDestinationConfiguration

Describes the configuration of a destination in Amazon ES.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  |
|**domainARN** | [**String**](String.md) |  |  [optional] |
|**clusterEndpoint** | [**String**](String.md) |  |  [optional] |
|**indexName** | [**String**](String.md) |  |  |
|**typeName** | [**String**](String.md) |  |  [optional] |
|**indexRotationPeriod** | [**ElasticsearchIndexRotationPeriod**](ElasticsearchIndexRotationPeriod.md) |  |  [optional] |
|**bufferingHints** | [**ElasticsearchDestinationConfigurationBufferingHints**](ElasticsearchDestinationConfigurationBufferingHints.md) |  |  [optional] |
|**retryOptions** | [**ElasticsearchDestinationConfigurationRetryOptions**](ElasticsearchDestinationConfigurationRetryOptions.md) |  |  [optional] |
|**s3BackupMode** | [**ElasticsearchS3BackupMode**](ElasticsearchS3BackupMode.md) |  |  [optional] |
|**s3Configuration** | [**ElasticsearchDestinationConfigurationS3Configuration**](ElasticsearchDestinationConfigurationS3Configuration.md) |  |  |
|**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**S3DestinationDescriptionCloudWatchLoggingOptions**](S3DestinationDescriptionCloudWatchLoggingOptions.md) |  |  [optional] |
|**vpcConfiguration** | [**ElasticsearchDestinationConfigurationVpcConfiguration**](ElasticsearchDestinationConfigurationVpcConfiguration.md) |  |  [optional] |



