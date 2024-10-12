# GeographicApi.EventsApi

All URIs are relative to *http://api.nytimes.com/svc/semantic/v2/geocodes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryJsonGet**](EventsApi.md#queryJsonGet) | **GET** /query.json | Geographic API



## queryJsonGet

> QueryJsonGet200Response queryJsonGet(opts)

Geographic API

Geographic API

### Example

```javascript
import GeographicApi from 'geographic_api';
let defaultClient = GeographicApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GeographicApi.EventsApi();
let opts = {
  'name': "name_example", // String | A displayable name for the specified place.
  'latitude': "latitude_example", // String | The latitude of the specified place. 
  'longitude': "longitude_example", // String | The longitude of the specified place.
  'elevation': 56, // Number | The elevation of the specified place, in meters.
  'sw': "sw_example", // String | Along with ne, forms a bounded box using the longitude and latitude coordinates specified as the southwest corner. The search results are limited to the resulting box. Two float values, separated by a comma `latitude,longitude` <br/> The ne parameter is required to use this parameter.
  'query': "query_example", // String | Search keywords to perform a text search on the fields: web_description, event_name and venue_name. 'AND' searches can be performed by wrapping query terms in quotes. If you do not specify a query, all results will be returned. 
  'filter': "filter_example", // String | Filters search results based on the facets provided.  For more information on the values you can filter on, see Facets. 
  'dateRange': "dateRange_example", // String | Start date to end date in the following format- YYYY-MM-DD:YYYY-MM-DD
  'facets': 0, // Number | When facets is set to 1, a count of all facets will be included in the response.
  'sort': "sort_example", // String | Sorts your results on the fields specified. <br/> `sort_value1+[asc | desc],sort_value2+[asc|desc],[...]`<br/> Appending +asc to a facet or response will sort results on that value in ascending order. Appending +desc to a facet or response  will sort results in descending order. You can sort on multiple fields. You can sort on any facet. For the list of responses you can sort on, see the Sortable Field column in the Response table. <br/><br/>If you are doing a spatial search with the ll parameter, you can also sort by the distance from the center of the search: dist+[asc | desc] <br/> **Note:** either +asc or +desc is required when using the sort parameter. 
  'limit': 20, // Number | Limits the number of results returned
  'offset': 0 // Number | Sets the starting point of the result set
};
apiInstance.queryJsonGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| A displayable name for the specified place. | [optional] 
 **latitude** | **String**| The latitude of the specified place.  | [optional] 
 **longitude** | **String**| The longitude of the specified place. | [optional] 
 **elevation** | **Number**| The elevation of the specified place, in meters. | [optional] 
 **sw** | **String**| Along with ne, forms a bounded box using the longitude and latitude coordinates specified as the southwest corner. The search results are limited to the resulting box. Two float values, separated by a comma &#x60;latitude,longitude&#x60; &lt;br/&gt; The ne parameter is required to use this parameter. | [optional] 
 **query** | **String**| Search keywords to perform a text search on the fields: web_description, event_name and venue_name. &#39;AND&#39; searches can be performed by wrapping query terms in quotes. If you do not specify a query, all results will be returned.  | [optional] 
 **filter** | **String**| Filters search results based on the facets provided.  For more information on the values you can filter on, see Facets.  | [optional] 
 **dateRange** | **String**| Start date to end date in the following format- YYYY-MM-DD:YYYY-MM-DD | [optional] 
 **facets** | **Number**| When facets is set to 1, a count of all facets will be included in the response. | [optional] [default to 0]
 **sort** | **String**| Sorts your results on the fields specified. &lt;br/&gt; &#x60;sort_value1+[asc | desc],sort_value2+[asc|desc],[...]&#x60;&lt;br/&gt; Appending +asc to a facet or response will sort results on that value in ascending order. Appending +desc to a facet or response  will sort results in descending order. You can sort on multiple fields. You can sort on any facet. For the list of responses you can sort on, see the Sortable Field column in the Response table. &lt;br/&gt;&lt;br/&gt;If you are doing a spatial search with the ll parameter, you can also sort by the distance from the center of the search: dist+[asc | desc] &lt;br/&gt; **Note:** either +asc or +desc is required when using the sort parameter.  | [optional] 
 **limit** | **Number**| Limits the number of results returned | [optional] [default to 20]
 **offset** | **Number**| Sets the starting point of the result set | [optional] [default to 0]

### Return type

[**QueryJsonGet200Response**](QueryJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

