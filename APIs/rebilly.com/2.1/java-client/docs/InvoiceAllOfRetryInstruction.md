

# InvoiceAllOfRetryInstruction

The invoice retry instruction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afterAttemptPolicies** | [**List&lt;AfterAttemptPoliciesEnum&gt;**](#List&lt;AfterAttemptPoliciesEnum&gt;) | The policy on the attempt finishes. |  |
|**afterRetryEndPolicies** | [**List&lt;AfterRetryEndPoliciesEnum&gt;**](#List&lt;AfterRetryEndPoliciesEnum&gt;) | The policy on the retry ends. |  |
|**attempts** | [**List&lt;InvoiceAllOfRetryInstructionAttempts&gt;**](InvoiceAllOfRetryInstructionAttempts.md) |  |  |



## Enum: List&lt;AfterAttemptPoliciesEnum&gt;

| Name | Value |
|---- | -----|
| CHANGE_SUBSCRIPTION_RENEWAL_TIME | &quot;change-subscription-renewal-time&quot; |



## Enum: List&lt;AfterRetryEndPoliciesEnum&gt;

| Name | Value |
|---- | -----|
| ABANDON_INVOICE | &quot;abandon-invoice&quot; |
| CANCEL_SUBSCRIPTION | &quot;cancel-subscription&quot; |



