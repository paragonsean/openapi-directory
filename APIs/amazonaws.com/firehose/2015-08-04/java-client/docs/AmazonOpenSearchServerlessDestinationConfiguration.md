

# AmazonOpenSearchServerlessDestinationConfiguration

Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  |
|**collectionEndpoint** | [**String**](String.md) |  |  [optional] |
|**indexName** | [**String**](String.md) |  |  |
|**bufferingHints** | [**AmazonOpenSearchServerlessDestinationConfigurationBufferingHints**](AmazonOpenSearchServerlessDestinationConfigurationBufferingHints.md) |  |  [optional] |
|**retryOptions** | [**AmazonOpenSearchServerlessDestinationConfigurationRetryOptions**](AmazonOpenSearchServerlessDestinationConfigurationRetryOptions.md) |  |  [optional] |
|**s3BackupMode** | [**AmazonOpenSearchServerlessS3BackupMode**](AmazonOpenSearchServerlessS3BackupMode.md) |  |  [optional] |
|**s3Configuration** | [**S3DestinationConfiguration**](S3DestinationConfiguration.md) |  |  |
|**processingConfiguration** | [**ProcessingConfiguration**](ProcessingConfiguration.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**CloudWatchLoggingOptions**](CloudWatchLoggingOptions.md) |  |  [optional] |
|**vpcConfiguration** | [**VpcConfiguration**](VpcConfiguration.md) |  |  [optional] |



