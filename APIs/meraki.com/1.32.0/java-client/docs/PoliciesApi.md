# PoliciesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationAdaptivePolicyPolicy_2**](PoliciesApi.md#createOrganizationAdaptivePolicyPolicy_2) | **POST** /organizations/{organizationId}/adaptivePolicy/policies | Add an Adaptive Policy |
| [**deleteOrganizationAdaptivePolicyPolicy_2**](PoliciesApi.md#deleteOrganizationAdaptivePolicyPolicy_2) | **DELETE** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Delete an Adaptive Policy |
| [**getNetworkPoliciesByClient_1**](PoliciesApi.md#getNetworkPoliciesByClient_1) | **GET** /networks/{networkId}/policies/byClient | Get policies for all clients with policies |
| [**getOrganizationAdaptivePolicyPolicies_2**](PoliciesApi.md#getOrganizationAdaptivePolicyPolicies_2) | **GET** /organizations/{organizationId}/adaptivePolicy/policies | List adaptive policies in an organization |
| [**getOrganizationAdaptivePolicyPolicy_2**](PoliciesApi.md#getOrganizationAdaptivePolicyPolicy_2) | **GET** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Return an adaptive policy |
| [**updateOrganizationAdaptivePolicyPolicy_2**](PoliciesApi.md#updateOrganizationAdaptivePolicyPolicy_2) | **PUT** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Update an Adaptive Policy |


<a id="createOrganizationAdaptivePolicyPolicy_2"></a>
# **createOrganizationAdaptivePolicyPolicy_2**
> Object createOrganizationAdaptivePolicyPolicy_2(organizationId, createOrganizationAdaptivePolicyPolicyRequest)

Add an Adaptive Policy

Add an Adaptive Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationAdaptivePolicyPolicyRequest createOrganizationAdaptivePolicyPolicyRequest = new CreateOrganizationAdaptivePolicyPolicyRequest(); // CreateOrganizationAdaptivePolicyPolicyRequest | 
    try {
      Object result = apiInstance.createOrganizationAdaptivePolicyPolicy_2(organizationId, createOrganizationAdaptivePolicyPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#createOrganizationAdaptivePolicyPolicy_2");
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
| **organizationId** | **String**|  | |
| **createOrganizationAdaptivePolicyPolicyRequest** | [**CreateOrganizationAdaptivePolicyPolicyRequest**](CreateOrganizationAdaptivePolicyPolicyRequest.md)|  | |

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

<a id="deleteOrganizationAdaptivePolicyPolicy_2"></a>
# **deleteOrganizationAdaptivePolicyPolicy_2**
> deleteOrganizationAdaptivePolicyPolicy_2(organizationId, id)

Delete an Adaptive Policy

Delete an Adaptive Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganizationAdaptivePolicyPolicy_2(organizationId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#deleteOrganizationAdaptivePolicyPolicy_2");
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
| **organizationId** | **String**|  | |
| **id** | **String**|  | |

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

<a id="getNetworkPoliciesByClient_1"></a>
# **getNetworkPoliciesByClient_1**
> List&lt;GetNetworkPoliciesByClient200ResponseInner&gt; getNetworkPoliciesByClient_1(networkId, perPage, startingAfter, endingBefore, t0, timespan)

Get policies for all clients with policies

Get policies for all clients with policies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<GetNetworkPoliciesByClient200ResponseInner> result = apiInstance.getNetworkPoliciesByClient_1(networkId, perPage, startingAfter, endingBefore, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#getNetworkPoliciesByClient_1");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**List&lt;GetNetworkPoliciesByClient200ResponseInner&gt;**](GetNetworkPoliciesByClient200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationAdaptivePolicyPolicies_2"></a>
# **getOrganizationAdaptivePolicyPolicies_2**
> List&lt;Object&gt; getOrganizationAdaptivePolicyPolicies_2(organizationId)

List adaptive policies in an organization

List adaptive policies in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationAdaptivePolicyPolicies_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#getOrganizationAdaptivePolicyPolicies_2");
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
| **organizationId** | **String**|  | |

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

<a id="getOrganizationAdaptivePolicyPolicy_2"></a>
# **getOrganizationAdaptivePolicyPolicy_2**
> Object getOrganizationAdaptivePolicyPolicy_2(organizationId, id)

Return an adaptive policy

Return an adaptive policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationAdaptivePolicyPolicy_2(organizationId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#getOrganizationAdaptivePolicyPolicy_2");
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
| **organizationId** | **String**|  | |
| **id** | **String**|  | |

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

<a id="updateOrganizationAdaptivePolicyPolicy_2"></a>
# **updateOrganizationAdaptivePolicyPolicy_2**
> Object updateOrganizationAdaptivePolicyPolicy_2(organizationId, id, updateOrganizationAdaptivePolicyPolicyRequest)

Update an Adaptive Policy

Update an Adaptive Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PoliciesApi apiInstance = new PoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    UpdateOrganizationAdaptivePolicyPolicyRequest updateOrganizationAdaptivePolicyPolicyRequest = new UpdateOrganizationAdaptivePolicyPolicyRequest(); // UpdateOrganizationAdaptivePolicyPolicyRequest | 
    try {
      Object result = apiInstance.updateOrganizationAdaptivePolicyPolicy_2(organizationId, id, updateOrganizationAdaptivePolicyPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoliciesApi#updateOrganizationAdaptivePolicyPolicy_2");
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
| **organizationId** | **String**|  | |
| **id** | **String**|  | |
| **updateOrganizationAdaptivePolicyPolicyRequest** | [**UpdateOrganizationAdaptivePolicyPolicyRequest**](UpdateOrganizationAdaptivePolicyPolicyRequest.md)|  | [optional] |

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

