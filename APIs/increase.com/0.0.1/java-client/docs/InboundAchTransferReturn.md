

# InboundAchTransferReturn

If unauthorized activity occurs via ACH, you can create an Inbound ACH Transfer Return and we'll reverse the transaction. You can create an Inbound ACH Transfer return the first two days after receiving an Inbound ACH Transfer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The ID of the Inbound ACH Transfer Return. |  |
|**inboundAchTransferTransactionId** | **String** | The ID for the Transaction that is being returned. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason why this transfer will be returned. This is sent to the initiating bank. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The lifecycle status of the transfer. |  |
|**submission** | [**InboundACHTransferReturnSubmission**](InboundACHTransferReturnSubmission.md) |  |  |
|**transactionId** | **String** | The ID for the transaction refunding the transfer. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;inbound_ach_transfer_return&#x60;. |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION_REVOKED_BY_CUSTOMER | &quot;authorization_revoked_by_customer&quot; |
| PAYMENT_STOPPED | &quot;payment_stopped&quot; |
| CUSTOMER_ADVISED_UNAUTHORIZED_IMPROPER_INELIGIBLE_OR_INCOMPLETE | &quot;customer_advised_unauthorized_improper_ineligible_or_incomplete&quot; |
| REPRESENTATIVE_PAYEE_DECEASED_OR_UNABLE_TO_CONTINUE_IN_THAT_CAPACITY | &quot;representative_payee_deceased_or_unable_to_continue_in_that_capacity&quot; |
| BENEFICIARY_OR_ACCOUNT_HOLDER_DECEASED | &quot;beneficiary_or_account_holder_deceased&quot; |
| CREDIT_ENTRY_REFUSED_BY_RECEIVER | &quot;credit_entry_refused_by_receiver&quot; |
| DUPLICATE_ENTRY | &quot;duplicate_entry&quot; |
| CORPORATE_CUSTOMER_ADVISED_NOT_AUTHORIZED | &quot;corporate_customer_advised_not_authorized&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_SUBMITTING | &quot;pending_submitting&quot; |
| SUBMITTED | &quot;submitted&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INBOUND_ACH_TRANSFER_RETURN | &quot;inbound_ach_transfer_return&quot; |



