# MetadataApi

All URIs are relative to *https://mermade.org.uk/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStatus**](MetadataApi.md#getStatus) | **GET** /status | Get the status of the API |


<a id="getStatus"></a>
# **getStatus**
> Object getStatus()

Get the status of the API



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mermade.org.uk/api/v1");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    try {
      Object result = apiInstance.getStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#getStatus");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | default |  -  |

