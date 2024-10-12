# PricingApi

All URIs are relative to *https://gateway.seven.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pricing**](PricingApi.md#pricing) | **GET** /pricing |  |


<a id="pricing"></a>
# **pricing**
> pricing(country, format)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String country = "country_example"; // String | The countries ISO code to get pricings for. Allowed values are de, fr, at. Omit to show pricings for all channels.
    String format = "format_example"; // String | Determines the response format. Allowed values are json and csv. The default value is json.
    try {
      apiInstance.pricing(country, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricing");
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
| **country** | **String**| The countries ISO code to get pricings for. Allowed values are de, fr, at. Omit to show pricings for all channels. | [optional] |
| **format** | **String**| Determines the response format. Allowed values are json and csv. The default value is json. | [optional] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

