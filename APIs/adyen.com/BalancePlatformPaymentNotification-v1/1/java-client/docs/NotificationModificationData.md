

# NotificationModificationData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The amount of the modification converted to the balance account&#39;s currency, in case the original transaction currency is different. For example, if a part of an authorised amount was cancelled, the value shows the amount that was cancelled.   * A _positive_ value means the amount is added to the balance account.   * A _negative_ value means the amount is deducted from the balance account.  |  [optional] |
|**type** | **String** | The type of modification.  Possible values: **Authorised**, **Cancelled**, **Captured**, **Error**, **Expired**, **OutgoingTransfer**, **PendingIncomingTransfer**, **PendingRefund**, **IncomingTransfer**, **Refunded**, **Refused**, **AuthAdjustmentAuthorised**. |  [optional] |



