# RebillyRestApi.InvoiceAllOfRetryInstruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterAttemptPolicies** | **[String]** | The policy on the attempt finishes. | 
**afterRetryEndPolicies** | **[String]** | The policy on the retry ends. | 
**attempts** | [**[InvoiceAllOfRetryInstructionAttempts]**](InvoiceAllOfRetryInstructionAttempts.md) |  | 



## Enum: [AfterAttemptPoliciesEnum]


* `change-subscription-renewal-time` (value: `"change-subscription-renewal-time"`)





## Enum: [AfterRetryEndPoliciesEnum]


* `abandon-invoice` (value: `"abandon-invoice"`)

* `cancel-subscription` (value: `"cancel-subscription"`)




