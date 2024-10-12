# ProviderApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**providerGetAvailableStacks**](ProviderApi.md#providerGetAvailableStacks) | **GET** /providers/Microsoft.Web/availableStacks | Get available application frameworks and their versions |
| [**providerGetAvailableStacksOnPrem**](ProviderApi.md#providerGetAvailableStacksOnPrem) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/availableStacks | Get available application frameworks and their versions |
| [**providerListOperations**](ProviderApi.md#providerListOperations) | **GET** /providers/Microsoft.Web/operations | Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions |


<a id="providerGetAvailableStacks"></a>
# **providerGetAvailableStacks**
> ApplicationStackCollection providerGetAvailableStacks(apiVersion, osTypeSelected)

Get available application frameworks and their versions

Get available application frameworks and their versions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    String osTypeSelected = "Windows"; // String | 
    try {
      ApplicationStackCollection result = apiInstance.providerGetAvailableStacks(apiVersion, osTypeSelected);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#providerGetAvailableStacks");
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
| **apiVersion** | **String**| API Version | |
| **osTypeSelected** | **String**|  | [optional] [enum: Windows, Linux, WindowsFunctions, LinuxFunctions] |

### Return type

[**ApplicationStackCollection**](ApplicationStackCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="providerGetAvailableStacksOnPrem"></a>
# **providerGetAvailableStacksOnPrem**
> ApplicationStackCollection providerGetAvailableStacksOnPrem(subscriptionId, apiVersion, osTypeSelected)

Get available application frameworks and their versions

Get available application frameworks and their versions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String osTypeSelected = "Windows"; // String | 
    try {
      ApplicationStackCollection result = apiInstance.providerGetAvailableStacksOnPrem(subscriptionId, apiVersion, osTypeSelected);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#providerGetAvailableStacksOnPrem");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **osTypeSelected** | **String**|  | [optional] [enum: Windows, Linux, WindowsFunctions, LinuxFunctions] |

### Return type

[**ApplicationStackCollection**](ApplicationStackCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="providerListOperations"></a>
# **providerListOperations**
> ProviderListOperations200Response providerListOperations(apiVersion)

Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions

Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ProviderListOperations200Response result = apiInstance.providerListOperations(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#providerListOperations");
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
| **apiVersion** | **String**| API Version | |

### Return type

[**ProviderListOperations200Response**](ProviderListOperations200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

