# ApplicationMigrationService.PutSourceServerActionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountID** | **String** | Source server post migration custom account ID. | [optional] 
**actionID** | **String** | Source server post migration custom action ID. | 
**actionName** | **String** | Source server post migration custom action name. | 
**active** | **Boolean** | Source server post migration custom action active status. | [optional] 
**category** | **String** | Source server post migration custom action category. | [optional] 
**description** | **String** | Source server post migration custom action description. | [optional] 
**documentIdentifier** | **String** | Source server post migration custom action document identifier. | 
**documentVersion** | **String** | Source server post migration custom action document version. | [optional] 
**externalParameters** | [**{String: SsmExternalParameter}**](SsmExternalParameter.md) | Source server post migration custom action external parameters. | [optional] 
**mustSucceedForCutover** | **Boolean** | Source server post migration custom action must succeed for cutover. | [optional] 
**order** | **Number** | Source server post migration custom action order. | 
**parameters** | **{String: Array}** | Source server post migration custom action parameters. | [optional] 
**sourceServerID** | **String** | Source server ID. | 
**timeoutSeconds** | **Number** | Source server post migration custom action timeout in seconds. | [optional] 



## Enum: CategoryEnum


* `DISASTER_RECOVERY` (value: `"DISASTER_RECOVERY"`)

* `OPERATING_SYSTEM` (value: `"OPERATING_SYSTEM"`)

* `LICENSE_AND_SUBSCRIPTION` (value: `"LICENSE_AND_SUBSCRIPTION"`)

* `VALIDATION` (value: `"VALIDATION"`)

* `OBSERVABILITY` (value: `"OBSERVABILITY"`)

* `SECURITY` (value: `"SECURITY"`)

* `NETWORKING` (value: `"NETWORKING"`)

* `CONFIGURATION` (value: `"CONFIGURATION"`)

* `BACKUP` (value: `"BACKUP"`)

* `OTHER` (value: `"OTHER"`)




