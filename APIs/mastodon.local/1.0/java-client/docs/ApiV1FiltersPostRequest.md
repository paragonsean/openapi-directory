

# ApiV1FiltersPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | [**List&lt;ContextEnum&gt;**](#List&lt;ContextEnum&gt;) | Array of enumerable strings &#x60;home&#x60;, &#x60;notifications&#x60;, &#x60;public&#x60;, &#x60;thread&#x60;. At least one context must be specified. |  |
|**expiresIn** | **Integer** | Number of seconds from now the filter should expire. Otherwise, null for a filter that doesn&#39;t expire. |  [optional] |
|**irreversible** | **Boolean** | Should the server irreversibly drop matching entities from home and notifications? |  [optional] |
|**phrase** | **String** | Text to be filtered. |  |
|**wholeWord** | **Boolean** | Consider word boundaries? |  [optional] |



## Enum: List&lt;ContextEnum&gt;

| Name | Value |
|---- | -----|
| HOME | &quot;home&quot; |
| NOTIFICATIONS | &quot;notifications&quot; |
| PUBLIC | &quot;public&quot; |
| THREAD | &quot;thread&quot; |



