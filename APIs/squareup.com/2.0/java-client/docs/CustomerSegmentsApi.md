# CustomerSegmentsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listCustomerSegments**](CustomerSegmentsApi.md#listCustomerSegments) | **GET** /v2/customers/segments | ListCustomerSegments |
| [**retrieveCustomerSegment**](CustomerSegmentsApi.md#retrieveCustomerSegment) | **GET** /v2/customers/segments/{segment_id} | RetrieveCustomerSegment |


<a id="listCustomerSegments"></a>
# **listCustomerSegments**
> ListCustomerSegmentsResponse listCustomerSegments(cursor, limit)

ListCustomerSegments

Retrieves the list of customer segments of a business.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSegmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomerSegmentsApi apiInstance = new CustomerSegmentsApi(defaultClient);
    String cursor = "cursor_example"; // String | A pagination cursor returned by previous calls to `ListCustomerSegments`. This cursor is used to retrieve the next set of query results.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    Integer limit = 56; // Integer | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 50. The default value is 50.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    try {
      ListCustomerSegmentsResponse result = apiInstance.listCustomerSegments(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSegmentsApi#listCustomerSegments");
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
| **cursor** | **String**| A pagination cursor returned by previous calls to &#x60;ListCustomerSegments&#x60;. This cursor is used to retrieve the next set of query results.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] |
| **limit** | **Integer**| The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 50. The default value is 50.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] |

### Return type

[**ListCustomerSegmentsResponse**](ListCustomerSegmentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveCustomerSegment"></a>
# **retrieveCustomerSegment**
> RetrieveCustomerSegmentResponse retrieveCustomerSegment(segmentId)

RetrieveCustomerSegment

Retrieves a specific customer segment as identified by the &#x60;segment_id&#x60; value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSegmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomerSegmentsApi apiInstance = new CustomerSegmentsApi(defaultClient);
    String segmentId = "segmentId_example"; // String | The Square-issued ID of the customer segment.
    try {
      RetrieveCustomerSegmentResponse result = apiInstance.retrieveCustomerSegment(segmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSegmentsApi#retrieveCustomerSegment");
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
| **segmentId** | **String**| The Square-issued ID of the customer segment. | |

### Return type

[**RetrieveCustomerSegmentResponse**](RetrieveCustomerSegmentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

