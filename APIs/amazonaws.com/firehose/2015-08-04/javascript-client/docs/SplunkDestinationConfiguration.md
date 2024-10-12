# AmazonKinesisFirehose.SplunkDestinationConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hECEndpoint** | **String** |  | 
**hECEndpointType** | [**HECEndpointType**](HECEndpointType.md) |  | 
**hECToken** | **String** |  | 
**hECAcknowledgmentTimeoutInSeconds** | **Number** |  | [optional] 
**retryOptions** | [**SplunkDestinationConfigurationRetryOptions**](SplunkDestinationConfigurationRetryOptions.md) |  | [optional] 
**s3BackupMode** | [**SplunkS3BackupMode**](SplunkS3BackupMode.md) |  | [optional] 
**s3Configuration** | [**ElasticsearchDestinationConfigurationS3Configuration**](ElasticsearchDestinationConfigurationS3Configuration.md) |  | 
**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  | [optional] 
**cloudWatchLoggingOptions** | [**S3DestinationDescriptionCloudWatchLoggingOptions**](S3DestinationDescriptionCloudWatchLoggingOptions.md) |  | [optional] 


