# AmazonKinesisFirehose.ElasticsearchDestinationUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roleARN** | **String** |  | [optional] 
**domainARN** | **String** |  | [optional] 
**clusterEndpoint** | **String** |  | [optional] 
**indexName** | **String** |  | [optional] 
**typeName** | **String** |  | [optional] 
**indexRotationPeriod** | [**ElasticsearchIndexRotationPeriod**](ElasticsearchIndexRotationPeriod.md) |  | [optional] 
**bufferingHints** | [**ElasticsearchDestinationUpdateBufferingHints**](ElasticsearchDestinationUpdateBufferingHints.md) |  | [optional] 
**retryOptions** | [**ElasticsearchDestinationConfigurationRetryOptions**](ElasticsearchDestinationConfigurationRetryOptions.md) |  | [optional] 
**s3Update** | [**ElasticsearchDestinationUpdateS3Update**](ElasticsearchDestinationUpdateS3Update.md) |  | [optional] 
**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  | [optional] 
**cloudWatchLoggingOptions** | [**S3DestinationConfigurationCloudWatchLoggingOptions**](S3DestinationConfigurationCloudWatchLoggingOptions.md) |  | [optional] 


