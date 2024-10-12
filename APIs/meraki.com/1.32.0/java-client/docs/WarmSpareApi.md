# WarmSpareApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceSwitchWarmSpare_1**](WarmSpareApi.md#getDeviceSwitchWarmSpare_1) | **GET** /devices/{serial}/switch/warmSpare | Return warm spare configuration for a switch |
| [**getNetworkApplianceWarmSpare_1**](WarmSpareApi.md#getNetworkApplianceWarmSpare_1) | **GET** /networks/{networkId}/appliance/warmSpare | Return MX warm spare settings |
| [**swapNetworkApplianceWarmSpare_1**](WarmSpareApi.md#swapNetworkApplianceWarmSpare_1) | **POST** /networks/{networkId}/appliance/warmSpare/swap | Swap MX primary and warm spare appliances |
| [**updateDeviceSwitchWarmSpare_1**](WarmSpareApi.md#updateDeviceSwitchWarmSpare_1) | **PUT** /devices/{serial}/switch/warmSpare | Update warm spare configuration for a switch |
| [**updateNetworkApplianceWarmSpare_1**](WarmSpareApi.md#updateNetworkApplianceWarmSpare_1) | **PUT** /networks/{networkId}/appliance/warmSpare | Update MX warm spare settings |


<a id="getDeviceSwitchWarmSpare_1"></a>
# **getDeviceSwitchWarmSpare_1**
> Object getDeviceSwitchWarmSpare_1(serial)

Return warm spare configuration for a switch

Return warm spare configuration for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarmSpareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WarmSpareApi apiInstance = new WarmSpareApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceSwitchWarmSpare_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarmSpareApi#getDeviceSwitchWarmSpare_1");
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

<a id="getNetworkApplianceWarmSpare_1"></a>
# **getNetworkApplianceWarmSpare_1**
> Object getNetworkApplianceWarmSpare_1(networkId)

Return MX warm spare settings

Return MX warm spare settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarmSpareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WarmSpareApi apiInstance = new WarmSpareApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceWarmSpare_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarmSpareApi#getNetworkApplianceWarmSpare_1");
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

<a id="swapNetworkApplianceWarmSpare_1"></a>
# **swapNetworkApplianceWarmSpare_1**
> Object swapNetworkApplianceWarmSpare_1(networkId)

Swap MX primary and warm spare appliances

Swap MX primary and warm spare appliances

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarmSpareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WarmSpareApi apiInstance = new WarmSpareApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.swapNetworkApplianceWarmSpare_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarmSpareApi#swapNetworkApplianceWarmSpare_1");
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

<a id="updateDeviceSwitchWarmSpare_1"></a>
# **updateDeviceSwitchWarmSpare_1**
> Object updateDeviceSwitchWarmSpare_1(serial, updateDeviceSwitchWarmSpareRequest)

Update warm spare configuration for a switch

Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarmSpareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WarmSpareApi apiInstance = new WarmSpareApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceSwitchWarmSpareRequest updateDeviceSwitchWarmSpareRequest = new UpdateDeviceSwitchWarmSpareRequest(); // UpdateDeviceSwitchWarmSpareRequest | 
    try {
      Object result = apiInstance.updateDeviceSwitchWarmSpare_1(serial, updateDeviceSwitchWarmSpareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarmSpareApi#updateDeviceSwitchWarmSpare_1");
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
| **updateDeviceSwitchWarmSpareRequest** | [**UpdateDeviceSwitchWarmSpareRequest**](UpdateDeviceSwitchWarmSpareRequest.md)|  | |

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

<a id="updateNetworkApplianceWarmSpare_1"></a>
# **updateNetworkApplianceWarmSpare_1**
> Object updateNetworkApplianceWarmSpare_1(networkId, updateNetworkApplianceWarmSpareRequest)

Update MX warm spare settings

Update MX warm spare settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarmSpareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WarmSpareApi apiInstance = new WarmSpareApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceWarmSpareRequest updateNetworkApplianceWarmSpareRequest = new UpdateNetworkApplianceWarmSpareRequest(); // UpdateNetworkApplianceWarmSpareRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceWarmSpare_1(networkId, updateNetworkApplianceWarmSpareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarmSpareApi#updateNetworkApplianceWarmSpare_1");
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
| **updateNetworkApplianceWarmSpareRequest** | [**UpdateNetworkApplianceWarmSpareRequest**](UpdateNetworkApplianceWarmSpareRequest.md)|  | |

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

