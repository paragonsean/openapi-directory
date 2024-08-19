

# PendingTransactionSource

This is an object giving more details on the network-level event that caused the Pending Transaction. For example, for a card transaction this lists the merchant's industry and location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountTransferInstruction** | [**AccountTransferInstruction**](AccountTransferInstruction.md) |  |  |
|**achTransferInstruction** | [**ACHTransferInstruction**](ACHTransferInstruction.md) |  |  |
|**cardAuthorization** | [**CardAuthorization**](CardAuthorization.md) |  |  |
|**cardRouteAuthorization** | [**DeprecatedCardAuthorization**](DeprecatedCardAuthorization.md) |  |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | The type of transaction that took place. We may add additional possible values for this enum over time; your application should be able to handle such additions gracefully. |  |
|**checkDepositInstruction** | [**CheckDepositInstruction**](CheckDepositInstruction.md) |  |  |
|**checkTransferInstruction** | [**CheckTransferInstruction**](CheckTransferInstruction.md) |  |  |
|**inboundFundsHold** | [**InboundFundsHold**](InboundFundsHold.md) |  |  |
|**realTimePaymentsTransferInstruction** | [**RealTimePaymentsTransferInstruction**](RealTimePaymentsTransferInstruction.md) |  |  |
|**wireDrawdownPaymentInstruction** | [**WireDrawdownPaymentInstruction**](WireDrawdownPaymentInstruction.md) |  |  |
|**wireTransferInstruction** | [**WireTransferInstruction**](WireTransferInstruction.md) |  |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| ACCOUNT_TRANSFER_INSTRUCTION | &quot;account_transfer_instruction&quot; |
| ACH_TRANSFER_INSTRUCTION | &quot;ach_transfer_instruction&quot; |
| CARD_AUTHORIZATION | &quot;card_authorization&quot; |
| CHECK_DEPOSIT_INSTRUCTION | &quot;check_deposit_instruction&quot; |
| CHECK_TRANSFER_INSTRUCTION | &quot;check_transfer_instruction&quot; |
| INBOUND_FUNDS_HOLD | &quot;inbound_funds_hold&quot; |
| CARD_ROUTE_AUTHORIZATION | &quot;card_route_authorization&quot; |
| REAL_TIME_PAYMENTS_TRANSFER_INSTRUCTION | &quot;real_time_payments_transfer_instruction&quot; |
| WIRE_DRAWDOWN_PAYMENT_INSTRUCTION | &quot;wire_drawdown_payment_instruction&quot; |
| WIRE_TRANSFER_INSTRUCTION | &quot;wire_transfer_instruction&quot; |
| OTHER | &quot;other&quot; |



