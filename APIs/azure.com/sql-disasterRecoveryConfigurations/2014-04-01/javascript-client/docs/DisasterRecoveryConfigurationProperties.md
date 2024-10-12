# AzureSqlDatabaseDisasterRecoveryConfigurations.DisasterRecoveryConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoFailover** | **String** | Whether or not failover can be done automatically. | 
**failoverPolicy** | **String** | How aggressive the automatic failover should be. | 
**logicalServerName** | **String** | Logical name of the server. | [optional] [readonly] 
**partnerLogicalServerName** | **String** | Logical name of the partner server. | [optional] [readonly] 
**partnerServerId** | **String** | Id of the partner server. | 
**role** | **String** | The role of the current server in the disaster recovery configuration. | [optional] [readonly] 
**status** | **String** | The status of the disaster recovery configuration. | [optional] [readonly] 



## Enum: AutoFailoverEnum


* `Off` (value: `"Off"`)

* `On` (value: `"On"`)





## Enum: FailoverPolicyEnum


* `Manual` (value: `"Manual"`)

* `Automatic` (value: `"Automatic"`)





## Enum: RoleEnum


* `None` (value: `"None"`)

* `Primary` (value: `"Primary"`)

* `Secondary` (value: `"Secondary"`)





## Enum: StatusEnum


* `Creating` (value: `"Creating"`)

* `Ready` (value: `"Ready"`)

* `FailingOver` (value: `"FailingOver"`)

* `Dropping` (value: `"Dropping"`)




