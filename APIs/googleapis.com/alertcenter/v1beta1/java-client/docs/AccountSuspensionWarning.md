

# AccountSuspensionWarning

A warning that the customer's account is about to be suspended.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appealWindow** | **String** | The amount of time remaining to appeal an imminent suspension. After this window has elapsed, the account will be suspended. Only populated if the account suspension is in WARNING state. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Account suspension warning state. |  [optional] |
|**suspensionDetails** | [**List&lt;AccountSuspensionDetails&gt;**](AccountSuspensionDetails.md) | Details about why an account is being suspended. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACCOUNT_SUSPENSION_WARNING_STATE_UNSPECIFIED | &quot;ACCOUNT_SUSPENSION_WARNING_STATE_UNSPECIFIED&quot; |
| WARNING | &quot;WARNING&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| APPEAL_APPROVED | &quot;APPEAL_APPROVED&quot; |
| APPEAL_SUBMITTED | &quot;APPEAL_SUBMITTED&quot; |



