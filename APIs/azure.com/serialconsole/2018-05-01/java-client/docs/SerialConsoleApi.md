# SerialConsoleApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disableConsole**](SerialConsoleApi.md#disableConsole) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}/disableConsole | Disable Serial Console for a subscription |
| [**enableConsole**](SerialConsoleApi.md#enableConsole) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}/enableConsole | Enable Serial Console for a subscription |
| [**getConsoleStatus**](SerialConsoleApi.md#getConsoleStatus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default} | Get the disabled status for a subscription |
| [**listOperations**](SerialConsoleApi.md#listOperations) | **GET** /providers/Microsoft.SerialConsole/operations |  |


<a id="disableConsole"></a>
# **disableConsole**
> DisableSerialConsoleResult disableConsole(apiVersion, subscriptionId, _default)

Disable Serial Console for a subscription

Disables the Serial Console service for all VMs and VM scale sets in the provided subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SerialConsoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SerialConsoleApi apiInstance = new SerialConsoleApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
    String _default = "_default_example"; // String | Default parameter. Leave the value as \"default\".
    try {
      DisableSerialConsoleResult result = apiInstance.disableConsole(apiVersion, subscriptionId, _default);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SerialConsoleApi#disableConsole");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it. | |
| **_default** | **String**| Default parameter. Leave the value as \&quot;default\&quot;. | |

### Return type

[**DisableSerialConsoleResult**](DisableSerialConsoleResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns a JSON object |  -  |
| **404** | Subscription not found - returns a JSON object with error details |  -  |

<a id="enableConsole"></a>
# **enableConsole**
> EnableSerialConsoleResult enableConsole(apiVersion, subscriptionId, _default)

Enable Serial Console for a subscription

Enables the Serial Console service for all VMs and VM scale sets in the provided subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SerialConsoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SerialConsoleApi apiInstance = new SerialConsoleApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
    String _default = "_default_example"; // String | Default parameter. Leave the value as \"default\".
    try {
      EnableSerialConsoleResult result = apiInstance.enableConsole(apiVersion, subscriptionId, _default);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SerialConsoleApi#enableConsole");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it. | |
| **_default** | **String**| Default parameter. Leave the value as \&quot;default\&quot;. | |

### Return type

[**EnableSerialConsoleResult**](EnableSerialConsoleResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Serial Console disabled |  -  |
| **404** | Subscription not found - returns a JSON object with error details |  -  |

<a id="getConsoleStatus"></a>
# **getConsoleStatus**
> SerialConsoleStatus getConsoleStatus(apiVersion, subscriptionId, _default)

Get the disabled status for a subscription

Gets whether or not Serial Console is disabled for a given subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SerialConsoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SerialConsoleApi apiInstance = new SerialConsoleApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
    String _default = "_default_example"; // String | Default parameter. Leave the value as \"default\".
    try {
      SerialConsoleStatus result = apiInstance.getConsoleStatus(apiVersion, subscriptionId, _default);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SerialConsoleApi#getConsoleStatus");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it. | |
| **_default** | **String**| Default parameter. Leave the value as \&quot;default\&quot;. | |

### Return type

[**SerialConsoleStatus**](SerialConsoleStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns a JSON object |  -  |
| **404** | Subscription not found - returns a JSON object with error details |  -  |

<a id="listOperations"></a>
# **listOperations**
> SerialConsoleOperations listOperations(apiVersion)



Gets a list of Serial Console API operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SerialConsoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SerialConsoleApi apiInstance = new SerialConsoleApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      SerialConsoleOperations result = apiInstance.listOperations(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SerialConsoleApi#listOperations");
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
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**SerialConsoleOperations**](SerialConsoleOperations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - returns a JSON object |  -  |

