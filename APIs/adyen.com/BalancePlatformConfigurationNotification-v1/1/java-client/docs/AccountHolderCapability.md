

# AccountHolderCapability


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowed** | **Boolean** | Indicates whether the capability is allowed. Adyen sets this to **true** if the verification is successful and the account holder is permitted to use the capability. |  [optional] |
|**allowedLevel** | [**AllowedLevelEnum**](#AllowedLevelEnum) | The capability level that is allowed for the account holder.  Possible values: **notApplicable**, **low**, **medium**, **high**. |  [optional] |
|**allowedSettings** | [**CapabilitySettings**](CapabilitySettings.md) | A JSON object containing the settings that are allowed for the account holder. |  [optional] |
|**enabled** | **Boolean** | Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account holder. |  [optional] |
|**problems** | [**List&lt;CapabilityProblem&gt;**](CapabilityProblem.md) | Contains verification errors and the actions that you can take to resolve them. |  [optional] |
|**requested** | **Boolean** | Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to the &#x60;allowed&#x60; field. |  [optional] |
|**requestedLevel** | [**RequestedLevelEnum**](#RequestedLevelEnum) | The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increase the capability, but also require additional checks and increased monitoring.  Possible values: **notApplicable**, **low**, **medium**, **high**. |  [optional] |
|**requestedSettings** | [**CapabilitySettings**](CapabilitySettings.md) | A JSON object containing the settings that were requested for the account holder. |  [optional] |
|**transferInstruments** | [**List&lt;AccountSupportingEntityCapability&gt;**](AccountSupportingEntityCapability.md) | Contains the status of the transfer instruments associated with this capability.  |  [optional] |
|**verificationStatus** | [**VerificationStatusEnum**](#VerificationStatusEnum) | The status of the verification checks for the capability.  Possible values:  * **pending**: Adyen is running the verification.  * **invalid**: The verification failed. Check if the &#x60;errors&#x60; array contains more information.  * **valid**: The verification has been successfully completed.  * **rejected**: Adyen has verified the information, but found reasons to not allow the capability.  |  [optional] |



## Enum: AllowedLevelEnum

| Name | Value |
|---- | -----|
| HIGH | &quot;high&quot; |
| LOW | &quot;low&quot; |
| MEDIUM | &quot;medium&quot; |
| NOT_APPLICABLE | &quot;notApplicable&quot; |



## Enum: RequestedLevelEnum

| Name | Value |
|---- | -----|
| HIGH | &quot;high&quot; |
| LOW | &quot;low&quot; |
| MEDIUM | &quot;medium&quot; |
| NOT_APPLICABLE | &quot;notApplicable&quot; |



## Enum: VerificationStatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;invalid&quot; |
| PENDING | &quot;pending&quot; |
| REJECTED | &quot;rejected&quot; |
| VALID | &quot;valid&quot; |



