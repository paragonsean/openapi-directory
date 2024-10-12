# RoutingApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceSwitchRoutingInterface_1**](RoutingApi.md#createDeviceSwitchRoutingInterface_1) | **POST** /devices/{serial}/switch/routing/interfaces | Create a layer 3 interface for a switch |
| [**createDeviceSwitchRoutingStaticRoute_1**](RoutingApi.md#createDeviceSwitchRoutingStaticRoute_1) | **POST** /devices/{serial}/switch/routing/staticRoutes | Create a layer 3 static route for a switch |
| [**createNetworkSwitchRoutingMulticastRendezvousPoint_1**](RoutingApi.md#createNetworkSwitchRoutingMulticastRendezvousPoint_1) | **POST** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | Create a multicast rendezvous point |
| [**createNetworkSwitchStackRoutingInterface_2**](RoutingApi.md#createNetworkSwitchStackRoutingInterface_2) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | Create a layer 3 interface for a switch stack |
| [**createNetworkSwitchStackRoutingStaticRoute_2**](RoutingApi.md#createNetworkSwitchStackRoutingStaticRoute_2) | **POST** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes | Create a layer 3 static route for a switch stack |
| [**deleteDeviceSwitchRoutingInterface_1**](RoutingApi.md#deleteDeviceSwitchRoutingInterface_1) | **DELETE** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Delete a layer 3 interface from the switch |
| [**deleteDeviceSwitchRoutingStaticRoute_1**](RoutingApi.md#deleteDeviceSwitchRoutingStaticRoute_1) | **DELETE** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Delete a layer 3 static route for a switch |
| [**deleteNetworkSwitchRoutingMulticastRendezvousPoint_1**](RoutingApi.md#deleteNetworkSwitchRoutingMulticastRendezvousPoint_1) | **DELETE** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Delete a multicast rendezvous point |
| [**deleteNetworkSwitchStackRoutingInterface_2**](RoutingApi.md#deleteNetworkSwitchStackRoutingInterface_2) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Delete a layer 3 interface from a switch stack |
| [**deleteNetworkSwitchStackRoutingStaticRoute_2**](RoutingApi.md#deleteNetworkSwitchStackRoutingStaticRoute_2) | **DELETE** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Delete a layer 3 static route for a switch stack |
| [**getDeviceSwitchRoutingInterfaceDhcp_1**](RoutingApi.md#getDeviceSwitchRoutingInterfaceDhcp_1) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch |
| [**getDeviceSwitchRoutingInterface_1**](RoutingApi.md#getDeviceSwitchRoutingInterface_1) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Return a layer 3 interface for a switch |
| [**getDeviceSwitchRoutingInterfaces_1**](RoutingApi.md#getDeviceSwitchRoutingInterfaces_1) | **GET** /devices/{serial}/switch/routing/interfaces | List layer 3 interfaces for a switch |
| [**getDeviceSwitchRoutingStaticRoute_1**](RoutingApi.md#getDeviceSwitchRoutingStaticRoute_1) | **GET** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Return a layer 3 static route for a switch |
| [**getDeviceSwitchRoutingStaticRoutes_1**](RoutingApi.md#getDeviceSwitchRoutingStaticRoutes_1) | **GET** /devices/{serial}/switch/routing/staticRoutes | List layer 3 static routes for a switch |
| [**getNetworkSwitchRoutingMulticastRendezvousPoint_1**](RoutingApi.md#getNetworkSwitchRoutingMulticastRendezvousPoint_1) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Return a multicast rendezvous point |
| [**getNetworkSwitchRoutingMulticastRendezvousPoints_1**](RoutingApi.md#getNetworkSwitchRoutingMulticastRendezvousPoints_1) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | List multicast rendezvous points |
| [**getNetworkSwitchRoutingMulticast_1**](RoutingApi.md#getNetworkSwitchRoutingMulticast_1) | **GET** /networks/{networkId}/switch/routing/multicast | Return multicast settings for a network |
| [**getNetworkSwitchRoutingOspf_1**](RoutingApi.md#getNetworkSwitchRoutingOspf_1) | **GET** /networks/{networkId}/switch/routing/ospf | Return layer 3 OSPF routing configuration |
| [**getNetworkSwitchStackRoutingInterfaceDhcp_2**](RoutingApi.md#getNetworkSwitchStackRoutingInterfaceDhcp_2) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch stack |
| [**getNetworkSwitchStackRoutingInterface_2**](RoutingApi.md#getNetworkSwitchStackRoutingInterface_2) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Return a layer 3 interface from a switch stack |
| [**getNetworkSwitchStackRoutingInterfaces_2**](RoutingApi.md#getNetworkSwitchStackRoutingInterfaces_2) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces | List layer 3 interfaces for a switch stack |
| [**getNetworkSwitchStackRoutingStaticRoute_2**](RoutingApi.md#getNetworkSwitchStackRoutingStaticRoute_2) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Return a layer 3 static route for a switch stack |
| [**getNetworkSwitchStackRoutingStaticRoutes_2**](RoutingApi.md#getNetworkSwitchStackRoutingStaticRoutes_2) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes | List layer 3 static routes for a switch stack |
| [**updateDeviceSwitchRoutingInterfaceDhcp_1**](RoutingApi.md#updateDeviceSwitchRoutingInterfaceDhcp_1) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch |
| [**updateDeviceSwitchRoutingInterface_1**](RoutingApi.md#updateDeviceSwitchRoutingInterface_1) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch |
| [**updateDeviceSwitchRoutingStaticRoute_1**](RoutingApi.md#updateDeviceSwitchRoutingStaticRoute_1) | **PUT** /devices/{serial}/switch/routing/staticRoutes/{staticRouteId} | Update a layer 3 static route for a switch |
| [**updateNetworkSwitchRoutingMulticastRendezvousPoint_1**](RoutingApi.md#updateNetworkSwitchRoutingMulticastRendezvousPoint_1) | **PUT** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Update a multicast rendezvous point |
| [**updateNetworkSwitchRoutingMulticast_1**](RoutingApi.md#updateNetworkSwitchRoutingMulticast_1) | **PUT** /networks/{networkId}/switch/routing/multicast | Update multicast settings for a network |
| [**updateNetworkSwitchRoutingOspf_1**](RoutingApi.md#updateNetworkSwitchRoutingOspf_1) | **PUT** /networks/{networkId}/switch/routing/ospf | Update layer 3 OSPF routing configuration |
| [**updateNetworkSwitchStackRoutingInterfaceDhcp_2**](RoutingApi.md#updateNetworkSwitchStackRoutingInterfaceDhcp_2) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch stack |
| [**updateNetworkSwitchStackRoutingInterface_2**](RoutingApi.md#updateNetworkSwitchStackRoutingInterface_2) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId} | Update a layer 3 interface for a switch stack |
| [**updateNetworkSwitchStackRoutingStaticRoute_2**](RoutingApi.md#updateNetworkSwitchStackRoutingStaticRoute_2) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId} | Update a layer 3 static route for a switch stack |


<a id="createDeviceSwitchRoutingInterface_1"></a>
# **createDeviceSwitchRoutingInterface_1**
> GetDeviceSwitchRoutingInterfaces200ResponseInner createDeviceSwitchRoutingInterface_1(serial, createDeviceSwitchRoutingInterfaceRequest)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = new CreateDeviceSwitchRoutingInterfaceRequest(); // CreateDeviceSwitchRoutingInterfaceRequest | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.createDeviceSwitchRoutingInterface_1(serial, createDeviceSwitchRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#createDeviceSwitchRoutingInterface_1");
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

<a id="createDeviceSwitchRoutingStaticRoute_1"></a>
# **createDeviceSwitchRoutingStaticRoute_1**
> Object createDeviceSwitchRoutingStaticRoute_1(serial, createDeviceSwitchRoutingStaticRouteRequest)

Create a layer 3 static route for a switch

Create a layer 3 static route for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceSwitchRoutingStaticRouteRequest createDeviceSwitchRoutingStaticRouteRequest = new CreateDeviceSwitchRoutingStaticRouteRequest(); // CreateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.createDeviceSwitchRoutingStaticRoute_1(serial, createDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#createDeviceSwitchRoutingStaticRoute_1");
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

<a id="createNetworkSwitchRoutingMulticastRendezvousPoint_1"></a>
# **createNetworkSwitchRoutingMulticastRendezvousPoint_1**
> Object createNetworkSwitchRoutingMulticastRendezvousPoint_1(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest)

Create a multicast rendezvous point

Create a multicast rendezvous point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchRoutingMulticastRendezvousPointRequest createNetworkSwitchRoutingMulticastRendezvousPointRequest = new CreateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // CreateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchRoutingMulticastRendezvousPoint_1(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#createNetworkSwitchRoutingMulticastRendezvousPoint_1");
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
| **createNetworkSwitchRoutingMulticastRendezvousPointRequest** | [**CreateNetworkSwitchRoutingMulticastRendezvousPointRequest**](CreateNetworkSwitchRoutingMulticastRendezvousPointRequest.md)|  | |

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

<a id="createNetworkSwitchStackRoutingInterface_2"></a>
# **createNetworkSwitchStackRoutingInterface_2**
> Object createNetworkSwitchStackRoutingInterface_2(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    CreateNetworkSwitchStackRoutingInterfaceRequest createNetworkSwitchStackRoutingInterfaceRequest = new CreateNetworkSwitchStackRoutingInterfaceRequest(); // CreateNetworkSwitchStackRoutingInterfaceRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStackRoutingInterface_2(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#createNetworkSwitchStackRoutingInterface_2");
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

<a id="createNetworkSwitchStackRoutingStaticRoute_2"></a>
# **createNetworkSwitchStackRoutingStaticRoute_2**
> Object createNetworkSwitchStackRoutingStaticRoute_2(networkId, switchStackId, createDeviceSwitchRoutingStaticRouteRequest)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    CreateDeviceSwitchRoutingStaticRouteRequest createDeviceSwitchRoutingStaticRouteRequest = new CreateDeviceSwitchRoutingStaticRouteRequest(); // CreateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchStackRoutingStaticRoute_2(networkId, switchStackId, createDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#createNetworkSwitchStackRoutingStaticRoute_2");
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

<a id="deleteDeviceSwitchRoutingInterface_1"></a>
# **deleteDeviceSwitchRoutingInterface_1**
> deleteDeviceSwitchRoutingInterface_1(serial, interfaceId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      apiInstance.deleteDeviceSwitchRoutingInterface_1(serial, interfaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#deleteDeviceSwitchRoutingInterface_1");
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

<a id="deleteDeviceSwitchRoutingStaticRoute_1"></a>
# **deleteDeviceSwitchRoutingStaticRoute_1**
> deleteDeviceSwitchRoutingStaticRoute_1(serial, staticRouteId)

Delete a layer 3 static route for a switch

Delete a layer 3 static route for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      apiInstance.deleteDeviceSwitchRoutingStaticRoute_1(serial, staticRouteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#deleteDeviceSwitchRoutingStaticRoute_1");
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

<a id="deleteNetworkSwitchRoutingMulticastRendezvousPoint_1"></a>
# **deleteNetworkSwitchRoutingMulticastRendezvousPoint_1**
> deleteNetworkSwitchRoutingMulticastRendezvousPoint_1(networkId, rendezvousPointId)

Delete a multicast rendezvous point

Delete a multicast rendezvous point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchRoutingMulticastRendezvousPoint_1(networkId, rendezvousPointId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#deleteNetworkSwitchRoutingMulticastRendezvousPoint_1");
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
| **rendezvousPointId** | **String**|  | |

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

<a id="deleteNetworkSwitchStackRoutingInterface_2"></a>
# **deleteNetworkSwitchStackRoutingInterface_2**
> deleteNetworkSwitchStackRoutingInterface_2(networkId, switchStackId, interfaceId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStackRoutingInterface_2(networkId, switchStackId, interfaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#deleteNetworkSwitchStackRoutingInterface_2");
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

<a id="deleteNetworkSwitchStackRoutingStaticRoute_2"></a>
# **deleteNetworkSwitchStackRoutingStaticRoute_2**
> deleteNetworkSwitchStackRoutingStaticRoute_2(networkId, switchStackId, staticRouteId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchStackRoutingStaticRoute_2(networkId, switchStackId, staticRouteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#deleteNetworkSwitchStackRoutingStaticRoute_2");
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

<a id="getDeviceSwitchRoutingInterfaceDhcp_1"></a>
# **getDeviceSwitchRoutingInterfaceDhcp_1**
> Object getDeviceSwitchRoutingInterfaceDhcp_1(serial, interfaceId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getDeviceSwitchRoutingInterfaceDhcp_1(serial, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getDeviceSwitchRoutingInterfaceDhcp_1");
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

<a id="getDeviceSwitchRoutingInterface_1"></a>
# **getDeviceSwitchRoutingInterface_1**
> GetDeviceSwitchRoutingInterfaces200ResponseInner getDeviceSwitchRoutingInterface_1(serial, interfaceId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.getDeviceSwitchRoutingInterface_1(serial, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getDeviceSwitchRoutingInterface_1");
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

<a id="getDeviceSwitchRoutingInterfaces_1"></a>
# **getDeviceSwitchRoutingInterfaces_1**
> List&lt;GetDeviceSwitchRoutingInterfaces200ResponseInner&gt; getDeviceSwitchRoutingInterfaces_1(serial)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<GetDeviceSwitchRoutingInterfaces200ResponseInner> result = apiInstance.getDeviceSwitchRoutingInterfaces_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getDeviceSwitchRoutingInterfaces_1");
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

<a id="getDeviceSwitchRoutingStaticRoute_1"></a>
# **getDeviceSwitchRoutingStaticRoute_1**
> GetDeviceSwitchRoutingStaticRoute200Response getDeviceSwitchRoutingStaticRoute_1(serial, staticRouteId)

Return a layer 3 static route for a switch

Return a layer 3 static route for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      GetDeviceSwitchRoutingStaticRoute200Response result = apiInstance.getDeviceSwitchRoutingStaticRoute_1(serial, staticRouteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getDeviceSwitchRoutingStaticRoute_1");
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
| **staticRouteId** | **String**|  | |

### Return type

[**GetDeviceSwitchRoutingStaticRoute200Response**](GetDeviceSwitchRoutingStaticRoute200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchRoutingStaticRoutes_1"></a>
# **getDeviceSwitchRoutingStaticRoutes_1**
> List&lt;Object&gt; getDeviceSwitchRoutingStaticRoutes_1(serial)

List layer 3 static routes for a switch

List layer 3 static routes for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceSwitchRoutingStaticRoutes_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getDeviceSwitchRoutingStaticRoutes_1");
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

<a id="getNetworkSwitchRoutingMulticastRendezvousPoint_1"></a>
# **getNetworkSwitchRoutingMulticastRendezvousPoint_1**
> Object getNetworkSwitchRoutingMulticastRendezvousPoint_1(networkId, rendezvousPointId)

Return a multicast rendezvous point

Return a multicast rendezvous point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoint_1(networkId, rendezvousPointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchRoutingMulticastRendezvousPoint_1");
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
| **rendezvousPointId** | **String**|  | |

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

<a id="getNetworkSwitchRoutingMulticastRendezvousPoints_1"></a>
# **getNetworkSwitchRoutingMulticastRendezvousPoints_1**
> List&lt;List&lt;Object&gt;&gt; getNetworkSwitchRoutingMulticastRendezvousPoints_1(networkId)

List multicast rendezvous points

List multicast rendezvous points

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<List<Object>> result = apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoints_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchRoutingMulticastRendezvousPoints_1");
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

[**List&lt;List&lt;Object&gt;&gt;**](List.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchRoutingMulticast_1"></a>
# **getNetworkSwitchRoutingMulticast_1**
> Object getNetworkSwitchRoutingMulticast_1(networkId)

Return multicast settings for a network

Return multicast settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingMulticast_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchRoutingMulticast_1");
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

<a id="getNetworkSwitchRoutingOspf_1"></a>
# **getNetworkSwitchRoutingOspf_1**
> Object getNetworkSwitchRoutingOspf_1(networkId)

Return layer 3 OSPF routing configuration

Return layer 3 OSPF routing configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingOspf_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchRoutingOspf_1");
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

<a id="getNetworkSwitchStackRoutingInterfaceDhcp_2"></a>
# **getNetworkSwitchStackRoutingInterfaceDhcp_2**
> Object getNetworkSwitchStackRoutingInterfaceDhcp_2(networkId, switchStackId, interfaceId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterfaceDhcp_2(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchStackRoutingInterfaceDhcp_2");
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

<a id="getNetworkSwitchStackRoutingInterface_2"></a>
# **getNetworkSwitchStackRoutingInterface_2**
> Object getNetworkSwitchStackRoutingInterface_2(networkId, switchStackId, interfaceId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterface_2(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchStackRoutingInterface_2");
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

<a id="getNetworkSwitchStackRoutingInterfaces_2"></a>
# **getNetworkSwitchStackRoutingInterfaces_2**
> List&lt;Object&gt; getNetworkSwitchStackRoutingInterfaces_2(networkId, switchStackId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStackRoutingInterfaces_2(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchStackRoutingInterfaces_2");
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

<a id="getNetworkSwitchStackRoutingStaticRoute_2"></a>
# **getNetworkSwitchStackRoutingStaticRoute_2**
> Object getNetworkSwitchStackRoutingStaticRoute_2(networkId, switchStackId, staticRouteId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingStaticRoute_2(networkId, switchStackId, staticRouteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchStackRoutingStaticRoute_2");
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

<a id="getNetworkSwitchStackRoutingStaticRoutes_2"></a>
# **getNetworkSwitchStackRoutingStaticRoutes_2**
> List&lt;Object&gt; getNetworkSwitchStackRoutingStaticRoutes_2(networkId, switchStackId)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchStackRoutingStaticRoutes_2(networkId, switchStackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#getNetworkSwitchStackRoutingStaticRoutes_2");
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

<a id="updateDeviceSwitchRoutingInterfaceDhcp_1"></a>
# **updateDeviceSwitchRoutingInterfaceDhcp_1**
> Object updateDeviceSwitchRoutingInterfaceDhcp_1(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateDeviceSwitchRoutingInterfaceDhcpRequest updateDeviceSwitchRoutingInterfaceDhcpRequest = new UpdateDeviceSwitchRoutingInterfaceDhcpRequest(); // UpdateDeviceSwitchRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateDeviceSwitchRoutingInterfaceDhcp_1(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateDeviceSwitchRoutingInterfaceDhcp_1");
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

<a id="updateDeviceSwitchRoutingInterface_1"></a>
# **updateDeviceSwitchRoutingInterface_1**
> GetDeviceSwitchRoutingInterfaces200ResponseInner updateDeviceSwitchRoutingInterface_1(serial, interfaceId, createDeviceSwitchRoutingInterfaceRequest)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = new CreateDeviceSwitchRoutingInterfaceRequest(); // CreateDeviceSwitchRoutingInterfaceRequest | 
    try {
      GetDeviceSwitchRoutingInterfaces200ResponseInner result = apiInstance.updateDeviceSwitchRoutingInterface_1(serial, interfaceId, createDeviceSwitchRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateDeviceSwitchRoutingInterface_1");
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

<a id="updateDeviceSwitchRoutingStaticRoute_1"></a>
# **updateDeviceSwitchRoutingStaticRoute_1**
> Object updateDeviceSwitchRoutingStaticRoute_1(serial, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest)

Update a layer 3 static route for a switch

Update a layer 3 static route for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    UpdateDeviceSwitchRoutingStaticRouteRequest updateDeviceSwitchRoutingStaticRouteRequest = new UpdateDeviceSwitchRoutingStaticRouteRequest(); // UpdateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.updateDeviceSwitchRoutingStaticRoute_1(serial, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateDeviceSwitchRoutingStaticRoute_1");
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

<a id="updateNetworkSwitchRoutingMulticastRendezvousPoint_1"></a>
# **updateNetworkSwitchRoutingMulticastRendezvousPoint_1**
> Object updateNetworkSwitchRoutingMulticastRendezvousPoint_1(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest)

Update a multicast rendezvous point

Update a multicast rendezvous point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest updateNetworkSwitchRoutingMulticastRendezvousPointRequest = new UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingMulticastRendezvousPoint_1(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateNetworkSwitchRoutingMulticastRendezvousPoint_1");
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
| **rendezvousPointId** | **String**|  | |
| **updateNetworkSwitchRoutingMulticastRendezvousPointRequest** | [**UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest**](UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest.md)|  | |

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

<a id="updateNetworkSwitchRoutingMulticast_1"></a>
# **updateNetworkSwitchRoutingMulticast_1**
> Object updateNetworkSwitchRoutingMulticast_1(networkId, updateNetworkSwitchRoutingMulticastRequest)

Update multicast settings for a network

Update multicast settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchRoutingMulticastRequest updateNetworkSwitchRoutingMulticastRequest = new UpdateNetworkSwitchRoutingMulticastRequest(); // UpdateNetworkSwitchRoutingMulticastRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingMulticast_1(networkId, updateNetworkSwitchRoutingMulticastRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateNetworkSwitchRoutingMulticast_1");
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
| **updateNetworkSwitchRoutingMulticastRequest** | [**UpdateNetworkSwitchRoutingMulticastRequest**](UpdateNetworkSwitchRoutingMulticastRequest.md)|  | [optional] |

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

<a id="updateNetworkSwitchRoutingOspf_1"></a>
# **updateNetworkSwitchRoutingOspf_1**
> Object updateNetworkSwitchRoutingOspf_1(networkId, updateNetworkSwitchRoutingOspfRequest)

Update layer 3 OSPF routing configuration

Update layer 3 OSPF routing configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchRoutingOspfRequest updateNetworkSwitchRoutingOspfRequest = new UpdateNetworkSwitchRoutingOspfRequest(); // UpdateNetworkSwitchRoutingOspfRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingOspf_1(networkId, updateNetworkSwitchRoutingOspfRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateNetworkSwitchRoutingOspf_1");
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
| **updateNetworkSwitchRoutingOspfRequest** | [**UpdateNetworkSwitchRoutingOspfRequest**](UpdateNetworkSwitchRoutingOspfRequest.md)|  | [optional] |

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

<a id="updateNetworkSwitchStackRoutingInterfaceDhcp_2"></a>
# **updateNetworkSwitchStackRoutingInterfaceDhcp_2**
> Object updateNetworkSwitchStackRoutingInterfaceDhcp_2(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest updateNetworkSwitchStackRoutingInterfaceDhcpRequest = new UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest(); // UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterfaceDhcp_2(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateNetworkSwitchStackRoutingInterfaceDhcp_2");
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

<a id="updateNetworkSwitchStackRoutingInterface_2"></a>
# **updateNetworkSwitchStackRoutingInterface_2**
> Object updateNetworkSwitchStackRoutingInterface_2(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceRequest updateNetworkSwitchStackRoutingInterfaceRequest = new UpdateNetworkSwitchStackRoutingInterfaceRequest(); // UpdateNetworkSwitchStackRoutingInterfaceRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterface_2(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateNetworkSwitchStackRoutingInterface_2");
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

<a id="updateNetworkSwitchStackRoutingStaticRoute_2"></a>
# **updateNetworkSwitchStackRoutingStaticRoute_2**
> Object updateNetworkSwitchStackRoutingStaticRoute_2(networkId, switchStackId, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest)

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
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String staticRouteId = "staticRouteId_example"; // String | 
    UpdateDeviceSwitchRoutingStaticRouteRequest updateDeviceSwitchRoutingStaticRouteRequest = new UpdateDeviceSwitchRoutingStaticRouteRequest(); // UpdateDeviceSwitchRoutingStaticRouteRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingStaticRoute_2(networkId, switchStackId, staticRouteId, updateDeviceSwitchRoutingStaticRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#updateNetworkSwitchStackRoutingStaticRoute_2");
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

