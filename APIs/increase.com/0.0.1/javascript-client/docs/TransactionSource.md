# IncreaseApi.TransactionSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountTransferIntention** | [**AccountTransferIntention**](AccountTransferIntention.md) |  | 
**achCheckConversion** | [**ACHCheckConversion**](ACHCheckConversion.md) |  | 
**achCheckConversionReturn** | [**ACHCheckConversionReturn**](ACHCheckConversionReturn.md) |  | 
**achTransferIntention** | [**ACHTransferIntention**](ACHTransferIntention.md) |  | 
**achTransferRejection** | [**ACHTransferRejection**](ACHTransferRejection.md) |  | 
**achTransferReturn** | [**ACHTransferReturn1**](ACHTransferReturn1.md) |  | 
**cardDisputeAcceptance** | [**CardDisputeAcceptance1**](CardDisputeAcceptance1.md) |  | 
**cardRefund** | [**CardRefund**](CardRefund.md) |  | 
**cardRevenuePayment** | [**CardRevenuePayment**](CardRevenuePayment.md) |  | 
**cardRouteRefund** | [**DeprecatedCardRefund**](DeprecatedCardRefund.md) |  | 
**cardRouteSettlement** | [**DeprecatedCardSettlement**](DeprecatedCardSettlement.md) |  | 
**cardSettlement** | [**CardSettlement**](CardSettlement.md) |  | 
**category** | **String** | The type of transaction that took place. We may add additional possible values for this enum over time; your application should be able to handle such additions gracefully. | 
**checkDepositAcceptance** | [**CheckDepositAcceptance1**](CheckDepositAcceptance1.md) |  | 
**checkDepositReturn** | [**CheckDepositReturn1**](CheckDepositReturn1.md) |  | 
**checkTransferIntention** | [**CheckTransferIntention**](CheckTransferIntention.md) |  | 
**checkTransferRejection** | [**CheckTransferRejection**](CheckTransferRejection.md) |  | 
**checkTransferReturn** | [**CheckTransferReturn1**](CheckTransferReturn1.md) |  | 
**checkTransferStopPaymentRequest** | [**CheckTransferStopPaymentRequest1**](CheckTransferStopPaymentRequest1.md) |  | 
**disputeResolution** | [**DisputeResolution**](DisputeResolution.md) |  | 
**empyrealCashDeposit** | [**EmpyrealCashDeposit**](EmpyrealCashDeposit.md) |  | 
**feePayment** | [**FeePayment**](FeePayment.md) |  | 
**inboundAchTransfer** | [**InboundACHTransfer**](InboundACHTransfer.md) |  | 
**inboundCheck** | [**InboundCheck**](InboundCheck.md) |  | 
**inboundInternationalAchTransfer** | [**InboundInternationalACHTransfer**](InboundInternationalACHTransfer.md) |  | 
**inboundRealTimePaymentsTransferConfirmation** | [**InboundRealTimePaymentsTransferConfirmation**](InboundRealTimePaymentsTransferConfirmation.md) |  | 
**inboundWireDrawdownPayment** | [**InboundWireDrawdownPayment**](InboundWireDrawdownPayment.md) |  | 
**inboundWireDrawdownPaymentReversal** | [**InboundWireDrawdownPaymentReversal**](InboundWireDrawdownPaymentReversal.md) |  | 
**inboundWireReversal** | [**InboundWireReversal**](InboundWireReversal.md) |  | 
**inboundWireTransfer** | [**InboundWireTransfer**](InboundWireTransfer.md) |  | 
**interestPayment** | [**InterestPayment**](InterestPayment.md) |  | 
**internalSource** | [**InternalSource**](InternalSource.md) |  | 
**realTimePaymentsTransferAcknowledgement** | [**RealTimePaymentsTransferAcknowledgement**](RealTimePaymentsTransferAcknowledgement.md) |  | 
**sampleFunds** | [**SampleFunds**](SampleFunds.md) |  | 
**wireDrawdownPaymentIntention** | [**WireDrawdownPaymentIntention**](WireDrawdownPaymentIntention.md) |  | 
**wireDrawdownPaymentRejection** | [**WireDrawdownPaymentRejection**](WireDrawdownPaymentRejection.md) |  | 
**wireTransferIntention** | [**WireTransferIntention**](WireTransferIntention.md) |  | 
**wireTransferRejection** | [**WireTransferRejection**](WireTransferRejection.md) |  | 



## Enum: CategoryEnum


* `account_transfer_intention` (value: `"account_transfer_intention"`)

* `ach_check_conversion_return` (value: `"ach_check_conversion_return"`)

* `ach_check_conversion` (value: `"ach_check_conversion"`)

* `ach_transfer_intention` (value: `"ach_transfer_intention"`)

* `ach_transfer_rejection` (value: `"ach_transfer_rejection"`)

* `ach_transfer_return` (value: `"ach_transfer_return"`)

* `card_dispute_acceptance` (value: `"card_dispute_acceptance"`)

* `card_refund` (value: `"card_refund"`)

* `card_settlement` (value: `"card_settlement"`)

* `card_revenue_payment` (value: `"card_revenue_payment"`)

* `check_deposit_acceptance` (value: `"check_deposit_acceptance"`)

* `check_deposit_return` (value: `"check_deposit_return"`)

* `check_transfer_intention` (value: `"check_transfer_intention"`)

* `check_transfer_return` (value: `"check_transfer_return"`)

* `check_transfer_rejection` (value: `"check_transfer_rejection"`)

* `check_transfer_stop_payment_request` (value: `"check_transfer_stop_payment_request"`)

* `dispute_resolution` (value: `"dispute_resolution"`)

* `empyreal_cash_deposit` (value: `"empyreal_cash_deposit"`)

* `fee_payment` (value: `"fee_payment"`)

* `inbound_ach_transfer` (value: `"inbound_ach_transfer"`)

* `inbound_ach_transfer_return_intention` (value: `"inbound_ach_transfer_return_intention"`)

* `inbound_check` (value: `"inbound_check"`)

* `inbound_international_ach_transfer` (value: `"inbound_international_ach_transfer"`)

* `inbound_real_time_payments_transfer_confirmation` (value: `"inbound_real_time_payments_transfer_confirmation"`)

* `inbound_wire_drawdown_payment_reversal` (value: `"inbound_wire_drawdown_payment_reversal"`)

* `inbound_wire_drawdown_payment` (value: `"inbound_wire_drawdown_payment"`)

* `inbound_wire_reversal` (value: `"inbound_wire_reversal"`)

* `inbound_wire_transfer` (value: `"inbound_wire_transfer"`)

* `interest_payment` (value: `"interest_payment"`)

* `internal_general_ledger_transaction` (value: `"internal_general_ledger_transaction"`)

* `internal_source` (value: `"internal_source"`)

* `card_route_refund` (value: `"card_route_refund"`)

* `card_route_settlement` (value: `"card_route_settlement"`)

* `real_time_payments_transfer_acknowledgement` (value: `"real_time_payments_transfer_acknowledgement"`)

* `sample_funds` (value: `"sample_funds"`)

* `wire_drawdown_payment_intention` (value: `"wire_drawdown_payment_intention"`)

* `wire_drawdown_payment_rejection` (value: `"wire_drawdown_payment_rejection"`)

* `wire_transfer_intention` (value: `"wire_transfer_intention"`)

* `wire_transfer_rejection` (value: `"wire_transfer_rejection"`)

* `other` (value: `"other"`)




