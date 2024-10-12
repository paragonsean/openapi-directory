# GeneralServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthCheck**](GeneralServicesApi.md#healthCheck) | **GET** /health/check | /health/check |


<a id="healthCheck"></a>
# **healthCheck**
> HealthCheck200Response healthCheck(acceptLanguage)

/health/check

Health check Use this service to determine whether the Viator API is presently online and that your API key is valid. You should receive a response identical to the example shown. If you have not yet received an API key, please request one from your business development partner. If you have not yet signed up as a Viator merchant partner and would like to, please visit our [distribution partner website](https://www.viator.com/distribution-partners?mcid&#x3D;58463#api-solutions).\&quot; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    GeneralServicesApi apiInstance = new GeneralServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    try {
      HealthCheck200Response result = apiInstance.healthCheck(acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralServicesApi#healthCheck");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |

### Return type

[**HealthCheck200Response**](HealthCheck200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

