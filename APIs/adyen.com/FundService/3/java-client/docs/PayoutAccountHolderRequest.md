

# PayoutAccountHolderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | The code of the account from which the payout is to be made. |  |
|**accountHolderCode** | **String** | The code of the Account Holder who owns the account from which the payout is to be made. The Account Holder is the party to which the payout will be made. |  |
|**amount** | [**Amount**](Amount.md) | An object containing the currency and value of the payout. If the account has multiple currencies, specify the currency to be used. If the &#x60;bankAccountUUID&#x60; is provided in the request, the currency supported by the bank is used. If the &#x60;payoutMethodCode&#x60; is provided in the request, the specified payout method is selected. |  [optional] |
|**bankAccountUUID** | **String** | The unique ID of the Bank Account held by the Account Holder to which the payout is to be made. If left blank, a bank account is automatically selected. |  [optional] |
|**description** | **String** | A description of the payout. Maximum 200 characters. Allowed: **abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/?:().,&#39;+ \&quot;;** |  [optional] |
|**merchantReference** | **String** | A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another. |  [optional] |



