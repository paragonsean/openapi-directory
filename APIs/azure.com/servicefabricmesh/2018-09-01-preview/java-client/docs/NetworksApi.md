# NetworksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkCreate**](NetworksApi.md#networkCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/networks/{networkResourceName} | Creates or updates a network resource. |
| [**networkDelete**](NetworksApi.md#networkDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/networks/{networkResourceName} | Deletes the network resource. |
| [**networkGet**](NetworksApi.md#networkGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/networks/{networkResourceName} | Gets the network resource with the given name. |
| [**networkListByResourceGroup**](NetworksApi.md#networkListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/networks | Gets all the network resources in a given resource group. |
| [**networkListBySubscription**](NetworksApi.md#networkListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabricMesh/networks | Gets all the network resources in a given subscription. |


<a id="networkCreate"></a>
# **networkCreate**
> NetworkResourceDescription networkCreate(subscriptionId, apiVersion, resourceGroupName, networkResourceName, networkResourceDescription)

Creates or updates a network resource.

Creates a network resource with the specified name, description and properties. If a network resource with the same name exists, then it is updated with the specified description and properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String networkResourceName = "networkResourceName_example"; // String | The identity of the network.
    NetworkResourceDescription networkResourceDescription = new NetworkResourceDescription(); // NetworkResourceDescription | Description for creating a Network resource.
    try {
      NetworkResourceDescription result = apiInstance.networkCreate(subscriptionId, apiVersion, resourceGroupName, networkResourceName, networkResourceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networkCreate");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **networkResourceName** | **String**| The identity of the network. | |
| **networkResourceDescription** | [**NetworkResourceDescription**](NetworkResourceDescription.md)| Description for creating a Network resource. | |

### Return type

[**NetworkResourceDescription**](NetworkResourceDescription.md)

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
| **202** | Accepted |  -  |
| **0** | Error |  -  |

<a id="networkDelete"></a>
# **networkDelete**
> networkDelete(subscriptionId, apiVersion, resourceGroupName, networkResourceName)

Deletes the network resource.

Deletes the network resource identified by the name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String networkResourceName = "networkResourceName_example"; // String | The identity of the network.
    try {
      apiInstance.networkDelete(subscriptionId, apiVersion, resourceGroupName, networkResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networkDelete");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **networkResourceName** | **String**| The identity of the network. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content - the specified network was not found. |  -  |
| **0** | Error |  -  |

<a id="networkGet"></a>
# **networkGet**
> NetworkResourceDescription networkGet(subscriptionId, apiVersion, resourceGroupName, networkResourceName)

Gets the network resource with the given name.

Gets the information about the network resource with the given name. The information include the description and other properties of the network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String networkResourceName = "networkResourceName_example"; // String | The identity of the network.
    try {
      NetworkResourceDescription result = apiInstance.networkGet(subscriptionId, apiVersion, resourceGroupName, networkResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networkGet");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |
| **networkResourceName** | **String**| The identity of the network. | |

### Return type

[**NetworkResourceDescription**](NetworkResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="networkListByResourceGroup"></a>
# **networkListByResourceGroup**
> NetworkResourceDescriptionList networkListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Gets all the network resources in a given resource group.

Gets the information about all network resources in a given resource group. The information include the description and other properties of the Network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    try {
      NetworkResourceDescriptionList result = apiInstance.networkListByResourceGroup(subscriptionId, apiVersion, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networkListByResourceGroup");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |
| **resourceGroupName** | **String**| Azure resource group name | |

### Return type

[**NetworkResourceDescriptionList**](NetworkResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="networkListBySubscription"></a>
# **networkListBySubscription**
> NetworkResourceDescriptionList networkListBySubscription(subscriptionId, apiVersion)

Gets all the network resources in a given subscription.

Gets the information about all network resources in a given resource group. The information include the description and other properties of the network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String apiVersion = "2018-09-01-preview"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
    try {
      NetworkResourceDescriptionList result = apiInstance.networkListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#networkListBySubscription");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to 2018-09-01-preview] [enum: 2018-09-01-preview] |

### Return type

[**NetworkResourceDescriptionList**](NetworkResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

