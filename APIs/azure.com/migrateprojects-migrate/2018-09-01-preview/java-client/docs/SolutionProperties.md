

# SolutionProperties

Class for solution properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cleanupState** | [**CleanupStateEnum**](#CleanupStateEnum) | Gets or sets the cleanup state of the solution. |  [optional] |
|**details** | [**SolutionDetails**](SolutionDetails.md) |  |  [optional] |
|**goal** | [**GoalEnum**](#GoalEnum) | Gets or sets the goal of the solution. |  [optional] |
|**purpose** | [**PurposeEnum**](#PurposeEnum) | Gets or sets the purpose of the solution. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Gets or sets the current status of the solution. |  [optional] |
|**summary** | [**SolutionSummary**](SolutionSummary.md) |  |  [optional] |
|**tool** | [**ToolEnum**](#ToolEnum) | Gets or sets the tool being used in the solution. |  [optional] |



## Enum: CleanupStateEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| STARTED | &quot;Started&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| SERVERS | &quot;Servers&quot; |
| DATABASES | &quot;Databases&quot; |



## Enum: PurposeEnum

| Name | Value |
|---- | -----|
| DISCOVERY | &quot;Discovery&quot; |
| ASSESSMENT | &quot;Assessment&quot; |
| MIGRATION | &quot;Migration&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INACTIVE | &quot;Inactive&quot; |
| ACTIVE | &quot;Active&quot; |



## Enum: ToolEnum

| Name | Value |
|---- | -----|
| SERVER_DISCOVERY | &quot;ServerDiscovery&quot; |
| SERVER_ASSESSMENT | &quot;ServerAssessment&quot; |
| SERVER_MIGRATION | &quot;ServerMigration&quot; |
| CLOUDAMIZE | &quot;Cloudamize&quot; |
| TURBONOMIC | &quot;Turbonomic&quot; |
| ZERTO | &quot;Zerto&quot; |
| CORENT_TECH | &quot;CorentTech&quot; |
| SERVER_ASSESSMENT_V1 | &quot;ServerAssessmentV1&quot; |
| SERVER_MIGRATION_REPLICATION | &quot;ServerMigration_Replication&quot; |
| CARBONITE | &quot;Carbonite&quot; |
| DATA_MIGRATION_ASSISTANT | &quot;DataMigrationAssistant&quot; |
| DATABASE_MIGRATION_SERVICE | &quot;DatabaseMigrationService&quot; |



