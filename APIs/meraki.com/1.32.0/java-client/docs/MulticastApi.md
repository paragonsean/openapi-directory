# MulticastApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchRoutingMulticastRendezvousPoint_2**](MulticastApi.md#createNetworkSwitchRoutingMulticastRendezvousPoint_2) | **POST** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | Create a multicast rendezvous point |
| [**deleteNetworkSwitchRoutingMulticastRendezvousPoint_2**](MulticastApi.md#deleteNetworkSwitchRoutingMulticastRendezvousPoint_2) | **DELETE** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Delete a multicast rendezvous point |
| [**getNetworkSwitchRoutingMulticastRendezvousPoint_2**](MulticastApi.md#getNetworkSwitchRoutingMulticastRendezvousPoint_2) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Return a multicast rendezvous point |
| [**getNetworkSwitchRoutingMulticastRendezvousPoints_2**](MulticastApi.md#getNetworkSwitchRoutingMulticastRendezvousPoints_2) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | List multicast rendezvous points |
| [**getNetworkSwitchRoutingMulticast_2**](MulticastApi.md#getNetworkSwitchRoutingMulticast_2) | **GET** /networks/{networkId}/switch/routing/multicast | Return multicast settings for a network |
| [**updateNetworkSwitchRoutingMulticastRendezvousPoint_2**](MulticastApi.md#updateNetworkSwitchRoutingMulticastRendezvousPoint_2) | **PUT** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Update a multicast rendezvous point |
| [**updateNetworkSwitchRoutingMulticast_2**](MulticastApi.md#updateNetworkSwitchRoutingMulticast_2) | **PUT** /networks/{networkId}/switch/routing/multicast | Update multicast settings for a network |


<a id="createNetworkSwitchRoutingMulticastRendezvousPoint_2"></a>
# **createNetworkSwitchRoutingMulticastRendezvousPoint_2**
> Object createNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest)

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
import org.openapitools.client.api.MulticastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MulticastApi apiInstance = new MulticastApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchRoutingMulticastRendezvousPointRequest createNetworkSwitchRoutingMulticastRendezvousPointRequest = new CreateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // CreateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MulticastApi#createNetworkSwitchRoutingMulticastRendezvousPoint_2");
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

<a id="deleteNetworkSwitchRoutingMulticastRendezvousPoint_2"></a>
# **deleteNetworkSwitchRoutingMulticastRendezvousPoint_2**
> deleteNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId)

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
import org.openapitools.client.api.MulticastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MulticastApi apiInstance = new MulticastApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MulticastApi#deleteNetworkSwitchRoutingMulticastRendezvousPoint_2");
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

<a id="getNetworkSwitchRoutingMulticastRendezvousPoint_2"></a>
# **getNetworkSwitchRoutingMulticastRendezvousPoint_2**
> Object getNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId)

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
import org.openapitools.client.api.MulticastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MulticastApi apiInstance = new MulticastApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MulticastApi#getNetworkSwitchRoutingMulticastRendezvousPoint_2");
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

<a id="getNetworkSwitchRoutingMulticastRendezvousPoints_2"></a>
# **getNetworkSwitchRoutingMulticastRendezvousPoints_2**
> List&lt;List&lt;Object&gt;&gt; getNetworkSwitchRoutingMulticastRendezvousPoints_2(networkId)

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
import org.openapitools.client.api.MulticastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MulticastApi apiInstance = new MulticastApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<List<Object>> result = apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoints_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MulticastApi#getNetworkSwitchRoutingMulticastRendezvousPoints_2");
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

<a id="getNetworkSwitchRoutingMulticast_2"></a>
# **getNetworkSwitchRoutingMulticast_2**
> Object getNetworkSwitchRoutingMulticast_2(networkId)

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
import org.openapitools.client.api.MulticastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MulticastApi apiInstance = new MulticastApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingMulticast_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MulticastApi#getNetworkSwitchRoutingMulticast_2");
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

<a id="updateNetworkSwitchRoutingMulticastRendezvousPoint_2"></a>
# **updateNetworkSwitchRoutingMulticastRendezvousPoint_2**
> Object updateNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest)

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
import org.openapitools.client.api.MulticastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MulticastApi apiInstance = new MulticastApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest updateNetworkSwitchRoutingMulticastRendezvousPointRequest = new UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MulticastApi#updateNetworkSwitchRoutingMulticastRendezvousPoint_2");
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

<a id="updateNetworkSwitchRoutingMulticast_2"></a>
# **updateNetworkSwitchRoutingMulticast_2**
> Object updateNetworkSwitchRoutingMulticast_2(networkId, updateNetworkSwitchRoutingMulticastRequest)

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
import org.openapitools.client.api.MulticastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MulticastApi apiInstance = new MulticastApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchRoutingMulticastRequest updateNetworkSwitchRoutingMulticastRequest = new UpdateNetworkSwitchRoutingMulticastRequest(); // UpdateNetworkSwitchRoutingMulticastRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingMulticast_2(networkId, updateNetworkSwitchRoutingMulticastRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MulticastApi#updateNetworkSwitchRoutingMulticast_2");
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

