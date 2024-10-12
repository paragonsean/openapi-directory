# GoogleWorkspaceAlertCenterApi.ActivityRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionNames** | **[String]** | List of action names associated with the rule threshold. | [optional] 
**createTime** | **String** | Rule create timestamp. | [optional] 
**description** | **String** | Description of the rule. | [optional] 
**displayName** | **String** | Alert display name. | [optional] 
**name** | **String** | Rule name. | [optional] 
**query** | **String** | Query that is used to get the data from the associated source. | [optional] 
**supersededAlerts** | **[String]** | List of alert IDs superseded by this alert. It is used to indicate that this alert is essentially extension of superseded alerts and we found the relationship after creating these alerts. | [optional] 
**supersedingAlert** | **String** | Alert ID superseding this alert. It is used to indicate that superseding alert is essentially extension of this alert and we found the relationship after creating both alerts. | [optional] 
**threshold** | **String** | Alert threshold is for example “COUNT &gt; 5”. | [optional] 
**triggerSource** | **String** | The trigger sources for this rule. * GMAIL_EVENTS * DEVICE_EVENTS * USER_EVENTS | [optional] 
**updateTime** | **String** | The timestamp of the last update to the rule. | [optional] 
**windowSize** | **String** | Rule window size. Possible values are 1 hour or 24 hours. | [optional] 


