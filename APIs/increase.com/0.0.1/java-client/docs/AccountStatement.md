

# AccountStatement

Account Statements are generated monthly for every active Account. You can access the statement's data via the API or retrieve a PDF with its details via its associated File.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The identifier for the Account this Account Statement belongs to. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Account Statement was created. |  |
|**endingBalance** | **Integer** | The Account&#39;s balance at the start of its statement period. |  |
|**fileId** | **String** | The identifier of the File containing a PDF of the statement. |  |
|**id** | **String** | The Account Statement identifier. |  |
|**startingBalance** | **Integer** | The Account&#39;s balance at the start of its statement period. |  |
|**statementPeriodEnd** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time representing the end of the period the Account Statement covers. |  |
|**statementPeriodStart** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time representing the start of the period the Account Statement covers. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;account_statement&#x60;. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_STATEMENT | &quot;account_statement&quot; |



