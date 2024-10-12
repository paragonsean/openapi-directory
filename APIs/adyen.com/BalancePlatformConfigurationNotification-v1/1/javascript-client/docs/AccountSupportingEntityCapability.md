# ConfigurationWebhooks.AccountSupportingEntityCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **Boolean** | Indicates whether the supporting entity capability is allowed. Adyen sets this to **true** if the verification is successful and the account holder is permitted to use the capability. | [optional] 
**allowedLevel** | **String** | The capability level that is allowed for the account holder.  Possible values: **notApplicable**, **low**, **medium**, **high**. | [optional] 
**enabled** | **Boolean** | Indicates whether the capability is enabled. If **false**, the capability is temporarily disabled for the account holder. | [optional] 
**id** | **String** | The ID of the supporting entity. | [optional] 
**requested** | **Boolean** | Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to the &#x60;allowed&#x60; field. | [optional] 
**requestedLevel** | **String** | The requested level of the capability. Some capabilities, such as those used in [card issuing](https://docs.adyen.com/issuing/add-capabilities#capability-levels), have different levels. Levels increase the capability, but also require additional checks and increased monitoring.  Possible values: **notApplicable**, **low**, **medium**, **high**. | [optional] 
**verificationStatus** | **String** | The status of the verification checks for the supporting entity capability.  Possible values:  * **pending**: Adyen is running the verification.  * **invalid**: The verification failed. Check if the &#x60;errors&#x60; array contains more information.  * **valid**: The verification has been successfully completed.  * **rejected**: Adyen has verified the information, but found reasons to not allow the capability.  | [optional] 



## Enum: AllowedLevelEnum


* `high` (value: `"high"`)

* `low` (value: `"low"`)

* `medium` (value: `"medium"`)

* `notApplicable` (value: `"notApplicable"`)





## Enum: RequestedLevelEnum


* `high` (value: `"high"`)

* `low` (value: `"low"`)

* `medium` (value: `"medium"`)

* `notApplicable` (value: `"notApplicable"`)





## Enum: VerificationStatusEnum


* `invalid` (value: `"invalid"`)

* `pending` (value: `"pending"`)

* `rejected` (value: `"rejected"`)

* `valid` (value: `"valid"`)




