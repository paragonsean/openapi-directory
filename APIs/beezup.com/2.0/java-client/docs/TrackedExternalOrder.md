

# TrackedExternalOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | The currency code &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_4217\&quot;&gt;(ISO 4217)&lt;/a&gt;  |  |
|**merchantOrderId** | **String** | The merchant order identifier |  |
|**paymentValidated** | **Boolean** | Indicate if the payment of this external order has been validated or not |  |
|**products** | [**List&lt;TrackedExternalOrderProduct&gt;**](TrackedExternalOrderProduct.md) | Can be null. The product list included in the external order |  [optional] |
|**totalAmount** | **BigDecimal** | The total amount of the external order |  |
|**utcDate** | **OffsetDateTime** | The utc date of the external order |  |
|**visitorId** | **String** | Can be null. The visitor identifier of the external order |  [optional] |



