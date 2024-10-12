# AmazonKinesisFirehose.CreateDeliveryStreamInputRedshiftDestinationConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roleARN** | **String** |  | 
**clusterJDBCURL** | **String** |  | 
**copyCommand** | [**RedshiftDestinationConfigurationCopyCommand**](RedshiftDestinationConfigurationCopyCommand.md) |  | 
**username** | **String** |  | 
**password** | **String** |  | 
**retryOptions** | [**RedshiftDestinationConfigurationRetryOptions**](RedshiftDestinationConfigurationRetryOptions.md) |  | [optional] 
**s3Configuration** | [**RedshiftDestinationConfigurationS3Configuration**](RedshiftDestinationConfigurationS3Configuration.md) |  | 
**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  | [optional] 
**s3BackupMode** | [**RedshiftS3BackupMode**](RedshiftS3BackupMode.md) |  | [optional] 
**s3BackupConfiguration** | [**ExtendedS3DestinationConfigurationS3BackupConfiguration**](ExtendedS3DestinationConfigurationS3BackupConfiguration.md) |  | [optional] 
**cloudWatchLoggingOptions** | [**S3DestinationConfigurationCloudWatchLoggingOptions**](S3DestinationConfigurationCloudWatchLoggingOptions.md) |  | [optional] 


