

# S3GlueParquetTarget

Specifies a data target that writes to Amazon S3 in Apache Parquet columnar storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**inputs** | [**List**](List.md) |  |  |
|**partitionKeys** | [**List**](List.md) |  |  [optional] |
|**path** | [**String**](String.md) |  |  |
|**compression** | [**ParquetCompressionType**](ParquetCompressionType.md) |  |  [optional] |
|**schemaChangePolicy** | [**S3GlueParquetTargetSchemaChangePolicy**](S3GlueParquetTargetSchemaChangePolicy.md) |  |  [optional] |



