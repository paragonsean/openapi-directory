

# PaymentReadRequest

PaymentReadSerializer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creditorAccount** | **UUID** | Registered creditor account |  [optional] |
|**creditorObject** | [**CreditorAccountWriteRequest**](CreditorAccountWriteRequest.md) | Creditor account |  [optional] |
|**customPaymentId** | **String** | Payment Custom Payment ID |  [optional] |
|**debtorAccount** | [**DebtorAccountWriteRequest**](DebtorAccountWriteRequest.md) |  |  |
|**description** | **String** | Payment description |  [optional] |
|**institutionId** | **String** | Institution ID for Payment |  [optional] |
|**instructedAmount** | [**InstructedAmountRequest**](InstructedAmountRequest.md) | Instructed amount |  |
|**paymentProduct** | **PaymentProductEnum** | Payment product  * &#x60;T2P&#x60; - target-2-payments * &#x60;SCT&#x60; - sepa-credit-transfers * &#x60;ISCT&#x60; - instant-sepa-credit-transfer * &#x60;CBCT&#x60; - cross-border-credit-transfers * &#x60;BACS&#x60; - Back Payment Scheme * &#x60;CHAPS&#x60; - CHAPS Payment Scheme * &#x60;FPS&#x60; - Faster Payment Scheme * &#x60;SWIFT&#x60; - Swift Payment Service * &#x60;BT&#x60; - Balance Transfer * &#x60;MT&#x60; - Money Transfer |  [optional] |
|**redirect** | **URI** | Redirect URL to your application after payment is done |  |



