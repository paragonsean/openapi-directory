# XeroBankFeedsApi.Statement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endBalance** | [**EndBalance**](EndBalance.md) |  | [optional] 
**endDate** | **Date** | Closing balance date ISO-8601 YYYY-MM-DD | [optional] 
**errors** | [**[Error]**](Error.md) |  | [optional] 
**feedConnectionId** | **String** | The Xero generated feed connection Id that identifies the Xero Bank Account Container into which the statement should be delivered. This is obtained by calling GET FeedConnections. | [optional] 
**id** | **String** | GUID used to identify the Statement. | [optional] 
**startBalance** | [**StartBalance**](StartBalance.md) |  | [optional] 
**startDate** | **Date** | Opening balance date (can be no older than one year from the current date) ISO-8601 YYYY-MM-DD | [optional] 
**statementLineCount** | **Number** |  | [optional] 
**statementLines** | [**[StatementLine]**](StatementLine.md) |  | [optional] 
**status** | **String** | Current status of statements | [optional] 



## Enum: StatusEnum


* `PENDING` (value: `"PENDING"`)

* `REJECTED` (value: `"REJECTED"`)

* `DELIVERED` (value: `"DELIVERED"`)




