# MerakiDashboardApi.CreateOrganizationAlertsProfileRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertCondition** | [**CreateOrganizationAlertsProfileRequestAlertCondition**](CreateOrganizationAlertsProfileRequestAlertCondition.md) |  | 
**description** | **String** | User supplied description of the alert | [optional] 
**networkTags** | **[String]** | Networks with these tags will be monitored for the alert | 
**recipients** | [**CreateOrganizationAlertsProfileRequestRecipients**](CreateOrganizationAlertsProfileRequestRecipients.md) |  | 
**type** | **String** | The alert type | 



## Enum: TypeEnum


* `appOutage` (value: `"appOutage"`)

* `voipJitter` (value: `"voipJitter"`)

* `voipMos` (value: `"voipMos"`)

* `voipPacketLoss` (value: `"voipPacketLoss"`)

* `wanLatency` (value: `"wanLatency"`)

* `wanPacketLoss` (value: `"wanPacketLoss"`)

* `wanStatus` (value: `"wanStatus"`)

* `wanUtilization` (value: `"wanUtilization"`)




