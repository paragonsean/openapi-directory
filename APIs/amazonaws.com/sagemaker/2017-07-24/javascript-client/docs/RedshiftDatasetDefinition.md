# AmazonSageMakerService.RedshiftDatasetDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterId** | **String** | The Redshift cluster Identifier. | 
**database** | **String** | The name of the Redshift database used in Redshift query execution. | 
**dbUser** | **String** | The database user name used in Redshift query execution. | 
**queryString** | **String** | The SQL query statements to be executed. | 
**clusterRoleArn** | **String** |  | 
**outputS3Uri** | **String** |  | 
**kmsKeyId** | **String** |  | [optional] 
**outputFormat** | [**RedshiftResultFormat**](RedshiftResultFormat.md) |  | 
**outputCompression** | [**RedshiftResultCompressionType**](RedshiftResultCompressionType.md) |  | [optional] 


