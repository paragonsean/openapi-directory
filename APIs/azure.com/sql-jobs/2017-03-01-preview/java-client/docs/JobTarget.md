

# JobTarget

A job target, for example a specific database or a container of databases that is evaluated during job execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseName** | **String** | The target database name. |  [optional] |
|**elasticPoolName** | **String** | The target elastic pool name. |  [optional] |
|**membershipType** | [**MembershipTypeEnum**](#MembershipTypeEnum) | Whether the target is included or excluded from the group. |  [optional] |
|**refreshCredential** | **String** | The resource ID of the credential that is used during job execution to connect to the target and determine the list of databases inside the target. |  [optional] |
|**serverName** | **String** | The target server name. |  [optional] |
|**shardMapName** | **String** | The target shard map. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The target type. |  |



## Enum: MembershipTypeEnum

| Name | Value |
|---- | -----|
| INCLUDE | &quot;Include&quot; |
| EXCLUDE | &quot;Exclude&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TARGET_GROUP | &quot;TargetGroup&quot; |
| SQL_DATABASE | &quot;SqlDatabase&quot; |
| SQL_ELASTIC_POOL | &quot;SqlElasticPool&quot; |
| SQL_SHARD_MAP | &quot;SqlShardMap&quot; |
| SQL_SERVER | &quot;SqlServer&quot; |



