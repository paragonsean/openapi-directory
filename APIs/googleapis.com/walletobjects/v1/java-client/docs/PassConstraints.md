

# PassConstraints

Container for any constraints that may be placed on passes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nfcConstraint** | [**List&lt;NfcConstraintEnum&gt;**](#List&lt;NfcConstraintEnum&gt;) | The NFC constraints for the pass. |  [optional] |
|**screenshotEligibility** | [**ScreenshotEligibilityEnum**](#ScreenshotEligibilityEnum) | The screenshot eligibility for the pass. |  [optional] |



## Enum: List&lt;NfcConstraintEnum&gt;

| Name | Value |
|---- | -----|
| NFC_CONSTRAINT_UNSPECIFIED | &quot;NFC_CONSTRAINT_UNSPECIFIED&quot; |
| BLOCK_PAYMENT | &quot;BLOCK_PAYMENT&quot; |
| BLOCK_CLOSED_LOOP_TRANSIT | &quot;BLOCK_CLOSED_LOOP_TRANSIT&quot; |



## Enum: ScreenshotEligibilityEnum

| Name | Value |
|---- | -----|
| SCREENSHOT_ELIGIBILITY_UNSPECIFIED | &quot;SCREENSHOT_ELIGIBILITY_UNSPECIFIED&quot; |
| ELIGIBLE | &quot;ELIGIBLE&quot; |
| INELIGIBLE | &quot;INELIGIBLE&quot; |



