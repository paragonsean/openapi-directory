# AzureMigrateHub.SolutionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleanupState** | **String** | Gets or sets the cleanup state of the solution. | [optional] 
**details** | [**SolutionDetails**](SolutionDetails.md) |  | [optional] 
**goal** | **String** | Gets or sets the goal of the solution. | [optional] 
**purpose** | **String** | Gets or sets the purpose of the solution. | [optional] 
**status** | **String** | Gets or sets the current status of the solution. | [optional] 
**summary** | [**SolutionSummary**](SolutionSummary.md) |  | [optional] 
**tool** | **String** | Gets or sets the tool being used in the solution. | [optional] 



## Enum: CleanupStateEnum


* `None` (value: `"None"`)

* `Started` (value: `"Started"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)





## Enum: GoalEnum


* `Servers` (value: `"Servers"`)

* `Databases` (value: `"Databases"`)





## Enum: PurposeEnum


* `Discovery` (value: `"Discovery"`)

* `Assessment` (value: `"Assessment"`)

* `Migration` (value: `"Migration"`)





## Enum: StatusEnum


* `Inactive` (value: `"Inactive"`)

* `Active` (value: `"Active"`)





## Enum: ToolEnum


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




