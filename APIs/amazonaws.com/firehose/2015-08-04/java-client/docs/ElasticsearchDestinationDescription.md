

# ElasticsearchDestinationDescription

The destination description in Amazon ES.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  [optional] |
|**domainARN** | [**String**](String.md) |  |  [optional] |
|**clusterEndpoint** | [**String**](String.md) |  |  [optional] |
|**indexName** | [**String**](String.md) |  |  [optional] |
|**typeName** | [**String**](String.md) |  |  [optional] |
|**indexRotationPeriod** | [**ElasticsearchIndexRotationPeriod**](ElasticsearchIndexRotationPeriod.md) |  |  [optional] |
|**bufferingHints** | [**ElasticsearchDestinationDescriptionBufferingHints**](ElasticsearchDestinationDescriptionBufferingHints.md) |  |  [optional] |
|**retryOptions** | [**ElasticsearchDestinationDescriptionRetryOptions**](ElasticsearchDestinationDescriptionRetryOptions.md) |  |  [optional] |
|**s3BackupMode** | [**ElasticsearchS3BackupMode**](ElasticsearchS3BackupMode.md) |  |  [optional] |
|**s3DestinationDescription** | [**RedshiftDestinationDescriptionS3DestinationDescription**](RedshiftDestinationDescriptionS3DestinationDescription.md) |  |  [optional] |
|**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**ElasticsearchDestinationDescriptionCloudWatchLoggingOptions**](ElasticsearchDestinationDescriptionCloudWatchLoggingOptions.md) |  |  [optional] |
|**vpcConfigurationDescription** | [**ElasticsearchDestinationDescriptionVpcConfigurationDescription**](ElasticsearchDestinationDescriptionVpcConfigurationDescription.md) |  |  [optional] |



