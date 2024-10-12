# ThePlaidApi.APR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aprPercentage** | **Number** | Annual Percentage Rate applied.  | 
**aprType** | **String** | The type of balance to which the APR applies. | 
**balanceSubjectToApr** | **Number** | Amount of money that is subjected to the APR if a balance was carried beyond payment due date. How it is calculated can vary by card issuer. It is often calculated as an average daily balance. | 
**interestChargeAmount** | **Number** | Amount of money charged due to interest from last statement. | 



## Enum: AprTypeEnum


* `balance_transfer_apr` (value: `"balance_transfer_apr"`)

* `cash_apr` (value: `"cash_apr"`)

* `purchase_apr` (value: `"purchase_apr"`)

* `special` (value: `"special"`)




