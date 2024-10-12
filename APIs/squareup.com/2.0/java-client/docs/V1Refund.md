

# V1Refund

V1Refund

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | The time when the merchant initiated the refund for Square to process, in ISO 8601 format. |  [optional] |
|**isExchange** | **Boolean** | Indicates whether or not the refund is associated with an exchange. If is_exchange is true, the refund reflects the value of goods returned in the exchange not the total money refunded. |  [optional] |
|**merchantId** | **String** |  |  [optional] |
|**paymentId** | **String** | A Square-issued ID associated with the refund. For single-tender refunds, payment_id is the ID of the original payment ID. For split-tender refunds, payment_id is the ID of the original tender. For exchange-based refunds (is_exchange &#x3D;&#x3D; true), payment_id is the ID of the original payment ID even if the payment includes other tenders. |  [optional] |
|**processedAt** | **String** | The time when Square processed the refund on behalf of the merchant, in ISO 8601 format. |  [optional] |
|**reason** | **String** | The merchant-specified reason for the refund. |  [optional] |
|**refundedAdditiveTax** | [**List&lt;V1PaymentTax&gt;**](V1PaymentTax.md) | All of the additive taxes associated with the refund. |  [optional] |
|**refundedAdditiveTaxMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**refundedDiscountMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**refundedInclusiveTax** | [**List&lt;V1PaymentTax&gt;**](V1PaymentTax.md) | All of the inclusive taxes associated with the refund. |  [optional] |
|**refundedInclusiveTaxMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**refundedMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**refundedProcessingFeeMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**refundedSurchargeMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**refundedSurcharges** | [**List&lt;V1PaymentSurcharge&gt;**](V1PaymentSurcharge.md) | A list of all surcharges associated with the refund. |  [optional] |
|**refundedTaxMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**refundedTipMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**type** | **String** | The type of refund |  [optional] |



