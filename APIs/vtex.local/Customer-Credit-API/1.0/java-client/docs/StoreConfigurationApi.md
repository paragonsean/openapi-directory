# StoreConfigurationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createorchangestoreconfiguration**](StoreConfigurationApi.md#createorchangestoreconfiguration) | **PUT** /api/creditcontrol/storeconfig | Create or change store configuration |
| [**retrievestoreconfiguration**](StoreConfigurationApi.md#retrievestoreconfiguration) | **GET** /api/creditcontrol/storeconfig | Retrieve store configuration |


<a id="createorchangestoreconfiguration"></a>
# **createorchangestoreconfiguration**
> Savestoreconfig1 createorchangestoreconfiguration(accept, contentType, createorchangestoreconfigurationRequest1)

Create or change store configuration

Create or change store configuration data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoreConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    StoreConfigurationApi apiInstance = new StoreConfigurationApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    CreateorchangestoreconfigurationRequest1 createorchangestoreconfigurationRequest1 = new CreateorchangestoreconfigurationRequest1(); // CreateorchangestoreconfigurationRequest1 | 
    try {
      Savestoreconfig1 result = apiInstance.createorchangestoreconfiguration(accept, contentType, createorchangestoreconfigurationRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoreConfigurationApi#createorchangestoreconfiguration");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **createorchangestoreconfigurationRequest1** | [**CreateorchangestoreconfigurationRequest1**](CreateorchangestoreconfigurationRequest1.md)|  | |

### Return type

[**Savestoreconfig1**](Savestoreconfig1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="retrievestoreconfiguration"></a>
# **retrievestoreconfiguration**
> Storeconfig1 retrievestoreconfiguration(contentType, accept)

Retrieve store configuration

Get store configuration data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoreConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    StoreConfigurationApi apiInstance = new StoreConfigurationApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    try {
      Storeconfig1 result = apiInstance.retrievestoreconfiguration(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoreConfigurationApi#retrievestoreconfiguration");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |

### Return type

[**Storeconfig1**](Storeconfig1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

