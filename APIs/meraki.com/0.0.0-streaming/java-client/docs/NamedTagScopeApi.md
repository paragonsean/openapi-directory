# NamedTagScopeApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSmTargetGroup**](NamedTagScopeApi.md#createNetworkSmTargetGroup) | **POST** /networks/{networkId}/sm/targetGroups | Add a target group |
| [**deleteNetworkSmTargetGroup**](NamedTagScopeApi.md#deleteNetworkSmTargetGroup) | **DELETE** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Delete a target group from a network |
| [**getNetworkSmTargetGroup**](NamedTagScopeApi.md#getNetworkSmTargetGroup) | **GET** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Return a target group |
| [**getNetworkSmTargetGroups**](NamedTagScopeApi.md#getNetworkSmTargetGroups) | **GET** /networks/{networkId}/sm/targetGroups | List the target groups in this network |
| [**updateNetworkSmTargetGroup**](NamedTagScopeApi.md#updateNetworkSmTargetGroup) | **PUT** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Update a target group |


<a id="createNetworkSmTargetGroup"></a>
# **createNetworkSmTargetGroup**
> Object createNetworkSmTargetGroup(networkId, createNetworkSmTargetGroupRequest)

Add a target group

Add a target group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamedTagScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NamedTagScopeApi apiInstance = new NamedTagScopeApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSmTargetGroupRequest createNetworkSmTargetGroupRequest = new CreateNetworkSmTargetGroupRequest(); // CreateNetworkSmTargetGroupRequest | 
    try {
      Object result = apiInstance.createNetworkSmTargetGroup(networkId, createNetworkSmTargetGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamedTagScopeApi#createNetworkSmTargetGroup");
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
| **createNetworkSmTargetGroupRequest** | [**CreateNetworkSmTargetGroupRequest**](CreateNetworkSmTargetGroupRequest.md)|  | [optional] |

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

<a id="deleteNetworkSmTargetGroup"></a>
# **deleteNetworkSmTargetGroup**
> deleteNetworkSmTargetGroup(networkId, targetGroupId)

Delete a target group from a network

Delete a target group from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamedTagScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NamedTagScopeApi apiInstance = new NamedTagScopeApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String targetGroupId = "targetGroupId_example"; // String | 
    try {
      apiInstance.deleteNetworkSmTargetGroup(networkId, targetGroupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamedTagScopeApi#deleteNetworkSmTargetGroup");
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
| **targetGroupId** | **String**|  | |

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

<a id="getNetworkSmTargetGroup"></a>
# **getNetworkSmTargetGroup**
> Object getNetworkSmTargetGroup(networkId, targetGroupId, withDetails)

Return a target group

Return a target group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamedTagScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NamedTagScopeApi apiInstance = new NamedTagScopeApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String targetGroupId = "targetGroupId_example"; // String | 
    Boolean withDetails = true; // Boolean | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
    try {
      Object result = apiInstance.getNetworkSmTargetGroup(networkId, targetGroupId, withDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamedTagScopeApi#getNetworkSmTargetGroup");
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
| **targetGroupId** | **String**|  | |
| **withDetails** | **Boolean**| Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response | [optional] |

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

<a id="getNetworkSmTargetGroups"></a>
# **getNetworkSmTargetGroups**
> List&lt;Object&gt; getNetworkSmTargetGroups(networkId, withDetails)

List the target groups in this network

List the target groups in this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamedTagScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NamedTagScopeApi apiInstance = new NamedTagScopeApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Boolean withDetails = true; // Boolean | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
    try {
      List<Object> result = apiInstance.getNetworkSmTargetGroups(networkId, withDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamedTagScopeApi#getNetworkSmTargetGroups");
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
| **withDetails** | **Boolean**| Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response | [optional] |

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

<a id="updateNetworkSmTargetGroup"></a>
# **updateNetworkSmTargetGroup**
> Object updateNetworkSmTargetGroup(networkId, targetGroupId, createNetworkSmTargetGroupRequest)

Update a target group

Update a target group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamedTagScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NamedTagScopeApi apiInstance = new NamedTagScopeApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String targetGroupId = "targetGroupId_example"; // String | 
    CreateNetworkSmTargetGroupRequest createNetworkSmTargetGroupRequest = new CreateNetworkSmTargetGroupRequest(); // CreateNetworkSmTargetGroupRequest | 
    try {
      Object result = apiInstance.updateNetworkSmTargetGroup(networkId, targetGroupId, createNetworkSmTargetGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamedTagScopeApi#updateNetworkSmTargetGroup");
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
| **targetGroupId** | **String**|  | |
| **createNetworkSmTargetGroupRequest** | [**CreateNetworkSmTargetGroupRequest**](CreateNetworkSmTargetGroupRequest.md)|  | [optional] |

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

