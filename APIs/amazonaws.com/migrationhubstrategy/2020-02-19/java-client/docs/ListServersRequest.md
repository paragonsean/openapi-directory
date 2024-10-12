

# ListServersRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterValue** | **String** |  Specifies the filter value, which is based on the type of server criteria. For example, if &lt;code&gt;serverCriteria&lt;/code&gt; is &lt;code&gt;OS_NAME&lt;/code&gt;, and the &lt;code&gt;filterValue&lt;/code&gt; is equal to &lt;code&gt;WindowsServer&lt;/code&gt;, then &lt;code&gt;ListServers&lt;/code&gt; returns all of the servers matching the OS name &lt;code&gt;WindowsServer&lt;/code&gt;.  |  [optional] |
|**groupIdFilter** | [**List&lt;Group&gt;**](Group.md) |  Specifies the group ID to filter on.  |  [optional] |
|**maxResults** | **Integer** |  The maximum number of items to include in the response. The maximum value is 100.  |  [optional] |
|**nextToken** | **String** |  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set &lt;code&gt;maxResults&lt;/code&gt; to 10. You&#39;ll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.  |  [optional] |
|**serverCriteria** | [**ServerCriteriaEnum**](#ServerCriteriaEnum) |  Criteria for filtering servers.  |  [optional] |
|**sort** | [**SortEnum**](#SortEnum) |  Specifies whether to sort by ascending (&lt;code&gt;ASC&lt;/code&gt;) or descending (&lt;code&gt;DESC&lt;/code&gt;) order.  |  [optional] |



## Enum: ServerCriteriaEnum

| Name | Value |
|---- | -----|
| NOT_DEFINED | &quot;NOT_DEFINED&quot; |
| OS_NAME | &quot;OS_NAME&quot; |
| STRATEGY | &quot;STRATEGY&quot; |
| DESTINATION | &quot;DESTINATION&quot; |
| SERVER_ID | &quot;SERVER_ID&quot; |
| ANALYSIS_STATUS | &quot;ANALYSIS_STATUS&quot; |
| ERROR_CATEGORY | &quot;ERROR_CATEGORY&quot; |



## Enum: SortEnum

| Name | Value |
|---- | -----|
| ASC | &quot;ASC&quot; |
| DESC | &quot;DESC&quot; |



