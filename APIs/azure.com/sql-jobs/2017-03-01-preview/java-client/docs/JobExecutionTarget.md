

# JobExecutionTarget

The target that a job execution is executed on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseName** | **String** | The database name. |  [optional] [readonly] |
|**serverName** | **String** | The server name. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the target. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TARGET_GROUP | &quot;TargetGroup&quot; |
| SQL_DATABASE | &quot;SqlDatabase&quot; |
| SQL_ELASTIC_POOL | &quot;SqlElasticPool&quot; |
| SQL_SHARD_MAP | &quot;SqlShardMap&quot; |
| SQL_SERVER | &quot;SqlServer&quot; |



