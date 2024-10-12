# TerminalSettingsTerminalLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTerminalsTerminalIdTerminalLogos**](TerminalSettingsTerminalLevelApi.md#getTerminalsTerminalIdTerminalLogos) | **GET** /terminals/{terminalId}/terminalLogos | Get the terminal logo |
| [**getTerminalsTerminalIdTerminalSettings**](TerminalSettingsTerminalLevelApi.md#getTerminalsTerminalIdTerminalSettings) | **GET** /terminals/{terminalId}/terminalSettings | Get terminal settings |
| [**patchTerminalsTerminalIdTerminalLogos**](TerminalSettingsTerminalLevelApi.md#patchTerminalsTerminalIdTerminalLogos) | **PATCH** /terminals/{terminalId}/terminalLogos | Update the logo |
| [**patchTerminalsTerminalIdTerminalSettings**](TerminalSettingsTerminalLevelApi.md#patchTerminalsTerminalIdTerminalSettings) | **PATCH** /terminals/{terminalId}/terminalSettings | Update terminal settings |


<a id="getTerminalsTerminalIdTerminalLogos"></a>
# **getTerminalsTerminalIdTerminalLogos**
> Logo getTerminalsTerminalIdTerminalLogos(terminalId)

Get the terminal logo

Returns the logo that is configured for the payment terminal identified in the path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalSettingsTerminalLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalSettingsTerminalLevelApi apiInstance = new TerminalSettingsTerminalLevelApi(defaultClient);
    String terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
    try {
      Logo result = apiInstance.getTerminalsTerminalIdTerminalLogos(terminalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalSettingsTerminalLevelApi#getTerminalsTerminalIdTerminalLogos");
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
| **terminalId** | **String**| The unique identifier of the payment terminal. | |

### Return type

[**Logo**](Logo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getTerminalsTerminalIdTerminalSettings"></a>
# **getTerminalsTerminalIdTerminalSettings**
> TerminalSettings getTerminalsTerminalIdTerminalSettings(terminalId)

Get terminal settings

Returns the settings that are configured for the payment terminal identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalSettingsTerminalLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalSettingsTerminalLevelApi apiInstance = new TerminalSettingsTerminalLevelApi(defaultClient);
    String terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
    try {
      TerminalSettings result = apiInstance.getTerminalsTerminalIdTerminalSettings(terminalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalSettingsTerminalLevelApi#getTerminalsTerminalIdTerminalSettings");
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
| **terminalId** | **String**| The unique identifier of the payment terminal. | |

### Return type

[**TerminalSettings**](TerminalSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchTerminalsTerminalIdTerminalLogos"></a>
# **patchTerminalsTerminalIdTerminalLogos**
> Logo patchTerminalsTerminalIdTerminalLogos(terminalId, logo)

Update the logo

Updates the logo for the payment terminal identified in the path.  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from a higher level (store, merchant account, or company account), specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalSettingsTerminalLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalSettingsTerminalLevelApi apiInstance = new TerminalSettingsTerminalLevelApi(defaultClient);
    String terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
    Logo logo = new Logo(); // Logo | 
    try {
      Logo result = apiInstance.patchTerminalsTerminalIdTerminalLogos(terminalId, logo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalSettingsTerminalLevelApi#patchTerminalsTerminalIdTerminalLogos");
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
| **terminalId** | **String**| The unique identifier of the payment terminal. | |
| **logo** | [**Logo**](Logo.md)|  | [optional] |

### Return type

[**Logo**](Logo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchTerminalsTerminalIdTerminalSettings"></a>
# **patchTerminalsTerminalIdTerminalSettings**
> TerminalSettings patchTerminalsTerminalIdTerminalSettings(terminalId, terminalSettings)

Update terminal settings

Updates the settings that are configured for the payment terminal identified in the path.  * To change a parameter value, include the full object that contains the parameter, even if you don&#39;t want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalSettingsTerminalLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TerminalSettingsTerminalLevelApi apiInstance = new TerminalSettingsTerminalLevelApi(defaultClient);
    String terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
    TerminalSettings terminalSettings = new TerminalSettings(); // TerminalSettings | 
    try {
      TerminalSettings result = apiInstance.patchTerminalsTerminalIdTerminalSettings(terminalId, terminalSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalSettingsTerminalLevelApi#patchTerminalsTerminalIdTerminalSettings");
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
| **terminalId** | **String**| The unique identifier of the payment terminal. | |
| **terminalSettings** | [**TerminalSettings**](TerminalSettings.md)|  | [optional] |

### Return type

[**TerminalSettings**](TerminalSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

