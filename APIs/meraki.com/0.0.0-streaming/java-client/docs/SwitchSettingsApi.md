# SwitchSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchSettingsQosRule**](SwitchSettingsApi.md#createNetworkSwitchSettingsQosRule) | **POST** /networks/{networkId}/switch/settings/qosRules | Add a quality of service rule |
| [**deleteNetworkSwitchSettingsQosRule**](SwitchSettingsApi.md#deleteNetworkSwitchSettingsQosRule) | **DELETE** /networks/{networkId}/switch/settings/qosRules/{qosRuleId} | Delete a quality of service rule |
| [**getNetworkSwitchSettings**](SwitchSettingsApi.md#getNetworkSwitchSettings) | **GET** /networks/{networkId}/switch/settings | Returns the switch network settings |
| [**getNetworkSwitchSettingsMtu**](SwitchSettingsApi.md#getNetworkSwitchSettingsMtu) | **GET** /networks/{networkId}/switch/settings/mtu | Return the MTU configuration |
| [**getNetworkSwitchSettingsMulticast**](SwitchSettingsApi.md#getNetworkSwitchSettingsMulticast) | **GET** /networks/{networkId}/switch/settings/multicast | Return multicast settings for a network |
| [**getNetworkSwitchSettingsQosRule**](SwitchSettingsApi.md#getNetworkSwitchSettingsQosRule) | **GET** /networks/{networkId}/switch/settings/qosRules/{qosRuleId} | Return a quality of service rule |
| [**getNetworkSwitchSettingsQosRules**](SwitchSettingsApi.md#getNetworkSwitchSettingsQosRules) | **GET** /networks/{networkId}/switch/settings/qosRules | List quality of service rules |
| [**getNetworkSwitchSettingsQosRulesOrder**](SwitchSettingsApi.md#getNetworkSwitchSettingsQosRulesOrder) | **GET** /networks/{networkId}/switch/settings/qosRules/order | Return the quality of service rule IDs by order in which they will be processed by the switch |
| [**getNetworkSwitchSettingsStormControl**](SwitchSettingsApi.md#getNetworkSwitchSettingsStormControl) | **GET** /networks/{networkId}/switch/settings/stormControl | Return the storm control configuration for a switch network |
| [**updateNetworkSwitchSettings**](SwitchSettingsApi.md#updateNetworkSwitchSettings) | **PUT** /networks/{networkId}/switch/settings | Update switch network settings |
| [**updateNetworkSwitchSettingsMulticast**](SwitchSettingsApi.md#updateNetworkSwitchSettingsMulticast) | **PUT** /networks/{networkId}/switch/settings/multicast | Update multicast settings for a network |
| [**updateNetworkSwitchSettingsQosRule**](SwitchSettingsApi.md#updateNetworkSwitchSettingsQosRule) | **PUT** /networks/{networkId}/switch/settings/qosRules/{qosRuleId} | Update a quality of service rule |
| [**updateNetworkSwitchSettingsQosRulesOrder**](SwitchSettingsApi.md#updateNetworkSwitchSettingsQosRulesOrder) | **PUT** /networks/{networkId}/switch/settings/qosRules/order | Update the order in which the rules should be processed by the switch |
| [**updateNetworkSwitchSettingsStormControl**](SwitchSettingsApi.md#updateNetworkSwitchSettingsStormControl) | **PUT** /networks/{networkId}/switch/settings/stormControl | Update the storm control configuration for a switch network |


<a id="createNetworkSwitchSettingsQosRule"></a>
# **createNetworkSwitchSettingsQosRule**
> Object createNetworkSwitchSettingsQosRule(networkId, createNetworkSwitchSettingsQosRuleRequest)

Add a quality of service rule

Add a quality of service rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchSettingsQosRuleRequest createNetworkSwitchSettingsQosRuleRequest = new CreateNetworkSwitchSettingsQosRuleRequest(); // CreateNetworkSwitchSettingsQosRuleRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchSettingsQosRule(networkId, createNetworkSwitchSettingsQosRuleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#createNetworkSwitchSettingsQosRule");
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
| **createNetworkSwitchSettingsQosRuleRequest** | [**CreateNetworkSwitchSettingsQosRuleRequest**](CreateNetworkSwitchSettingsQosRuleRequest.md)|  | |

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

<a id="deleteNetworkSwitchSettingsQosRule"></a>
# **deleteNetworkSwitchSettingsQosRule**
> deleteNetworkSwitchSettingsQosRule(networkId, qosRuleId)

Delete a quality of service rule

Delete a quality of service rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchSettingsQosRule(networkId, qosRuleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#deleteNetworkSwitchSettingsQosRule");
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
| **qosRuleId** | **String**|  | |

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

<a id="getNetworkSwitchSettings"></a>
# **getNetworkSwitchSettings**
> Object getNetworkSwitchSettings(networkId)

Returns the switch network settings

Returns the switch network settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#getNetworkSwitchSettings");
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

<a id="getNetworkSwitchSettingsMtu"></a>
# **getNetworkSwitchSettingsMtu**
> Object getNetworkSwitchSettingsMtu(networkId)

Return the MTU configuration

Return the MTU configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchSettingsMtu(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#getNetworkSwitchSettingsMtu");
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

<a id="getNetworkSwitchSettingsMulticast"></a>
# **getNetworkSwitchSettingsMulticast**
> Object getNetworkSwitchSettingsMulticast(networkId)

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
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchSettingsMulticast(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#getNetworkSwitchSettingsMulticast");
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

<a id="getNetworkSwitchSettingsQosRule"></a>
# **getNetworkSwitchSettingsQosRule**
> Object getNetworkSwitchSettingsQosRule(networkId, qosRuleId)

Return a quality of service rule

Return a quality of service rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchSettingsQosRule(networkId, qosRuleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#getNetworkSwitchSettingsQosRule");
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
| **qosRuleId** | **String**|  | |

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

<a id="getNetworkSwitchSettingsQosRules"></a>
# **getNetworkSwitchSettingsQosRules**
> List&lt;Object&gt; getNetworkSwitchSettingsQosRules(networkId)

List quality of service rules

List quality of service rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchSettingsQosRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#getNetworkSwitchSettingsQosRules");
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

<a id="getNetworkSwitchSettingsQosRulesOrder"></a>
# **getNetworkSwitchSettingsQosRulesOrder**
> Object getNetworkSwitchSettingsQosRulesOrder(networkId)

Return the quality of service rule IDs by order in which they will be processed by the switch

Return the quality of service rule IDs by order in which they will be processed by the switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchSettingsQosRulesOrder(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#getNetworkSwitchSettingsQosRulesOrder");
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

<a id="getNetworkSwitchSettingsStormControl"></a>
# **getNetworkSwitchSettingsStormControl**
> Object getNetworkSwitchSettingsStormControl(networkId)

Return the storm control configuration for a switch network

Return the storm control configuration for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchSettingsStormControl(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#getNetworkSwitchSettingsStormControl");
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

<a id="updateNetworkSwitchSettings"></a>
# **updateNetworkSwitchSettings**
> Object updateNetworkSwitchSettings(networkId, updateNetworkSwitchSettingsRequest)

Update switch network settings

Update switch network settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchSettingsRequest updateNetworkSwitchSettingsRequest = new UpdateNetworkSwitchSettingsRequest(); // UpdateNetworkSwitchSettingsRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchSettings(networkId, updateNetworkSwitchSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#updateNetworkSwitchSettings");
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
| **updateNetworkSwitchSettingsRequest** | [**UpdateNetworkSwitchSettingsRequest**](UpdateNetworkSwitchSettingsRequest.md)|  | [optional] |

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

<a id="updateNetworkSwitchSettingsMulticast"></a>
# **updateNetworkSwitchSettingsMulticast**
> Object updateNetworkSwitchSettingsMulticast(networkId, updateNetworkSwitchSettingsMulticastRequest)

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
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchSettingsMulticastRequest updateNetworkSwitchSettingsMulticastRequest = new UpdateNetworkSwitchSettingsMulticastRequest(); // UpdateNetworkSwitchSettingsMulticastRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchSettingsMulticast(networkId, updateNetworkSwitchSettingsMulticastRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#updateNetworkSwitchSettingsMulticast");
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
| **updateNetworkSwitchSettingsMulticastRequest** | [**UpdateNetworkSwitchSettingsMulticastRequest**](UpdateNetworkSwitchSettingsMulticastRequest.md)|  | [optional] |

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

<a id="updateNetworkSwitchSettingsQosRule"></a>
# **updateNetworkSwitchSettingsQosRule**
> Object updateNetworkSwitchSettingsQosRule(networkId, qosRuleId, updateNetworkSwitchSettingsQosRuleRequest)

Update a quality of service rule

Update a quality of service rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    UpdateNetworkSwitchSettingsQosRuleRequest updateNetworkSwitchSettingsQosRuleRequest = new UpdateNetworkSwitchSettingsQosRuleRequest(); // UpdateNetworkSwitchSettingsQosRuleRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchSettingsQosRule(networkId, qosRuleId, updateNetworkSwitchSettingsQosRuleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#updateNetworkSwitchSettingsQosRule");
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
| **qosRuleId** | **String**|  | |
| **updateNetworkSwitchSettingsQosRuleRequest** | [**UpdateNetworkSwitchSettingsQosRuleRequest**](UpdateNetworkSwitchSettingsQosRuleRequest.md)|  | [optional] |

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

<a id="updateNetworkSwitchSettingsQosRulesOrder"></a>
# **updateNetworkSwitchSettingsQosRulesOrder**
> Object updateNetworkSwitchSettingsQosRulesOrder(networkId, updateNetworkSwitchSettingsQosRulesOrderRequest)

Update the order in which the rules should be processed by the switch

Update the order in which the rules should be processed by the switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchSettingsQosRulesOrderRequest updateNetworkSwitchSettingsQosRulesOrderRequest = new UpdateNetworkSwitchSettingsQosRulesOrderRequest(); // UpdateNetworkSwitchSettingsQosRulesOrderRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchSettingsQosRulesOrder(networkId, updateNetworkSwitchSettingsQosRulesOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#updateNetworkSwitchSettingsQosRulesOrder");
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
| **updateNetworkSwitchSettingsQosRulesOrderRequest** | [**UpdateNetworkSwitchSettingsQosRulesOrderRequest**](UpdateNetworkSwitchSettingsQosRulesOrderRequest.md)|  | |

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

<a id="updateNetworkSwitchSettingsStormControl"></a>
# **updateNetworkSwitchSettingsStormControl**
> Object updateNetworkSwitchSettingsStormControl(networkId, updateNetworkSwitchSettingsStormControlRequest)

Update the storm control configuration for a switch network

Update the storm control configuration for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwitchSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SwitchSettingsApi apiInstance = new SwitchSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchSettingsStormControlRequest updateNetworkSwitchSettingsStormControlRequest = new UpdateNetworkSwitchSettingsStormControlRequest(); // UpdateNetworkSwitchSettingsStormControlRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchSettingsStormControl(networkId, updateNetworkSwitchSettingsStormControlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwitchSettingsApi#updateNetworkSwitchSettingsStormControl");
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
| **updateNetworkSwitchSettingsStormControlRequest** | [**UpdateNetworkSwitchSettingsStormControlRequest**](UpdateNetworkSwitchSettingsStormControlRequest.md)|  | [optional] |

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

