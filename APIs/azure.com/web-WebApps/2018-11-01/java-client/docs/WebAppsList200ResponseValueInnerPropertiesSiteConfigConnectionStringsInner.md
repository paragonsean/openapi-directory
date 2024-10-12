

# WebAppsList200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner

Database connection string information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionString** | **String** | Connection string value. |  [optional] |
|**name** | **String** | Name of connection string. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of database. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MY_SQL | &quot;MySql&quot; |
| SQL_SERVER | &quot;SQLServer&quot; |
| SQL_AZURE | &quot;SQLAzure&quot; |
| CUSTOM | &quot;Custom&quot; |
| NOTIFICATION_HUB | &quot;NotificationHub&quot; |
| SERVICE_BUS | &quot;ServiceBus&quot; |
| EVENT_HUB | &quot;EventHub&quot; |
| API_HUB | &quot;ApiHub&quot; |
| DOC_DB | &quot;DocDb&quot; |
| REDIS_CACHE | &quot;RedisCache&quot; |
| POSTGRE_SQL | &quot;PostgreSQL&quot; |



