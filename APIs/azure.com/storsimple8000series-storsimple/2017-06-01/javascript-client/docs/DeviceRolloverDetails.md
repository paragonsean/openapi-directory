# StorSimple8000SeriesManagementClient.DeviceRolloverDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationEligibility** | **String** | The eligibility status of device for service data encryption key rollover. | [optional] 
**authorizationStatus** | **String** | The authorization status of the device for service data encryption key rollover. | [optional] 
**inEligibilityReason** | **String** | The reason for inEligibility of device, in case it&#39;s not eligible for service data encryption key rollover. | [optional] 



## Enum: AuthorizationEligibilityEnum


* `InEligible` (value: `"InEligible"`)

* `Eligible` (value: `"Eligible"`)





## Enum: AuthorizationStatusEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)





## Enum: InEligibilityReasonEnum


* `DeviceNotOnline` (value: `"DeviceNotOnline"`)

* `NotSupportedAppliance` (value: `"NotSupportedAppliance"`)

* `RolloverPending` (value: `"RolloverPending"`)




