

# Statement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endBalance** | [**EndBalance**](EndBalance.md) |  |  [optional] |
|**endDate** | **LocalDate** | Closing balance date ISO-8601 YYYY-MM-DD |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) |  |  [optional] |
|**feedConnectionId** | **UUID** | The Xero generated feed connection Id that identifies the Xero Bank Account Container into which the statement should be delivered. This is obtained by calling GET FeedConnections. |  [optional] |
|**id** | **UUID** | GUID used to identify the Statement. |  [optional] |
|**startBalance** | [**StartBalance**](StartBalance.md) |  |  [optional] |
|**startDate** | **LocalDate** | Opening balance date (can be no older than one year from the current date) ISO-8601 YYYY-MM-DD |  [optional] |
|**statementLineCount** | **Integer** |  |  [optional] |
|**statementLines** | [**List&lt;StatementLine&gt;**](StatementLine.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of statements |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| REJECTED | &quot;REJECTED&quot; |
| DELIVERED | &quot;DELIVERED&quot; |



