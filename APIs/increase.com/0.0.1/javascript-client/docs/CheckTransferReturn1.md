# IncreaseApi.CheckTransferReturn1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileId** | **String** | If available, a document with additional information about the return. | 
**reason** | **String** | The reason why the check was returned. | 
**returnedAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the check was returned. | 
**transactionId** | **String** | The identifier of the Transaction that was created to credit you for the returned check. | 
**transferId** | **String** | The identifier of the returned Check Transfer. | 



## Enum: ReasonEnum


* `mail_delivery_failure` (value: `"mail_delivery_failure"`)

* `refused_by_recipient` (value: `"refused_by_recipient"`)




