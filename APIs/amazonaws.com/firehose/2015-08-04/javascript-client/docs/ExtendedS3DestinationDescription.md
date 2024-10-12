# AmazonKinesisFirehose.ExtendedS3DestinationDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roleARN** | **String** |  | 
**bucketARN** | **String** |  | 
**prefix** | **String** |  | [optional] 
**errorOutputPrefix** | **String** |  | [optional] 
**bufferingHints** | [**ExtendedS3DestinationConfigurationBufferingHints**](ExtendedS3DestinationConfigurationBufferingHints.md) |  | 
**compressionFormat** | [**CompressionFormat**](CompressionFormat.md) |  | 
**encryptionConfiguration** | [**S3DestinationConfigurationEncryptionConfiguration**](S3DestinationConfigurationEncryptionConfiguration.md) |  | 
**cloudWatchLoggingOptions** | [**S3DestinationDescriptionCloudWatchLoggingOptions**](S3DestinationDescriptionCloudWatchLoggingOptions.md) |  | [optional] 
**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  | [optional] 
**s3BackupMode** | [**S3BackupMode**](S3BackupMode.md) |  | [optional] 
**s3BackupDescription** | [**ExtendedS3DestinationDescriptionS3BackupDescription**](ExtendedS3DestinationDescriptionS3BackupDescription.md) |  | [optional] 
**dataFormatConversionConfiguration** | [**ExtendedS3DestinationConfigurationDataFormatConversionConfiguration**](ExtendedS3DestinationConfigurationDataFormatConversionConfiguration.md) |  | [optional] 
**dynamicPartitioningConfiguration** | [**ExtendedS3DestinationConfigurationDynamicPartitioningConfiguration**](ExtendedS3DestinationConfigurationDynamicPartitioningConfiguration.md) |  | [optional] 


