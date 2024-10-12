# QosRulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchQosRule_1**](QosRulesApi.md#createNetworkSwitchQosRule_1) | **POST** /networks/{networkId}/switch/qosRules | Add a quality of service rule |
| [**deleteNetworkSwitchQosRule_1**](QosRulesApi.md#deleteNetworkSwitchQosRule_1) | **DELETE** /networks/{networkId}/switch/qosRules/{qosRuleId} | Delete a quality of service rule |
| [**getNetworkSwitchQosRule_1**](QosRulesApi.md#getNetworkSwitchQosRule_1) | **GET** /networks/{networkId}/switch/qosRules/{qosRuleId} | Return a quality of service rule |
| [**getNetworkSwitchQosRulesOrder_1**](QosRulesApi.md#getNetworkSwitchQosRulesOrder_1) | **GET** /networks/{networkId}/switch/qosRules/order | Return the quality of service rule IDs by order in which they will be processed by the switch |
| [**getNetworkSwitchQosRules_1**](QosRulesApi.md#getNetworkSwitchQosRules_1) | **GET** /networks/{networkId}/switch/qosRules | List quality of service rules |
| [**updateNetworkSwitchQosRule_1**](QosRulesApi.md#updateNetworkSwitchQosRule_1) | **PUT** /networks/{networkId}/switch/qosRules/{qosRuleId} | Update a quality of service rule |
| [**updateNetworkSwitchQosRulesOrder_1**](QosRulesApi.md#updateNetworkSwitchQosRulesOrder_1) | **PUT** /networks/{networkId}/switch/qosRules/order | Update the order in which the rules should be processed by the switch |


<a id="createNetworkSwitchQosRule_1"></a>
# **createNetworkSwitchQosRule_1**
> Object createNetworkSwitchQosRule_1(networkId, createNetworkSwitchQosRuleRequest)

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
import org.openapitools.client.api.QosRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QosRulesApi apiInstance = new QosRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchQosRuleRequest createNetworkSwitchQosRuleRequest = new CreateNetworkSwitchQosRuleRequest(); // CreateNetworkSwitchQosRuleRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchQosRule_1(networkId, createNetworkSwitchQosRuleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QosRulesApi#createNetworkSwitchQosRule_1");
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
| **createNetworkSwitchQosRuleRequest** | [**CreateNetworkSwitchQosRuleRequest**](CreateNetworkSwitchQosRuleRequest.md)|  | |

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

<a id="deleteNetworkSwitchQosRule_1"></a>
# **deleteNetworkSwitchQosRule_1**
> deleteNetworkSwitchQosRule_1(networkId, qosRuleId)

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
import org.openapitools.client.api.QosRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QosRulesApi apiInstance = new QosRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchQosRule_1(networkId, qosRuleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QosRulesApi#deleteNetworkSwitchQosRule_1");
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

<a id="getNetworkSwitchQosRule_1"></a>
# **getNetworkSwitchQosRule_1**
> Object getNetworkSwitchQosRule_1(networkId, qosRuleId)

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
import org.openapitools.client.api.QosRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QosRulesApi apiInstance = new QosRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchQosRule_1(networkId, qosRuleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QosRulesApi#getNetworkSwitchQosRule_1");
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

<a id="getNetworkSwitchQosRulesOrder_1"></a>
# **getNetworkSwitchQosRulesOrder_1**
> Object getNetworkSwitchQosRulesOrder_1(networkId)

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
import org.openapitools.client.api.QosRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QosRulesApi apiInstance = new QosRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchQosRulesOrder_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QosRulesApi#getNetworkSwitchQosRulesOrder_1");
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

<a id="getNetworkSwitchQosRules_1"></a>
# **getNetworkSwitchQosRules_1**
> List&lt;Object&gt; getNetworkSwitchQosRules_1(networkId)

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
import org.openapitools.client.api.QosRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QosRulesApi apiInstance = new QosRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchQosRules_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QosRulesApi#getNetworkSwitchQosRules_1");
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

<a id="updateNetworkSwitchQosRule_1"></a>
# **updateNetworkSwitchQosRule_1**
> Object updateNetworkSwitchQosRule_1(networkId, qosRuleId, updateNetworkSwitchQosRuleRequest)

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
import org.openapitools.client.api.QosRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QosRulesApi apiInstance = new QosRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String qosRuleId = "qosRuleId_example"; // String | 
    UpdateNetworkSwitchQosRuleRequest updateNetworkSwitchQosRuleRequest = new UpdateNetworkSwitchQosRuleRequest(); // UpdateNetworkSwitchQosRuleRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchQosRule_1(networkId, qosRuleId, updateNetworkSwitchQosRuleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QosRulesApi#updateNetworkSwitchQosRule_1");
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
| **updateNetworkSwitchQosRuleRequest** | [**UpdateNetworkSwitchQosRuleRequest**](UpdateNetworkSwitchQosRuleRequest.md)|  | [optional] |

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

<a id="updateNetworkSwitchQosRulesOrder_1"></a>
# **updateNetworkSwitchQosRulesOrder_1**
> Object updateNetworkSwitchQosRulesOrder_1(networkId, updateNetworkSwitchQosRulesOrderRequest)

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
import org.openapitools.client.api.QosRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QosRulesApi apiInstance = new QosRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchQosRulesOrderRequest updateNetworkSwitchQosRulesOrderRequest = new UpdateNetworkSwitchQosRulesOrderRequest(); // UpdateNetworkSwitchQosRulesOrderRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchQosRulesOrder_1(networkId, updateNetworkSwitchQosRulesOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QosRulesApi#updateNetworkSwitchQosRulesOrder_1");
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
| **updateNetworkSwitchQosRulesOrderRequest** | [**UpdateNetworkSwitchQosRulesOrderRequest**](UpdateNetworkSwitchQosRulesOrderRequest.md)|  | |

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

