

# GoogleCloudDataplexV1StorageFormat

Describes the format of the data within its storage location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compressionFormat** | [**CompressionFormatEnum**](#CompressionFormatEnum) | Optional. The compression type associated with the stored data. If unspecified, the data is uncompressed. |  [optional] |
|**csv** | [**GoogleCloudDataplexV1StorageFormatCsvOptions**](GoogleCloudDataplexV1StorageFormatCsvOptions.md) |  |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Output only. The data format associated with the stored data, which represents content type values. The value is inferred from mime type. |  [optional] [readonly] |
|**iceberg** | [**GoogleCloudDataplexV1StorageFormatIcebergOptions**](GoogleCloudDataplexV1StorageFormatIcebergOptions.md) |  |  [optional] |
|**json** | [**GoogleCloudDataplexV1StorageFormatJsonOptions**](GoogleCloudDataplexV1StorageFormatJsonOptions.md) |  |  [optional] |
|**mimeType** | **String** | Required. The mime type descriptor for the data. Must match the pattern {type}/{subtype}. Supported values: application/x-parquet application/x-avro application/x-orc application/x-tfrecord application/x-parquet+iceberg application/x-avro+iceberg application/x-orc+iceberg application/json application/{subtypes} text/csv text/ image/{image subtype} video/{video subtype} audio/{audio subtype} |  [optional] |



## Enum: CompressionFormatEnum

| Name | Value |
|---- | -----|
| COMPRESSION_FORMAT_UNSPECIFIED | &quot;COMPRESSION_FORMAT_UNSPECIFIED&quot; |
| GZIP | &quot;GZIP&quot; |
| BZIP2 | &quot;BZIP2&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| FORMAT_UNSPECIFIED | &quot;FORMAT_UNSPECIFIED&quot; |
| PARQUET | &quot;PARQUET&quot; |
| AVRO | &quot;AVRO&quot; |
| ORC | &quot;ORC&quot; |
| CSV | &quot;CSV&quot; |
| JSON | &quot;JSON&quot; |
| IMAGE | &quot;IMAGE&quot; |
| AUDIO | &quot;AUDIO&quot; |
| VIDEO | &quot;VIDEO&quot; |
| TEXT | &quot;TEXT&quot; |
| TFRECORD | &quot;TFRECORD&quot; |
| OTHER | &quot;OTHER&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



