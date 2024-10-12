

# AccountHolderPayoutNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | The code of the account from which the payout was made. |  [optional] |
|**accountHolderCode** | **String** | The code of the Account Holder to which the payout was made. |  [optional] |
|**amounts** | [**List&lt;Amount&gt;**](Amount.md) | The payout amounts (per currency). |  [optional] |
|**bankAccountDetail** | [**BankAccountDetail**](BankAccountDetail.md) | Details of the Bank Account to which the payout was made. |  [optional] |
|**description** | **String** | A description of the payout. |  [optional] |
|**estimatedArrivalDate** | [**ModelLocalDate**](ModelLocalDate.md) | The estimated date of arrival. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | Invalid fields list. |  [optional] |
|**merchantReference** | **String** | The merchant reference. |  [optional] |
|**originalPspReference** | **String** | The PSP reference of the original payout. |  [optional] |
|**payoutAccountCountry** | **String** | The country code of the bank from which the payout was initiated. |  [optional] |
|**payoutAccountNumber** | **String** | The account number of the bank from which the payout was initiated. |  [optional] |
|**payoutBalanceAccountId** | **String** | The balance account id to which payment was made |  [optional] |
|**payoutBankName** | **String** | The name of the bank the payout from which the payout was initiated. |  [optional] |
|**payoutBranchCode** | **String** | The branch code of the bank from which the payout was initiated. |  [optional] |
|**payoutReference** | **Long** | The unique payout identifier. |  [optional] |
|**payoutSpeed** | [**PayoutSpeedEnum**](#PayoutSpeedEnum) | Speed with which payouts for this account are processed. Permitted values: &#x60;STANDARD&#x60;, &#x60;SAME_DAY&#x60;. |  [optional] |
|**status** | [**OperationStatus**](OperationStatus.md) | The payout status. |  [optional] |



## Enum: PayoutSpeedEnum

| Name | Value |
|---- | -----|
| INSTANT | &quot;INSTANT&quot; |
| SAME_DAY | &quot;SAME_DAY&quot; |
| STANDARD | &quot;STANDARD&quot; |



