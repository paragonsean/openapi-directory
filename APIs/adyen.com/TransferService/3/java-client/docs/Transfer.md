

# Transfer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolder** | [**ResourceReference**](ResourceReference.md) | The account holder associated with the balance account used in the transfer. |  [optional] |
|**amount** | [**Amount**](Amount.md) | The amount of the transfer. |  |
|**balanceAccount** | [**ResourceReference**](ResourceReference.md) | Contains information about the balance account involved in the transfer. |  [optional] |
|**balanceAccountId** | **String** | The unique identifier of the source [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id). |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of transfer.  Possible values:   - **bank**: Transfer to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resParam_id) or a bank account.  - **internal**: Transfer to another [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id) within your platform.  - **issuedCard**: Transfer initiated by a Adyen-issued card.  - **platformPayment**: Fund movements related to payments that are acquired for your users. |  |
|**counterparty** | [**CounterpartyV3**](CounterpartyV3.md) | The other party in the transfer. |  |
|**creationDate** | **OffsetDateTime** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |  [optional] |
|**description** | **String** | Your description for the transfer. It is used by most banks as the transfer description. We recommend sending a maximum of 140 characters, otherwise the description may be truncated.  Supported characters: **[a-z] [A-Z] [0-9] / - ?** **: ( ) . , &#39; + Space**  Supported characters for **regular** and **fast** transfers to a US counterparty: **[a-z] [A-Z] [0-9] &amp; $ % # @** **~ &#x3D; + - _ &#39; \&quot; ! ?** |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction of the transfer.  Possible values: **incoming**, **outgoing**. |  [optional] |
|**id** | **String** | The ID of the resource. |  [optional] |
|**paymentInstrument** | [**PaymentInstrument**](PaymentInstrument.md) | Contains information about the payment instrument used in the transfer. |  [optional] |
|**paymentInstrumentId** | **String** | The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/balanceAccounts__resParam_id) used in the transfer. |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with &#x60;category&#x60; **bank**.  Possible values:  * **regular**: For normal, low-value transactions.  * **fast**: Faster way to transfer funds but has higher fees. Recommended for high-priority, low-value transactions.  * **wire**: Fastest way to transfer funds but has the highest fees. Recommended for high-priority, high-value transactions.  * **instant**: Instant way to transfer funds in [SEPA countries](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  * **crossBorder**: High-value transfer to a recipient in a different country.  * **internal**: Transfer to an Adyen-issued business bank account (by bank account number/IBAN). This will be removed in v4 and replaced with a new field. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Additional information about the status of the transfer. |  [optional] |
|**reference** | **String** | Your reference for the transfer, used internally within your platform. If you don&#39;t provide this in the request, Adyen generates a unique reference. |  [optional] |
|**referenceForBeneficiary** | **String** |  A reference that is sent to the recipient. This reference is also sent in all webhooks related to the transfer, so you can use it to track statuses for both the source and recipient of funds.   Supported characters: **a-z**, **A-Z**, **0-9**. The maximum length depends on the &#x60;category&#x60;.  - **internal**: 80 characters  - **bank**: 35 characters when transferring to an IBAN, 15 characters for others. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The result of the transfer.   For example, **authorised**, **refused**, or **error**. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| INTERNAL | &quot;internal&quot; |
| ISSUED_CARD | &quot;issuedCard&quot; |
| PLATFORM_PAYMENT | &quot;platformPayment&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INCOMING | &quot;incoming&quot; |
| OUTGOING | &quot;outgoing&quot; |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| CROSS_BORDER | &quot;crossBorder&quot; |
| FAST | &quot;fast&quot; |
| INSTANT | &quot;instant&quot; |
| INTERNAL | &quot;internal&quot; |
| REGULAR | &quot;regular&quot; |
| WIRE | &quot;wire&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| AMOUNT_LIMIT_EXCEEDED | &quot;amountLimitExceeded&quot; |
| APPROVED | &quot;approved&quot; |
| BALANCE_ACCOUNT_TEMPORARILY_BLOCKED_BY_TRANSACTION_RULE | &quot;balanceAccountTemporarilyBlockedByTransactionRule&quot; |
| COUNTERPARTY_ACCOUNT_BLOCKED | &quot;counterpartyAccountBlocked&quot; |
| COUNTERPARTY_ACCOUNT_CLOSED | &quot;counterpartyAccountClosed&quot; |
| COUNTERPARTY_ACCOUNT_NOT_FOUND | &quot;counterpartyAccountNotFound&quot; |
| COUNTERPARTY_ADDRESS_REQUIRED | &quot;counterpartyAddressRequired&quot; |
| COUNTERPARTY_BANK_TIMED_OUT | &quot;counterpartyBankTimedOut&quot; |
| COUNTERPARTY_BANK_UNAVAILABLE | &quot;counterpartyBankUnavailable&quot; |
| DECLINED_BY_TRANSACTION_RULE | &quot;declinedByTransactionRule&quot; |
| ERROR | &quot;error&quot; |
| NOT_ENOUGH_BALANCE | &quot;notEnoughBalance&quot; |
| REFUSED_BY_COUNTERPARTY_BANK | &quot;refusedByCounterpartyBank&quot; |
| ROUTE_NOT_FOUND | &quot;routeNotFound&quot; |
| SCA_FAILED | &quot;scaFailed&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVAL_PENDING | &quot;approvalPending&quot; |
| ATM_WITHDRAWAL | &quot;atmWithdrawal&quot; |
| ATM_WITHDRAWAL_REVERSAL_PENDING | &quot;atmWithdrawalReversalPending&quot; |
| ATM_WITHDRAWAL_REVERSED | &quot;atmWithdrawalReversed&quot; |
| AUTH_ADJUSTMENT_AUTHORISED | &quot;authAdjustmentAuthorised&quot; |
| AUTH_ADJUSTMENT_ERROR | &quot;authAdjustmentError&quot; |
| AUTH_ADJUSTMENT_REFUSED | &quot;authAdjustmentRefused&quot; |
| AUTHORISED | &quot;authorised&quot; |
| BANK_TRANSFER | &quot;bankTransfer&quot; |
| BANK_TRANSFER_PENDING | &quot;bankTransferPending&quot; |
| BOOKED | &quot;booked&quot; |
| BOOKING_PENDING | &quot;bookingPending&quot; |
| CANCELLED | &quot;cancelled&quot; |
| CAPTURE_PENDING | &quot;capturePending&quot; |
| CAPTURE_REVERSAL_PENDING | &quot;captureReversalPending&quot; |
| CAPTURE_REVERSED | &quot;captureReversed&quot; |
| CAPTURED | &quot;captured&quot; |
| CAPTURED_EXTERNALLY | &quot;capturedExternally&quot; |
| CHARGEBACK | &quot;chargeback&quot; |
| CHARGEBACK_EXTERNALLY | &quot;chargebackExternally&quot; |
| CHARGEBACK_PENDING | &quot;chargebackPending&quot; |
| CHARGEBACK_REVERSAL_PENDING | &quot;chargebackReversalPending&quot; |
| CHARGEBACK_REVERSED | &quot;chargebackReversed&quot; |
| CREDITED | &quot;credited&quot; |
| DEPOSIT_CORRECTION | &quot;depositCorrection&quot; |
| DEPOSIT_CORRECTION_PENDING | &quot;depositCorrectionPending&quot; |
| DISPUTE | &quot;dispute&quot; |
| DISPUTE_CLOSED | &quot;disputeClosed&quot; |
| DISPUTE_EXPIRED | &quot;disputeExpired&quot; |
| DISPUTE_NEEDS_REVIEW | &quot;disputeNeedsReview&quot; |
| ERROR | &quot;error&quot; |
| EXPIRED | &quot;expired&quot; |
| FAILED | &quot;failed&quot; |
| FEE | &quot;fee&quot; |
| FEE_PENDING | &quot;feePending&quot; |
| INTERNAL_TRANSFER | &quot;internalTransfer&quot; |
| INTERNAL_TRANSFER_PENDING | &quot;internalTransferPending&quot; |
| INVOICE_DEDUCTION | &quot;invoiceDeduction&quot; |
| INVOICE_DEDUCTION_PENDING | &quot;invoiceDeductionPending&quot; |
| MANUAL_CORRECTION_PENDING | &quot;manualCorrectionPending&quot; |
| MANUALLY_CORRECTED | &quot;manuallyCorrected&quot; |
| MATCHED_STATEMENT | &quot;matchedStatement&quot; |
| MATCHED_STATEMENT_PENDING | &quot;matchedStatementPending&quot; |
| MERCHANT_PAYIN | &quot;merchantPayin&quot; |
| MERCHANT_PAYIN_PENDING | &quot;merchantPayinPending&quot; |
| MERCHANT_PAYIN_REVERSED | &quot;merchantPayinReversed&quot; |
| MERCHANT_PAYIN_REVERSED_PENDING | &quot;merchantPayinReversedPending&quot; |
| MISC_COST | &quot;miscCost&quot; |
| MISC_COST_PENDING | &quot;miscCostPending&quot; |
| PAYMENT_COST | &quot;paymentCost&quot; |
| PAYMENT_COST_PENDING | &quot;paymentCostPending&quot; |
| RECEIVED | &quot;received&quot; |
| REFUND_PENDING | &quot;refundPending&quot; |
| REFUND_REVERSAL_PENDING | &quot;refundReversalPending&quot; |
| REFUND_REVERSED | &quot;refundReversed&quot; |
| REFUNDED | &quot;refunded&quot; |
| REFUNDED_EXTERNALLY | &quot;refundedExternally&quot; |
| REFUSED | &quot;refused&quot; |
| RESERVE_ADJUSTMENT | &quot;reserveAdjustment&quot; |
| RESERVE_ADJUSTMENT_PENDING | &quot;reserveAdjustmentPending&quot; |
| RETURNED | &quot;returned&quot; |
| SECOND_CHARGEBACK | &quot;secondChargeback&quot; |
| SECOND_CHARGEBACK_PENDING | &quot;secondChargebackPending&quot; |
| UNDEFINED | &quot;undefined&quot; |



