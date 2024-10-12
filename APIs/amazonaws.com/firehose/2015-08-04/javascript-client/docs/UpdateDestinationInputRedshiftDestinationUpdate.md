# AmazonKinesisFirehose.UpdateDestinationInputRedshiftDestinationUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roleARN** | **String** |  | [optional] 
**clusterJDBCURL** | **String** |  | [optional] 
**copyCommand** | [**RedshiftDestinationConfigurationCopyCommand**](RedshiftDestinationConfigurationCopyCommand.md) |  | [optional] 
**username** | **String** |  | [optional] 
**password** | **String** |  | [optional] 
**retryOptions** | [**RedshiftDestinationConfigurationRetryOptions**](RedshiftDestinationConfigurationRetryOptions.md) |  | [optional] 
**s3Update** | [**RedshiftDestinationUpdateS3Update**](RedshiftDestinationUpdateS3Update.md) |  | [optional] 
**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  | [optional] 
**s3BackupMode** | [**RedshiftS3BackupMode**](RedshiftS3BackupMode.md) |  | [optional] 
**s3BackupUpdate** | [**ExtendedS3DestinationUpdateS3BackupUpdate**](ExtendedS3DestinationUpdateS3BackupUpdate.md) |  | [optional] 
**cloudWatchLoggingOptions** | [**S3DestinationDescriptionCloudWatchLoggingOptions**](S3DestinationDescriptionCloudWatchLoggingOptions.md) |  | [optional] 


