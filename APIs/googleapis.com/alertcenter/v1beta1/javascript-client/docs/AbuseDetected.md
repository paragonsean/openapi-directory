# GoogleWorkspaceAlertCenterApi.AbuseDetected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalDetails** | [**EntityList**](EntityList.md) |  | [optional] 
**product** | **String** | Product that the abuse is originating from. | [optional] 
**subAlertId** | **String** | Unique identifier of each sub alert that is onboarded. | [optional] 
**variationType** | **String** | Variation of AbuseDetected alerts. The variation_type determines the texts displayed the alert details. This differs from sub_alert_id because each sub alert can have multiple variation_types, representing different stages of the alert. | [optional] 



## Enum: VariationTypeEnum


* `ABUSE_DETECTED_VARIATION_TYPE_UNSPECIFIED` (value: `"ABUSE_DETECTED_VARIATION_TYPE_UNSPECIFIED"`)

* `DRIVE_ABUSIVE_CONTENT` (value: `"DRIVE_ABUSIVE_CONTENT"`)

* `LIMITED_DISABLE` (value: `"LIMITED_DISABLE"`)




