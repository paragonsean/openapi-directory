# SqlManagementClient.JobTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseName** | **String** | The target database name. | [optional] 
**elasticPoolName** | **String** | The target elastic pool name. | [optional] 
**membershipType** | **String** | Whether the target is included or excluded from the group. | [optional] [default to &#39;Include&#39;]
**refreshCredential** | **String** | The resource ID of the credential that is used during job execution to connect to the target and determine the list of databases inside the target. | [optional] 
**serverName** | **String** | The target server name. | [optional] 
**shardMapName** | **String** | The target shard map. | [optional] 
**type** | **String** | The target type. | 



## Enum: MembershipTypeEnum


* `Include` (value: `"Include"`)

* `Exclude` (value: `"Exclude"`)





## Enum: TypeEnum


* `TargetGroup` (value: `"TargetGroup"`)

* `SqlDatabase` (value: `"SqlDatabase"`)

* `SqlElasticPool` (value: `"SqlElasticPool"`)

* `SqlShardMap` (value: `"SqlShardMap"`)

* `SqlServer` (value: `"SqlServer"`)




