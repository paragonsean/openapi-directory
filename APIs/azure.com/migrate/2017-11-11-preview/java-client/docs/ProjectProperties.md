

# ProjectProperties

Properties of a project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTimestamp** | **OffsetDateTime** | Time when this project was created. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**customerWorkspaceId** | **String** | ARM ID of the Service Map workspace created by user. |  [optional] |
|**discoveryStatus** | [**DiscoveryStatusEnum**](#DiscoveryStatusEnum) | Reports whether project is under discovery. |  [optional] [readonly] |
|**numberOfAssessments** | **Integer** | Number of assessments created in the project. |  [optional] [readonly] |
|**numberOfGroups** | **Integer** | Number of groups created in the project. |  [optional] [readonly] |
|**numberOfMachines** | **Integer** | Number of machines in the project. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the project. |  [optional] |
|**updatedTimestamp** | **OffsetDateTime** | Time when this project was last updated. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |



## Enum: DiscoveryStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NOT_STARTED | &quot;NotStarted&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |
| MOVING | &quot;Moving&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



