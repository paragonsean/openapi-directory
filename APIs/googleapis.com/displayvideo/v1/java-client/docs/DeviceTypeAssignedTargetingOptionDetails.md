

# DeviceTypeAssignedTargetingOptionDetails

Targeting details for device type. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_DEVICE_TYPE`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceType** | [**DeviceTypeEnum**](#DeviceTypeEnum) | Required. The display name of the device type. |  [optional] |
|**targetingOptionId** | **String** | Required. ID of the device type. |  [optional] |



## Enum: DeviceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DEVICE_TYPE_UNSPECIFIED&quot; |
| COMPUTER | &quot;DEVICE_TYPE_COMPUTER&quot; |
| CONNECTED_TV | &quot;DEVICE_TYPE_CONNECTED_TV&quot; |
| SMART_PHONE | &quot;DEVICE_TYPE_SMART_PHONE&quot; |
| TABLET | &quot;DEVICE_TYPE_TABLET&quot; |



