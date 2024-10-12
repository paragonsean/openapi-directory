# StacksApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addNetworkSwitchStack_1**](StacksApi.md#addNetworkSwitchStack_1) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/add | Add a switch to a stack |
| [**createNetworkSwitchStackRoutingInterface_1**](StacksApi.md#createNetworkSwitchStackRoutingInterface_1) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | Create a layer 3 interface for a switch stack |
| [**createNetworkSwitchStackRoutingStaticRoute_1**](StacksApi.md#createNetworkSwitchStackRoutingStaticRoute_1) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes | Create a layer 3 static route for a switch stack |
| [**createNetworkSwitchStack_1**](StacksApi.md#createNetworkSwitchStack_1) | **POST** /networks/{networkId}/switch/stacks | Create a stack |
| [**deleteNetworkSwitchStackRoutingInterface_1**](StacksApi.md#deleteNetworkSwitchStackRoutingInterface_1) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Delete a layer 3 interface from a switch stack |
| [**deleteNetworkSwitchStackRoutingStaticRoute_1**](StacksApi.md#deleteNetworkSwitchStackRoutingStaticRoute_1) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Delete a layer 3 static route for a switch stack |
| [**deleteNetworkSwitchStack_1**](StacksApi.md#deleteNetworkSwitchStack_1) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId} | Delete a stack |
| [**getNetworkSwitchStackRoutingInterfaceDhcp_1**](StacksApi.md#getNetworkSwitchStackRoutingInterfaceDhcp_1) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch stack |
| [**getNetworkSwitchStackRoutingInterface_1**](StacksApi.md#getNetworkSwitchStackRoutingInterface_1) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Return a layer 3 interface from a switch stack |
| [**getNetworkSwitchStackRoutingInterfaces_1**](StacksApi.md#getNetworkSwitchStackRoutingInterfaces_1) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | List layer 3 interfaces for a switch stack |
| [**getNetworkSwitchStackRoutingStaticRoute_1**](StacksApi.md#getNetworkSwitchStackRoutingStaticRoute_1) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Return a layer 3 static route for a switch stack |
| [**getNetworkSwitchStackRoutingStaticRoutes_1**](StacksApi.md#getNetworkSwitchStackRoutingStaticRoutes_1) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes | List layer 3 static routes for a switch stack |
| [**getNetworkSwitchStack_1**](StacksApi.md#getNetworkSwitchStack_1) | **GET** /networks/{networkId}/switch/stacks/{switchStackId} | Show a switch stack |
| [**getNetworkSwitchStacks_1**](StacksApi.md#getNetworkSwitchStacks_1) | **GET** /networks/{networkId}/switch/stacks | List the switch stacks in a network |
| [**removeNetworkSwitchStack_1**](StacksApi.md#removeNetworkSwitchStack_1) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/remove | Remove a switch from a stack |
| [**updateNetworkSwitchStackRoutingInterfaceDhcp_1**](StacksApi.md#updateNetworkSwitchStackRoutingInterfaceDhcp_1) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch stack |
| [**updateNetworkSwitchStackRoutingInterface_1**](StacksApi.md#updateNetworkSwitchStackRoutingInterface_1) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch stack |
| [**updateNetworkSwitchStackRoutingStaticRoute_1**](StacksApi.md#updateNetworkSwitchStackRoutingStaticRoute_1) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Update a layer 3 static route for a switch stack |


<a id="addNetworkSwitchStack_1"></a>
# **addNetworkSwitchStack_1**
> Object addNetworkSwitchStack_1(networkId, switchStackId, addNetworkSwitchStackRequest)

Add a switch to a stack

Add a switch to a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    AddNetworkSwitchStackRequest addNetworkSwitchStackRequest = new AddNetworkSwitchStackRequest(); // AddNetworkSwitchStackRequest | 
    try {
      Object result = apiInstance.addNetworkSwitchStack_1(networkId, switchStackId, addNetworkSwitchStackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#addNetworkSwitchStack_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **addNetworkSwitchStackRequest** | [**AddNetworkSwitchStackRequest**](AddNetworkSwitchStackRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createNetworkSwitchStackRoutingInterface_1"></a>
# **createNetworkSwitchStackRoutingInterface_1**
> Object createNetworkSwitchStackRoutingInterface_1(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest)

Create a layer 3 interface for a switch stack

Create a layer 3 interface for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    CreateNetworkSwitchStackRoutingInterfaceRequest createNetworkSwitchStackRoutingInterfaceRequest = new CreateNetworkSwitchStackRoutingInterfaceRequest(); // CreateNetworkSwitchStackRoutingInterfaceRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStackRoutingInterface_1(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#createNetworkSwitchStackRoutingInterface_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **createNetworkSwitchStackRoutingInterfaceRequest** | [**CreateNetworkSwitchStackRoutingInterfaceRequest**](CreateNetworkSwitchStackRoutingInterfaceRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchStackRoutingStaticRoute_1"></a>
# **createNetworkSwitchStackRoutingStaticRoute_1**
> Object createNetworkSwitchStackRoutingStaticRoute_1(networkId, switchStackId, createDeviceSwitchRoutingStaticRouteRequest)

Create a layer 3 static route for a switch stack

Create a layer 3 static route for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    CreateDeviceSwitchRoutingStaticRouteRequest createDeviceSwitchRoutingStaticRouteRequest = new CreateDeviceSwitchRoutingStaticRouteRequest(); // CreateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStackRoutingStaticRoute_1(networkId, switchStackId, createDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#createNetworkSwitchStackRoutingStaticRoute_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **createDeviceSwitchRoutingStaticRouteRequest** | [**CreateDeviceSwitchRoutingStaticRouteRequest**](CreateDeviceSwitchRoutingStaticRouteRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchStack_1"></a>
# **createNetworkSwitchStack_1**
> Object createNetworkSwitchStack_1(networkId, createNetworkSwitchStackRequest)

Create a stack

Create a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchStackRequest createNetworkSwitchStackRequest = new CreateNetworkSwitchStackRequest(); // CreateNetworkSwitchStackRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStack_1(networkId, createNetworkSwitchStackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#createNetworkSwitchStack_1");
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
| **networkId** | **String**|  | |
| **createNetworkSwitchStackRequest** | [**CreateNetworkSwitchStackRequest**](CreateNetworkSwitchStackRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkSwitchStackRoutingInterface_1"></a>
# **deleteNetworkSwitchStackRoutingInterface_1**
> deleteNetworkSwitchStackRoutingInterface_1(networkId, switchStackId, interfaceId)

Delete a layer 3 interface from a switch stack

Delete a layer 3 interface from a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStackRoutingInterface_1(networkId, switchStackId, interfaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#deleteNetworkSwitchStackRoutingInterface_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchStackRoutingStaticRoute_1"></a>
# **deleteNetworkSwitchStackRoutingStaticRoute_1**
> deleteNetworkSwitchStackRoutingStaticRoute_1(networkId, switchStackId, staticRouteId)

Delete a layer 3 static route for a switch stack

Delete a layer 3 static route for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStackRoutingStaticRoute_1(networkId, switchStackId, staticRouteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#deleteNetworkSwitchStackRoutingStaticRoute_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkSwitchStack_1"></a>
# **deleteNetworkSwitchStack_1**
> deleteNetworkSwitchStack_1(networkId, switchStackId)

Delete a stack

Delete a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStack_1(networkId, switchStackId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#deleteNetworkSwitchStack_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingInterfaceDhcp_1"></a>
# **getNetworkSwitchStackRoutingInterfaceDhcp_1**
> Object getNetworkSwitchStackRoutingInterfaceDhcp_1(networkId, switchStackId, interfaceId)

Return a layer 3 interface DHCP configuration for a switch stack

Return a layer 3 interface DHCP configuration for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterfaceDhcp_1(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#getNetworkSwitchStackRoutingInterfaceDhcp_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingInterface_1"></a>
# **getNetworkSwitchStackRoutingInterface_1**
> Object getNetworkSwitchStackRoutingInterface_1(networkId, switchStackId, interfaceId)

Return a layer 3 interface from a switch stack

Return a layer 3 interface from a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterface_1(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#getNetworkSwitchStackRoutingInterface_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingInterfaces_1"></a>
# **getNetworkSwitchStackRoutingInterfaces_1**
> List&lt;Object&gt; getNetworkSwitchStackRoutingInterfaces_1(networkId, switchStackId)

List layer 3 interfaces for a switch stack

List layer 3 interfaces for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStackRoutingInterfaces_1(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#getNetworkSwitchStackRoutingInterfaces_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingStaticRoute_1"></a>
# **getNetworkSwitchStackRoutingStaticRoute_1**
> Object getNetworkSwitchStackRoutingStaticRoute_1(networkId, switchStackId, staticRouteId)

Return a layer 3 static route for a switch stack

Return a layer 3 static route for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingStaticRoute_1(networkId, switchStackId, staticRouteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#getNetworkSwitchStackRoutingStaticRoute_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **staticRouteId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingStaticRoutes_1"></a>
# **getNetworkSwitchStackRoutingStaticRoutes_1**
> List&lt;Object&gt; getNetworkSwitchStackRoutingStaticRoutes_1(networkId, switchStackId)

List layer 3 static routes for a switch stack

List layer 3 static routes for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStackRoutingStaticRoutes_1(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#getNetworkSwitchStackRoutingStaticRoutes_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStack_1"></a>
# **getNetworkSwitchStack_1**
> GetNetworkSwitchStack200Response getNetworkSwitchStack_1(networkId, switchStackId)

Show a switch stack

Show a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      GetNetworkSwitchStack200Response result = apiInstance.getNetworkSwitchStack_1(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#getNetworkSwitchStack_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |

### Return type

[**GetNetworkSwitchStack200Response**](GetNetworkSwitchStack200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStacks_1"></a>
# **getNetworkSwitchStacks_1**
> List&lt;Object&gt; getNetworkSwitchStacks_1(networkId)

List the switch stacks in a network

List the switch stacks in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStacks_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#getNetworkSwitchStacks_1");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="removeNetworkSwitchStack_1"></a>
# **removeNetworkSwitchStack_1**
> Object removeNetworkSwitchStack_1(networkId, switchStackId, removeNetworkSwitchStackRequest)

Remove a switch from a stack

Remove a switch from a stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    RemoveNetworkSwitchStackRequest removeNetworkSwitchStackRequest = new RemoveNetworkSwitchStackRequest(); // RemoveNetworkSwitchStackRequest | 
    try {
      Object result = apiInstance.removeNetworkSwitchStack_1(networkId, switchStackId, removeNetworkSwitchStackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#removeNetworkSwitchStack_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **removeNetworkSwitchStackRequest** | [**RemoveNetworkSwitchStackRequest**](RemoveNetworkSwitchStackRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStackRoutingInterfaceDhcp_1"></a>
# **updateNetworkSwitchStackRoutingInterfaceDhcp_1**
> Object updateNetworkSwitchStackRoutingInterfaceDhcp_1(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest)

Update a layer 3 interface DHCP configuration for a switch stack

Update a layer 3 interface DHCP configuration for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest updateNetworkSwitchStackRoutingInterfaceDhcpRequest = new UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest(); // UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterfaceDhcp_1(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#updateNetworkSwitchStackRoutingInterfaceDhcp_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |
| **updateNetworkSwitchStackRoutingInterfaceDhcpRequest** | [**UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest**](UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStackRoutingInterface_1"></a>
# **updateNetworkSwitchStackRoutingInterface_1**
> Object updateNetworkSwitchStackRoutingInterface_1(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest)

Update a layer 3 interface for a switch stack

Update a layer 3 interface for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceRequest updateNetworkSwitchStackRoutingInterfaceRequest = new UpdateNetworkSwitchStackRoutingInterfaceRequest(); // UpdateNetworkSwitchStackRoutingInterfaceRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterface_1(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#updateNetworkSwitchStackRoutingInterface_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |
| **updateNetworkSwitchStackRoutingInterfaceRequest** | [**UpdateNetworkSwitchStackRoutingInterfaceRequest**](UpdateNetworkSwitchStackRoutingInterfaceRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStackRoutingStaticRoute_1"></a>
# **updateNetworkSwitchStackRoutingStaticRoute_1**
> Object updateNetworkSwitchStackRoutingStaticRoute_1(networkId, switchStackId, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest)

Update a layer 3 static route for a switch stack

Update a layer 3 static route for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StacksApi apiInstance = new StacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    UpdateDeviceSwitchRoutingStaticRouteRequest updateDeviceSwitchRoutingStaticRouteRequest = new UpdateDeviceSwitchRoutingStaticRouteRequest(); // UpdateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingStaticRoute_1(networkId, switchStackId, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StacksApi#updateNetworkSwitchStackRoutingStaticRoute_1");
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
| **networkId** | **String**|  | |
| **switchStackId** | **String**|  | |
| **staticRouteId** | **String**|  | |
| **updateDeviceSwitchRoutingStaticRouteRequest** | [**UpdateDeviceSwitchRoutingStaticRouteRequest**](UpdateDeviceSwitchRoutingStaticRouteRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

