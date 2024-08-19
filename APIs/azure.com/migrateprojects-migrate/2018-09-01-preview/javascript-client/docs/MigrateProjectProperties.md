# AzureMigrateHub.MigrateProjectProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastSummaryRefreshedTime** | **Date** | Gets the last time the project summary was refreshed. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the migrate project. | [optional] 
**refreshSummaryState** | **String** | Gets the refresh summary state. | [optional] [readonly] 
**registeredTools** | **[String]** | Gets or sets the list of tools registered with the migrate project. | [optional] 
**summary** | [**{String: ProjectSummary}**](ProjectSummary.md) | Gets the summary of the migrate project. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Accepted` (value: `"Accepted"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)

* `Moving` (value: `"Moving"`)

* `Succeeded` (value: `"Succeeded"`)





## Enum: RefreshSummaryStateEnum


* `Started` (value: `"Started"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)





## Enum: [RegisteredToolsEnum]


* `ServerDiscovery` (value: `"ServerDiscovery"`)

* `ServerAssessment` (value: `"ServerAssessment"`)

* `ServerMigration` (value: `"ServerMigration"`)

* `Cloudamize` (value: `"Cloudamize"`)

* `Turbonomic` (value: `"Turbonomic"`)

* `Zerto` (value: `"Zerto"`)

* `CorentTech` (value: `"CorentTech"`)

* `ServerAssessmentV1` (value: `"ServerAssessmentV1"`)

* `ServerMigration_Replication` (value: `"ServerMigration_Replication"`)

* `Carbonite` (value: `"Carbonite"`)

* `DataMigrationAssistant` (value: `"DataMigrationAssistant"`)

* `DatabaseMigrationService` (value: `"DatabaseMigrationService"`)




