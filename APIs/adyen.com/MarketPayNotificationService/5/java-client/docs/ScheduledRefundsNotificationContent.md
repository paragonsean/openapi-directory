

# ScheduledRefundsNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | The code of the account. |  [optional] |
|**accountHolderCode** | **String** | The code of the Account Holder. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | Invalid fields list. |  [optional] |
|**lastPayout** | [**Transaction**](Transaction.md) | The most recent payout (after which all transactions were scheduled to be refunded). |  [optional] |
|**refundResults** | [**List&lt;RefundResult&gt;**](RefundResult.md) | A list of the refunds that have been scheduled and their results. |  [optional] |



