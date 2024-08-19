

# TransactionSource

This is an object giving more details on the network-level event that caused the Transaction. Note that for backwards compatibility reasons, additional undocumented keys may appear in this object. These should be treated as deprecated and will be removed in the future.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountTransferIntention** | [**AccountTransferIntention**](AccountTransferIntention.md) |  |  |
|**achCheckConversion** | [**ACHCheckConversion**](ACHCheckConversion.md) |  |  |
|**achCheckConversionReturn** | [**ACHCheckConversionReturn**](ACHCheckConversionReturn.md) |  |  |
|**achTransferIntention** | [**ACHTransferIntention**](ACHTransferIntention.md) |  |  |
|**achTransferRejection** | [**ACHTransferRejection**](ACHTransferRejection.md) |  |  |
|**achTransferReturn** | [**ACHTransferReturn1**](ACHTransferReturn1.md) |  |  |
|**cardDisputeAcceptance** | [**CardDisputeAcceptance1**](CardDisputeAcceptance1.md) |  |  |
|**cardRefund** | [**CardRefund**](CardRefund.md) |  |  |
|**cardRevenuePayment** | [**CardRevenuePayment**](CardRevenuePayment.md) |  |  |
|**cardRouteRefund** | [**DeprecatedCardRefund**](DeprecatedCardRefund.md) |  |  |
|**cardRouteSettlement** | [**DeprecatedCardSettlement**](DeprecatedCardSettlement.md) |  |  |
|**cardSettlement** | [**CardSettlement**](CardSettlement.md) |  |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | The type of transaction that took place. We may add additional possible values for this enum over time; your application should be able to handle such additions gracefully. |  |
|**checkDepositAcceptance** | [**CheckDepositAcceptance1**](CheckDepositAcceptance1.md) |  |  |
|**checkDepositReturn** | [**CheckDepositReturn1**](CheckDepositReturn1.md) |  |  |
|**checkTransferIntention** | [**CheckTransferIntention**](CheckTransferIntention.md) |  |  |
|**checkTransferRejection** | [**CheckTransferRejection**](CheckTransferRejection.md) |  |  |
|**checkTransferReturn** | [**CheckTransferReturn1**](CheckTransferReturn1.md) |  |  |
|**checkTransferStopPaymentRequest** | [**CheckTransferStopPaymentRequest1**](CheckTransferStopPaymentRequest1.md) |  |  |
|**disputeResolution** | [**DisputeResolution**](DisputeResolution.md) |  |  |
|**empyrealCashDeposit** | [**EmpyrealCashDeposit**](EmpyrealCashDeposit.md) |  |  |
|**feePayment** | [**FeePayment**](FeePayment.md) |  |  |
|**inboundAchTransfer** | [**InboundACHTransfer**](InboundACHTransfer.md) |  |  |
|**inboundCheck** | [**InboundCheck**](InboundCheck.md) |  |  |
|**inboundInternationalAchTransfer** | [**InboundInternationalACHTransfer**](InboundInternationalACHTransfer.md) |  |  |
|**inboundRealTimePaymentsTransferConfirmation** | [**InboundRealTimePaymentsTransferConfirmation**](InboundRealTimePaymentsTransferConfirmation.md) |  |  |
|**inboundWireDrawdownPayment** | [**InboundWireDrawdownPayment**](InboundWireDrawdownPayment.md) |  |  |
|**inboundWireDrawdownPaymentReversal** | [**InboundWireDrawdownPaymentReversal**](InboundWireDrawdownPaymentReversal.md) |  |  |
|**inboundWireReversal** | [**InboundWireReversal**](InboundWireReversal.md) |  |  |
|**inboundWireTransfer** | [**InboundWireTransfer**](InboundWireTransfer.md) |  |  |
|**interestPayment** | [**InterestPayment**](InterestPayment.md) |  |  |
|**internalSource** | [**InternalSource**](InternalSource.md) |  |  |
|**realTimePaymentsTransferAcknowledgement** | [**RealTimePaymentsTransferAcknowledgement**](RealTimePaymentsTransferAcknowledgement.md) |  |  |
|**sampleFunds** | [**SampleFunds**](SampleFunds.md) |  |  |
|**wireDrawdownPaymentIntention** | [**WireDrawdownPaymentIntention**](WireDrawdownPaymentIntention.md) |  |  |
|**wireDrawdownPaymentRejection** | [**WireDrawdownPaymentRejection**](WireDrawdownPaymentRejection.md) |  |  |
|**wireTransferIntention** | [**WireTransferIntention**](WireTransferIntention.md) |  |  |
|**wireTransferRejection** | [**WireTransferRejection**](WireTransferRejection.md) |  |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| ACCOUNT_TRANSFER_INTENTION | &quot;account_transfer_intention&quot; |
| ACH_CHECK_CONVERSION_RETURN | &quot;ach_check_conversion_return&quot; |
| ACH_CHECK_CONVERSION | &quot;ach_check_conversion&quot; |
| ACH_TRANSFER_INTENTION | &quot;ach_transfer_intention&quot; |
| ACH_TRANSFER_REJECTION | &quot;ach_transfer_rejection&quot; |
| ACH_TRANSFER_RETURN | &quot;ach_transfer_return&quot; |
| CARD_DISPUTE_ACCEPTANCE | &quot;card_dispute_acceptance&quot; |
| CARD_REFUND | &quot;card_refund&quot; |
| CARD_SETTLEMENT | &quot;card_settlement&quot; |
| CARD_REVENUE_PAYMENT | &quot;card_revenue_payment&quot; |
| CHECK_DEPOSIT_ACCEPTANCE | &quot;check_deposit_acceptance&quot; |
| CHECK_DEPOSIT_RETURN | &quot;check_deposit_return&quot; |
| CHECK_TRANSFER_INTENTION | &quot;check_transfer_intention&quot; |
| CHECK_TRANSFER_RETURN | &quot;check_transfer_return&quot; |
| CHECK_TRANSFER_REJECTION | &quot;check_transfer_rejection&quot; |
| CHECK_TRANSFER_STOP_PAYMENT_REQUEST | &quot;check_transfer_stop_payment_request&quot; |
| DISPUTE_RESOLUTION | &quot;dispute_resolution&quot; |
| EMPYREAL_CASH_DEPOSIT | &quot;empyreal_cash_deposit&quot; |
| FEE_PAYMENT | &quot;fee_payment&quot; |
| INBOUND_ACH_TRANSFER | &quot;inbound_ach_transfer&quot; |
| INBOUND_ACH_TRANSFER_RETURN_INTENTION | &quot;inbound_ach_transfer_return_intention&quot; |
| INBOUND_CHECK | &quot;inbound_check&quot; |
| INBOUND_INTERNATIONAL_ACH_TRANSFER | &quot;inbound_international_ach_transfer&quot; |
| INBOUND_REAL_TIME_PAYMENTS_TRANSFER_CONFIRMATION | &quot;inbound_real_time_payments_transfer_confirmation&quot; |
| INBOUND_WIRE_DRAWDOWN_PAYMENT_REVERSAL | &quot;inbound_wire_drawdown_payment_reversal&quot; |
| INBOUND_WIRE_DRAWDOWN_PAYMENT | &quot;inbound_wire_drawdown_payment&quot; |
| INBOUND_WIRE_REVERSAL | &quot;inbound_wire_reversal&quot; |
| INBOUND_WIRE_TRANSFER | &quot;inbound_wire_transfer&quot; |
| INTEREST_PAYMENT | &quot;interest_payment&quot; |
| INTERNAL_GENERAL_LEDGER_TRANSACTION | &quot;internal_general_ledger_transaction&quot; |
| INTERNAL_SOURCE | &quot;internal_source&quot; |
| CARD_ROUTE_REFUND | &quot;card_route_refund&quot; |
| CARD_ROUTE_SETTLEMENT | &quot;card_route_settlement&quot; |
| REAL_TIME_PAYMENTS_TRANSFER_ACKNOWLEDGEMENT | &quot;real_time_payments_transfer_acknowledgement&quot; |
| SAMPLE_FUNDS | &quot;sample_funds&quot; |
| WIRE_DRAWDOWN_PAYMENT_INTENTION | &quot;wire_drawdown_payment_intention&quot; |
| WIRE_DRAWDOWN_PAYMENT_REJECTION | &quot;wire_drawdown_payment_rejection&quot; |
| WIRE_TRANSFER_INTENTION | &quot;wire_transfer_intention&quot; |
| WIRE_TRANSFER_REJECTION | &quot;wire_transfer_rejection&quot; |
| OTHER | &quot;other&quot; |



