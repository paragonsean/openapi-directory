# TrafficShapingApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkApplianceTrafficShapingCustomPerformanceClass_1**](TrafficShapingApi.md#createNetworkApplianceTrafficShapingCustomPerformanceClass_1) | **POST** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | Add a custom performance class for an MX network |
| [**deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1**](TrafficShapingApi.md#deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1) | **DELETE** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Delete a custom performance class from an MX network |
| [**getNetworkApplianceTrafficShapingCustomPerformanceClass_1**](TrafficShapingApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClass_1) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Return a custom performance class for an MX network |
| [**getNetworkApplianceTrafficShapingCustomPerformanceClasses_1**](TrafficShapingApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClasses_1) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | List all custom performance classes for an MX network |
| [**getNetworkApplianceTrafficShapingRules_1**](TrafficShapingApi.md#getNetworkApplianceTrafficShapingRules_1) | **GET** /networks/{networkId}/appliance/trafficShaping/rules | Display the traffic shaping settings rules for an MX network |
| [**getNetworkApplianceTrafficShapingUplinkBandwidth_1**](TrafficShapingApi.md#getNetworkApplianceTrafficShapingUplinkBandwidth_1) | **GET** /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth | Returns the uplink bandwidth limits for your MX network |
| [**getNetworkApplianceTrafficShapingUplinkSelection_1**](TrafficShapingApi.md#getNetworkApplianceTrafficShapingUplinkSelection_1) | **GET** /networks/{networkId}/appliance/trafficShaping/uplinkSelection | Show uplink selection settings for an MX network |
| [**getNetworkApplianceTrafficShaping_1**](TrafficShapingApi.md#getNetworkApplianceTrafficShaping_1) | **GET** /networks/{networkId}/appliance/trafficShaping | Display the traffic shaping settings for an MX network |
| [**getNetworkTrafficShapingApplicationCategories_1**](TrafficShapingApi.md#getNetworkTrafficShapingApplicationCategories_1) | **GET** /networks/{networkId}/trafficShaping/applicationCategories | Returns the application categories for traffic shaping rules. |
| [**getNetworkTrafficShapingDscpTaggingOptions_1**](TrafficShapingApi.md#getNetworkTrafficShapingDscpTaggingOptions_1) | **GET** /networks/{networkId}/trafficShaping/dscpTaggingOptions | Returns the available DSCP tagging options for your traffic shaping rules. |
| [**getNetworkWirelessSsidTrafficShapingRules_2**](TrafficShapingApi.md#getNetworkWirelessSsidTrafficShapingRules_2) | **GET** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Display the traffic shaping settings for a SSID on an MR network |
| [**updateNetworkApplianceTrafficShapingCustomPerformanceClass_1**](TrafficShapingApi.md#updateNetworkApplianceTrafficShapingCustomPerformanceClass_1) | **PUT** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Update a custom performance class for an MX network |
| [**updateNetworkApplianceTrafficShapingRules_1**](TrafficShapingApi.md#updateNetworkApplianceTrafficShapingRules_1) | **PUT** /networks/{networkId}/appliance/trafficShaping/rules | Update the traffic shaping settings rules for an MX network |
| [**updateNetworkApplianceTrafficShapingUplinkBandwidth_1**](TrafficShapingApi.md#updateNetworkApplianceTrafficShapingUplinkBandwidth_1) | **PUT** /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth | Updates the uplink bandwidth settings for your MX network. |
| [**updateNetworkApplianceTrafficShapingUplinkSelection_1**](TrafficShapingApi.md#updateNetworkApplianceTrafficShapingUplinkSelection_1) | **PUT** /networks/{networkId}/appliance/trafficShaping/uplinkSelection | Update uplink selection settings for an MX network |
| [**updateNetworkApplianceTrafficShaping_1**](TrafficShapingApi.md#updateNetworkApplianceTrafficShaping_1) | **PUT** /networks/{networkId}/appliance/trafficShaping | Update the traffic shaping settings for an MX network |
| [**updateNetworkWirelessSsidTrafficShapingRules_2**](TrafficShapingApi.md#updateNetworkWirelessSsidTrafficShapingRules_2) | **PUT** /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules | Update the traffic shaping settings for an SSID on an MR network |


<a id="createNetworkApplianceTrafficShapingCustomPerformanceClass_1"></a>
# **createNetworkApplianceTrafficShapingCustomPerformanceClass_1**
> Object createNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest)

Add a custom performance class for an MX network

Add a custom performance class for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest createNetworkApplianceTrafficShapingCustomPerformanceClassRequest = new CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(); // CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
    try {
      Object result = apiInstance.createNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#createNetworkApplianceTrafficShapingCustomPerformanceClass_1");
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
| **createNetworkApplianceTrafficShapingCustomPerformanceClassRequest** | [**CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest**](CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.md)|  | |

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

<a id="deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1"></a>
# **deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1**
> deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId)

Delete a custom performance class from an MX network

Delete a custom performance class from an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    try {
      apiInstance.deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1");
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
| **customPerformanceClassId** | **String**|  | |

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

<a id="getNetworkApplianceTrafficShapingCustomPerformanceClass_1"></a>
# **getNetworkApplianceTrafficShapingCustomPerformanceClass_1**
> Object getNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId)

Return a custom performance class for an MX network

Return a custom performance class for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkApplianceTrafficShapingCustomPerformanceClass_1");
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
| **customPerformanceClassId** | **String**|  | |

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

<a id="getNetworkApplianceTrafficShapingCustomPerformanceClasses_1"></a>
# **getNetworkApplianceTrafficShapingCustomPerformanceClasses_1**
> List&lt;Object&gt; getNetworkApplianceTrafficShapingCustomPerformanceClasses_1(networkId)

List all custom performance classes for an MX network

List all custom performance classes for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClasses_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkApplianceTrafficShapingCustomPerformanceClasses_1");
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

<a id="getNetworkApplianceTrafficShapingRules_1"></a>
# **getNetworkApplianceTrafficShapingRules_1**
> Object getNetworkApplianceTrafficShapingRules_1(networkId)

Display the traffic shaping settings rules for an MX network

Display the traffic shaping settings rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceTrafficShapingRules_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkApplianceTrafficShapingRules_1");
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

<a id="getNetworkApplianceTrafficShapingUplinkBandwidth_1"></a>
# **getNetworkApplianceTrafficShapingUplinkBandwidth_1**
> GetNetworkApplianceTrafficShapingUplinkBandwidth200Response getNetworkApplianceTrafficShapingUplinkBandwidth_1(networkId)

Returns the uplink bandwidth limits for your MX network

Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device&#39;s hardware capabilities.  For more information on your device&#39;s hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceTrafficShapingUplinkBandwidth200Response result = apiInstance.getNetworkApplianceTrafficShapingUplinkBandwidth_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkApplianceTrafficShapingUplinkBandwidth_1");
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

[**GetNetworkApplianceTrafficShapingUplinkBandwidth200Response**](GetNetworkApplianceTrafficShapingUplinkBandwidth200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceTrafficShapingUplinkSelection_1"></a>
# **getNetworkApplianceTrafficShapingUplinkSelection_1**
> GetNetworkApplianceTrafficShapingUplinkSelection200Response getNetworkApplianceTrafficShapingUplinkSelection_1(networkId)

Show uplink selection settings for an MX network

Show uplink selection settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceTrafficShapingUplinkSelection200Response result = apiInstance.getNetworkApplianceTrafficShapingUplinkSelection_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkApplianceTrafficShapingUplinkSelection_1");
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

[**GetNetworkApplianceTrafficShapingUplinkSelection200Response**](GetNetworkApplianceTrafficShapingUplinkSelection200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkApplianceTrafficShaping_1"></a>
# **getNetworkApplianceTrafficShaping_1**
> Object getNetworkApplianceTrafficShaping_1(networkId)

Display the traffic shaping settings for an MX network

Display the traffic shaping settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceTrafficShaping_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkApplianceTrafficShaping_1");
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

<a id="getNetworkTrafficShapingApplicationCategories_1"></a>
# **getNetworkTrafficShapingApplicationCategories_1**
> Object getNetworkTrafficShapingApplicationCategories_1(networkId)

Returns the application categories for traffic shaping rules.

Returns the application categories for traffic shaping rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkTrafficShapingApplicationCategories_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkTrafficShapingApplicationCategories_1");
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

<a id="getNetworkTrafficShapingDscpTaggingOptions_1"></a>
# **getNetworkTrafficShapingDscpTaggingOptions_1**
> List&lt;Object&gt; getNetworkTrafficShapingDscpTaggingOptions_1(networkId)

Returns the available DSCP tagging options for your traffic shaping rules.

Returns the available DSCP tagging options for your traffic shaping rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkTrafficShapingDscpTaggingOptions_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkTrafficShapingDscpTaggingOptions_1");
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

<a id="getNetworkWirelessSsidTrafficShapingRules_2"></a>
# **getNetworkWirelessSsidTrafficShapingRules_2**
> Object getNetworkWirelessSsidTrafficShapingRules_2(networkId, number)

Display the traffic shaping settings for a SSID on an MR network

Display the traffic shaping settings for a SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidTrafficShapingRules_2(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#getNetworkWirelessSsidTrafficShapingRules_2");
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
| **number** | **String**|  | |

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

<a id="updateNetworkApplianceTrafficShapingCustomPerformanceClass_1"></a>
# **updateNetworkApplianceTrafficShapingCustomPerformanceClass_1**
> Object updateNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId, updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest)

Update a custom performance class for an MX network

Update a custom performance class for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest = new UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(); // UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId, updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#updateNetworkApplianceTrafficShapingCustomPerformanceClass_1");
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
| **customPerformanceClassId** | **String**|  | |
| **updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest** | [**UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest**](UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.md)|  | [optional] |

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

<a id="updateNetworkApplianceTrafficShapingRules_1"></a>
# **updateNetworkApplianceTrafficShapingRules_1**
> Object updateNetworkApplianceTrafficShapingRules_1(networkId, updateNetworkApplianceTrafficShapingRulesRequest)

Update the traffic shaping settings rules for an MX network

Update the traffic shaping settings rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingRulesRequest updateNetworkApplianceTrafficShapingRulesRequest = new UpdateNetworkApplianceTrafficShapingRulesRequest(); // UpdateNetworkApplianceTrafficShapingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingRules_1(networkId, updateNetworkApplianceTrafficShapingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#updateNetworkApplianceTrafficShapingRules_1");
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
| **updateNetworkApplianceTrafficShapingRulesRequest** | [**UpdateNetworkApplianceTrafficShapingRulesRequest**](UpdateNetworkApplianceTrafficShapingRulesRequest.md)|  | [optional] |

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

<a id="updateNetworkApplianceTrafficShapingUplinkBandwidth_1"></a>
# **updateNetworkApplianceTrafficShapingUplinkBandwidth_1**
> Object updateNetworkApplianceTrafficShapingUplinkBandwidth_1(networkId, updateNetworkApplianceTrafficShapingUplinkBandwidthRequest)

Updates the uplink bandwidth settings for your MX network.

Updates the uplink bandwidth settings for your MX network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest updateNetworkApplianceTrafficShapingUplinkBandwidthRequest = new UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest(); // UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingUplinkBandwidth_1(networkId, updateNetworkApplianceTrafficShapingUplinkBandwidthRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#updateNetworkApplianceTrafficShapingUplinkBandwidth_1");
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
| **updateNetworkApplianceTrafficShapingUplinkBandwidthRequest** | [**UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest**](UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.md)|  | [optional] |

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

<a id="updateNetworkApplianceTrafficShapingUplinkSelection_1"></a>
# **updateNetworkApplianceTrafficShapingUplinkSelection_1**
> GetNetworkApplianceTrafficShapingUplinkSelection200Response updateNetworkApplianceTrafficShapingUplinkSelection_1(networkId, updateNetworkApplianceTrafficShapingUplinkSelectionRequest)

Update uplink selection settings for an MX network

Update uplink selection settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest updateNetworkApplianceTrafficShapingUplinkSelectionRequest = new UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest(); // UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest | 
    try {
      GetNetworkApplianceTrafficShapingUplinkSelection200Response result = apiInstance.updateNetworkApplianceTrafficShapingUplinkSelection_1(networkId, updateNetworkApplianceTrafficShapingUplinkSelectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#updateNetworkApplianceTrafficShapingUplinkSelection_1");
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
| **updateNetworkApplianceTrafficShapingUplinkSelectionRequest** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceTrafficShapingUplinkSelection200Response**](GetNetworkApplianceTrafficShapingUplinkSelection200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceTrafficShaping_1"></a>
# **updateNetworkApplianceTrafficShaping_1**
> Object updateNetworkApplianceTrafficShaping_1(networkId, updateNetworkApplianceTrafficShapingRequest)

Update the traffic shaping settings for an MX network

Update the traffic shaping settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingRequest updateNetworkApplianceTrafficShapingRequest = new UpdateNetworkApplianceTrafficShapingRequest(); // UpdateNetworkApplianceTrafficShapingRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShaping_1(networkId, updateNetworkApplianceTrafficShapingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#updateNetworkApplianceTrafficShaping_1");
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
| **updateNetworkApplianceTrafficShapingRequest** | [**UpdateNetworkApplianceTrafficShapingRequest**](UpdateNetworkApplianceTrafficShapingRequest.md)|  | [optional] |

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

<a id="updateNetworkWirelessSsidTrafficShapingRules_2"></a>
# **updateNetworkWirelessSsidTrafficShapingRules_2**
> Object updateNetworkWirelessSsidTrafficShapingRules_2(networkId, number, updateNetworkWirelessSsidTrafficShapingRulesRequest)

Update the traffic shaping settings for an SSID on an MR network

Update the traffic shaping settings for an SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingApi apiInstance = new TrafficShapingApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidTrafficShapingRulesRequest updateNetworkWirelessSsidTrafficShapingRulesRequest = new UpdateNetworkWirelessSsidTrafficShapingRulesRequest(); // UpdateNetworkWirelessSsidTrafficShapingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidTrafficShapingRules_2(networkId, number, updateNetworkWirelessSsidTrafficShapingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingApi#updateNetworkWirelessSsidTrafficShapingRules_2");
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
| **number** | **String**|  | |
| **updateNetworkWirelessSsidTrafficShapingRulesRequest** | [**UpdateNetworkWirelessSsidTrafficShapingRulesRequest**](UpdateNetworkWirelessSsidTrafficShapingRulesRequest.md)|  | [optional] |

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

