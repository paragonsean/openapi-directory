

# AbuseDetected

A generic alert for abusive user activity occurring with a customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalDetails** | [**EntityList**](EntityList.md) |  |  [optional] |
|**product** | **String** | Product that the abuse is originating from. |  [optional] |
|**subAlertId** | **String** | Unique identifier of each sub alert that is onboarded. |  [optional] |
|**variationType** | [**VariationTypeEnum**](#VariationTypeEnum) | Variation of AbuseDetected alerts. The variation_type determines the texts displayed the alert details. This differs from sub_alert_id because each sub alert can have multiple variation_types, representing different stages of the alert. |  [optional] |



## Enum: VariationTypeEnum

| Name | Value |
|---- | -----|
| ABUSE_DETECTED_VARIATION_TYPE_UNSPECIFIED | &quot;ABUSE_DETECTED_VARIATION_TYPE_UNSPECIFIED&quot; |
| DRIVE_ABUSIVE_CONTENT | &quot;DRIVE_ABUSIVE_CONTENT&quot; |
| LIMITED_DISABLE | &quot;LIMITED_DISABLE&quot; |



