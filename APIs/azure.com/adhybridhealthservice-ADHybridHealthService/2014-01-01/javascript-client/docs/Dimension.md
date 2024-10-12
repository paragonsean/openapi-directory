# AdHybridHealthService.Dimension

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeAlerts** | **Number** | The count of alerts that are currently active for the service. | [optional] 
**additionalInformation** | **String** | The additional information related to the service. | [optional] 
**displayName** | **String** | The display name of the service. | [optional] 
**health** | **String** | The health status for the domain controller. | [optional] 
**lastUpdated** | **Date** | The date or time , in UTC, when the service properties were last updated. | [optional] 
**resolvedAlerts** | **Number** | The total count of alerts that has been resolved for the service. | [optional] 
**signature** | **String** | The signature of the service. | [optional] 
**simpleProperties** | **Object** | List of service specific configuration properties. | [optional] 
**type** | **String** | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] 



## Enum: HealthEnum


* `Healthy` (value: `"Healthy"`)

* `Warning` (value: `"Warning"`)

* `Error` (value: `"Error"`)

* `NotMonitored` (value: `"NotMonitored"`)

* `Missing` (value: `"Missing"`)




