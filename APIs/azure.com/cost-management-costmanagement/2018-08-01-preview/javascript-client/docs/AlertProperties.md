# CostManagementClient.AlertProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closeTime** | **Date** | The time when the alert was closed (resolved / overridden). | [optional] [readonly] 
**costEntityId** | **String** | The id of the creating cost-entity (budget, invoice, credit). | [optional] [readonly] 
**creationTime** | **Date** | The time when the alert was created. | [optional] [readonly] 
**definition** | [**AlertDefinition**](AlertDefinition.md) |  | [optional] 
**description** | **String** | Description of an alert. | [optional] [readonly] 
**details** | **{String: String}** | Specific details of an alert - key-value dictionary. | [optional] [readonly] 
**modificationTime** | **Date** | The current status when alert was modified. | [optional] [readonly] 
**modificationUsername** | **String** | The username who modified the alert. | [optional] [readonly] 
**scope** | **String** | The scope of an alert. | [optional] [readonly] 
**source** | **String** | The source of an Alert | [optional] [readonly] 
**status** | **String** | The current status of the alert. | [optional] 
**statusModificationTime** | **Date** | The current status when alert status was modified. | [optional] [readonly] 



## Enum: SourceEnum


* `Preset` (value: `"Preset"`)

* `User` (value: `"User"`)





## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Overridden` (value: `"Overridden"`)

* `Resolved` (value: `"Resolved"`)

* `Dismissed` (value: `"Dismissed"`)




