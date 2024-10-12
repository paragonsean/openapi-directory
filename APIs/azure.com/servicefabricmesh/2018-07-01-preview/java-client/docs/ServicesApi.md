# ServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceGet**](ServicesApi.md#serviceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services/{serviceName} | Gets the properties of the service. |
| [**serviceListByApplicationName**](ServicesApi.md#serviceListByApplicationName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services | Gets services of a given application. |


<a id="serviceGet"></a>
# **serviceGet**
> ServiceResourceDescription serviceGet(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName)

Gets the properties of the service.

The operation returns the properties of the service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-07-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String applicationName = "applicationName_example"; // String | The identity of the application.
    String serviceName = "serviceName_example"; // String | The identity of the service.
    try {
      ServiceResourceDescription result = apiInstance.serviceGet(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#serviceGet");
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
| **subscriptionId** | **String**| The customer subscription identifier | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to 2018-07-01-preview] [enum: 2018-07-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **applicationName** | **String**| The identity of the application. | |
| **serviceName** | **String**| The identity of the service. | |

### Return type

[**ServiceResourceDescription**](ServiceResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serviceListByApplicationName"></a>
# **serviceListByApplicationName**
> ServiceList serviceListByApplicationName(subscriptionId, apiVersion, resourceGroupName, applicationName)

Gets services of a given application.

Gets the information about all services of a given service of an application. The information includes the runtime properties of the service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-07-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String applicationName = "applicationName_example"; // String | The identity of the application.
    try {
      ServiceList result = apiInstance.serviceListByApplicationName(subscriptionId, apiVersion, resourceGroupName, applicationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#serviceListByApplicationName");
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
| **subscriptionId** | **String**| The customer subscription identifier | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to 2018-07-01-preview] [enum: 2018-07-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **applicationName** | **String**| The identity of the application. | |

### Return type

[**ServiceList**](ServiceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

