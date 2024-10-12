

# ElasticPoolActivityProperties

Represents the properties of an elastic pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elasticPoolName** | **String** | The name of the elastic pool. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | The time the operation finished (ISO8601 format). |  [optional] [readonly] |
|**errorCode** | **Integer** | The error code if available. |  [optional] [readonly] |
|**errorMessage** | **String** | The error message if available. |  [optional] [readonly] |
|**errorSeverity** | **Integer** | The error severity if available. |  [optional] [readonly] |
|**operation** | **String** | The operation name. |  [optional] [readonly] |
|**operationId** | **UUID** | The unique operation ID. |  [optional] [readonly] |
|**percentComplete** | **Integer** | The percentage complete if available. |  [optional] [readonly] |
|**requestedDatabaseDtuCap** | **Integer** | The requested per database DTU cap. |  [optional] [readonly] |
|**requestedDatabaseDtuGuarantee** | **Integer** | The requested per database DTU guarantee. |  [optional] [readonly] |
|**requestedDatabaseDtuMax** | **Integer** | The requested max DTU per database if available. |  [optional] [readonly] |
|**requestedDatabaseDtuMin** | **Integer** | The requested min DTU per database if available. |  [optional] [readonly] |
|**requestedDtu** | **Integer** | The requested DTU for the pool if available. |  [optional] [readonly] |
|**requestedDtuGuarantee** | **Integer** | The requested DTU guarantee. |  [optional] [readonly] |
|**requestedElasticPoolName** | **String** | The requested name for the elastic pool if available. |  [optional] [readonly] |
|**requestedStorageLimitInGB** | **Long** | The requested storage limit for the pool in GB if available. |  [optional] [readonly] |
|**requestedStorageLimitInMB** | **Integer** | The requested storage limit in MB. |  [optional] [readonly] |
|**serverName** | **String** | The name of the server the elastic pool is in. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The time the operation started (ISO8601 format). |  [optional] [readonly] |
|**state** | **String** | The current state of the operation. |  [optional] [readonly] |



