# CloudSpannerApi.RequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **String** | Priority for the request. | [optional] 
**requestTag** | **String** | A per-request tag which can be applied to queries or reads, used for statistics collection. Both request_tag and transaction_tag can be specified for a read or query that belongs to a transaction. This field is ignored for requests where it&#39;s not applicable (e.g. CommitRequest). Legal characters for &#x60;request_tag&#x60; values are all printable characters (ASCII 32 - 126) and the length of a request_tag is limited to 50 characters. Values that exceed this limit are truncated. Any leading underscore (_) characters will be removed from the string. | [optional] 
**transactionTag** | **String** | A tag used for statistics collection about this transaction. Both request_tag and transaction_tag can be specified for a read or query that belongs to a transaction. The value of transaction_tag should be the same for all requests belonging to the same transaction. If this request doesn&#39;t belong to any transaction, transaction_tag will be ignored. Legal characters for &#x60;transaction_tag&#x60; values are all printable characters (ASCII 32 - 126) and the length of a transaction_tag is limited to 50 characters. Values that exceed this limit are truncated. Any leading underscore (_) characters will be removed from the string. | [optional] 



## Enum: PriorityEnum


* `UNSPECIFIED` (value: `"PRIORITY_UNSPECIFIED"`)

* `LOW` (value: `"PRIORITY_LOW"`)

* `MEDIUM` (value: `"PRIORITY_MEDIUM"`)

* `HIGH` (value: `"PRIORITY_HIGH"`)




