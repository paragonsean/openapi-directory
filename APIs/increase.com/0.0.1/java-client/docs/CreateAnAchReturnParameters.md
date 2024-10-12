

# CreateAnAchReturnParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason why this transfer will be returned. The most usual return codes are &#x60;payment_stopped&#x60; for debits and &#x60;credit_entry_refused_by_receiver&#x60; for credits. |  |
|**transactionId** | **String** | The transaction identifier of the Inbound ACH Transfer to return to the originating financial institution. |  |



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



