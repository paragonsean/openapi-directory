# DedicatedHostsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dedicatedHostsCreateOrUpdate**](DedicatedHostsApi.md#dedicatedHostsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName} |  |
| [**dedicatedHostsDelete**](DedicatedHostsApi.md#dedicatedHostsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName} |  |
| [**dedicatedHostsGet**](DedicatedHostsApi.md#dedicatedHostsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName} |  |
| [**dedicatedHostsUpdate**](DedicatedHostsApi.md#dedicatedHostsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName} |  |


<a id="dedicatedHostsCreateOrUpdate"></a>
# **dedicatedHostsCreateOrUpdate**
> DedicatedHost dedicatedHostsCreateOrUpdate(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, parameters)



Create or update a dedicated host .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHostsApi apiInstance = new DedicatedHostsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
    String hostName = "hostName_example"; // String | The name of the dedicated host .
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DedicatedHost parameters = new DedicatedHost(); // DedicatedHost | Parameters supplied to the Create Dedicated Host.
    try {
      DedicatedHost result = apiInstance.dedicatedHostsCreateOrUpdate(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHostsApi#dedicatedHostsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **hostGroupName** | **String**| The name of the dedicated host group. | |
| **hostName** | **String**| The name of the dedicated host . | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**DedicatedHost**](DedicatedHost.md)| Parameters supplied to the Create Dedicated Host. | |

### Return type

[**DedicatedHost**](DedicatedHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="dedicatedHostsDelete"></a>
# **dedicatedHostsDelete**
> dedicatedHostsDelete(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId)



Delete a dedicated host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHostsApi apiInstance = new DedicatedHostsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
    String hostName = "hostName_example"; // String | The name of the dedicated host.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.dedicatedHostsDelete(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHostsApi#dedicatedHostsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **hostGroupName** | **String**| The name of the dedicated host group. | |
| **hostName** | **String**| The name of the dedicated host. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content |  -  |

<a id="dedicatedHostsGet"></a>
# **dedicatedHostsGet**
> DedicatedHost dedicatedHostsGet(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, $expand)



Retrieves information about a dedicated host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHostsApi apiInstance = new DedicatedHostsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
    String hostName = "hostName_example"; // String | The name of the dedicated host.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "instanceView"; // String | The expand expression to apply on the operation.
    try {
      DedicatedHost result = apiInstance.dedicatedHostsGet(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHostsApi#dedicatedHostsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **hostGroupName** | **String**| The name of the dedicated host group. | |
| **hostName** | **String**| The name of the dedicated host. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| The expand expression to apply on the operation. | [optional] [enum: instanceView] |

### Return type

[**DedicatedHost**](DedicatedHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="dedicatedHostsUpdate"></a>
# **dedicatedHostsUpdate**
> DedicatedHost dedicatedHostsUpdate(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, parameters)



Update an dedicated host .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHostsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHostsApi apiInstance = new DedicatedHostsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
    String hostName = "hostName_example"; // String | The name of the dedicated host .
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DedicatedHostUpdate parameters = new DedicatedHostUpdate(); // DedicatedHostUpdate | Parameters supplied to the Update Dedicated Host operation.
    try {
      DedicatedHost result = apiInstance.dedicatedHostsUpdate(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHostsApi#dedicatedHostsUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **hostGroupName** | **String**| The name of the dedicated host group. | |
| **hostName** | **String**| The name of the dedicated host . | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**DedicatedHostUpdate**](DedicatedHostUpdate.md)| Parameters supplied to the Update Dedicated Host operation. | |

### Return type

[**DedicatedHost**](DedicatedHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

