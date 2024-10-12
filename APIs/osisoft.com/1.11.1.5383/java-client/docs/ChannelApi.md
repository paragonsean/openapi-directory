# ChannelApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**channelInstances**](ChannelApi.md#channelInstances) | **GET** /channels/instances | Retrieves a list of currently running channel instances. |


<a id="channelInstances"></a>
# **channelInstances**
> ItemsChannelInstance channelInstances()

Retrieves a list of currently running channel instances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    ChannelApi apiInstance = new ChannelApi(defaultClient);
    try {
      ItemsChannelInstance result = apiInstance.channelInstances();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelApi#channelInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ItemsChannelInstance**](ItemsChannelInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of currently running channel instances. |  -  |

