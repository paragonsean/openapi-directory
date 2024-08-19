# CustomSearchClient.QueryContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adultIntent** | **Boolean** | A Boolean value that indicates whether the specified query has adult intent. The value is true if the query has adult intent; otherwise, false. | [optional] [readonly] 
**alterationOverrideQuery** | **String** | The query string to use to force Bing to use the original string. For example, if the query string is \&quot;saling downwind\&quot;, the override query string will be \&quot;+saling downwind\&quot;. Remember to encode the query string which results in \&quot;%2Bsaling+downwind\&quot;. This field is included only if the original query string contains a spelling mistake. | [optional] [readonly] 
**alteredQuery** | **String** | The query string used by Bing to perform the query. Bing uses the altered query string if the original query string contained spelling mistakes. For example, if the query string is \&quot;saling downwind\&quot;, the altered query string will be \&quot;sailing downwind\&quot;. This field is included only if the original query string contains a spelling mistake. | [optional] [readonly] 
**originalQuery** | **String** | The query string as specified in the request. | 


