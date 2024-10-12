

# TransferFundsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The amount to be transferred. |  |
|**destinationAccountCode** | **String** | The code of the account to which the funds are to be credited. &gt;The state of the Account Holder of this account must be Active. |  |
|**merchantReference** | **String** | A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another. |  [optional] |
|**sourceAccountCode** | **String** | The code of the account from which the funds are to be debited. &gt;The state of the Account Holder of this account must be Active and allow payouts. |  |
|**transferCode** | **String** | The code related to the type of transfer being performed. &gt;The permitted codes differ for each platform account and are defined in their service level agreement. |  |



