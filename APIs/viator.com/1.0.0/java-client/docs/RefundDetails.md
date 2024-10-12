

# RefundDetails

Details of the refund  **Note**: Bookings that have not been confirmed by the supplier and have a status of `\"PENDING\"` will report an `itemPrice`, `refundAmount` and `refundPercentage` of `0`, as no fees are charged until the booking has been accepted by the supplier and its status is `\"CONFIRMED\"`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | Three-letter code indicating the currency in which &#x60;itemPrice&#x60; and &#x60;refundAmount&#x60; are displayed |  [optional] |
|**itemPrice** | **BigDecimal** | The merchant net price at the time this product was booked |  [optional] |
|**refundAmount** | **BigDecimal** | Numeric currency amount that will be refunded if this booking is cancelled now |  [optional] |
|**refundPercentage** | **BigDecimal** | Percentage of the item price that will be refunded if this booking is cancelled now |  [optional] |



