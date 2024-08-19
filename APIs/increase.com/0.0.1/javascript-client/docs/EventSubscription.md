# IncreaseApi.EventSubscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The time the event subscription was created. | 
**id** | **String** | The event subscription identifier. | 
**selectedEventCategory** | **String** | If specified, this subscription will only receive webhooks for Events with the specified &#x60;category&#x60;. | 
**sharedSecret** | **String** | The key that will be used to sign webhooks. | 
**status** | **String** | This indicates if we&#39;ll send notifications to this subscription. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;event_subscription&#x60;. | 
**url** | **String** | The webhook url where we&#39;ll send notifications. | 



## Enum: SelectedEventCategoryEnum


* `account.created` (value: `"account.created"`)

* `account.updated` (value: `"account.updated"`)

* `account_number.created` (value: `"account_number.created"`)

* `account_number.updated` (value: `"account_number.updated"`)

* `account_statement.created` (value: `"account_statement.created"`)

* `account_transfer.created` (value: `"account_transfer.created"`)

* `account_transfer.updated` (value: `"account_transfer.updated"`)

* `ach_prenotification.created` (value: `"ach_prenotification.created"`)

* `ach_prenotification.updated` (value: `"ach_prenotification.updated"`)

* `ach_transfer.created` (value: `"ach_transfer.created"`)

* `ach_transfer.updated` (value: `"ach_transfer.updated"`)

* `card.created` (value: `"card.created"`)

* `card.updated` (value: `"card.updated"`)

* `card_payment.created` (value: `"card_payment.created"`)

* `card_payment.updated` (value: `"card_payment.updated"`)

* `card_dispute.created` (value: `"card_dispute.created"`)

* `card_dispute.updated` (value: `"card_dispute.updated"`)

* `check_deposit.created` (value: `"check_deposit.created"`)

* `check_deposit.updated` (value: `"check_deposit.updated"`)

* `check_transfer.created` (value: `"check_transfer.created"`)

* `check_transfer.updated` (value: `"check_transfer.updated"`)

* `declined_transaction.created` (value: `"declined_transaction.created"`)

* `digital_wallet_token.created` (value: `"digital_wallet_token.created"`)

* `digital_wallet_token.updated` (value: `"digital_wallet_token.updated"`)

* `document.created` (value: `"document.created"`)

* `entity.created` (value: `"entity.created"`)

* `entity.updated` (value: `"entity.updated"`)

* `external_account.created` (value: `"external_account.created"`)

* `file.created` (value: `"file.created"`)

* `group.updated` (value: `"group.updated"`)

* `group.heartbeat` (value: `"group.heartbeat"`)

* `inbound_ach_transfer_return.created` (value: `"inbound_ach_transfer_return.created"`)

* `inbound_ach_transfer_return.updated` (value: `"inbound_ach_transfer_return.updated"`)

* `inbound_wire_drawdown_request.created` (value: `"inbound_wire_drawdown_request.created"`)

* `oauth_connection.created` (value: `"oauth_connection.created"`)

* `oauth_connection.deactivated` (value: `"oauth_connection.deactivated"`)

* `pending_transaction.created` (value: `"pending_transaction.created"`)

* `pending_transaction.updated` (value: `"pending_transaction.updated"`)

* `real_time_decision.card_authorization_requested` (value: `"real_time_decision.card_authorization_requested"`)

* `real_time_decision.digital_wallet_token_requested` (value: `"real_time_decision.digital_wallet_token_requested"`)

* `real_time_decision.digital_wallet_authentication_requested` (value: `"real_time_decision.digital_wallet_authentication_requested"`)

* `real_time_payments_transfer.created` (value: `"real_time_payments_transfer.created"`)

* `real_time_payments_transfer.updated` (value: `"real_time_payments_transfer.updated"`)

* `real_time_payments_request_for_payment.created` (value: `"real_time_payments_request_for_payment.created"`)

* `real_time_payments_request_for_payment.updated` (value: `"real_time_payments_request_for_payment.updated"`)

* `transaction.created` (value: `"transaction.created"`)

* `wire_drawdown_request.created` (value: `"wire_drawdown_request.created"`)

* `wire_drawdown_request.updated` (value: `"wire_drawdown_request.updated"`)

* `wire_transfer.created` (value: `"wire_transfer.created"`)

* `wire_transfer.updated` (value: `"wire_transfer.updated"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `disabled` (value: `"disabled"`)

* `deleted` (value: `"deleted"`)

* `requires_attention` (value: `"requires_attention"`)





## Enum: TypeEnum


* `event_subscription` (value: `"event_subscription"`)




