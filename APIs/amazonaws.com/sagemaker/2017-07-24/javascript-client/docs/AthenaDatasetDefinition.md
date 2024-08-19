# AmazonSageMakerService.AthenaDatasetDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **String** | The name of the data catalog used in Athena query execution. | 
**database** | **String** | The name of the database used in the Athena query execution. | 
**queryString** | **String** | The SQL query statements, to be executed. | 
**workGroup** | **String** | The name of the workgroup in which the Athena query is being started. | [optional] 
**outputS3Uri** | **String** |  | 
**kmsKeyId** | **String** |  | [optional] 
**outputFormat** | [**AthenaResultFormat**](AthenaResultFormat.md) |  | 
**outputCompression** | [**AthenaResultCompressionType**](AthenaResultCompressionType.md) |  | [optional] 


