# VeteranConfirmationStatusApi

All URIs are relative to *https://sandbox-api.va.gov/services/veteran_confirmation/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVeteranStatus**](VeteranConfirmationStatusApi.md#getVeteranStatus) | **POST** /status | Get confirmation about an individual&#39;s Veteran status according to the VA |


<a id="getVeteranStatus"></a>
# **getVeteranStatus**
> VeteranStatusConfirmation getVeteranStatus(veteranStatusRequest)

Get confirmation about an individual&#39;s Veteran status according to the VA

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VeteranConfirmationStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/veteran_confirmation/v0");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    VeteranConfirmationStatusApi apiInstance = new VeteranConfirmationStatusApi(defaultClient);
    VeteranStatusRequest veteranStatusRequest = new VeteranStatusRequest(); // VeteranStatusRequest | 
    try {
      VeteranStatusConfirmation result = apiInstance.getVeteranStatus(veteranStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VeteranConfirmationStatusApi#getVeteranStatus");
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
| **veteranStatusRequest** | [**VeteranStatusRequest**](VeteranStatusRequest.md)|  | |

### Return type

[**VeteranStatusConfirmation**](VeteranStatusConfirmation.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Confirmation status successfully retrieved |  -  |
| **400** | Bad request - invalid or missing query parameters |  -  |
| **401** | Missing API token |  -  |
| **403** | Invalid API token |  -  |
| **503** | We encountered a temporary error. Check back in the future. |  -  |

