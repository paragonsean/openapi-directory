

# S3DestinationDescription

Describes a destination in Amazon S3.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  |
|**bucketARN** | [**String**](String.md) |  |  |
|**prefix** | [**String**](String.md) |  |  [optional] |
|**errorOutputPrefix** | [**String**](String.md) |  |  [optional] |
|**bufferingHints** | [**S3DestinationConfigurationBufferingHints**](S3DestinationConfigurationBufferingHints.md) |  |  |
|**compressionFormat** | [**CompressionFormat**](CompressionFormat.md) |  |  |
|**encryptionConfiguration** | [**S3DestinationConfigurationEncryptionConfiguration**](S3DestinationConfigurationEncryptionConfiguration.md) |  |  |
|**cloudWatchLoggingOptions** | [**S3DestinationDescriptionCloudWatchLoggingOptions**](S3DestinationDescriptionCloudWatchLoggingOptions.md) |  |  [optional] |



