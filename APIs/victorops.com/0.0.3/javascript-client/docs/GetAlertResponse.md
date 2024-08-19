# VictorOps.GetAlertResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ackAuthor** | **String** | The user that acknowledged the incident. | [optional] 
**ackMsg** | **String** | A user entered comment for the acknowledgment. | [optional] 
**entityDisplayName** | **String** | Used within VictorOps to display a human-readable name for the entity. | [optional] 
**entityId** | **String** | Identifies the entity (host, service, etc.) this alert was about.  | [optional] 
**messageType** | **String** | The type of alert; INFO, WARNING, ACKNOWLEDGEMENT, CRITICAL, RECOVERY  | [optional] 
**monitoringTool** | **String** | The name of the monitoring system software (eg. nagios, icinga, sensu, etc.) | [optional] 
**raw** | **String** | The full, raw alert details JSON string (i.e. parse the string into a JSON object)  | [optional] 
**stateMessage** | **String** | Any additional status information from the alert item. | [optional] 
**stateStartTime** | **Number** | The time this entity entered its current state (seconds since epoch). | [optional] 
**timestamp** | **Number** | Timestamp of the alert in seconds since epoch. | [optional] 


