

# RedshiftDatasetDefinition

Configuration for Redshift Dataset Definition input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterId** | **String** | The Redshift cluster Identifier. |  |
|**database** | **String** | The name of the Redshift database used in Redshift query execution. |  |
|**dbUser** | **String** | The database user name used in Redshift query execution. |  |
|**queryString** | **String** | The SQL query statements to be executed. |  |
|**clusterRoleArn** | [**String**](String.md) |  |  |
|**outputS3Uri** | [**String**](String.md) |  |  |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**outputFormat** | **RedshiftResultFormat** |  |  |
|**outputCompression** | **RedshiftResultCompressionType** |  |  [optional] |



