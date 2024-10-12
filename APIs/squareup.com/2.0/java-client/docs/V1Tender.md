

# V1Tender

A tender represents a discrete monetary exchange. Square represents this exchange as a money object with a specific currency and amount, where the amount is given in the smallest denomination of the given currency.  Square POS can accept more than one form of tender for a single payment (such as by splitting a bill between a credit card and a gift card). The `tender` field of the Payment object lists all forms of tender used for the payment.  Split tender payments behave slightly differently from single tender payments:  The receipt_url for a split tender corresponds only to the first tender listed in the tender field. To get the receipt URLs for the remaining tenders, use the receipt_url fields of the corresponding Tender objects.  *A note on gift cards**: when a customer purchases a Square gift card from a merchant, the merchant receives the full amount of the gift card in the associated payment.  When that gift card is used as a tender, the balance of the gift card is reduced and the merchant receives no funds. A `Tender` object with a type of `SQUARE_GIFT_CARD` indicates a gift card was used for some or all of the associated payment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardBrand** | **String** | The brand of credit card provided. |  [optional] |
|**changeBackMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**employeeId** | **String** | The ID of the employee that processed the tender. |  [optional] |
|**entryMethod** | **String** | The tender&#39;s unique ID. |  [optional] |
|**id** | **String** | The tender&#39;s unique ID. |  [optional] |
|**isExchange** | **Boolean** | Indicates whether or not the tender is associated with an exchange. If is_exchange is true, the tender represents the value of goods returned in an exchange not the actual money paid. The exchange value reduces the tender amounts needed to pay for items purchased in the exchange. |  [optional] |
|**name** | **String** | A human-readable description of the tender. |  [optional] |
|**panSuffix** | **String** | The last four digits of the provided credit card&#39;s account number. |  [optional] |
|**paymentNote** | **String** | Notes entered by the merchant about the tender at the time of payment, if any. Typically only present for tender with the type: OTHER. |  [optional] |
|**receiptUrl** | **String** | The URL of the receipt for the tender. |  [optional] |
|**refundedMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**settledAt** | **String** | The time when the tender was settled, in ISO 8601 format. |  [optional] |
|**tenderedAt** | **String** | The time when the tender was created, in ISO 8601 format. |  [optional] |
|**tenderedMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**totalMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**type** | **String** | The type of tender. |  [optional] |



