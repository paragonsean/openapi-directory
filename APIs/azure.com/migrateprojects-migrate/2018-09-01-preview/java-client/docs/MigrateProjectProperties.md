

# MigrateProjectProperties

Class for migrate project properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastSummaryRefreshedTime** | **OffsetDateTime** | Gets the last time the project summary was refreshed. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the migrate project. |  [optional] |
|**refreshSummaryState** | [**RefreshSummaryStateEnum**](#RefreshSummaryStateEnum) | Gets the refresh summary state. |  [optional] [readonly] |
|**registeredTools** | [**List&lt;RegisteredToolsEnum&gt;**](#List&lt;RegisteredToolsEnum&gt;) | Gets or sets the list of tools registered with the migrate project. |  [optional] |
|**summary** | [**Map&lt;String, ProjectSummary&gt;**](ProjectSummary.md) | Gets the summary of the migrate project. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |
| MOVING | &quot;Moving&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



## Enum: RefreshSummaryStateEnum

| Name | Value |
|---- | -----|
| STARTED | &quot;Started&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: List&lt;RegisteredToolsEnum&gt;

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



