# TargetGroupsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSmTargetGroup_1**](TargetGroupsApi.md#createNetworkSmTargetGroup_1) | **POST** /networks/{networkId}/sm/targetGroups | Add a target group |
| [**deleteNetworkSmTargetGroup_1**](TargetGroupsApi.md#deleteNetworkSmTargetGroup_1) | **DELETE** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Delete a target group from a network |
| [**getNetworkSmTargetGroup_1**](TargetGroupsApi.md#getNetworkSmTargetGroup_1) | **GET** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Return a target group |
| [**getNetworkSmTargetGroups_1**](TargetGroupsApi.md#getNetworkSmTargetGroups_1) | **GET** /networks/{networkId}/sm/targetGroups | List the target groups in this network |
| [**updateNetworkSmTargetGroup_1**](TargetGroupsApi.md#updateNetworkSmTargetGroup_1) | **PUT** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Update a target group |


<a id="createNetworkSmTargetGroup_1"></a>
# **createNetworkSmTargetGroup_1**
> Object createNetworkSmTargetGroup_1(networkId, createNetworkSmTargetGroupRequest)

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
import org.openapitools.client.api.TargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TargetGroupsApi apiInstance = new TargetGroupsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSmTargetGroupRequest createNetworkSmTargetGroupRequest = new CreateNetworkSmTargetGroupRequest(); // CreateNetworkSmTargetGroupRequest | 
    try {
      Object result = apiInstance.createNetworkSmTargetGroup_1(networkId, createNetworkSmTargetGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TargetGroupsApi#createNetworkSmTargetGroup_1");
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

<a id="deleteNetworkSmTargetGroup_1"></a>
# **deleteNetworkSmTargetGroup_1**
> deleteNetworkSmTargetGroup_1(networkId, targetGroupId)

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
import org.openapitools.client.api.TargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TargetGroupsApi apiInstance = new TargetGroupsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String targetGroupId = "targetGroupId_example"; // String | 
    try {
      apiInstance.deleteNetworkSmTargetGroup_1(networkId, targetGroupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TargetGroupsApi#deleteNetworkSmTargetGroup_1");
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

<a id="getNetworkSmTargetGroup_1"></a>
# **getNetworkSmTargetGroup_1**
> Object getNetworkSmTargetGroup_1(networkId, targetGroupId, withDetails)

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
import org.openapitools.client.api.TargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TargetGroupsApi apiInstance = new TargetGroupsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String targetGroupId = "targetGroupId_example"; // String | 
    Boolean withDetails = true; // Boolean | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
    try {
      Object result = apiInstance.getNetworkSmTargetGroup_1(networkId, targetGroupId, withDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TargetGroupsApi#getNetworkSmTargetGroup_1");
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

<a id="getNetworkSmTargetGroups_1"></a>
# **getNetworkSmTargetGroups_1**
> List&lt;Object&gt; getNetworkSmTargetGroups_1(networkId, withDetails)

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
import org.openapitools.client.api.TargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TargetGroupsApi apiInstance = new TargetGroupsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Boolean withDetails = true; // Boolean | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
    try {
      List<Object> result = apiInstance.getNetworkSmTargetGroups_1(networkId, withDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TargetGroupsApi#getNetworkSmTargetGroups_1");
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

<a id="updateNetworkSmTargetGroup_1"></a>
# **updateNetworkSmTargetGroup_1**
> Object updateNetworkSmTargetGroup_1(networkId, targetGroupId, createNetworkSmTargetGroupRequest)

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
import org.openapitools.client.api.TargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TargetGroupsApi apiInstance = new TargetGroupsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String targetGroupId = "targetGroupId_example"; // String | 
    CreateNetworkSmTargetGroupRequest createNetworkSmTargetGroupRequest = new CreateNetworkSmTargetGroupRequest(); // CreateNetworkSmTargetGroupRequest | 
    try {
      Object result = apiInstance.updateNetworkSmTargetGroup_1(networkId, targetGroupId, createNetworkSmTargetGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TargetGroupsApi#updateNetworkSmTargetGroup_1");
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

