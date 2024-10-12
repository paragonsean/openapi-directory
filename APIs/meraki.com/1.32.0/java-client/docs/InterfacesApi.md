# InterfacesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceSwitchRoutingInterface_2**](InterfacesApi.md#createDeviceSwitchRoutingInterface_2) | **POST** /devices/{serial}/switch/routing/interfaces | Create a layer 3 interface for a switch |
| [**createNetworkSwitchStackRoutingInterface_3**](InterfacesApi.md#createNetworkSwitchStackRoutingInterface_3) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | Create a layer 3 interface for a switch stack |
| [**deleteDeviceSwitchRoutingInterface_2**](InterfacesApi.md#deleteDeviceSwitchRoutingInterface_2) | **DELETE** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Delete a layer 3 interface from the switch |
| [**deleteNetworkSwitchStackRoutingInterface_3**](InterfacesApi.md#deleteNetworkSwitchStackRoutingInterface_3) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Delete a layer 3 interface from a switch stack |
| [**getDeviceSwitchRoutingInterfaceDhcp_2**](InterfacesApi.md#getDeviceSwitchRoutingInterfaceDhcp_2) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch |
| [**getDeviceSwitchRoutingInterface_2**](InterfacesApi.md#getDeviceSwitchRoutingInterface_2) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Return a layer 3 interface for a switch |
| [**getDeviceSwitchRoutingInterfaces_2**](InterfacesApi.md#getDeviceSwitchRoutingInterfaces_2) | **GET** /devices/{serial}/switch/routing/interfaces | List layer 3 interfaces for a switch |
| [**getNetworkSwitchStackRoutingInterfaceDhcp_3**](InterfacesApi.md#getNetworkSwitchStackRoutingInterfaceDhcp_3) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch stack |
| [**getNetworkSwitchStackRoutingInterface_3**](InterfacesApi.md#getNetworkSwitchStackRoutingInterface_3) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Return a layer 3 interface from a switch stack |
| [**getNetworkSwitchStackRoutingInterfaces_3**](InterfacesApi.md#getNetworkSwitchStackRoutingInterfaces_3) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | List layer 3 interfaces for a switch stack |
| [**updateDeviceSwitchRoutingInterfaceDhcp_2**](InterfacesApi.md#updateDeviceSwitchRoutingInterfaceDhcp_2) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch |
| [**updateDeviceSwitchRoutingInterface_2**](InterfacesApi.md#updateDeviceSwitchRoutingInterface_2) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch |
| [**updateNetworkSwitchStackRoutingInterfaceDhcp_3**](InterfacesApi.md#updateNetworkSwitchStackRoutingInterfaceDhcp_3) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch stack |
| [**updateNetworkSwitchStackRoutingInterface_3**](InterfacesApi.md#updateNetworkSwitchStackRoutingInterface_3) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch stack |


<a id="createDeviceSwitchRoutingInterface_2"></a>
# **createDeviceSwitchRoutingInterface_2**
> GetDeviceSwitchRoutingInterfaces200ResponseInner createDeviceSwitchRoutingInterface_2(serial, createDeviceSwitchRoutingInterfaceRequest)

Create a layer 3 interface for a switch

Create a layer 3 interface for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = new CreateDeviceSwitchRoutingInterfaceRequest(); // CreateDeviceSwitchRoutingInterfaceRequest | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.createDeviceSwitchRoutingInterface_2(serial, createDeviceSwitchRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#createDeviceSwitchRoutingInterface_2");
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
| **serial** | **String**|  | |
| **createDeviceSwitchRoutingInterfaceRequest** | [**CreateDeviceSwitchRoutingInterfaceRequest**](CreateDeviceSwitchRoutingInterfaceRequest.md)|  | [optional] |

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkSwitchStackRoutingInterface_3"></a>
# **createNetworkSwitchStackRoutingInterface_3**
> Object createNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest)

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
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    CreateNetworkSwitchStackRoutingInterfaceRequest createNetworkSwitchStackRoutingInterfaceRequest = new CreateNetworkSwitchStackRoutingInterfaceRequest(); // CreateNetworkSwitchStackRoutingInterfaceRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#createNetworkSwitchStackRoutingInterface_3");
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

<a id="deleteDeviceSwitchRoutingInterface_2"></a>
# **deleteDeviceSwitchRoutingInterface_2**
> deleteDeviceSwitchRoutingInterface_2(serial, interfaceId)

Delete a layer 3 interface from the switch

Delete a layer 3 interface from the switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      apiInstance.deleteDeviceSwitchRoutingInterface_2(serial, interfaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#deleteDeviceSwitchRoutingInterface_2");
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
| **serial** | **String**|  | |
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

<a id="deleteNetworkSwitchStackRoutingInterface_3"></a>
# **deleteNetworkSwitchStackRoutingInterface_3**
> deleteNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId)

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
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#deleteNetworkSwitchStackRoutingInterface_3");
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

<a id="getDeviceSwitchRoutingInterfaceDhcp_2"></a>
# **getDeviceSwitchRoutingInterfaceDhcp_2**
> Object getDeviceSwitchRoutingInterfaceDhcp_2(serial, interfaceId)

Return a layer 3 interface DHCP configuration for a switch

Return a layer 3 interface DHCP configuration for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getDeviceSwitchRoutingInterfaceDhcp_2(serial, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#getDeviceSwitchRoutingInterfaceDhcp_2");
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
| **serial** | **String**|  | |
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

<a id="getDeviceSwitchRoutingInterface_2"></a>
# **getDeviceSwitchRoutingInterface_2**
> GetDeviceSwitchRoutingInterfaces200ResponseInner getDeviceSwitchRoutingInterface_2(serial, interfaceId)

Return a layer 3 interface for a switch

Return a layer 3 interface for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.getDeviceSwitchRoutingInterface_2(serial, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#getDeviceSwitchRoutingInterface_2");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchRoutingInterfaces_2"></a>
# **getDeviceSwitchRoutingInterfaces_2**
> List&lt;GetDeviceSwitchRoutingInterfaces200ResponseInner&gt; getDeviceSwitchRoutingInterfaces_2(serial)

List layer 3 interfaces for a switch

List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<GetDeviceSwitchRoutingInterfaces200ResponseInner> result = apiInstance.getDeviceSwitchRoutingInterfaces_2(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#getDeviceSwitchRoutingInterfaces_2");
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
| **serial** | **String**|  | |

### Return type

[**List&lt;GetDeviceSwitchRoutingInterfaces200ResponseInner&gt;**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchStackRoutingInterfaceDhcp_3"></a>
# **getNetworkSwitchStackRoutingInterfaceDhcp_3**
> Object getNetworkSwitchStackRoutingInterfaceDhcp_3(networkId, switchStackId, interfaceId)

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
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterfaceDhcp_3(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#getNetworkSwitchStackRoutingInterfaceDhcp_3");
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

<a id="getNetworkSwitchStackRoutingInterface_3"></a>
# **getNetworkSwitchStackRoutingInterface_3**
> Object getNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId)

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
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#getNetworkSwitchStackRoutingInterface_3");
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

<a id="getNetworkSwitchStackRoutingInterfaces_3"></a>
# **getNetworkSwitchStackRoutingInterfaces_3**
> List&lt;Object&gt; getNetworkSwitchStackRoutingInterfaces_3(networkId, switchStackId)

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
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStackRoutingInterfaces_3(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#getNetworkSwitchStackRoutingInterfaces_3");
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

<a id="updateDeviceSwitchRoutingInterfaceDhcp_2"></a>
# **updateDeviceSwitchRoutingInterfaceDhcp_2**
> Object updateDeviceSwitchRoutingInterfaceDhcp_2(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest)

Update a layer 3 interface DHCP configuration for a switch

Update a layer 3 interface DHCP configuration for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateDeviceSwitchRoutingInterfaceDhcpRequest updateDeviceSwitchRoutingInterfaceDhcpRequest = new UpdateDeviceSwitchRoutingInterfaceDhcpRequest(); // UpdateDeviceSwitchRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateDeviceSwitchRoutingInterfaceDhcp_2(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#updateDeviceSwitchRoutingInterfaceDhcp_2");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |
| **updateDeviceSwitchRoutingInterfaceDhcpRequest** | [**UpdateDeviceSwitchRoutingInterfaceDhcpRequest**](UpdateDeviceSwitchRoutingInterfaceDhcpRequest.md)|  | [optional] |

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

<a id="updateDeviceSwitchRoutingInterface_2"></a>
# **updateDeviceSwitchRoutingInterface_2**
> GetDeviceSwitchRoutingInterfaces200ResponseInner updateDeviceSwitchRoutingInterface_2(serial, interfaceId, createDeviceSwitchRoutingInterfaceRequest)

Update a layer 3 interface for a switch

Update a layer 3 interface for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = new CreateDeviceSwitchRoutingInterfaceRequest(); // CreateDeviceSwitchRoutingInterfaceRequest | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.updateDeviceSwitchRoutingInterface_2(serial, interfaceId, createDeviceSwitchRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#updateDeviceSwitchRoutingInterface_2");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |
| **createDeviceSwitchRoutingInterfaceRequest** | [**CreateDeviceSwitchRoutingInterfaceRequest**](CreateDeviceSwitchRoutingInterfaceRequest.md)|  | [optional] |

### Return type

[**GetDeviceSwitchRoutingInterfaces200ResponseInner**](GetDeviceSwitchRoutingInterfaces200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStackRoutingInterfaceDhcp_3"></a>
# **updateNetworkSwitchStackRoutingInterfaceDhcp_3**
> Object updateNetworkSwitchStackRoutingInterfaceDhcp_3(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest)

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
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest updateNetworkSwitchStackRoutingInterfaceDhcpRequest = new UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest(); // UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterfaceDhcp_3(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#updateNetworkSwitchStackRoutingInterfaceDhcp_3");
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

<a id="updateNetworkSwitchStackRoutingInterface_3"></a>
# **updateNetworkSwitchStackRoutingInterface_3**
> Object updateNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest)

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
import org.openapitools.client.api.InterfacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InterfacesApi apiInstance = new InterfacesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceRequest updateNetworkSwitchStackRoutingInterfaceRequest = new UpdateNetworkSwitchStackRoutingInterfaceRequest(); // UpdateNetworkSwitchStackRoutingInterfaceRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InterfacesApi#updateNetworkSwitchStackRoutingInterface_3");
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

