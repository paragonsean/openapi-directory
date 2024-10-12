

# AlertProperties

describes security alert properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionTaken** | **String** | The action that was taken as a response to the alert (Active, Blocked etc.) |  [optional] [readonly] |
|**alertDisplayName** | **String** | Display name of the alert type |  [optional] [readonly] |
|**alertName** | **String** | Name of the alert type |  [optional] [readonly] |
|**associatedResource** | **String** | Azure resource ID of the associated resource |  [optional] [readonly] |
|**canBeInvestigated** | **Boolean** | Whether this alert can be investigated with Azure Security Center |  [optional] [readonly] |
|**compromisedEntity** | **String** | The entity that the incident happened on |  [optional] [readonly] |
|**confidenceReasons** | [**List&lt;AlertConfidenceReason&gt;**](AlertConfidenceReason.md) | reasons the alert got the confidenceScore value |  [optional] |
|**confidenceScore** | **Float** | level of confidence we have on the alert |  [optional] [readonly] |
|**correlationKey** | **String** | Alerts with the same CorrelationKey will be grouped together in Ibiza. |  [optional] [readonly] |
|**description** | **String** | Description of the incident and what it means |  [optional] [readonly] |
|**detectedTimeUtc** | **OffsetDateTime** | The time the incident was detected by the vendor |  [optional] [readonly] |
|**entities** | **List&lt;AlertEntity&gt;** | objects that are related to this alerts |  [optional] |
|**extendedProperties** | **Map&lt;String, Object&gt;** | Changing set of properties depending on the alert type. |  [optional] |
|**instanceId** | **String** | Instance ID of the alert. |  [optional] [readonly] |
|**isIncident** | **Boolean** | Whether this alert is for incident type or not (otherwise - single alert) |  [optional] [readonly] |
|**remediationSteps** | **String** | Recommended steps to reradiate the incident |  [optional] [readonly] |
|**reportedSeverity** | [**ReportedSeverityEnum**](#ReportedSeverityEnum) | Estimated severity of this alert |  [optional] [readonly] |
|**reportedTimeUtc** | **OffsetDateTime** | The time the incident was reported to Microsoft.Security in UTC |  [optional] [readonly] |
|**state** | **String** | State of the alert (Active, Dismissed etc.) |  [optional] [readonly] |
|**subscriptionId** | **String** | Azure subscription ID of the resource that had the security alert or the subscription ID of the workspace that this resource reports to |  [optional] [readonly] |
|**systemSource** | **String** | The type of the alerted resource (Azure, Non-Azure) |  [optional] [readonly] |
|**vendorName** | **String** | Name of the vendor that discovered the incident |  [optional] [readonly] |
|**workspaceArmId** | **String** | Azure resource ID of the workspace that the alert was reported to. |  [optional] [readonly] |



## Enum: ReportedSeverityEnum

| Name | Value |
|---- | -----|
| SILENT | &quot;Silent&quot; |
| INFORMATION | &quot;Information&quot; |
| LOW | &quot;Low&quot; |
| HIGH | &quot;High&quot; |



