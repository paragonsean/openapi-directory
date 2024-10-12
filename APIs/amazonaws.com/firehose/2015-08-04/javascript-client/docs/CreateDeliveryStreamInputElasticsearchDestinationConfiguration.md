# AmazonKinesisFirehose.CreateDeliveryStreamInputElasticsearchDestinationConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roleARN** | **String** |  | 
**domainARN** | **String** |  | [optional] 
**clusterEndpoint** | **String** |  | [optional] 
**indexName** | **String** |  | 
**typeName** | **String** |  | [optional] 
**indexRotationPeriod** | [**ElasticsearchIndexRotationPeriod**](ElasticsearchIndexRotationPeriod.md) |  | [optional] 
**bufferingHints** | [**ElasticsearchDestinationConfigurationBufferingHints**](ElasticsearchDestinationConfigurationBufferingHints.md) |  | [optional] 
**retryOptions** | [**ElasticsearchDestinationConfigurationRetryOptions**](ElasticsearchDestinationConfigurationRetryOptions.md) |  | [optional] 
**s3BackupMode** | [**ElasticsearchS3BackupMode**](ElasticsearchS3BackupMode.md) |  | [optional] 
**s3Configuration** | [**ElasticsearchDestinationConfigurationS3Configuration**](ElasticsearchDestinationConfigurationS3Configuration.md) |  | 
**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  | [optional] 
**cloudWatchLoggingOptions** | [**S3DestinationDescriptionCloudWatchLoggingOptions**](S3DestinationDescriptionCloudWatchLoggingOptions.md) |  | [optional] 
**vpcConfiguration** | [**ElasticsearchDestinationConfigurationVpcConfiguration**](ElasticsearchDestinationConfigurationVpcConfiguration.md) |  | [optional] 


