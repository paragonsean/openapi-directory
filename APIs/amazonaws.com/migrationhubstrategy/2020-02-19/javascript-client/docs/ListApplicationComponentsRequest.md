# MigrationHubStrategyRecommendations.ListApplicationComponentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationComponentCriteria** | **String** |  Criteria for filtering the list of application components.  | [optional] 
**filterValue** | **String** |  Specify the value based on the application component criteria type. For example, if &lt;code&gt;applicationComponentCriteria&lt;/code&gt; is set to &lt;code&gt;SERVER_ID&lt;/code&gt; and &lt;code&gt;filterValue&lt;/code&gt; is set to &lt;code&gt;server1&lt;/code&gt;, then &lt;a&gt;ListApplicationComponents&lt;/a&gt; returns all the application components running on server1.  | [optional] 
**groupIdFilter** | [**[Group]**](Group.md) |  The group ID specified in to filter on.  | [optional] 
**maxResults** | **Number** |  The maximum number of items to include in the response. The maximum value is 100.  | [optional] 
**nextToken** | **String** |  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set &lt;code&gt;maxResults&lt;/code&gt; to 10. You&#39;ll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.  | [optional] 
**sort** | **String** |  Specifies whether to sort by ascending (&lt;code&gt;ASC&lt;/code&gt;) or descending (&lt;code&gt;DESC&lt;/code&gt;) order.  | [optional] 



## Enum: ApplicationComponentCriteriaEnum


* `NOT_DEFINED` (value: `"NOT_DEFINED"`)

* `APP_NAME` (value: `"APP_NAME"`)

* `SERVER_ID` (value: `"SERVER_ID"`)

* `APP_TYPE` (value: `"APP_TYPE"`)

* `STRATEGY` (value: `"STRATEGY"`)

* `DESTINATION` (value: `"DESTINATION"`)

* `ANALYSIS_STATUS` (value: `"ANALYSIS_STATUS"`)

* `ERROR_CATEGORY` (value: `"ERROR_CATEGORY"`)





## Enum: SortEnum


* `ASC` (value: `"ASC"`)

* `DESC` (value: `"DESC"`)




