# EndpointKeysApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**endpointKeysRefreshKeys**](EndpointKeysApi.md#endpointKeysRefreshKeys) | **PATCH** /endpointkeys/{keyType} | Re-generates an endpoint key. |
| [**endpointSettingsUpdateSettings**](EndpointKeysApi.md#endpointSettingsUpdateSettings) | **PATCH** /endpointSettings | Updates endpoint settings for an endpoint. |


<a id="endpointKeysRefreshKeys"></a>
# **endpointKeysRefreshKeys**
> EndpointKeysDTO endpointKeysRefreshKeys(keyType)

Re-generates an endpoint key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    EndpointKeysApi apiInstance = new EndpointKeysApi(defaultClient);
    String keyType = "keyType_example"; // String | Type of Key
    try {
      EndpointKeysDTO result = apiInstance.endpointKeysRefreshKeys(keyType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointKeysApi#endpointKeysRefreshKeys");
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
| **keyType** | **String**| Type of Key | |

### Return type

[**EndpointKeysDTO**](EndpointKeysDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the endpoint keys generated. |  -  |
| **0** | Error response. |  -  |

<a id="endpointSettingsUpdateSettings"></a>
# **endpointSettingsUpdateSettings**
> String endpointSettingsUpdateSettings(endpointSettingsPayload)

Updates endpoint settings for an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    EndpointKeysApi apiInstance = new EndpointKeysApi(defaultClient);
    EndpointSettingsDTO endpointSettingsPayload = new EndpointSettingsDTO(); // EndpointSettingsDTO | Post body of the request.
    try {
      String result = apiInstance.endpointSettingsUpdateSettings(endpointSettingsPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointKeysApi#endpointSettingsUpdateSettings");
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
| **endpointSettingsPayload** | [**EndpointSettingsDTO**](EndpointSettingsDTO.md)| Post body of the request. | |

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response with endpointSettings update status. |  -  |
| **0** | Error response. |  -  |

