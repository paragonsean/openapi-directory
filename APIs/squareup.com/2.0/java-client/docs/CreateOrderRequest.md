

# CreateOrderRequest



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**idempotencyKey** | **String** | A value you specify that uniquely identifies this order among orders you have created.  If you are unsure whether a particular order was created successfully, you can try it again with the same idempotency key without worrying about creating duplicate orders.  For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency). |  [optional] |
|**order** | [**Order**](Order.md) |  |  [optional] |



