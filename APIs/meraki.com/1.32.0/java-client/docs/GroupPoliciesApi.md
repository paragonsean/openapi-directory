# GroupPoliciesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkGroupPolicy_1**](GroupPoliciesApi.md#createNetworkGroupPolicy_1) | **POST** /networks/{networkId}/groupPolicies | Create a group policy |
| [**deleteNetworkGroupPolicy_1**](GroupPoliciesApi.md#deleteNetworkGroupPolicy_1) | **DELETE** /networks/{networkId}/groupPolicies/{groupPolicyId} | Delete a group policy |
| [**getNetworkGroupPolicies_1**](GroupPoliciesApi.md#getNetworkGroupPolicies_1) | **GET** /networks/{networkId}/groupPolicies | List the group policies in a network |
| [**getNetworkGroupPolicy_1**](GroupPoliciesApi.md#getNetworkGroupPolicy_1) | **GET** /networks/{networkId}/groupPolicies/{groupPolicyId} | Display a group policy |
| [**updateNetworkGroupPolicy_1**](GroupPoliciesApi.md#updateNetworkGroupPolicy_1) | **PUT** /networks/{networkId}/groupPolicies/{groupPolicyId} | Update a group policy |


<a id="createNetworkGroupPolicy_1"></a>
# **createNetworkGroupPolicy_1**
> Object createNetworkGroupPolicy_1(networkId, createNetworkGroupPolicyRequest)

Create a group policy

Create a group policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    GroupPoliciesApi apiInstance = new GroupPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkGroupPolicyRequest createNetworkGroupPolicyRequest = new CreateNetworkGroupPolicyRequest(); // CreateNetworkGroupPolicyRequest | 
    try {
      Object result = apiInstance.createNetworkGroupPolicy_1(networkId, createNetworkGroupPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupPoliciesApi#createNetworkGroupPolicy_1");
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
| **createNetworkGroupPolicyRequest** | [**CreateNetworkGroupPolicyRequest**](CreateNetworkGroupPolicyRequest.md)|  | |

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

<a id="deleteNetworkGroupPolicy_1"></a>
# **deleteNetworkGroupPolicy_1**
> deleteNetworkGroupPolicy_1(networkId, groupPolicyId)

Delete a group policy

Delete a group policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    GroupPoliciesApi apiInstance = new GroupPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupPolicyId = "groupPolicyId_example"; // String | 
    try {
      apiInstance.deleteNetworkGroupPolicy_1(networkId, groupPolicyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupPoliciesApi#deleteNetworkGroupPolicy_1");
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
| **groupPolicyId** | **String**|  | |

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

<a id="getNetworkGroupPolicies_1"></a>
# **getNetworkGroupPolicies_1**
> List&lt;Object&gt; getNetworkGroupPolicies_1(networkId)

List the group policies in a network

List the group policies in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    GroupPoliciesApi apiInstance = new GroupPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkGroupPolicies_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupPoliciesApi#getNetworkGroupPolicies_1");
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

<a id="getNetworkGroupPolicy_1"></a>
# **getNetworkGroupPolicy_1**
> Object getNetworkGroupPolicy_1(networkId, groupPolicyId)

Display a group policy

Display a group policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    GroupPoliciesApi apiInstance = new GroupPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupPolicyId = "groupPolicyId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkGroupPolicy_1(networkId, groupPolicyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupPoliciesApi#getNetworkGroupPolicy_1");
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
| **groupPolicyId** | **String**|  | |

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

<a id="updateNetworkGroupPolicy_1"></a>
# **updateNetworkGroupPolicy_1**
> Object updateNetworkGroupPolicy_1(networkId, groupPolicyId, updateNetworkGroupPolicyRequest)

Update a group policy

Update a group policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    GroupPoliciesApi apiInstance = new GroupPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupPolicyId = "groupPolicyId_example"; // String | 
    UpdateNetworkGroupPolicyRequest updateNetworkGroupPolicyRequest = new UpdateNetworkGroupPolicyRequest(); // UpdateNetworkGroupPolicyRequest | 
    try {
      Object result = apiInstance.updateNetworkGroupPolicy_1(networkId, groupPolicyId, updateNetworkGroupPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupPoliciesApi#updateNetworkGroupPolicy_1");
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
| **groupPolicyId** | **String**|  | |
| **updateNetworkGroupPolicyRequest** | [**UpdateNetworkGroupPolicyRequest**](UpdateNetworkGroupPolicyRequest.md)|  | [optional] |

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

