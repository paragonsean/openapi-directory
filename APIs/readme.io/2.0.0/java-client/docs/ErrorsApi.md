# ErrorsApi

All URIs are relative to *https://dash.readme.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getErrors**](ErrorsApi.md#getErrors) | **GET** /errors | Get errors |


<a id="getErrors"></a>
# **getErrors**
> getErrors()

Get errors

Returns with all of the error page types for this project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    try {
      apiInstance.getErrors();
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#getErrors");
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

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of the errors |  -  |

