

# Tender

Represents a tender (i.e., a method of payment) used in a Square transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalRecipients** | [**List&lt;AdditionalRecipient&gt;**](AdditionalRecipient.md) | Additional recipients (other than the merchant) receiving a portion of this tender. For example, fees assessed on the purchase by a third party integration. |  [optional] |
|**amountMoney** | [**Money**](Money.md) |  |  [optional] |
|**cardDetails** | [**TenderCardDetails**](TenderCardDetails.md) |  |  [optional] |
|**cashDetails** | [**TenderCashDetails**](TenderCashDetails.md) |  |  [optional] |
|**createdAt** | **String** | The timestamp for when the tender was created, in RFC 3339 format. |  [optional] |
|**customerId** | **String** | If the tender is associated with a customer or represents a customer&#39;s card on file, this is the ID of the associated customer. |  [optional] |
|**id** | **String** | The tender&#39;s unique ID. |  [optional] |
|**locationId** | **String** | The ID of the transaction&#39;s associated location. |  [optional] |
|**note** | **String** | An optional note associated with the tender at the time of payment. |  [optional] |
|**paymentId** | **String** | The ID of the [Payment](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) that corresponds to this tender. This value is only present for payments created with the v2 Payments API. |  [optional] |
|**processingFeeMoney** | [**Money**](Money.md) |  |  [optional] |
|**tipMoney** | [**Money**](Money.md) |  |  [optional] |
|**transactionId** | **String** | The ID of the tender&#39;s associated transaction. |  [optional] |
|**type** | **String** | The type of tender, such as &#x60;CARD&#x60; or &#x60;CASH&#x60;. |  |



