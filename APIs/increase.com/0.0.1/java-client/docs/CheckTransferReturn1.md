

# CheckTransferReturn1

A Check Transfer Return object. This field will be present in the JSON response if and only if `category` is equal to `check_transfer_return`.

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



