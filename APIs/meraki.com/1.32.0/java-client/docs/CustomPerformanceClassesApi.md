# CustomPerformanceClassesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkApplianceTrafficShapingCustomPerformanceClass_2**](CustomPerformanceClassesApi.md#createNetworkApplianceTrafficShapingCustomPerformanceClass_2) | **POST** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | Add a custom performance class for an MX network |
| [**deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2**](CustomPerformanceClassesApi.md#deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2) | **DELETE** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Delete a custom performance class from an MX network |
| [**getNetworkApplianceTrafficShapingCustomPerformanceClass_2**](CustomPerformanceClassesApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClass_2) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Return a custom performance class for an MX network |
| [**getNetworkApplianceTrafficShapingCustomPerformanceClasses_2**](CustomPerformanceClassesApi.md#getNetworkApplianceTrafficShapingCustomPerformanceClasses_2) | **GET** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses | List all custom performance classes for an MX network |
| [**updateNetworkApplianceTrafficShapingCustomPerformanceClass_2**](CustomPerformanceClassesApi.md#updateNetworkApplianceTrafficShapingCustomPerformanceClass_2) | **PUT** /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId} | Update a custom performance class for an MX network |


<a id="createNetworkApplianceTrafficShapingCustomPerformanceClass_2"></a>
# **createNetworkApplianceTrafficShapingCustomPerformanceClass_2**
> Object createNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest)

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
import org.openapitools.client.api.CustomPerformanceClassesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomPerformanceClassesApi apiInstance = new CustomPerformanceClassesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest createNetworkApplianceTrafficShapingCustomPerformanceClassRequest = new CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(); // CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
    try {
      Object result = apiInstance.createNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPerformanceClassesApi#createNetworkApplianceTrafficShapingCustomPerformanceClass_2");
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

<a id="deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2"></a>
# **deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2**
> deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId)

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
import org.openapitools.client.api.CustomPerformanceClassesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomPerformanceClassesApi apiInstance = new CustomPerformanceClassesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    try {
      apiInstance.deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPerformanceClassesApi#deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2");
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

<a id="getNetworkApplianceTrafficShapingCustomPerformanceClass_2"></a>
# **getNetworkApplianceTrafficShapingCustomPerformanceClass_2**
> Object getNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId)

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
import org.openapitools.client.api.CustomPerformanceClassesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomPerformanceClassesApi apiInstance = new CustomPerformanceClassesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPerformanceClassesApi#getNetworkApplianceTrafficShapingCustomPerformanceClass_2");
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

<a id="getNetworkApplianceTrafficShapingCustomPerformanceClasses_2"></a>
# **getNetworkApplianceTrafficShapingCustomPerformanceClasses_2**
> List&lt;Object&gt; getNetworkApplianceTrafficShapingCustomPerformanceClasses_2(networkId)

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
import org.openapitools.client.api.CustomPerformanceClassesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomPerformanceClassesApi apiInstance = new CustomPerformanceClassesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkApplianceTrafficShapingCustomPerformanceClasses_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPerformanceClassesApi#getNetworkApplianceTrafficShapingCustomPerformanceClasses_2");
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

<a id="updateNetworkApplianceTrafficShapingCustomPerformanceClass_2"></a>
# **updateNetworkApplianceTrafficShapingCustomPerformanceClass_2**
> Object updateNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId, updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest)

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
import org.openapitools.client.api.CustomPerformanceClassesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CustomPerformanceClassesApi apiInstance = new CustomPerformanceClassesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String customPerformanceClassId = "customPerformanceClassId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest = new UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest(); // UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingCustomPerformanceClass_2(networkId, customPerformanceClassId, updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPerformanceClassesApi#updateNetworkApplianceTrafficShapingCustomPerformanceClass_2");
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

