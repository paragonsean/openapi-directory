# AdHybridHealthService.Alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeAlertProperties** | [**[Item]**](Item.md) | The active alert properties. | [optional] 
**additionalInformation** | [**[AdditionalInformation]**](AdditionalInformation.md) | Additional information related to the alert. | [optional] 
**alertId** | **String** | The alert Id. | [optional] 
**createdDate** | **Date** | The date and time,in UTC,when the alert was created. | [optional] 
**description** | **String** | The alert description. | [optional] 
**displayName** | **String** | The display name for the alert. | [optional] 
**lastUpdated** | **Date** | The date and time, in UTC, when the alert was last updated. | [optional] 
**level** | **String** | The alert level which indicates the severity of the alert. | [optional] 
**monitorRoleType** | **String** | The monitoring role type for which the alert was raised. | [optional] 
**relatedLinks** | [**[HelpLink]**](HelpLink.md) | The help links to get more information related to the alert. | [optional] 
**remediation** | **String** | The alert remediation. | [optional] 
**resolvedAlertProperties** | [**[Item]**](Item.md) | The resolved alert properties. | [optional] 
**resolvedDate** | **Date** | The date and time, in UTC, when the alert was resolved. | [optional] 
**scope** | **String** | The scope of the alert. Indicates if it is a service or a server related alert. | [optional] 
**serviceId** | **String** | The service Id. | [optional] 
**serviceMemberId** | **String** | The server Id. | [optional] 
**shortName** | **String** | The alert short name. | [optional] 
**state** | **String** | The alert state which can be either active or resolved with multiple resolution types. | [optional] 
**tenantId** | **String** | The tenant Id. | [optional] 



## Enum: LevelEnum


* `Warning` (value: `"Warning"`)

* `Error` (value: `"Error"`)

* `PreWarning` (value: `"PreWarning"`)





## Enum: StateEnum


* `Active` (value: `"Active"`)

* `ResolvedByPositiveResult` (value: `"ResolvedByPositiveResult"`)

* `ResolvedManually` (value: `"ResolvedManually"`)

* `ResolvedByTimer` (value: `"ResolvedByTimer"`)

* `ResolvedByStateChange` (value: `"ResolvedByStateChange"`)




