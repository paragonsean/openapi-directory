

# DeviceRolloverDetails

The additional device details for the service data encryption key rollover.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationEligibility** | [**AuthorizationEligibilityEnum**](#AuthorizationEligibilityEnum) | The eligibility status of device for service data encryption key rollover. |  [optional] |
|**authorizationStatus** | [**AuthorizationStatusEnum**](#AuthorizationStatusEnum) | The authorization status of the device for service data encryption key rollover. |  [optional] |
|**inEligibilityReason** | [**InEligibilityReasonEnum**](#InEligibilityReasonEnum) | The reason for inEligibility of device, in case it&#39;s not eligible for service data encryption key rollover. |  [optional] |



## Enum: AuthorizationEligibilityEnum

| Name | Value |
|---- | -----|
| IN_ELIGIBLE | &quot;InEligible&quot; |
| ELIGIBLE | &quot;Eligible&quot; |



## Enum: AuthorizationStatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



## Enum: InEligibilityReasonEnum

| Name | Value |
|---- | -----|
| DEVICE_NOT_ONLINE | &quot;DeviceNotOnline&quot; |
| NOT_SUPPORTED_APPLIANCE | &quot;NotSupportedAppliance&quot; |
| ROLLOVER_PENDING | &quot;RolloverPending&quot; |



