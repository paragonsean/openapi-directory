# ExpressRoutePortsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRoutePortsCreateOrUpdate**](ExpressRoutePortsApi.md#expressRoutePortsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName} |  |
| [**expressRoutePortsDelete**](ExpressRoutePortsApi.md#expressRoutePortsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName} |  |
| [**expressRoutePortsGet**](ExpressRoutePortsApi.md#expressRoutePortsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName} |  |
| [**expressRoutePortsList**](ExpressRoutePortsApi.md#expressRoutePortsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ExpressRoutePorts |  |
| [**expressRoutePortsListByResourceGroup**](ExpressRoutePortsApi.md#expressRoutePortsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts |  |
| [**expressRoutePortsUpdateTags**](ExpressRoutePortsApi.md#expressRoutePortsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName} |  |


<a id="expressRoutePortsCreateOrUpdate"></a>
# **expressRoutePortsCreateOrUpdate**
> ExpressRoutePort expressRoutePortsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, parameters)



Creates or updates the specified ExpressRoutePort resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRoutePortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRoutePortsApi apiInstance = new ExpressRoutePortsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
    ExpressRoutePort parameters = new ExpressRoutePort(); // ExpressRoutePort | Parameters supplied to the create ExpressRoutePort operation.
    try {
      ExpressRoutePort result = apiInstance.expressRoutePortsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRoutePortsApi#expressRoutePortsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | |
| **parameters** | [**ExpressRoutePort**](ExpressRoutePort.md)| Parameters supplied to the create ExpressRoutePort operation. | |

### Return type

[**ExpressRoutePort**](ExpressRoutePort.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ExpressRoutePort resource. |  -  |
| **201** | Create successful. The operation returns the resulting ExpressRoutePort resource. |  -  |

<a id="expressRoutePortsDelete"></a>
# **expressRoutePortsDelete**
> expressRoutePortsDelete(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName)



Deletes the specified ExpressRoutePort resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRoutePortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRoutePortsApi apiInstance = new ExpressRoutePortsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
    try {
      apiInstance.expressRoutePortsDelete(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRoutePortsApi#expressRoutePortsDelete");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | |

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
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Request successful. Resource does not exist. |  -  |

<a id="expressRoutePortsGet"></a>
# **expressRoutePortsGet**
> ExpressRoutePort expressRoutePortsGet(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName)



Retrieves the requested ExpressRoutePort resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRoutePortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRoutePortsApi apiInstance = new ExpressRoutePortsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRoutePortName = "expressRoutePortName_example"; // String | The name of ExpressRoutePort.
    try {
      ExpressRoutePort result = apiInstance.expressRoutePortsGet(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRoutePortsApi#expressRoutePortsGet");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **expressRoutePortName** | **String**| The name of ExpressRoutePort. | |

### Return type

[**ExpressRoutePort**](ExpressRoutePort.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the requested ExpressRoutePort resource. |  -  |

<a id="expressRoutePortsList"></a>
# **expressRoutePortsList**
> ExpressRoutePortListResult expressRoutePortsList(subscriptionId, apiVersion)



List all the ExpressRoutePort resources in the specified subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRoutePortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRoutePortsApi apiInstance = new ExpressRoutePortsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ExpressRoutePortListResult result = apiInstance.expressRoutePortsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRoutePortsApi#expressRoutePortsList");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ExpressRoutePortListResult**](ExpressRoutePortListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ExpressRoutePort resources. If there are no ExpressRoutePort resources then an empty list is returned. |  -  |

<a id="expressRoutePortsListByResourceGroup"></a>
# **expressRoutePortsListByResourceGroup**
> ExpressRoutePortListResult expressRoutePortsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)



List all the ExpressRoutePort resources in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRoutePortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRoutePortsApi apiInstance = new ExpressRoutePortsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    try {
      ExpressRoutePortListResult result = apiInstance.expressRoutePortsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRoutePortsApi#expressRoutePortsListByResourceGroup");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| The name of the resource group. | |

### Return type

[**ExpressRoutePortListResult**](ExpressRoutePortListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ExpressRoutePort resources. If there are no ExpressRoutePort resources then an empty list is returned. |  -  |

<a id="expressRoutePortsUpdateTags"></a>
# **expressRoutePortsUpdateTags**
> ExpressRoutePort expressRoutePortsUpdateTags(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, parameters)



Update ExpressRoutePort tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRoutePortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRoutePortsApi apiInstance = new ExpressRoutePortsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
    ExpressRoutePortsUpdateTagsRequest parameters = new ExpressRoutePortsUpdateTagsRequest(); // ExpressRoutePortsUpdateTagsRequest | Parameters supplied to update ExpressRoutePort resource tags.
    try {
      ExpressRoutePort result = apiInstance.expressRoutePortsUpdateTags(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRoutePortsApi#expressRoutePortsUpdateTags");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | |
| **parameters** | [**ExpressRoutePortsUpdateTagsRequest**](ExpressRoutePortsUpdateTagsRequest.md)| Parameters supplied to update ExpressRoutePort resource tags. | |

### Return type

[**ExpressRoutePort**](ExpressRoutePort.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ExpressRoutePort resource. |  -  |

