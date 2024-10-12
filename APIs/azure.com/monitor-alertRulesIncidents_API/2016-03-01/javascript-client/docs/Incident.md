# MonitorManagementClient.Incident

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activatedTime** | **Date** | The time at which the incident was activated in ISO8601 format. | [optional] [readonly] 
**isActive** | **Boolean** | A boolean to indicate whether the incident is active or resolved. | [optional] [readonly] 
**name** | **String** | Incident name. | [optional] [readonly] 
**resolvedTime** | **Date** | The time at which the incident was resolved in ISO8601 format. If null, it means the incident is still active. | [optional] [readonly] 
**ruleName** | **String** | Rule name that is associated with the incident. | [optional] [readonly] 


