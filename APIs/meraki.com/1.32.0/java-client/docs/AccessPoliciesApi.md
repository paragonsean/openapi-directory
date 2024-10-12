# AccessPoliciesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchAccessPolicy_1**](AccessPoliciesApi.md#createNetworkSwitchAccessPolicy_1) | **POST** /networks/{networkId}/switch/accessPolicies | Create an access policy for a switch network |
| [**deleteNetworkSwitchAccessPolicy_1**](AccessPoliciesApi.md#deleteNetworkSwitchAccessPolicy_1) | **DELETE** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Delete an access policy for a switch network |
| [**getNetworkSwitchAccessPolicies_1**](AccessPoliciesApi.md#getNetworkSwitchAccessPolicies_1) | **GET** /networks/{networkId}/switch/accessPolicies | List the access policies for a switch network |
| [**getNetworkSwitchAccessPolicy_1**](AccessPoliciesApi.md#getNetworkSwitchAccessPolicy_1) | **GET** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Return a specific access policy for a switch network |
| [**updateNetworkSwitchAccessPolicy_1**](AccessPoliciesApi.md#updateNetworkSwitchAccessPolicy_1) | **PUT** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Update an access policy for a switch network |


<a id="createNetworkSwitchAccessPolicy_1"></a>
# **createNetworkSwitchAccessPolicy_1**
> GetNetworkSwitchAccessPolicies200ResponseInner createNetworkSwitchAccessPolicy_1(networkId, createNetworkSwitchAccessPolicyRequest)

Create an access policy for a switch network

Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchAccessPolicyRequest createNetworkSwitchAccessPolicyRequest = new CreateNetworkSwitchAccessPolicyRequest(); // CreateNetworkSwitchAccessPolicyRequest | 
    try {
      GetNetworkSwitchAccessPolicies200ResponseInner result = apiInstance.createNetworkSwitchAccessPolicy_1(networkId, createNetworkSwitchAccessPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#createNetworkSwitchAccessPolicy_1");
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
| **createNetworkSwitchAccessPolicyRequest** | [**CreateNetworkSwitchAccessPolicyRequest**](CreateNetworkSwitchAccessPolicyRequest.md)|  | |

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkSwitchAccessPolicy_1"></a>
# **deleteNetworkSwitchAccessPolicy_1**
> deleteNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber)

Delete an access policy for a switch network

Delete an access policy for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String accessPolicyNumber = "accessPolicyNumber_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#deleteNetworkSwitchAccessPolicy_1");
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
| **accessPolicyNumber** | **String**|  | |

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

<a id="getNetworkSwitchAccessPolicies_1"></a>
# **getNetworkSwitchAccessPolicies_1**
> List&lt;GetNetworkSwitchAccessPolicies200ResponseInner&gt; getNetworkSwitchAccessPolicies_1(networkId)

List the access policies for a switch network

List the access policies for a switch network. Only returns access policies with &#39;my RADIUS server&#39; as authentication method

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkSwitchAccessPolicies200ResponseInner> result = apiInstance.getNetworkSwitchAccessPolicies_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#getNetworkSwitchAccessPolicies_1");
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

[**List&lt;GetNetworkSwitchAccessPolicies200ResponseInner&gt;**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchAccessPolicy_1"></a>
# **getNetworkSwitchAccessPolicy_1**
> GetNetworkSwitchAccessPolicies200ResponseInner getNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber)

Return a specific access policy for a switch network

Return a specific access policy for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String accessPolicyNumber = "accessPolicyNumber_example"; // String | 
    try {
      GetNetworkSwitchAccessPolicies200ResponseInner result = apiInstance.getNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#getNetworkSwitchAccessPolicy_1");
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
| **accessPolicyNumber** | **String**|  | |

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchAccessPolicy_1"></a>
# **updateNetworkSwitchAccessPolicy_1**
> GetNetworkSwitchAccessPolicies200ResponseInner updateNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber, updateNetworkSwitchAccessPolicyRequest)

Update an access policy for a switch network

Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String accessPolicyNumber = "accessPolicyNumber_example"; // String | 
    UpdateNetworkSwitchAccessPolicyRequest updateNetworkSwitchAccessPolicyRequest = new UpdateNetworkSwitchAccessPolicyRequest(); // UpdateNetworkSwitchAccessPolicyRequest | 
    try {
      GetNetworkSwitchAccessPolicies200ResponseInner result = apiInstance.updateNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber, updateNetworkSwitchAccessPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#updateNetworkSwitchAccessPolicy_1");
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
| **accessPolicyNumber** | **String**|  | |
| **updateNetworkSwitchAccessPolicyRequest** | [**UpdateNetworkSwitchAccessPolicyRequest**](UpdateNetworkSwitchAccessPolicyRequest.md)|  | [optional] |

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

