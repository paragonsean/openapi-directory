

# DebitAccountHolderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder. |  |
|**amount** | [**Amount**](Amount.md) | The amount to be debited from the account holder&#39;s bank account. |  |
|**bankAccountUUID** | **String** | The Adyen-generated unique alphanumeric identifier (UUID) of the account holder&#39;s bank account. |  |
|**description** | **String** | A description of the direct debit. Maximum length: 35 characters.  Allowed characters: **a-z**, **A-Z**, **0-9**, and special characters **_/?:().,&#39;+ \&quot;;**. |  [optional] |
|**merchantAccount** | **String** | Your merchant account. |  |
|**splits** | [**List&lt;Split&gt;**](Split.md) | Contains instructions on how to split the funds between the accounts in your platform. The request must have at least one split item. |  |



