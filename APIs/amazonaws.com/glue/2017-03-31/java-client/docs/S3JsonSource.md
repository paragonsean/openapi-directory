

# S3JsonSource

Specifies a JSON data store stored in Amazon S3.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**paths** | [**List**](List.md) |  |  |
|**compressionType** | [**CompressionType**](CompressionType.md) |  |  [optional] |
|**exclusions** | [**List**](List.md) |  |  [optional] |
|**groupSize** | [**String**](String.md) |  |  [optional] |
|**groupFiles** | [**String**](String.md) |  |  [optional] |
|**recurse** | [**Boolean**](Boolean.md) |  |  [optional] |
|**maxBand** | [**Integer**](Integer.md) |  |  [optional] |
|**maxFilesInBand** | [**Integer**](Integer.md) |  |  [optional] |
|**additionalOptions** | [**S3CsvSourceAdditionalOptions**](S3CsvSourceAdditionalOptions.md) |  |  [optional] |
|**jsonPath** | [**String**](String.md) |  |  [optional] |
|**multiline** | [**Boolean**](Boolean.md) |  |  [optional] |
|**outputSchemas** | [**List**](List.md) |  |  [optional] |



