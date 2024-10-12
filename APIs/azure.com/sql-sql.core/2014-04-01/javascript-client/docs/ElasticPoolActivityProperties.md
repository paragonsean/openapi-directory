# AzureSqlDatabase.ElasticPoolActivityProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elasticPoolName** | **String** | The name of the elastic pool. | [optional] [readonly] 
**endTime** | **Date** | The time the operation finished (ISO8601 format). | [optional] [readonly] 
**errorCode** | **Number** | The error code if available. | [optional] [readonly] 
**errorMessage** | **String** | The error message if available. | [optional] [readonly] 
**errorSeverity** | **Number** | The error severity if available. | [optional] [readonly] 
**operation** | **String** | The operation name. | [optional] [readonly] 
**operationId** | **String** | The unique operation ID. | [optional] [readonly] 
**percentComplete** | **Number** | The percentage complete if available. | [optional] [readonly] 
**requestedDatabaseDtuCap** | **Number** | The requested per database DTU cap. | [optional] [readonly] 
**requestedDatabaseDtuGuarantee** | **Number** | The requested per database DTU guarantee. | [optional] [readonly] 
**requestedDatabaseDtuMax** | **Number** | The requested max DTU per database if available. | [optional] [readonly] 
**requestedDatabaseDtuMin** | **Number** | The requested min DTU per database if available. | [optional] [readonly] 
**requestedDtu** | **Number** | The requested DTU for the pool if available. | [optional] [readonly] 
**requestedDtuGuarantee** | **Number** | The requested DTU guarantee. | [optional] [readonly] 
**requestedElasticPoolName** | **String** | The requested name for the elastic pool if available. | [optional] [readonly] 
**requestedStorageLimitInGB** | **Number** | The requested storage limit for the pool in GB if available. | [optional] [readonly] 
**requestedStorageLimitInMB** | **Number** | The requested storage limit in MB. | [optional] [readonly] 
**serverName** | **String** | The name of the server the elastic pool is in. | [optional] [readonly] 
**startTime** | **Date** | The time the operation started (ISO8601 format). | [optional] [readonly] 
**state** | **String** | The current state of the operation. | [optional] [readonly] 


