# RequestTagApi

All URIs are relative to *https://api.nasa.gov/planetary*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apodGet**](RequestTagApi.md#apodGet) | **GET** /apod | Returns images |


<a id="apodGet"></a>
# **apodGet**
> List&lt;Object&gt; apodGet(date, hd)

Returns images

Returns the picture of the day

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestTagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nasa.gov/planetary");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RequestTagApi apiInstance = new RequestTagApi(defaultClient);
    String date = "date_example"; // String | The date of the APOD image to retrieve
    Boolean hd = true; // Boolean | Retrieve the URL for the high resolution image
    try {
      List<Object> result = apiInstance.apodGet(date, hd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestTagApi#apodGet");
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
| **date** | **String**| The date of the APOD image to retrieve | [optional] |
| **hd** | **Boolean**| Retrieve the URL for the high resolution image | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Date must be between Jun 16, 1995 and Mar 28, 2019. |  -  |

