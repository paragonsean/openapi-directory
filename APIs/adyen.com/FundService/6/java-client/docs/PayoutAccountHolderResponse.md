

# PayoutAccountHolderResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccountUUID** | **String** | The unique ID of the Bank Account to which the payout was made. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | Contains field validation errors that would prevent requests from being processed. |  [optional] |
|**merchantReference** | **String** | The value supplied by the executing user when initiating the transfer; may be used to link multiple transactions. |  [optional] |
|**payoutSpeed** | [**PayoutSpeedEnum**](#PayoutSpeedEnum) | Speed with which payouts for this account are processed. Permitted values: &#x60;STANDARD&#x60;, &#x60;SAME_DAY&#x60;. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |



## Enum: PayoutSpeedEnum

| Name | Value |
|---- | -----|
| INSTANT | &quot;INSTANT&quot; |
| SAME_DAY | &quot;SAME_DAY&quot; |
| STANDARD | &quot;STANDARD&quot; |



