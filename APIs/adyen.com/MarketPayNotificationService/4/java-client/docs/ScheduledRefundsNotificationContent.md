

# ScheduledRefundsNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | The code of the account. |  [optional] |
|**accountHolderCode** | **String** | The code of the Account Holder. |  [optional] |
|**lastPayout** | [**Transaction**](Transaction.md) | The most recent payout (after which all transactions were scheduled to be refunded). |  [optional] |
|**refundResults** | [**List&lt;RefundResultWrapper&gt;**](RefundResultWrapper.md) | A list of the refunds that have been scheduled and their results. |  [optional] |



