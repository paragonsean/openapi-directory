

# QueryContext

Defines the query context that Bing used for the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** |  |  |
|**adultIntent** | **Boolean** | A Boolean value that indicates whether the specified query has adult intent. The value is true if the query has adult intent; otherwise, false. |  [optional] [readonly] |
|**alterationOverrideQuery** | **String** | The query string to use to force Bing to use the original string. For example, if the query string is \&quot;saling downwind\&quot;, the override query string will be \&quot;+saling downwind\&quot;. Remember to encode the query string which results in \&quot;%2Bsaling+downwind\&quot;. This field is included only if the original query string contains a spelling mistake. |  [optional] [readonly] |
|**alteredQuery** | **String** | The query string used by Bing to perform the query. Bing uses the altered query string if the original query string contained spelling mistakes. For example, if the query string is \&quot;saling downwind\&quot;, the altered query string will be \&quot;sailing downwind\&quot;. This field is included only if the original query string contains a spelling mistake. |  [optional] [readonly] |
|**askUserForLocation** | **Boolean** | A Boolean value that indicates whether Bing requires the user&#39;s location to provide accurate results. If you specified the user&#39;s location by using the X-MSEdge-ClientIP and X-Search-Location headers, you can ignore this field. For location aware queries, such as \&quot;today&#39;s weather\&quot; or \&quot;restaurants near me\&quot; that need the user&#39;s location to provide accurate results, this field is set to true. For location aware queries that include the location (for example, \&quot;Seattle weather\&quot;), this field is set to false. This field is also set to false for queries that are not location aware, such as \&quot;best sellers\&quot;. |  [optional] [readonly] |
|**isTransactional** | **Boolean** |  |  [optional] [readonly] |
|**originalQuery** | **String** | The query string as specified in the request. |  |



