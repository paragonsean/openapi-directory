

# RedshiftDestinationDescription

Describes a destination in Amazon Redshift.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  |
|**clusterJDBCURL** | [**String**](String.md) |  |  |
|**copyCommand** | [**RedshiftDestinationConfigurationCopyCommand**](RedshiftDestinationConfigurationCopyCommand.md) |  |  |
|**username** | [**String**](String.md) |  |  |
|**retryOptions** | [**RedshiftDestinationConfigurationRetryOptions**](RedshiftDestinationConfigurationRetryOptions.md) |  |  [optional] |
|**s3DestinationDescription** | [**RedshiftDestinationDescriptionS3DestinationDescription**](RedshiftDestinationDescriptionS3DestinationDescription.md) |  |  |
|**processingConfiguration** | [**ExtendedS3DestinationConfigurationProcessingConfiguration**](ExtendedS3DestinationConfigurationProcessingConfiguration.md) |  |  [optional] |
|**s3BackupMode** | [**RedshiftS3BackupMode**](RedshiftS3BackupMode.md) |  |  [optional] |
|**s3BackupDescription** | [**ExtendedS3DestinationDescriptionS3BackupDescription**](ExtendedS3DestinationDescriptionS3BackupDescription.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**S3DestinationDescriptionCloudWatchLoggingOptions**](S3DestinationDescriptionCloudWatchLoggingOptions.md) |  |  [optional] |



