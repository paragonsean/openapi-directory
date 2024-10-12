# ClassicMobileServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**classicMobileServicesDeleteClassicMobileService**](ClassicMobileServicesApi.md#classicMobileServicesDeleteClassicMobileService) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/classicMobileServices/{name} | Delete a mobile service. |
| [**classicMobileServicesGetClassicMobileService**](ClassicMobileServicesApi.md#classicMobileServicesGetClassicMobileService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/classicMobileServices/{name} | Get a mobile service. |
| [**classicMobileServicesGetClassicMobileServices**](ClassicMobileServicesApi.md#classicMobileServicesGetClassicMobileServices) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/classicMobileServices | Get all mobile services in a resource group. |


<a id="classicMobileServicesDeleteClassicMobileService"></a>
# **classicMobileServicesDeleteClassicMobileService**
> Object classicMobileServicesDeleteClassicMobileService(resourceGroupName, name, subscriptionId, apiVersion)

Delete a mobile service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassicMobileServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClassicMobileServicesApi apiInstance = new ClassicMobileServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of mobile service
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.classicMobileServicesDeleteClassicMobileService(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassicMobileServicesApi#classicMobileServicesDeleteClassicMobileService");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of mobile service | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="classicMobileServicesGetClassicMobileService"></a>
# **classicMobileServicesGetClassicMobileService**
> ClassicMobileService classicMobileServicesGetClassicMobileService(resourceGroupName, name, subscriptionId, apiVersion)

Get a mobile service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassicMobileServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClassicMobileServicesApi apiInstance = new ClassicMobileServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of mobile service
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ClassicMobileService result = apiInstance.classicMobileServicesGetClassicMobileService(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassicMobileServicesApi#classicMobileServicesGetClassicMobileService");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of mobile service | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ClassicMobileService**](ClassicMobileService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="classicMobileServicesGetClassicMobileServices"></a>
# **classicMobileServicesGetClassicMobileServices**
> ClassicMobileServiceCollection classicMobileServicesGetClassicMobileServices(resourceGroupName, subscriptionId, apiVersion)

Get all mobile services in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassicMobileServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClassicMobileServicesApi apiInstance = new ClassicMobileServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ClassicMobileServiceCollection result = apiInstance.classicMobileServicesGetClassicMobileServices(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassicMobileServicesApi#classicMobileServicesGetClassicMobileServices");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ClassicMobileServiceCollection**](ClassicMobileServiceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

