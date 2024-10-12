# MicrosoftResourceHealth.StatusActiveEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud** | **String** | The cloud type of this active event. | [optional] 
**description** | **String** | The details of active event. | [optional] 
**impacts** | [**[EmergingIssueImpact]**](EmergingIssueImpact.md) | The list of emerging issues impacts. | [optional] 
**lastModifiedTime** | **Date** | The last time modified on this banner. | [optional] 
**published** | **Boolean** | The boolean value of this active event if published or not. | [optional] 
**severity** | **String** | The severity level of this active event. | [optional] 
**stage** | **String** | The stage of this active event. | [optional] 
**startTime** | **Date** | The impact start time on this active event. | [optional] 
**title** | **String** | The active event title. | [optional] 
**trackingId** | **String** | The tracking id of this active event. | [optional] 



## Enum: SeverityEnum


* `Information` (value: `"Information"`)

* `Warning` (value: `"Warning"`)

* `Error` (value: `"Error"`)





## Enum: StageEnum


* `Active` (value: `"Active"`)

* `Resolve` (value: `"Resolve"`)

* `Archived` (value: `"Archived"`)




