

# UserorderdetailsCancellationData

Information about order cancellation, when it applies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancellationDate** | **String** | The date when the order was cancelled. |  |
|**reason** | **String** | The reason why the order was cancelled. |  |
|**requestedByPaymentNotification** | **Boolean** | If the order cancellation was requested by the payment gateway (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  |
|**requestedBySellerNotification** | **Boolean** | If the order cancellation was requested by the seller (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  |
|**requestedBySystem** | **Boolean** | If the order cancellation was made by the system (&#x60;true&#x60;) or not (&#x60;false&#x60;). This type of order cancellation happens in [incomplete orders](https://help.vtex.com/en/tutorial/how-incomplete-orders-work--tutorials_294), for example. |  |
|**requestedByUser** | **Boolean** | If the order cancellation was requested by the costumer (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  |



