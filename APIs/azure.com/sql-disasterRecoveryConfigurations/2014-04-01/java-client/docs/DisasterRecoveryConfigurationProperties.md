

# DisasterRecoveryConfigurationProperties

Represents the properties of a disaster recovery configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoFailover** | [**AutoFailoverEnum**](#AutoFailoverEnum) | Whether or not failover can be done automatically. |  |
|**failoverPolicy** | [**FailoverPolicyEnum**](#FailoverPolicyEnum) | How aggressive the automatic failover should be. |  |
|**logicalServerName** | **String** | Logical name of the server. |  [optional] [readonly] |
|**partnerLogicalServerName** | **String** | Logical name of the partner server. |  [optional] [readonly] |
|**partnerServerId** | **String** | Id of the partner server. |  |
|**role** | [**RoleEnum**](#RoleEnum) | The role of the current server in the disaster recovery configuration. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the disaster recovery configuration. |  [optional] [readonly] |



## Enum: AutoFailoverEnum

| Name | Value |
|---- | -----|
| OFF | &quot;Off&quot; |
| ON | &quot;On&quot; |



## Enum: FailoverPolicyEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;Manual&quot; |
| AUTOMATIC | &quot;Automatic&quot; |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PRIMARY | &quot;Primary&quot; |
| SECONDARY | &quot;Secondary&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| READY | &quot;Ready&quot; |
| FAILING_OVER | &quot;FailingOver&quot; |
| DROPPING | &quot;Dropping&quot; |



