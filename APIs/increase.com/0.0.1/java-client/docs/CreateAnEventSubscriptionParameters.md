

# CreateAnEventSubscriptionParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**selectedEventCategory** | [**SelectedEventCategoryEnum**](#SelectedEventCategoryEnum) | If specified, this subscription will only receive webhooks for Events with the specified &#x60;category&#x60;. |  [optional] |
|**sharedSecret** | **String** | The key that will be used to sign webhooks. If no value is passed, a random string will be used as default. |  [optional] |
|**url** | **String** | The URL you&#39;d like us to send webhooks to. |  |



## Enum: SelectedEventCategoryEnum

| Name | Value |
|---- | -----|
| ACCOUNT_CREATED | &quot;account.created&quot; |
| ACCOUNT_UPDATED | &quot;account.updated&quot; |
| ACCOUNT_NUMBER_CREATED | &quot;account_number.created&quot; |
| ACCOUNT_NUMBER_UPDATED | &quot;account_number.updated&quot; |
| ACCOUNT_STATEMENT_CREATED | &quot;account_statement.created&quot; |
| ACCOUNT_TRANSFER_CREATED | &quot;account_transfer.created&quot; |
| ACCOUNT_TRANSFER_UPDATED | &quot;account_transfer.updated&quot; |
| ACH_PRENOTIFICATION_CREATED | &quot;ach_prenotification.created&quot; |
| ACH_PRENOTIFICATION_UPDATED | &quot;ach_prenotification.updated&quot; |
| ACH_TRANSFER_CREATED | &quot;ach_transfer.created&quot; |
| ACH_TRANSFER_UPDATED | &quot;ach_transfer.updated&quot; |
| CARD_CREATED | &quot;card.created&quot; |
| CARD_UPDATED | &quot;card.updated&quot; |
| CARD_PAYMENT_CREATED | &quot;card_payment.created&quot; |
| CARD_PAYMENT_UPDATED | &quot;card_payment.updated&quot; |
| CARD_DISPUTE_CREATED | &quot;card_dispute.created&quot; |
| CARD_DISPUTE_UPDATED | &quot;card_dispute.updated&quot; |
| CHECK_DEPOSIT_CREATED | &quot;check_deposit.created&quot; |
| CHECK_DEPOSIT_UPDATED | &quot;check_deposit.updated&quot; |
| CHECK_TRANSFER_CREATED | &quot;check_transfer.created&quot; |
| CHECK_TRANSFER_UPDATED | &quot;check_transfer.updated&quot; |
| DECLINED_TRANSACTION_CREATED | &quot;declined_transaction.created&quot; |
| DIGITAL_WALLET_TOKEN_CREATED | &quot;digital_wallet_token.created&quot; |
| DIGITAL_WALLET_TOKEN_UPDATED | &quot;digital_wallet_token.updated&quot; |
| DOCUMENT_CREATED | &quot;document.created&quot; |
| ENTITY_CREATED | &quot;entity.created&quot; |
| ENTITY_UPDATED | &quot;entity.updated&quot; |
| EXTERNAL_ACCOUNT_CREATED | &quot;external_account.created&quot; |
| FILE_CREATED | &quot;file.created&quot; |
| GROUP_UPDATED | &quot;group.updated&quot; |
| GROUP_HEARTBEAT | &quot;group.heartbeat&quot; |
| INBOUND_ACH_TRANSFER_RETURN_CREATED | &quot;inbound_ach_transfer_return.created&quot; |
| INBOUND_ACH_TRANSFER_RETURN_UPDATED | &quot;inbound_ach_transfer_return.updated&quot; |
| INBOUND_WIRE_DRAWDOWN_REQUEST_CREATED | &quot;inbound_wire_drawdown_request.created&quot; |
| OAUTH_CONNECTION_CREATED | &quot;oauth_connection.created&quot; |
| OAUTH_CONNECTION_DEACTIVATED | &quot;oauth_connection.deactivated&quot; |
| PENDING_TRANSACTION_CREATED | &quot;pending_transaction.created&quot; |
| PENDING_TRANSACTION_UPDATED | &quot;pending_transaction.updated&quot; |
| REAL_TIME_DECISION_CARD_AUTHORIZATION_REQUESTED | &quot;real_time_decision.card_authorization_requested&quot; |
| REAL_TIME_DECISION_DIGITAL_WALLET_TOKEN_REQUESTED | &quot;real_time_decision.digital_wallet_token_requested&quot; |
| REAL_TIME_DECISION_DIGITAL_WALLET_AUTHENTICATION_REQUESTED | &quot;real_time_decision.digital_wallet_authentication_requested&quot; |
| REAL_TIME_PAYMENTS_TRANSFER_CREATED | &quot;real_time_payments_transfer.created&quot; |
| REAL_TIME_PAYMENTS_TRANSFER_UPDATED | &quot;real_time_payments_transfer.updated&quot; |
| REAL_TIME_PAYMENTS_REQUEST_FOR_PAYMENT_CREATED | &quot;real_time_payments_request_for_payment.created&quot; |
| REAL_TIME_PAYMENTS_REQUEST_FOR_PAYMENT_UPDATED | &quot;real_time_payments_request_for_payment.updated&quot; |
| TRANSACTION_CREATED | &quot;transaction.created&quot; |
| WIRE_DRAWDOWN_REQUEST_CREATED | &quot;wire_drawdown_request.created&quot; |
| WIRE_DRAWDOWN_REQUEST_UPDATED | &quot;wire_drawdown_request.updated&quot; |
| WIRE_TRANSFER_CREATED | &quot;wire_transfer.created&quot; |
| WIRE_TRANSFER_UPDATED | &quot;wire_transfer.updated&quot; |



