# AlternateManagementInterfaceApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSwitchAlternateManagementInterface_1**](AlternateManagementInterfaceApi.md#getNetworkSwitchAlternateManagementInterface_1) | **GET** /networks/{networkId}/switch/alternateManagementInterface | Return the switch alternate management interface for the network |
| [**getNetworkWirelessAlternateManagementInterface_1**](AlternateManagementInterfaceApi.md#getNetworkWirelessAlternateManagementInterface_1) | **GET** /networks/{networkId}/wireless/alternateManagementInterface | Return alternate management interface and devices with IP assigned |
| [**updateNetworkSwitchAlternateManagementInterface_1**](AlternateManagementInterfaceApi.md#updateNetworkSwitchAlternateManagementInterface_1) | **PUT** /networks/{networkId}/switch/alternateManagementInterface | Update the switch alternate management interface for the network |
| [**updateNetworkWirelessAlternateManagementInterface_1**](AlternateManagementInterfaceApi.md#updateNetworkWirelessAlternateManagementInterface_1) | **PUT** /networks/{networkId}/wireless/alternateManagementInterface | Update alternate management interface and device static IP |


<a id="getNetworkSwitchAlternateManagementInterface_1"></a>
# **getNetworkSwitchAlternateManagementInterface_1**
> Object getNetworkSwitchAlternateManagementInterface_1(networkId)

Return the switch alternate management interface for the network

Return the switch alternate management interface for the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlternateManagementInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AlternateManagementInterfaceApi apiInstance = new AlternateManagementInterfaceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchAlternateManagementInterface_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlternateManagementInterfaceApi#getNetworkSwitchAlternateManagementInterface_1");
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

<a id="getNetworkWirelessAlternateManagementInterface_1"></a>
# **getNetworkWirelessAlternateManagementInterface_1**
> Object getNetworkWirelessAlternateManagementInterface_1(networkId)

Return alternate management interface and devices with IP assigned

Return alternate management interface and devices with IP assigned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlternateManagementInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AlternateManagementInterfaceApi apiInstance = new AlternateManagementInterfaceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessAlternateManagementInterface_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlternateManagementInterfaceApi#getNetworkWirelessAlternateManagementInterface_1");
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

<a id="updateNetworkSwitchAlternateManagementInterface_1"></a>
# **updateNetworkSwitchAlternateManagementInterface_1**
> Object updateNetworkSwitchAlternateManagementInterface_1(networkId, updateNetworkSwitchAlternateManagementInterfaceRequest)

Update the switch alternate management interface for the network

Update the switch alternate management interface for the network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlternateManagementInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AlternateManagementInterfaceApi apiInstance = new AlternateManagementInterfaceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchAlternateManagementInterfaceRequest updateNetworkSwitchAlternateManagementInterfaceRequest = new UpdateNetworkSwitchAlternateManagementInterfaceRequest(); // UpdateNetworkSwitchAlternateManagementInterfaceRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchAlternateManagementInterface_1(networkId, updateNetworkSwitchAlternateManagementInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlternateManagementInterfaceApi#updateNetworkSwitchAlternateManagementInterface_1");
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
| **updateNetworkSwitchAlternateManagementInterfaceRequest** | [**UpdateNetworkSwitchAlternateManagementInterfaceRequest**](UpdateNetworkSwitchAlternateManagementInterfaceRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessAlternateManagementInterface_1"></a>
# **updateNetworkWirelessAlternateManagementInterface_1**
> Object updateNetworkWirelessAlternateManagementInterface_1(networkId, updateNetworkWirelessAlternateManagementInterfaceRequest)

Update alternate management interface and device static IP

Update alternate management interface and device static IP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlternateManagementInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AlternateManagementInterfaceApi apiInstance = new AlternateManagementInterfaceApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkWirelessAlternateManagementInterfaceRequest updateNetworkWirelessAlternateManagementInterfaceRequest = new UpdateNetworkWirelessAlternateManagementInterfaceRequest(); // UpdateNetworkWirelessAlternateManagementInterfaceRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessAlternateManagementInterface_1(networkId, updateNetworkWirelessAlternateManagementInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlternateManagementInterfaceApi#updateNetworkWirelessAlternateManagementInterface_1");
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
| **updateNetworkWirelessAlternateManagementInterfaceRequest** | [**UpdateNetworkWirelessAlternateManagementInterfaceRequest**](UpdateNetworkWirelessAlternateManagementInterfaceRequest.md)|  | [optional] |

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

