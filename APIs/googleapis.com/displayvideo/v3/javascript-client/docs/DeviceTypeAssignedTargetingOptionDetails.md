# DisplayVideo360Api.DeviceTypeAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceType** | **String** | Required. The display name of the device type. | [optional] 
**youtubeAndPartnersBidMultiplier** | **Number** | Output only. Bid multiplier allows you to show your ads more or less frequently based on the device type. It will apply a multiplier on the original bid price. When this field is 0, it indicates this field is not applicable instead of multiplying 0 on the original bid price. For example, if the bid price without multiplier is $10.0 and the multiplier is 1.5 for Tablet, the resulting bid price for Tablet will be $15.0. Only applicable to YouTube and Partners line items. | [optional] [readonly] 



## Enum: DeviceTypeEnum


* `UNSPECIFIED` (value: `"DEVICE_TYPE_UNSPECIFIED"`)

* `COMPUTER` (value: `"DEVICE_TYPE_COMPUTER"`)

* `CONNECTED_TV` (value: `"DEVICE_TYPE_CONNECTED_TV"`)

* `SMART_PHONE` (value: `"DEVICE_TYPE_SMART_PHONE"`)

* `TABLET` (value: `"DEVICE_TYPE_TABLET"`)




