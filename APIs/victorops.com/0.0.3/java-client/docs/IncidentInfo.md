

# IncidentInfo

Incidents contain the following fields (all should be considered optional)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ackTime** | **String** | The time of the last acknowledgment of the incident |  [optional] |
|**ackUser** | [**AckUser**](AckUser.md) |  |  [optional] |
|**ackUserId** | **String** | The VictorOps user id of the user that acknowledged the incident |  [optional] |
|**alertCount** | **BigDecimal** | The number of alerts received for this incident |  [optional] |
|**currentPhase** | **String** | The current phase of the incident \&quot;resolved\&quot;, \&quot;triggered\&quot; or \&quot;acknowledged\&quot;. |  [optional] |
|**endTime** | **String** | The time the incident ended |  [optional] |
|**entityDispName** | **String** | The display name of the entity causing the incident |  [optional] |
|**entityId** | **String** | The unique identification of the entity being monitored that caused the incident |  [optional] |
|**entityType** | **String** | The type of entity causing the incident (host/service) |  [optional] |
|**host** | **String** | The host on which the incident occurred |  [optional] |
|**incidentNumber** | **String** | The VictorOps incident number |  [optional] |
|**lastAlertID** | **String** | The unique id of the last alert for the incident |  [optional] |
|**lastAlertTime** | **String** | The time of the last alert received for the incident |  [optional] |
|**service** | **String** | The service name causing the incident (if any) |  [optional] |
|**startTime** | **String** | The time the incident started |  [optional] |
|**teams** | **String** | The teams that were paged for the incident (comma separated). |  [optional] |



