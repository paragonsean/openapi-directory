# RendezvousPointsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchRoutingMulticastRendezvousPoint_3**](RendezvousPointsApi.md#createNetworkSwitchRoutingMulticastRendezvousPoint_3) | **POST** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | Create a multicast rendezvous point |
| [**deleteNetworkSwitchRoutingMulticastRendezvousPoint_3**](RendezvousPointsApi.md#deleteNetworkSwitchRoutingMulticastRendezvousPoint_3) | **DELETE** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Delete a multicast rendezvous point |
| [**getNetworkSwitchRoutingMulticastRendezvousPoint_3**](RendezvousPointsApi.md#getNetworkSwitchRoutingMulticastRendezvousPoint_3) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Return a multicast rendezvous point |
| [**getNetworkSwitchRoutingMulticastRendezvousPoints_3**](RendezvousPointsApi.md#getNetworkSwitchRoutingMulticastRendezvousPoints_3) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | List multicast rendezvous points |
| [**updateNetworkSwitchRoutingMulticastRendezvousPoint_3**](RendezvousPointsApi.md#updateNetworkSwitchRoutingMulticastRendezvousPoint_3) | **PUT** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Update a multicast rendezvous point |


<a id="createNetworkSwitchRoutingMulticastRendezvousPoint_3"></a>
# **createNetworkSwitchRoutingMulticastRendezvousPoint_3**
> Object createNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest)

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
import org.openapitools.client.api.RendezvousPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RendezvousPointsApi apiInstance = new RendezvousPointsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchRoutingMulticastRendezvousPointRequest createNetworkSwitchRoutingMulticastRendezvousPointRequest = new CreateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // CreateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RendezvousPointsApi#createNetworkSwitchRoutingMulticastRendezvousPoint_3");
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

<a id="deleteNetworkSwitchRoutingMulticastRendezvousPoint_3"></a>
# **deleteNetworkSwitchRoutingMulticastRendezvousPoint_3**
> deleteNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId)

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
import org.openapitools.client.api.RendezvousPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RendezvousPointsApi apiInstance = new RendezvousPointsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RendezvousPointsApi#deleteNetworkSwitchRoutingMulticastRendezvousPoint_3");
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

<a id="getNetworkSwitchRoutingMulticastRendezvousPoint_3"></a>
# **getNetworkSwitchRoutingMulticastRendezvousPoint_3**
> Object getNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId)

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
import org.openapitools.client.api.RendezvousPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RendezvousPointsApi apiInstance = new RendezvousPointsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RendezvousPointsApi#getNetworkSwitchRoutingMulticastRendezvousPoint_3");
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

<a id="getNetworkSwitchRoutingMulticastRendezvousPoints_3"></a>
# **getNetworkSwitchRoutingMulticastRendezvousPoints_3**
> List&lt;List&lt;Object&gt;&gt; getNetworkSwitchRoutingMulticastRendezvousPoints_3(networkId)

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
import org.openapitools.client.api.RendezvousPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RendezvousPointsApi apiInstance = new RendezvousPointsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<List<Object>> result = apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoints_3(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RendezvousPointsApi#getNetworkSwitchRoutingMulticastRendezvousPoints_3");
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

<a id="updateNetworkSwitchRoutingMulticastRendezvousPoint_3"></a>
# **updateNetworkSwitchRoutingMulticastRendezvousPoint_3**
> Object updateNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest)

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
import org.openapitools.client.api.RendezvousPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RendezvousPointsApi apiInstance = new RendezvousPointsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String rendezvousPointId = "rendezvousPointId_example"; // String | 
    UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest updateNetworkSwitchRoutingMulticastRendezvousPointRequest = new UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RendezvousPointsApi#updateNetworkSwitchRoutingMulticastRendezvousPoint_3");
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

