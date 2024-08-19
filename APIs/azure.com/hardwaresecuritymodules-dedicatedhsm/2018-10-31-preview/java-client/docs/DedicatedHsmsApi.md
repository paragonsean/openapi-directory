# DedicatedHsmsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dedicatedHsmCreateOrUpdate**](DedicatedHsmsApi.md#dedicatedHsmCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name} |  |
| [**dedicatedHsmDelete**](DedicatedHsmsApi.md#dedicatedHsmDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name} |  |
| [**dedicatedHsmGet**](DedicatedHsmsApi.md#dedicatedHsmGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name} |  |
| [**dedicatedHsmListByResourceGroup**](DedicatedHsmsApi.md#dedicatedHsmListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs |  |
| [**dedicatedHsmListBySubscription**](DedicatedHsmsApi.md#dedicatedHsmListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs |  |
| [**dedicatedHsmUpdate**](DedicatedHsmsApi.md#dedicatedHsmUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name} |  |


<a id="dedicatedHsmCreateOrUpdate"></a>
# **dedicatedHsmCreateOrUpdate**
> DedicatedHsm dedicatedHsmCreateOrUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Create or Update a dedicated HSM in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHsmsApi apiInstance = new DedicatedHsmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the resource belongs.
    String name = "name_example"; // String | Name of the dedicated Hsm
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DedicatedHsm parameters = new DedicatedHsm(); // DedicatedHsm | Parameters to create or update the dedicated hsm
    try {
      DedicatedHsm result = apiInstance.dedicatedHsmCreateOrUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHsmsApi#dedicatedHsmCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the resource belongs. | |
| **name** | **String**| Name of the dedicated Hsm | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**DedicatedHsm**](DedicatedHsm.md)| Parameters to create or update the dedicated hsm | |

### Return type

[**DedicatedHsm**](DedicatedHsm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created dedicated HSM |  -  |
| **201** | Created dedicated HSM |  -  |
| **0** | The error response describing why the operation failed. |  -  |

<a id="dedicatedHsmDelete"></a>
# **dedicatedHsmDelete**
> dedicatedHsmDelete(resourceGroupName, name, apiVersion, subscriptionId)



Deletes the specified Azure Dedicated HSM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHsmsApi apiInstance = new DedicatedHsmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the dedicated HSM belongs.
    String name = "name_example"; // String | The name of the dedicated HSM to delete
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.dedicatedHsmDelete(resourceGroupName, name, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHsmsApi#dedicatedHsmDelete");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the dedicated HSM belongs. | |
| **name** | **String**| The name of the dedicated HSM to delete | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK Response. |  -  |
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | The error response describing why the operation failed. |  -  |

<a id="dedicatedHsmGet"></a>
# **dedicatedHsmGet**
> DedicatedHsm dedicatedHsmGet(resourceGroupName, name, apiVersion, subscriptionId)



Gets the specified Azure dedicated HSM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHsmsApi apiInstance = new DedicatedHsmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the dedicated hsm belongs.
    String name = "name_example"; // String | The name of the dedicated HSM.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DedicatedHsm result = apiInstance.dedicatedHsmGet(resourceGroupName, name, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHsmsApi#dedicatedHsmGet");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the dedicated hsm belongs. | |
| **name** | **String**| The name of the dedicated HSM. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DedicatedHsm**](DedicatedHsm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieved dedicated HSM |  -  |
| **0** | The error response describing why the operation failed. |  -  |

<a id="dedicatedHsmListByResourceGroup"></a>
# **dedicatedHsmListByResourceGroup**
> DedicatedHsmListResult dedicatedHsmListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $top)



The List operation gets information about the dedicated hsms associated with the subscription and within the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHsmsApi apiInstance = new DedicatedHsmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the dedicated HSM belongs.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Maximum number of results to return.
    try {
      DedicatedHsmListResult result = apiInstance.dedicatedHsmListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHsmsApi#dedicatedHsmListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the dedicated HSM belongs. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Maximum number of results to return. | [optional] |

### Return type

[**DedicatedHsmListResult**](DedicatedHsmListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get information about all dedicated HSMs in the specified resource group. |  -  |
| **0** | The error response describing why the operation failed. |  -  |

<a id="dedicatedHsmListBySubscription"></a>
# **dedicatedHsmListBySubscription**
> DedicatedHsmListResult dedicatedHsmListBySubscription(apiVersion, subscriptionId, $top)



The List operation gets information about the dedicated HSMs associated with the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHsmsApi apiInstance = new DedicatedHsmsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Maximum number of results to return.
    try {
      DedicatedHsmListResult result = apiInstance.dedicatedHsmListBySubscription(apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHsmsApi#dedicatedHsmListBySubscription");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Maximum number of results to return. | [optional] |

### Return type

[**DedicatedHsmListResult**](DedicatedHsmListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get information about all dedicated HSMs in the specified subscription. |  -  |
| **0** | The error response describing why the operation failed. |  -  |

<a id="dedicatedHsmUpdate"></a>
# **dedicatedHsmUpdate**
> DedicatedHsm dedicatedHsmUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Update a dedicated HSM in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedHsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedHsmsApi apiInstance = new DedicatedHsmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the server belongs.
    String name = "name_example"; // String | Name of the dedicated HSM
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DedicatedHsmPatchParameters parameters = new DedicatedHsmPatchParameters(); // DedicatedHsmPatchParameters | Parameters to patch the dedicated HSM
    try {
      DedicatedHsm result = apiInstance.dedicatedHsmUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedHsmsApi#dedicatedHsmUpdate");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the server belongs. | |
| **name** | **String**| Name of the dedicated HSM | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**DedicatedHsmPatchParameters**](DedicatedHsmPatchParameters.md)| Parameters to patch the dedicated HSM | |

### Return type

[**DedicatedHsm**](DedicatedHsm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Patched dedicated HSM |  -  |
| **0** | The error response describing why the operation failed. |  -  |

