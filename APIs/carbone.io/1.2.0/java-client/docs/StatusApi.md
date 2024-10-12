# StatusApi

All URIs are relative to *https://api.carbone.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statusGet**](StatusApi.md#statusGet) | **GET** /status | Fetch the API status and version |


<a id="statusGet"></a>
# **statusGet**
> StatusGet200Response statusGet()

Fetch the API status and version

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
    defaultClient.setBasePath("https://api.carbone.io");

    StatusApi apiInstance = new StatusApi(defaultClient);
    try {
      StatusGet200Response result = apiInstance.statusGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#statusGet");
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

[**StatusGet200Response**](StatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check the API status and version |  -  |
| **500** | Something went wrong, contact support on the chat |  -  |

