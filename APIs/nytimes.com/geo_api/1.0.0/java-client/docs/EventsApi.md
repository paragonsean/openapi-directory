# EventsApi

All URIs are relative to *http://api.nytimes.com/svc/semantic/v2/geocodes*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryJsonGet**](EventsApi.md#queryJsonGet) | **GET** /query.json | Geographic API |


<a id="queryJsonGet"></a>
# **queryJsonGet**
> QueryJsonGet200Response queryJsonGet(name, latitude, longitude, elevation, sw, query, filter, dateRange, facets, sort, limit, offset)

Geographic API

Geographic API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/semantic/v2/geocodes");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String name = "name_example"; // String | A displayable name for the specified place.
    String latitude = "latitude_example"; // String | The latitude of the specified place. 
    String longitude = "longitude_example"; // String | The longitude of the specified place.
    Integer elevation = 56; // Integer | The elevation of the specified place, in meters.
    String sw = "sw_example"; // String | Along with ne, forms a bounded box using the longitude and latitude coordinates specified as the southwest corner. The search results are limited to the resulting box. Two float values, separated by a comma `latitude,longitude` <br/> The ne parameter is required to use this parameter.
    String query = "query_example"; // String | Search keywords to perform a text search on the fields: web_description, event_name and venue_name. 'AND' searches can be performed by wrapping query terms in quotes. If you do not specify a query, all results will be returned. 
    String filter = "filter_example"; // String | Filters search results based on the facets provided.  For more information on the values you can filter on, see Facets. 
    String dateRange = "dateRange_example"; // String | Start date to end date in the following format- YYYY-MM-DD:YYYY-MM-DD
    Integer facets = 0; // Integer | When facets is set to 1, a count of all facets will be included in the response.
    String sort = "sort_example"; // String | Sorts your results on the fields specified. <br/> `sort_value1+[asc | desc],sort_value2+[asc|desc],[...]`<br/> Appending +asc to a facet or response will sort results on that value in ascending order. Appending +desc to a facet or response  will sort results in descending order. You can sort on multiple fields. You can sort on any facet. For the list of responses you can sort on, see the Sortable Field column in the Response table. <br/><br/>If you are doing a spatial search with the ll parameter, you can also sort by the distance from the center of the search: dist+[asc | desc] <br/> **Note:** either +asc or +desc is required when using the sort parameter. 
    Integer limit = 20; // Integer | Limits the number of results returned
    Integer offset = 0; // Integer | Sets the starting point of the result set
    try {
      QueryJsonGet200Response result = apiInstance.queryJsonGet(name, latitude, longitude, elevation, sw, query, filter, dateRange, facets, sort, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#queryJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| A displayable name for the specified place. | [optional] |
| **latitude** | **String**| The latitude of the specified place.  | [optional] |
| **longitude** | **String**| The longitude of the specified place. | [optional] |
| **elevation** | **Integer**| The elevation of the specified place, in meters. | [optional] |
| **sw** | **String**| Along with ne, forms a bounded box using the longitude and latitude coordinates specified as the southwest corner. The search results are limited to the resulting box. Two float values, separated by a comma &#x60;latitude,longitude&#x60; &lt;br/&gt; The ne parameter is required to use this parameter. | [optional] |
| **query** | **String**| Search keywords to perform a text search on the fields: web_description, event_name and venue_name. &#39;AND&#39; searches can be performed by wrapping query terms in quotes. If you do not specify a query, all results will be returned.  | [optional] |
| **filter** | **String**| Filters search results based on the facets provided.  For more information on the values you can filter on, see Facets.  | [optional] |
| **dateRange** | **String**| Start date to end date in the following format- YYYY-MM-DD:YYYY-MM-DD | [optional] |
| **facets** | **Integer**| When facets is set to 1, a count of all facets will be included in the response. | [optional] [default to 0] [enum: 0, 1] |
| **sort** | **String**| Sorts your results on the fields specified. &lt;br/&gt; &#x60;sort_value1+[asc | desc],sort_value2+[asc|desc],[...]&#x60;&lt;br/&gt; Appending +asc to a facet or response will sort results on that value in ascending order. Appending +desc to a facet or response  will sort results in descending order. You can sort on multiple fields. You can sort on any facet. For the list of responses you can sort on, see the Sortable Field column in the Response table. &lt;br/&gt;&lt;br/&gt;If you are doing a spatial search with the ll parameter, you can also sort by the distance from the center of the search: dist+[asc | desc] &lt;br/&gt; **Note:** either +asc or +desc is required when using the sort parameter.  | [optional] |
| **limit** | **Integer**| Limits the number of results returned | [optional] [default to 20] |
| **offset** | **Integer**| Sets the starting point of the result set | [optional] [default to 0] |

### Return type

[**QueryJsonGet200Response**](QueryJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of events |  -  |

