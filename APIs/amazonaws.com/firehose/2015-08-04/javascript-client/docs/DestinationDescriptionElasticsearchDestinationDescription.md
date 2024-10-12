# AmazonKinesisFirehose.DestinationDescriptionElasticsearchDestinationDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roleARN** | **String** |  | [optional] 
**domainARN** | **String** |  | [optional] 
**clusterEndpoint** | **String** |  | [optional] 
**indexName** | **String** |  | [optional] 
**typeName** | **String** |  | [optional] 
**indexRotationPeriod** | [**ElasticsearchIndexRotationPeriod**](ElasticsearchIndexRotationPeriod.md) |  | [optional] 
**bufferingHints** | [**ElasticsearchDestinationDescriptionBufferingHints**](ElasticsearchDestinationDescriptionBufferingHints.md) |  | [optional] 
**retryOptions** | [**ElasticsearchDestinationDescriptionRetryOptions**](ElasticsearchDestinationDescriptionRetryOptions.md) |  | [optional] 
**s3BackupMode** | [**ElasticsearchS3BackupMode**](ElasticsearchS3BackupMode.md) |  | [optional] 
**s3DestinationDescription** | [**RedshiftDestinationDescriptionS3DestinationDescription**](RedshiftDestinationDescriptionS3DestinationDescription.md) |  | [optional] 
**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  | [optional] 
**cloudWatchLoggingOptions** | [**ElasticsearchDestinationDescriptionCloudWatchLoggingOptions**](ElasticsearchDestinationDescriptionCloudWatchLoggingOptions.md) |  | [optional] 
**vpcConfigurationDescription** | [**ElasticsearchDestinationDescriptionVpcConfigurationDescription**](ElasticsearchDestinationDescriptionVpcConfigurationDescription.md) |  | [optional] 


