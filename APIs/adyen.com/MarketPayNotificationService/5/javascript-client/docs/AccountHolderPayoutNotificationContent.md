# ClassicPlatformsNotifications.AccountHolderPayoutNotificationContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | The code of the account from which the payout was made. | [optional] 
**accountHolderCode** | **String** | The code of the Account Holder to which the payout was made. | [optional] 
**amount** | [**Amount**](Amount.md) | The payout amount. | [optional] 
**amounts** | [**[Amount]**](Amount.md) | The payout amounts (per currency). | [optional] 
**bankAccountDetail** | [**BankAccountDetail**](BankAccountDetail.md) | Details of the Bank Account to which the payout was made. | [optional] 
**description** | **String** | A description of the payout. | [optional] 
**estimatedArrivalDate** | [**LocalDate**](LocalDate.md) | The estimated date of arrival. | [optional] 
**invalidFields** | [**[ErrorFieldType]**](ErrorFieldType.md) | Invalid fields list. | [optional] 
**merchantReference** | **String** | The merchant reference. | [optional] 
**originalPspReference** | **String** | The PSP reference of the original payout. | [optional] 
**payoutSpeed** | **String** | Speed with which payouts for this account are processed. Permitted values: &#x60;STANDARD&#x60;, &#x60;SAME_DAY&#x60;. | [optional] 
**status** | [**OperationStatus**](OperationStatus.md) | The payout status. | [optional] 



## Enum: PayoutSpeedEnum


* `INSTANT` (value: `"INSTANT"`)

* `SAME_DAY` (value: `"SAME_DAY"`)

* `STANDARD` (value: `"STANDARD"`)




