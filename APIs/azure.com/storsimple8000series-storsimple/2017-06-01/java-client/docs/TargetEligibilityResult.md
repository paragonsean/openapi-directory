

# TargetEligibilityResult

The eligibility result of device, as a failover target device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eligibilityStatus** | [**EligibilityStatusEnum**](#EligibilityStatusEnum) | The eligibility status of device, as a failover target device. |  [optional] |
|**messages** | [**List&lt;TargetEligibilityErrorMessage&gt;**](TargetEligibilityErrorMessage.md) | The list of error messages, if a device does not qualify as a failover target device. |  [optional] |



## Enum: EligibilityStatusEnum

| Name | Value |
|---- | -----|
| NOT_ELIGIBLE | &quot;NotEligible&quot; |
| ELIGIBLE | &quot;Eligible&quot; |



