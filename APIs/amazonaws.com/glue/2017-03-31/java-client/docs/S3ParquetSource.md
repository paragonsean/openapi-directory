

# S3ParquetSource

Specifies an Apache Parquet data store stored in Amazon S3.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**paths** | [**List**](List.md) |  |  |
|**compressionType** | [**ParquetCompressionType**](ParquetCompressionType.md) |  |  [optional] |
|**exclusions** | [**List**](List.md) |  |  [optional] |
|**groupSize** | [**String**](String.md) |  |  [optional] |
|**groupFiles** | [**String**](String.md) |  |  [optional] |
|**recurse** | [**Boolean**](Boolean.md) |  |  [optional] |
|**maxBand** | [**Integer**](Integer.md) |  |  [optional] |
|**maxFilesInBand** | [**Integer**](Integer.md) |  |  [optional] |
|**additionalOptions** | [**S3CsvSourceAdditionalOptions**](S3CsvSourceAdditionalOptions.md) |  |  [optional] |
|**outputSchemas** | [**List**](List.md) |  |  [optional] |



