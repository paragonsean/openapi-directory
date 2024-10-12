

# UpdateOrderRequest

Defines the fields that are included in requests to the [UpdateOrder](https://developer.squareup.com/reference/square_2021-08-18/orders-api/update-order) endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldsToClear** | **List&lt;String&gt;** | The [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation) fields to clear. For example, &#x60;line_items[uid].note&#x60;. For more information, see [Deleting fields](https://developer.squareup.com/docs/orders-api/manage-orders#delete-fields). |  [optional] |
|**idempotencyKey** | **String** | A value you specify that uniquely identifies this update request.  If you are unsure whether a particular update was applied to an order successfully, you can reattempt it with the same idempotency key without worrying about creating duplicate updates to the order. The latest order version is returned.  For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency). |  [optional] |
|**order** | [**Order**](Order.md) |  |  [optional] |



