# MerakiDashboardApi.UpdateOrganizationAlertsProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertCondition** | [**CreateOrganizationAlertsProfileRequestAlertCondition**](CreateOrganizationAlertsProfileRequestAlertCondition.md) |  | [optional] 
**description** | **String** | User supplied description of the alert | [optional] 
**enabled** | **Boolean** | Is the alert config enabled | [optional] 
**networkTags** | **[String]** | Networks with these tags will be monitored for the alert | [optional] 
**recipients** | [**CreateOrganizationAlertsProfileRequestRecipients**](CreateOrganizationAlertsProfileRequestRecipients.md) |  | [optional] 
**type** | **String** | The alert type | [optional] 



## Enum: TypeEnum


* `appOutage` (value: `"appOutage"`)

* `voipJitter` (value: `"voipJitter"`)

* `voipMos` (value: `"voipMos"`)

* `voipPacketLoss` (value: `"voipPacketLoss"`)

* `wanLatency` (value: `"wanLatency"`)

* `wanPacketLoss` (value: `"wanPacketLoss"`)

* `wanStatus` (value: `"wanStatus"`)

* `wanUtilization` (value: `"wanUtilization"`)




