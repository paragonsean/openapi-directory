

# CreateRefundRequest

Defines the body parameters that can be included in a request to the [CreateRefund](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/create-refund) endpoint.  Deprecated - recommend using [RefundPayment](https://developer.squareup.com/reference/square_2021-08-18/refunds-api/refund-payment)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountMoney** | [**Money**](Money.md) |  |  |
|**idempotencyKey** | **String** | A value you specify that uniquely identifies this refund among refunds you&#39;ve created for the tender.  If you&#39;re unsure whether a particular refund succeeded, you can reattempt it with the same idempotency key without worrying about duplicating the refund.  See [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency) for more information. |  |
|**reason** | **String** | A description of the reason for the refund.  Default value: &#x60;Refund via API&#x60; |  [optional] |
|**tenderId** | **String** | The ID of the tender to refund.  A [&#x60;Transaction&#x60;](https://developer.squareup.com/reference/square_2021-08-18/objects/Transaction) has one or more &#x60;tenders&#x60; (i.e., methods of payment) associated with it, and you refund each tender separately with the Connect API. |  |



