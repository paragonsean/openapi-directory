

# AthenaDatasetDefinition

Configuration for Athena Dataset Definition input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalog** | **String** | The name of the data catalog used in Athena query execution. |  |
|**database** | **String** | The name of the database used in the Athena query execution. |  |
|**queryString** | **String** | The SQL query statements, to be executed. |  |
|**workGroup** | **String** | The name of the workgroup in which the Athena query is being started. |  [optional] |
|**outputS3Uri** | [**String**](String.md) |  |  |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**outputFormat** | **AthenaResultFormat** |  |  |
|**outputCompression** | **AthenaResultCompressionType** |  |  [optional] |



