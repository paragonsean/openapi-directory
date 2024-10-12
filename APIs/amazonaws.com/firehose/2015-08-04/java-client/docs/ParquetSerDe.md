

# ParquetSerDe

A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see <a href=\"https://parquet.apache.org/documentation/latest/\">Apache Parquet</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockSizeBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**pageSizeBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**compression** | [**ParquetCompression**](ParquetCompression.md) |  |  [optional] |
|**enableDictionaryCompression** | [**Boolean**](Boolean.md) |  |  [optional] |
|**maxPaddingBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**writerVersion** | [**ParquetWriterVersion**](ParquetWriterVersion.md) |  |  [optional] |



