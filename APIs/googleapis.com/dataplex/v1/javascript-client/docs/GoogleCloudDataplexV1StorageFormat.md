# CloudDataplexApi.GoogleCloudDataplexV1StorageFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compressionFormat** | **String** | Optional. The compression type associated with the stored data. If unspecified, the data is uncompressed. | [optional] 
**csv** | [**GoogleCloudDataplexV1StorageFormatCsvOptions**](GoogleCloudDataplexV1StorageFormatCsvOptions.md) |  | [optional] 
**format** | **String** | Output only. The data format associated with the stored data, which represents content type values. The value is inferred from mime type. | [optional] [readonly] 
**iceberg** | [**GoogleCloudDataplexV1StorageFormatIcebergOptions**](GoogleCloudDataplexV1StorageFormatIcebergOptions.md) |  | [optional] 
**json** | [**GoogleCloudDataplexV1StorageFormatJsonOptions**](GoogleCloudDataplexV1StorageFormatJsonOptions.md) |  | [optional] 
**mimeType** | **String** | Required. The mime type descriptor for the data. Must match the pattern {type}/{subtype}. Supported values: application/x-parquet application/x-avro application/x-orc application/x-tfrecord application/x-parquet+iceberg application/x-avro+iceberg application/x-orc+iceberg application/json application/{subtypes} text/csv text/ image/{image subtype} video/{video subtype} audio/{audio subtype} | [optional] 



## Enum: CompressionFormatEnum


* `COMPRESSION_FORMAT_UNSPECIFIED` (value: `"COMPRESSION_FORMAT_UNSPECIFIED"`)

* `GZIP` (value: `"GZIP"`)

* `BZIP2` (value: `"BZIP2"`)





## Enum: FormatEnum


* `FORMAT_UNSPECIFIED` (value: `"FORMAT_UNSPECIFIED"`)

* `PARQUET` (value: `"PARQUET"`)

* `AVRO` (value: `"AVRO"`)

* `ORC` (value: `"ORC"`)

* `CSV` (value: `"CSV"`)

* `JSON` (value: `"JSON"`)

* `IMAGE` (value: `"IMAGE"`)

* `AUDIO` (value: `"AUDIO"`)

* `VIDEO` (value: `"VIDEO"`)

* `TEXT` (value: `"TEXT"`)

* `TFRECORD` (value: `"TFRECORD"`)

* `OTHER` (value: `"OTHER"`)

* `UNKNOWN` (value: `"UNKNOWN"`)




