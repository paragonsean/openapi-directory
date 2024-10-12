# AmazonKinesisFirehose.CreateDeliveryStreamInputAmazonopensearchserviceDestinationConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roleARN** | **String** |  | 
**domainARN** | **String** |  | [optional] 
**clusterEndpoint** | **String** |  | [optional] 
**indexName** | **String** |  | 
**typeName** | **String** |  | [optional] 
**indexRotationPeriod** | [**AmazonopensearchserviceIndexRotationPeriod**](AmazonopensearchserviceIndexRotationPeriod.md) |  | [optional] 
**bufferingHints** | [**AmazonopensearchserviceDestinationConfigurationBufferingHints**](AmazonopensearchserviceDestinationConfigurationBufferingHints.md) |  | [optional] 
**retryOptions** | [**AmazonopensearchserviceDestinationConfigurationRetryOptions**](AmazonopensearchserviceDestinationConfigurationRetryOptions.md) |  | [optional] 
**s3BackupMode** | [**AmazonopensearchserviceS3BackupMode**](AmazonopensearchserviceS3BackupMode.md) |  | [optional] 
**s3Configuration** | [**S3DestinationConfiguration**](S3DestinationConfiguration.md) |  | 
**processingConfiguration** | [**ProcessingConfiguration**](ProcessingConfiguration.md) |  | [optional] 
**cloudWatchLoggingOptions** | [**CloudWatchLoggingOptions**](CloudWatchLoggingOptions.md) |  | [optional] 
**vpcConfiguration** | [**VpcConfiguration**](VpcConfiguration.md) |  | [optional] 


