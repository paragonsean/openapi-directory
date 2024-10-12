# IncreaseApi.PendingTransactionSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountTransferInstruction** | [**AccountTransferInstruction**](AccountTransferInstruction.md) |  | 
**achTransferInstruction** | [**ACHTransferInstruction**](ACHTransferInstruction.md) |  | 
**cardAuthorization** | [**CardAuthorization**](CardAuthorization.md) |  | 
**cardRouteAuthorization** | [**DeprecatedCardAuthorization**](DeprecatedCardAuthorization.md) |  | 
**category** | **String** | The type of transaction that took place. We may add additional possible values for this enum over time; your application should be able to handle such additions gracefully. | 
**checkDepositInstruction** | [**CheckDepositInstruction**](CheckDepositInstruction.md) |  | 
**checkTransferInstruction** | [**CheckTransferInstruction**](CheckTransferInstruction.md) |  | 
**inboundFundsHold** | [**InboundFundsHold**](InboundFundsHold.md) |  | 
**realTimePaymentsTransferInstruction** | [**RealTimePaymentsTransferInstruction**](RealTimePaymentsTransferInstruction.md) |  | 
**wireDrawdownPaymentInstruction** | [**WireDrawdownPaymentInstruction**](WireDrawdownPaymentInstruction.md) |  | 
**wireTransferInstruction** | [**WireTransferInstruction**](WireTransferInstruction.md) |  | 



## Enum: CategoryEnum


* `account_transfer_instruction` (value: `"account_transfer_instruction"`)

* `ach_transfer_instruction` (value: `"ach_transfer_instruction"`)

* `card_authorization` (value: `"card_authorization"`)

* `check_deposit_instruction` (value: `"check_deposit_instruction"`)

* `check_transfer_instruction` (value: `"check_transfer_instruction"`)

* `inbound_funds_hold` (value: `"inbound_funds_hold"`)

* `card_route_authorization` (value: `"card_route_authorization"`)

* `real_time_payments_transfer_instruction` (value: `"real_time_payments_transfer_instruction"`)

* `wire_drawdown_payment_instruction` (value: `"wire_drawdown_payment_instruction"`)

* `wire_transfer_instruction` (value: `"wire_transfer_instruction"`)

* `other` (value: `"other"`)




