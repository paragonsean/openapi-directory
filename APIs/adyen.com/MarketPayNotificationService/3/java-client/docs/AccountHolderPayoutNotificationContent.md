

# AccountHolderPayoutNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | The code of the account from which the payout was made. |  [optional] |
|**accountHolderCode** | **String** | The code of the Account Holder to which the payout was made. |  [optional] |
|**amount** | [**Amount**](Amount.md) | The payout amount. |  [optional] |
|**amounts** | [**List&lt;AmountWrapper&gt;**](AmountWrapper.md) | The payout amounts (per currency). |  [optional] |
|**bankAccountDetail** | [**BankAccountDetail**](BankAccountDetail.md) | Details of the Bank Account to which the payout was made. |  [optional] |
|**description** | **String** | A description of the payout. |  [optional] |
|**merchantReference** | **String** | The merchant reference. |  [optional] |
|**status** | [**OperationStatus**](OperationStatus.md) | The payout status. |  [optional] |



