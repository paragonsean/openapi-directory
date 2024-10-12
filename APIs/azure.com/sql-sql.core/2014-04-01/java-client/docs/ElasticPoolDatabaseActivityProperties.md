

# ElasticPoolDatabaseActivityProperties

Represents the properties of an elastic pool database activity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentElasticPoolName** | **String** | The name of the current elastic pool the database is in if available. |  [optional] [readonly] |
|**currentServiceObjective** | **String** | The name of the current service objective if available. |  [optional] [readonly] |
|**databaseName** | **String** | The database name. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | The time the operation finished (ISO8601 format). |  [optional] [readonly] |
|**errorCode** | **Integer** | The error code if available. |  [optional] [readonly] |
|**errorMessage** | **String** | The error message if available. |  [optional] [readonly] |
|**errorSeverity** | **Integer** | The error severity if available. |  [optional] [readonly] |
|**operation** | **String** | The operation name. |  [optional] [readonly] |
|**operationId** | **UUID** | The unique operation ID. |  [optional] [readonly] |
|**percentComplete** | **Integer** | The percentage complete if available. |  [optional] [readonly] |
|**requestedElasticPoolName** | **String** | The name for the elastic pool the database is moving into if available. |  [optional] [readonly] |
|**requestedServiceObjective** | **String** | The name of the requested service objective if available. |  [optional] [readonly] |
|**serverName** | **String** | The name of the server the elastic pool is in. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The time the operation started (ISO8601 format). |  [optional] [readonly] |
|**state** | **String** | The current state of the operation. |  [optional] [readonly] |



