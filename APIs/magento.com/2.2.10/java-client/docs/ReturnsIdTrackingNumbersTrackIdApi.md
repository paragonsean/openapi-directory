# ReturnsIdTrackingNumbersTrackIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaTrackManagementV1RemoveTrackByIdDelete**](ReturnsIdTrackingNumbersTrackIdApi.md#rmaTrackManagementV1RemoveTrackByIdDelete) | **DELETE** /V1/returns/{id}/tracking-numbers/{trackId} | returns/{id}/tracking-numbers/{trackId} |


<a id="rmaTrackManagementV1RemoveTrackByIdDelete"></a>
# **rmaTrackManagementV1RemoveTrackByIdDelete**
> Boolean rmaTrackManagementV1RemoveTrackByIdDelete(id, trackId)

returns/{id}/tracking-numbers/{trackId}

Remove track by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdTrackingNumbersTrackIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdTrackingNumbersTrackIdApi apiInstance = new ReturnsIdTrackingNumbersTrackIdApi(defaultClient);
    Integer id = 56; // Integer | 
    Integer trackId = 56; // Integer | 
    try {
      Boolean result = apiInstance.rmaTrackManagementV1RemoveTrackByIdDelete(id, trackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdTrackingNumbersTrackIdApi#rmaTrackManagementV1RemoveTrackByIdDelete");
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
| **id** | **Integer**|  | |
| **trackId** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

