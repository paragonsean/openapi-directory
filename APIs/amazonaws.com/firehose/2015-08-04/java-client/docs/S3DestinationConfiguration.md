

# S3DestinationConfiguration

Describes the configuration of a destination in Amazon S3.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  |
|**bucketARN** | [**String**](String.md) |  |  |
|**prefix** | [**String**](String.md) |  |  [optional] |
|**errorOutputPrefix** | [**String**](String.md) |  |  [optional] |
|**bufferingHints** | [**S3DestinationConfigurationBufferingHints**](S3DestinationConfigurationBufferingHints.md) |  |  [optional] |
|**compressionFormat** | [**CompressionFormat**](CompressionFormat.md) |  |  [optional] |
|**encryptionConfiguration** | [**S3DestinationConfigurationEncryptionConfiguration**](S3DestinationConfigurationEncryptionConfiguration.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**S3DestinationConfigurationCloudWatchLoggingOptions**](S3DestinationConfigurationCloudWatchLoggingOptions.md) |  |  [optional] |



