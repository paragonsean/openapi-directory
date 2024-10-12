

# Error

On error, the API consumer will receive an HTTP response with a HTTP Status Code of 4xx or 5xx and a Content-Type of application/problem+json.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | Human readable detailed error description. |  [optional] |
|**status** | **Integer** | The numeric HTTP Status Code, e.g. 404 |  [optional] |
|**title** | **String** | Human readable high level error description. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Identifies the type of error. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INVALID_REQUEST | &quot;invalid-request&quot; |
| INVALID_APPLICATION | &quot;invalid-application&quot; |
| INVALID_FEED_CONNECTION | &quot;invalid-feed-connection&quot; |
| DUPLICATE_STATEMENT | &quot;duplicate-statement&quot; |
| INVALID_END_BALANCE | &quot;invalid-end-balance&quot; |
| INVALID_START_AND_END_DATE | &quot;invalid-start-and-end-date&quot; |
| INVALID_START_DATE | &quot;invalid-start-date&quot; |
| INTERNAL_ERROR | &quot;internal-error&quot; |
| FEED_ALREADY_CONNECTED_IN_CURRENT_ORGANISATION | &quot;feed-already-connected-in-current-organisation&quot; |
| INVALID_END_DATE | &quot;invalid-end-date&quot; |
| STATEMENT_NOT_FOUND | &quot;statement-not-found&quot; |
| FEED_CONNECTED_IN_DIFFERENT_ORGANISATION | &quot;feed-connected-in-different-organisation&quot; |
| FEED_ALREADY_CONNECTED_IN_DIFFERENT_ORGANISATION | &quot;feed-already-connected-in-different-organisation&quot; |
| BANK_FEED_NOT_FOUND | &quot;bank-feed-not-found&quot; |
| INVALID_COUNTRY_SPECIFIED | &quot;invalid-country-specified&quot; |
| INVALID_ORGANISATION_BANK_FEEDS | &quot;invalid-organisation-bank-feeds&quot; |
| INVALID_ORGANISATION_MULTI_CURRENCY | &quot;invalid-organisation-multi-currency&quot; |
| INVALID_FEED_CONNECTION_FOR_ORGANISATION | &quot;invalid-feed-connection-for-organisation&quot; |
| INVALID_USER_ROLE | &quot;invalid-user-role&quot; |
| ACCOUNT_NOT_VALID | &quot;account-not-valid&quot; |



