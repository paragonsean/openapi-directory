

# CheckTransferReturn

After a check transfer is returned, this will contain supplemental details. A check transfer is returned when the receiver mails a never deposited check back to the bank printed on the check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileId** | **String** | If available, a document with additional information about the return. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason why the check was returned. |  |
|**returnedAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check was returned. |  |
|**transactionId** | **String** | The identifier of the Transaction that was created to credit you for the returned check. |  |
|**transferId** | **String** | The identifier of the returned Check Transfer. |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| MAIL_DELIVERY_FAILURE | &quot;mail_delivery_failure&quot; |
| REFUSED_BY_RECIPIENT | &quot;refused_by_recipient&quot; |



