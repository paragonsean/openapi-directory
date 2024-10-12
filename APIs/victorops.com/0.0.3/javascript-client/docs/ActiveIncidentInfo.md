# VictorOps.ActiveIncidentInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertCount** | **Number** | The number of alerts received for this incident | [optional] 
**currentPhase** | **String** | The current phase of the incident \&quot;resolved\&quot;, \&quot;triggered\&quot; or \&quot;acknowledged\&quot;. | [optional] 
**entityId** | **String** | The unique identification of the entity being monitored that caused the incident | [optional] 
**host** | **String** | The host on which the incident occurred | [optional] 
**incidentNumber** | **String** | The VictorOps incident number | [optional] 
**lastAlertId** | **String** | The unique id of the last alert for the incident | [optional] 
**lastAlertTime** | **String** | The time of the last alert received for the incident | [optional] 
**pagedPolicies** | [**[EscalationPolicyInfo]**](EscalationPolicyInfo.md) | The escalation policies that were triggered for the incident | [optional] 
**pagedTeams** | **[String]** | The teams that were paged for the incident | [optional] 
**pagedUsers** | **[String]** | The users that were paged for the incident. | [optional] 
**service** | **String** | The service name causing the incident (if any) | [optional] 
**startTime** | **String** | The time the incident started | [optional] 
**transitions** | [**[IncidentTransition]**](IncidentTransition.md) | Transitions of the incident state over time | [optional] 


