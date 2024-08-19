# AzureMigrateV2.ProjectProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessmentSolutionId** | **String** | Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects. | [optional] 
**createdTimestamp** | **Date** | Time when this project was created. Date-Time represented in ISO-8601 format. | [optional] [readonly] 
**customerWorkspaceId** | **String** | The ARM id of service map workspace created by customer. | [optional] 
**customerWorkspaceLocation** | **String** | Location of service map workspace created by customer. | [optional] 
**lastAssessmentTimestamp** | **Date** | Time when last assessment was created. Date-Time represented in ISO-8601 format. This value will be null until assessment is created. | [optional] [readonly] 
**numberOfAssessments** | **Number** | Number of assessments created in the project. | [optional] [readonly] 
**numberOfGroups** | **Number** | Number of groups created in the project. | [optional] [readonly] 
**numberOfMachines** | **Number** | Number of machines in the project. | [optional] [readonly] 
**projectStatus** | **String** | Assessment project status. | [optional] 
**provisioningState** | **String** | Provisioning state of the project. | [optional] [readonly] 
**serviceEndpoint** | **String** | Endpoint at which the collector agent can call agent REST API. | [optional] [readonly] 
**updatedTimestamp** | **Date** | Time when this project was last updated. Date-Time represented in ISO-8601 format. | [optional] [readonly] 



## Enum: ProjectStatusEnum


* `Active` (value: `"Active"`)

* `Inactive` (value: `"Inactive"`)





## Enum: ProvisioningStateEnum


* `Accepted` (value: `"Accepted"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)

* `Moving` (value: `"Moving"`)

* `Succeeded` (value: `"Succeeded"`)




