

# TrackedOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**BeezUPCommonChannelBasicInfo**](BeezUPCommonChannelBasicInfo.md) |  |  |
|**currencyCode** | **String** | The currency code &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_4217\&quot;&gt;(ISO 4217)&lt;/a&gt;  |  |
|**merchantOrderId** | **String** | The merchant order identifier |  |
|**paymentValidated** | **Boolean** | Indicate if the payment of this order has been validated or not |  |
|**products** | [**List&lt;TrackedOrderProduct&gt;**](TrackedOrderProduct.md) | The product list of this order |  |
|**totalAmount** | **BigDecimal** | The total amount of the order |  |
|**utcDate** | **OffsetDateTime** | The utc date of the order |  |



