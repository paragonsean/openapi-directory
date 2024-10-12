

# DeviceTypeAssignedTargetingOptionDetails

Targeting details for device type. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_DEVICE_TYPE`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceType** | [**DeviceTypeEnum**](#DeviceTypeEnum) | Required. The display name of the device type. |  [optional] |
|**youtubeAndPartnersBidMultiplier** | **Double** | Output only. Bid multiplier allows you to show your ads more or less frequently based on the device type. It will apply a multiplier on the original bid price. When this field is 0, it indicates this field is not applicable instead of multiplying 0 on the original bid price. For example, if the bid price without multiplier is $10.0 and the multiplier is 1.5 for Tablet, the resulting bid price for Tablet will be $15.0. Only applicable to YouTube and Partners line items. |  [optional] [readonly] |



## Enum: DeviceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DEVICE_TYPE_UNSPECIFIED&quot; |
| COMPUTER | &quot;DEVICE_TYPE_COMPUTER&quot; |
| CONNECTED_TV | &quot;DEVICE_TYPE_CONNECTED_TV&quot; |
| SMART_PHONE | &quot;DEVICE_TYPE_SMART_PHONE&quot; |
| TABLET | &quot;DEVICE_TYPE_TABLET&quot; |



