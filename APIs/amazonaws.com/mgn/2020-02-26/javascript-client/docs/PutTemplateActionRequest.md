# ApplicationMigrationService.PutTemplateActionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionID** | **String** | Template post migration custom action ID. | 
**actionName** | **String** | Template post migration custom action name. | 
**active** | **Boolean** | Template post migration custom action active status. | [optional] 
**category** | **String** | Template post migration custom action category. | [optional] 
**description** | **String** | Template post migration custom action description. | [optional] 
**documentIdentifier** | **String** | Template post migration custom action document identifier. | 
**documentVersion** | **String** | Template post migration custom action document version. | [optional] 
**externalParameters** | [**{String: SsmExternalParameter}**](SsmExternalParameter.md) | Template post migration custom action external parameters. | [optional] 
**launchConfigurationTemplateID** | **String** | Launch configuration template ID. | 
**mustSucceedForCutover** | **Boolean** | Template post migration custom action must succeed for cutover. | [optional] 
**operatingSystem** | **String** | Operating system eligible for this template post migration custom action. | [optional] 
**order** | **Number** | Template post migration custom action order. | 
**parameters** | **{String: Array}** | Template post migration custom action parameters. | [optional] 
**timeoutSeconds** | **Number** | Template post migration custom action timeout in seconds. | [optional] 



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




