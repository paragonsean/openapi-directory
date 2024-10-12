# PeerDetectionApi

All URIs are relative to *https://api.tokenjay.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPeersList**](PeerDetectionApi.md#getPeersList) | **GET** /peers/list | Lists known peers sorted by block height |


<a id="getPeersList"></a>
# **getPeersList**
> List&lt;NodePeer&gt; getPeersList(unreachable, closedApi, limit)

Lists known peers sorted by block height

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeerDetectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    PeerDetectionApi apiInstance = new PeerDetectionApi(defaultClient);
    Boolean unreachable = false; // Boolean | Set to true to show unreachable peers in the list
    Boolean closedApi = false; // Boolean | Set to true to show peers not open to be connected
    Integer limit = 50; // Integer | 
    try {
      List<NodePeer> result = apiInstance.getPeersList(unreachable, closedApi, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeerDetectionApi#getPeersList");
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
| **unreachable** | **Boolean**| Set to true to show unreachable peers in the list | [optional] [default to false] |
| **closedApi** | **Boolean**| Set to true to show peers not open to be connected | [optional] [default to false] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**List&lt;NodePeer&gt;**](NodePeer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

