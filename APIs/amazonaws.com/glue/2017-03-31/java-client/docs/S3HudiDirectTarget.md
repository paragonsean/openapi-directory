

# S3HudiDirectTarget

Specifies a target that writes to a Hudi data source in Amazon S3.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**inputs** | [**List**](List.md) |  |  |
|**path** | [**String**](String.md) |  |  |
|**compression** | [**HudiTargetCompressionType**](HudiTargetCompressionType.md) |  |  |
|**partitionKeys** | [**List**](List.md) |  |  [optional] |
|**format** | [**TargetFormat**](TargetFormat.md) |  |  |
|**additionalOptions** | [**Map**](Map.md) |  |  |
|**schemaChangePolicy** | [**S3GlueParquetTargetSchemaChangePolicy**](S3GlueParquetTargetSchemaChangePolicy.md) |  |  [optional] |



