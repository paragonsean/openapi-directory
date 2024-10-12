# StatusApi

All URIs are relative to *http://hashtag.peel-ci.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStatuses**](StatusApi.md#getStatuses) | **GET** /status/{showID} | Gets the last 100 statuses for this show. |


<a id="getStatuses"></a>
# **getStatuses**
> getStatuses(showID)

Gets the last 100 statuses for this show.

For Twitter, statuses are synonymous with tweets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://hashtag.peel-ci.com");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String showID = "showID_example"; // String | Unique ID for a show
    try {
      apiInstance.getStatuses(showID);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getStatuses");
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
| **showID** | **String**| Unique ID for a show | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

