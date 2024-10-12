

# CreateDeliveryStreamInputExtendedS3DestinationConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  |
|**bucketARN** | [**String**](String.md) |  |  |
|**prefix** | [**String**](String.md) |  |  [optional] |
|**errorOutputPrefix** | [**String**](String.md) |  |  [optional] |
|**bufferingHints** | [**ExtendedS3DestinationConfigurationBufferingHints**](ExtendedS3DestinationConfigurationBufferingHints.md) |  |  [optional] |
|**compressionFormat** | [**CompressionFormat**](CompressionFormat.md) |  |  [optional] |
|**encryptionConfiguration** | [**S3DestinationConfigurationEncryptionConfiguration**](S3DestinationConfigurationEncryptionConfiguration.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**S3DestinationDescriptionCloudWatchLoggingOptions**](S3DestinationDescriptionCloudWatchLoggingOptions.md) |  |  [optional] |
|**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  |  [optional] |
|**s3BackupMode** | [**S3BackupMode**](S3BackupMode.md) |  |  [optional] |
|**s3BackupConfiguration** | [**ExtendedS3DestinationConfigurationS3BackupConfiguration**](ExtendedS3DestinationConfigurationS3BackupConfiguration.md) |  |  [optional] |
|**dataFormatConversionConfiguration** | [**ExtendedS3DestinationConfigurationDataFormatConversionConfiguration**](ExtendedS3DestinationConfigurationDataFormatConversionConfiguration.md) |  |  [optional] |
|**dynamicPartitioningConfiguration** | [**ExtendedS3DestinationConfigurationDynamicPartitioningConfiguration**](ExtendedS3DestinationConfigurationDynamicPartitioningConfiguration.md) |  |  [optional] |



