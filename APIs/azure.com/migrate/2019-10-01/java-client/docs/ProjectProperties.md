

# ProjectProperties

Properties of a project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assessmentSolutionId** | **String** | Assessment solution ARM id tracked by Microsoft.Migrate/migrateProjects. |  [optional] |
|**createdTimestamp** | **OffsetDateTime** | Time when this project was created. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**customerWorkspaceId** | **String** | The ARM id of service map workspace created by customer. |  [optional] |
|**customerWorkspaceLocation** | **String** | Location of service map workspace created by customer. |  [optional] |
|**lastAssessmentTimestamp** | **OffsetDateTime** | Time when last assessment was created. Date-Time represented in ISO-8601 format. This value will be null until assessment is created. |  [optional] [readonly] |
|**numberOfAssessments** | **Integer** | Number of assessments created in the project. |  [optional] [readonly] |
|**numberOfGroups** | **Integer** | Number of groups created in the project. |  [optional] [readonly] |
|**numberOfMachines** | **Integer** | Number of machines in the project. |  [optional] [readonly] |
|**projectStatus** | [**ProjectStatusEnum**](#ProjectStatusEnum) | Assessment project status. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the project. |  [optional] [readonly] |
|**serviceEndpoint** | **String** | Endpoint at which the collector agent can call agent REST API. |  [optional] [readonly] |
|**updatedTimestamp** | **OffsetDateTime** | Time when this project was last updated. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |



## Enum: ProjectStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| INACTIVE | &quot;Inactive&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |
| MOVING | &quot;Moving&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



