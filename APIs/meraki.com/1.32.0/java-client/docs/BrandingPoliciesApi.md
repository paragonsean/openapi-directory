# BrandingPoliciesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationBrandingPolicy_1**](BrandingPoliciesApi.md#createOrganizationBrandingPolicy_1) | **POST** /organizations/{organizationId}/brandingPolicies | Add a new branding policy to an organization |
| [**deleteOrganizationBrandingPolicy_1**](BrandingPoliciesApi.md#deleteOrganizationBrandingPolicy_1) | **DELETE** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Delete a branding policy |
| [**getOrganizationBrandingPoliciesPriorities_1**](BrandingPoliciesApi.md#getOrganizationBrandingPoliciesPriorities_1) | **GET** /organizations/{organizationId}/brandingPolicies/priorities | Return the branding policy IDs of an organization in priority order |
| [**getOrganizationBrandingPolicies_1**](BrandingPoliciesApi.md#getOrganizationBrandingPolicies_1) | **GET** /organizations/{organizationId}/brandingPolicies | List the branding policies of an organization |
| [**getOrganizationBrandingPolicy_1**](BrandingPoliciesApi.md#getOrganizationBrandingPolicy_1) | **GET** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Return a branding policy |
| [**updateOrganizationBrandingPoliciesPriorities_1**](BrandingPoliciesApi.md#updateOrganizationBrandingPoliciesPriorities_1) | **PUT** /organizations/{organizationId}/brandingPolicies/priorities | Update the priority ordering of an organization&#39;s branding policies. |
| [**updateOrganizationBrandingPolicy_1**](BrandingPoliciesApi.md#updateOrganizationBrandingPolicy_1) | **PUT** /organizations/{organizationId}/brandingPolicies/{brandingPolicyId} | Update a branding policy |


<a id="createOrganizationBrandingPolicy_1"></a>
# **createOrganizationBrandingPolicy_1**
> CreateOrganizationBrandingPolicy201Response createOrganizationBrandingPolicy_1(organizationId, createOrganizationBrandingPolicyRequest)

Add a new branding policy to an organization

Add a new branding policy to an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BrandingPoliciesApi apiInstance = new BrandingPoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationBrandingPolicyRequest createOrganizationBrandingPolicyRequest = new CreateOrganizationBrandingPolicyRequest(); // CreateOrganizationBrandingPolicyRequest | 
    try {
      CreateOrganizationBrandingPolicy201Response result = apiInstance.createOrganizationBrandingPolicy_1(organizationId, createOrganizationBrandingPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingPoliciesApi#createOrganizationBrandingPolicy_1");
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
| **createOrganizationBrandingPolicyRequest** | [**CreateOrganizationBrandingPolicyRequest**](CreateOrganizationBrandingPolicyRequest.md)|  | [optional] |

### Return type

[**CreateOrganizationBrandingPolicy201Response**](CreateOrganizationBrandingPolicy201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteOrganizationBrandingPolicy_1"></a>
# **deleteOrganizationBrandingPolicy_1**
> deleteOrganizationBrandingPolicy_1(organizationId, brandingPolicyId)

Delete a branding policy

Delete a branding policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BrandingPoliciesApi apiInstance = new BrandingPoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String brandingPolicyId = "brandingPolicyId_example"; // String | 
    try {
      apiInstance.deleteOrganizationBrandingPolicy_1(organizationId, brandingPolicyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingPoliciesApi#deleteOrganizationBrandingPolicy_1");
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
| **brandingPolicyId** | **String**|  | |

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

<a id="getOrganizationBrandingPoliciesPriorities_1"></a>
# **getOrganizationBrandingPoliciesPriorities_1**
> GetOrganizationBrandingPoliciesPriorities200Response getOrganizationBrandingPoliciesPriorities_1(organizationId)

Return the branding policy IDs of an organization in priority order

Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BrandingPoliciesApi apiInstance = new BrandingPoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      GetOrganizationBrandingPoliciesPriorities200Response result = apiInstance.getOrganizationBrandingPoliciesPriorities_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingPoliciesApi#getOrganizationBrandingPoliciesPriorities_1");
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

[**GetOrganizationBrandingPoliciesPriorities200Response**](GetOrganizationBrandingPoliciesPriorities200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationBrandingPolicies_1"></a>
# **getOrganizationBrandingPolicies_1**
> List&lt;GetOrganizationBrandingPolicies200ResponseInner&gt; getOrganizationBrandingPolicies_1(organizationId)

List the branding policies of an organization

List the branding policies of an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BrandingPoliciesApi apiInstance = new BrandingPoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<GetOrganizationBrandingPolicies200ResponseInner> result = apiInstance.getOrganizationBrandingPolicies_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingPoliciesApi#getOrganizationBrandingPolicies_1");
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

[**List&lt;GetOrganizationBrandingPolicies200ResponseInner&gt;**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationBrandingPolicy_1"></a>
# **getOrganizationBrandingPolicy_1**
> GetOrganizationBrandingPolicies200ResponseInner getOrganizationBrandingPolicy_1(organizationId, brandingPolicyId)

Return a branding policy

Return a branding policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BrandingPoliciesApi apiInstance = new BrandingPoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String brandingPolicyId = "brandingPolicyId_example"; // String | 
    try {
      GetOrganizationBrandingPolicies200ResponseInner result = apiInstance.getOrganizationBrandingPolicy_1(organizationId, brandingPolicyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingPoliciesApi#getOrganizationBrandingPolicy_1");
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
| **brandingPolicyId** | **String**|  | |

### Return type

[**GetOrganizationBrandingPolicies200ResponseInner**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationBrandingPoliciesPriorities_1"></a>
# **updateOrganizationBrandingPoliciesPriorities_1**
> GetOrganizationBrandingPoliciesPriorities200Response updateOrganizationBrandingPoliciesPriorities_1(organizationId, updateOrganizationBrandingPoliciesPrioritiesRequest)

Update the priority ordering of an organization&#39;s branding policies.

Update the priority ordering of an organization&#39;s branding policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BrandingPoliciesApi apiInstance = new BrandingPoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationBrandingPoliciesPrioritiesRequest updateOrganizationBrandingPoliciesPrioritiesRequest = new UpdateOrganizationBrandingPoliciesPrioritiesRequest(); // UpdateOrganizationBrandingPoliciesPrioritiesRequest | 
    try {
      GetOrganizationBrandingPoliciesPriorities200Response result = apiInstance.updateOrganizationBrandingPoliciesPriorities_1(organizationId, updateOrganizationBrandingPoliciesPrioritiesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingPoliciesApi#updateOrganizationBrandingPoliciesPriorities_1");
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
| **updateOrganizationBrandingPoliciesPrioritiesRequest** | [**UpdateOrganizationBrandingPoliciesPrioritiesRequest**](UpdateOrganizationBrandingPoliciesPrioritiesRequest.md)|  | [optional] |

### Return type

[**GetOrganizationBrandingPoliciesPriorities200Response**](GetOrganizationBrandingPoliciesPriorities200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationBrandingPolicy_1"></a>
# **updateOrganizationBrandingPolicy_1**
> GetOrganizationBrandingPolicies200ResponseInner updateOrganizationBrandingPolicy_1(organizationId, brandingPolicyId, updateOrganizationBrandingPolicyRequest)

Update a branding policy

Update a branding policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BrandingPoliciesApi apiInstance = new BrandingPoliciesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String brandingPolicyId = "brandingPolicyId_example"; // String | 
    UpdateOrganizationBrandingPolicyRequest updateOrganizationBrandingPolicyRequest = new UpdateOrganizationBrandingPolicyRequest(); // UpdateOrganizationBrandingPolicyRequest | 
    try {
      GetOrganizationBrandingPolicies200ResponseInner result = apiInstance.updateOrganizationBrandingPolicy_1(organizationId, brandingPolicyId, updateOrganizationBrandingPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandingPoliciesApi#updateOrganizationBrandingPolicy_1");
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
| **brandingPolicyId** | **String**|  | |
| **updateOrganizationBrandingPolicyRequest** | [**UpdateOrganizationBrandingPolicyRequest**](UpdateOrganizationBrandingPolicyRequest.md)|  | [optional] |

### Return type

[**GetOrganizationBrandingPolicies200ResponseInner**](GetOrganizationBrandingPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

