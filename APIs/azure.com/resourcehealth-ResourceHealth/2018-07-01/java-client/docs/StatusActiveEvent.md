

# StatusActiveEvent

Active event type of emerging issue.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloud** | **String** | The cloud type of this active event. |  [optional] |
|**description** | **String** | The details of active event. |  [optional] |
|**impacts** | [**List&lt;EmergingIssueImpact&gt;**](EmergingIssueImpact.md) | The list of emerging issues impacts. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | The last time modified on this banner. |  [optional] |
|**published** | **Boolean** | The boolean value of this active event if published or not. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity level of this active event. |  [optional] |
|**stage** | [**StageEnum**](#StageEnum) | The stage of this active event. |  [optional] |
|**startTime** | **OffsetDateTime** | The impact start time on this active event. |  [optional] |
|**title** | **String** | The active event title. |  [optional] |
|**trackingId** | **String** | The tracking id of this active event. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFORMATION | &quot;Information&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |



## Enum: StageEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| RESOLVE | &quot;Resolve&quot; |
| ARCHIVED | &quot;Archived&quot; |



