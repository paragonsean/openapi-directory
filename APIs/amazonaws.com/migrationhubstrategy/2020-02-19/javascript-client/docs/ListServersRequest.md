# MigrationHubStrategyRecommendations.ListServersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterValue** | **String** |  Specifies the filter value, which is based on the type of server criteria. For example, if &lt;code&gt;serverCriteria&lt;/code&gt; is &lt;code&gt;OS_NAME&lt;/code&gt;, and the &lt;code&gt;filterValue&lt;/code&gt; is equal to &lt;code&gt;WindowsServer&lt;/code&gt;, then &lt;code&gt;ListServers&lt;/code&gt; returns all of the servers matching the OS name &lt;code&gt;WindowsServer&lt;/code&gt;.  | [optional] 
**groupIdFilter** | [**[Group]**](Group.md) |  Specifies the group ID to filter on.  | [optional] 
**maxResults** | **Number** |  The maximum number of items to include in the response. The maximum value is 100.  | [optional] 
**nextToken** | **String** |  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set &lt;code&gt;maxResults&lt;/code&gt; to 10. You&#39;ll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.  | [optional] 
**serverCriteria** | **String** |  Criteria for filtering servers.  | [optional] 
**sort** | **String** |  Specifies whether to sort by ascending (&lt;code&gt;ASC&lt;/code&gt;) or descending (&lt;code&gt;DESC&lt;/code&gt;) order.  | [optional] 



## Enum: ServerCriteriaEnum


* `NOT_DEFINED` (value: `"NOT_DEFINED"`)

* `OS_NAME` (value: `"OS_NAME"`)

* `STRATEGY` (value: `"STRATEGY"`)

* `DESTINATION` (value: `"DESTINATION"`)

* `SERVER_ID` (value: `"SERVER_ID"`)

* `ANALYSIS_STATUS` (value: `"ANALYSIS_STATUS"`)

* `ERROR_CATEGORY` (value: `"ERROR_CATEGORY"`)





## Enum: SortEnum


* `ASC` (value: `"ASC"`)

* `DESC` (value: `"DESC"`)




