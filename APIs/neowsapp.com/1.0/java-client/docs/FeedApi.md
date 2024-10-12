# FeedApi

All URIs are relative to *http://www.neowsapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveNEOFeedToday**](FeedApi.md#retrieveNEOFeedToday) | **GET** /rest/v1/feed/today | Find Near Earth Objects for today |
| [**retrieveNearEarthObjectFeed**](FeedApi.md#retrieveNearEarthObjectFeed) | **GET** /rest/v1/feed | Find Near Earth Objects by date |


<a id="retrieveNEOFeedToday"></a>
# **retrieveNEOFeedToday**
> NearEarthObjectList retrieveNEOFeedToday(detailed)

Find Near Earth Objects for today

Get a list of Near Earth Objects for today

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.neowsapp.com");

    FeedApi apiInstance = new FeedApi(defaultClient);
    Boolean detailed = true; // Boolean | detailed
    try {
      NearEarthObjectList result = apiInstance.retrieveNEOFeedToday(detailed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedApi#retrieveNEOFeedToday");
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
| **detailed** | **Boolean**| detailed | [optional] |

### Return type

[**NearEarthObjectList**](NearEarthObjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="retrieveNearEarthObjectFeed"></a>
# **retrieveNearEarthObjectFeed**
> NearEarthObjectList retrieveNearEarthObjectFeed(startDate, endDate, detailed)

Find Near Earth Objects by date

Get a list of Near Earth Objects within a date range, The max range in one query is 7 days

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.neowsapp.com");

    FeedApi apiInstance = new FeedApi(defaultClient);
    String startDate = "startDate_example"; // String | Start of date range search, format: yyyy-MM-dd - (ex: 2015-04-28)
    String endDate = "endDate_example"; // String | End of date range search, format: yyyy-MM-dd - (ex: 2015-04-28). If left off search will extends 7 days from start_date
    Boolean detailed = true; // Boolean | detailed
    try {
      NearEarthObjectList result = apiInstance.retrieveNearEarthObjectFeed(startDate, endDate, detailed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedApi#retrieveNearEarthObjectFeed");
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
| **startDate** | **String**| Start of date range search, format: yyyy-MM-dd - (ex: 2015-04-28) | [optional] |
| **endDate** | **String**| End of date range search, format: yyyy-MM-dd - (ex: 2015-04-28). If left off search will extends 7 days from start_date | [optional] |
| **detailed** | **Boolean**| detailed | [optional] |

### Return type

[**NearEarthObjectList**](NearEarthObjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

