# EventsApi

All URIs are relative to *https://api2.lotadata.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsGet**](EventsApi.md#eventsGet) | **GET** /events | Find event occurrences in the area. Returns results at specific place and time, event groups are expanded for every occurrence. |
| [**eventsIdGet**](EventsApi.md#eventsIdGet) | **GET** /events/{id} | Get Specific event details. |


<a id="eventsGet"></a>
# **eventsGet**
> EventsSearchResponse eventsGet(fieldset, category, activity, ambience, genre, name, q, fromDay, toDay, capacityMin, capacityMax, center, radius, bbox, polygon, within, offset, limit)

Find event occurrences in the area. Returns results at specific place and time, event groups are expanded for every occurrence.

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
    defaultClient.setBasePath("https://api2.lotadata.com/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String fieldset = "summary"; // String | Return results starting at specified offset (summary, context, detail)
    List<String> category = Arrays.asList(); // List<String> | List of required EventCategory ids (Tier 1)
    String activity = "activity_example"; // String | List of required activity type ids (compliment to category)
    String ambience = "ambience_example"; // String | List of required ambience ids
    String genre = "genre_example"; // String | List of required genre ids
    String name = "name_example"; // String | Matching on event and place names
    String q = "q_example"; // String | Text query matching titles, description, various text, tags, category
    String fromDay = "fromDay_example"; // String | Start on or after date specified (2015-10-16)
    String toDay = "toDay_example"; // String | Start on or before date specified (2015-10-16)
    BigDecimal capacityMin = new BigDecimal(78); // BigDecimal | Min capacity at location
    BigDecimal capacityMax = new BigDecimal(78); // BigDecimal | Min capacity at location
    String center = "center_example"; // String | latitude,longitude of the origin point
    Integer radius = 56; // Integer | Distance from origin in meters
    List<String> bbox = Arrays.asList(); // List<String> | Corner of a bounding box (lat,lng). Requires 0 or 2 pairs
    List<String> polygon = Arrays.asList(); // List<String> | Closed custom polygon. Ordered list of lat,lng pairs
    String within = "within_example"; // String | Search within specified geopolitical place id
    Integer offset = 56; // Integer | Return results starting at specified offset
    Integer limit = 56; // Integer | Max results to return
    try {
      EventsSearchResponse result = apiInstance.eventsGet(fieldset, category, activity, ambience, genre, name, q, fromDay, toDay, capacityMin, capacityMax, center, radius, bbox, polygon, within, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsGet");
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
| **fieldset** | **String**| Return results starting at specified offset (summary, context, detail) | [default to context] [enum: summary, detail, context, minicontext] |
| **category** | [**List&lt;String&gt;**](String.md)| List of required EventCategory ids (Tier 1) | [optional] |
| **activity** | **String**| List of required activity type ids (compliment to category) | [optional] |
| **ambience** | **String**| List of required ambience ids | [optional] |
| **genre** | **String**| List of required genre ids | [optional] |
| **name** | **String**| Matching on event and place names | [optional] |
| **q** | **String**| Text query matching titles, description, various text, tags, category | [optional] |
| **fromDay** | **String**| Start on or after date specified (2015-10-16) | [optional] |
| **toDay** | **String**| Start on or before date specified (2015-10-16) | [optional] |
| **capacityMin** | **BigDecimal**| Min capacity at location | [optional] |
| **capacityMax** | **BigDecimal**| Min capacity at location | [optional] |
| **center** | **String**| latitude,longitude of the origin point | [optional] |
| **radius** | **Integer**| Distance from origin in meters | [optional] |
| **bbox** | [**List&lt;String&gt;**](String.md)| Corner of a bounding box (lat,lng). Requires 0 or 2 pairs | [optional] |
| **polygon** | [**List&lt;String&gt;**](String.md)| Closed custom polygon. Ordered list of lat,lng pairs | [optional] |
| **within** | **String**| Search within specified geopolitical place id | [optional] |
| **offset** | **Integer**| Return results starting at specified offset | [optional] |
| **limit** | **Integer**| Max results to return | [optional] |

### Return type

[**EventsSearchResponse**](EventsSearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of matching events |  -  |
| **400** | Unexpected error |  -  |

<a id="eventsIdGet"></a>
# **eventsIdGet**
> EventOccurenceDetail eventsIdGet(id, fieldset)

Get Specific event details.

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
    defaultClient.setBasePath("https://api2.lotadata.com/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String id = "id_example"; // String | event @id
    String fieldset = "summary"; // String | 
    try {
      EventOccurenceDetail result = apiInstance.eventsIdGet(id, fieldset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsIdGet");
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
| **id** | **String**| event @id | |
| **fieldset** | **String**|  | [optional] [default to summary] [enum: summary, detail, context, minicontext] |

### Return type

[**EventOccurenceDetail**](EventOccurenceDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested event |  -  |
| **404** | Unexpected error |  -  |

