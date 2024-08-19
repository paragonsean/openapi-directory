

# CalculateLoyaltyPointsRequest

A request to calculate the points that a buyer can earn from  a specified purchase.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**orderId** | **String** | The [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) ID for which to calculate the points. Specify this field if your application uses the Orders API to process orders. Otherwise, specify the &#x60;transaction_amount_money&#x60;. |  [optional] |
|**transactionAmountMoney** | [**Money**](Money.md) |  |  [optional] |



