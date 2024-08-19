# AzureMigrate.ProjectProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTimestamp** | **Date** | Time when this project was created. Date-Time represented in ISO-8601 format. | [optional] [readonly] 
**customerWorkspaceId** | **String** | ARM ID of the Service Map workspace created by user. | [optional] 
**discoveryStatus** | **String** | Reports whether project is under discovery. | [optional] [readonly] 
**numberOfAssessments** | **Number** | Number of assessments created in the project. | [optional] [readonly] 
**numberOfGroups** | **Number** | Number of groups created in the project. | [optional] [readonly] 
**numberOfMachines** | **Number** | Number of machines in the project. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the project. | [optional] 
**updatedTimestamp** | **Date** | Time when this project was last updated. Date-Time represented in ISO-8601 format. | [optional] [readonly] 



## Enum: DiscoveryStatusEnum


* `Unknown` (value: `"Unknown"`)

* `NotStarted` (value: `"NotStarted"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)





## Enum: ProvisioningStateEnum


* `Accepted` (value: `"Accepted"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)

* `Moving` (value: `"Moving"`)

* `Succeeded` (value: `"Succeeded"`)




