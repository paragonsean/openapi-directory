

# ListApplicationComponentsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationComponentCriteria** | [**ApplicationComponentCriteriaEnum**](#ApplicationComponentCriteriaEnum) |  Criteria for filtering the list of application components.  |  [optional] |
|**filterValue** | **String** |  Specify the value based on the application component criteria type. For example, if &lt;code&gt;applicationComponentCriteria&lt;/code&gt; is set to &lt;code&gt;SERVER_ID&lt;/code&gt; and &lt;code&gt;filterValue&lt;/code&gt; is set to &lt;code&gt;server1&lt;/code&gt;, then &lt;a&gt;ListApplicationComponents&lt;/a&gt; returns all the application components running on server1.  |  [optional] |
|**groupIdFilter** | [**List&lt;Group&gt;**](Group.md) |  The group ID specified in to filter on.  |  [optional] |
|**maxResults** | **Integer** |  The maximum number of items to include in the response. The maximum value is 100.  |  [optional] |
|**nextToken** | **String** |  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set &lt;code&gt;maxResults&lt;/code&gt; to 10. You&#39;ll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.  |  [optional] |
|**sort** | [**SortEnum**](#SortEnum) |  Specifies whether to sort by ascending (&lt;code&gt;ASC&lt;/code&gt;) or descending (&lt;code&gt;DESC&lt;/code&gt;) order.  |  [optional] |



## Enum: ApplicationComponentCriteriaEnum

| Name | Value |
|---- | -----|
| NOT_DEFINED | &quot;NOT_DEFINED&quot; |
| APP_NAME | &quot;APP_NAME&quot; |
| SERVER_ID | &quot;SERVER_ID&quot; |
| APP_TYPE | &quot;APP_TYPE&quot; |
| STRATEGY | &quot;STRATEGY&quot; |
| DESTINATION | &quot;DESTINATION&quot; |
| ANALYSIS_STATUS | &quot;ANALYSIS_STATUS&quot; |
| ERROR_CATEGORY | &quot;ERROR_CATEGORY&quot; |



## Enum: SortEnum

| Name | Value |
|---- | -----|
| ASC | &quot;ASC&quot; |
| DESC | &quot;DESC&quot; |



