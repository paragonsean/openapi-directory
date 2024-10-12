# AdaptivePolicyApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationAdaptivePolicyAcl_1**](AdaptivePolicyApi.md#createOrganizationAdaptivePolicyAcl_1) | **POST** /organizations/{organizationId}/adaptivePolicy/acls | Creates new adaptive policy ACL |
| [**createOrganizationAdaptivePolicyGroup_1**](AdaptivePolicyApi.md#createOrganizationAdaptivePolicyGroup_1) | **POST** /organizations/{organizationId}/adaptivePolicy/groups | Creates a new adaptive policy group |
| [**createOrganizationAdaptivePolicyPolicy_1**](AdaptivePolicyApi.md#createOrganizationAdaptivePolicyPolicy_1) | **POST** /organizations/{organizationId}/adaptivePolicy/policies | Add an Adaptive Policy |
| [**deleteOrganizationAdaptivePolicyAcl_1**](AdaptivePolicyApi.md#deleteOrganizationAdaptivePolicyAcl_1) | **DELETE** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Deletes the specified adaptive policy ACL |
| [**deleteOrganizationAdaptivePolicyGroup_1**](AdaptivePolicyApi.md#deleteOrganizationAdaptivePolicyGroup_1) | **DELETE** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Deletes the specified adaptive policy group and any associated policies and references |
| [**deleteOrganizationAdaptivePolicyPolicy_1**](AdaptivePolicyApi.md#deleteOrganizationAdaptivePolicyPolicy_1) | **DELETE** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Delete an Adaptive Policy |
| [**getOrganizationAdaptivePolicyAcl_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyAcl_1) | **GET** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Returns the adaptive policy ACL information |
| [**getOrganizationAdaptivePolicyAcls_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyAcls_1) | **GET** /organizations/{organizationId}/adaptivePolicy/acls | List adaptive policy ACLs in a organization |
| [**getOrganizationAdaptivePolicyGroup_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyGroup_1) | **GET** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Returns an adaptive policy group |
| [**getOrganizationAdaptivePolicyGroups_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyGroups_1) | **GET** /organizations/{organizationId}/adaptivePolicy/groups | List adaptive policy groups in a organization |
| [**getOrganizationAdaptivePolicyOverview_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyOverview_1) | **GET** /organizations/{organizationId}/adaptivePolicy/overview | Returns adaptive policy aggregate statistics for an organization |
| [**getOrganizationAdaptivePolicyPolicies_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyPolicies_1) | **GET** /organizations/{organizationId}/adaptivePolicy/policies | List adaptive policies in an organization |
| [**getOrganizationAdaptivePolicyPolicy_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicyPolicy_1) | **GET** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Return an adaptive policy |
| [**getOrganizationAdaptivePolicySettings_1**](AdaptivePolicyApi.md#getOrganizationAdaptivePolicySettings_1) | **GET** /organizations/{organizationId}/adaptivePolicy/settings | Returns global adaptive policy settings in an organization |
| [**updateOrganizationAdaptivePolicyAcl_1**](AdaptivePolicyApi.md#updateOrganizationAdaptivePolicyAcl_1) | **PUT** /organizations/{organizationId}/adaptivePolicy/acls/{aclId} | Updates an adaptive policy ACL |
| [**updateOrganizationAdaptivePolicyGroup_1**](AdaptivePolicyApi.md#updateOrganizationAdaptivePolicyGroup_1) | **PUT** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Updates an adaptive policy group |
| [**updateOrganizationAdaptivePolicyPolicy_1**](AdaptivePolicyApi.md#updateOrganizationAdaptivePolicyPolicy_1) | **PUT** /organizations/{organizationId}/adaptivePolicy/policies/{id} | Update an Adaptive Policy |
| [**updateOrganizationAdaptivePolicySettings_1**](AdaptivePolicyApi.md#updateOrganizationAdaptivePolicySettings_1) | **PUT** /organizations/{organizationId}/adaptivePolicy/settings | Update global adaptive policy settings |


<a id="createOrganizationAdaptivePolicyAcl_1"></a>
# **createOrganizationAdaptivePolicyAcl_1**
> Object createOrganizationAdaptivePolicyAcl_1(organizationId, createOrganizationAdaptivePolicyAclRequest)

Creates new adaptive policy ACL

Creates new adaptive policy ACL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationAdaptivePolicyAclRequest createOrganizationAdaptivePolicyAclRequest = new CreateOrganizationAdaptivePolicyAclRequest(); // CreateOrganizationAdaptivePolicyAclRequest | 
    try {
      Object result = apiInstance.createOrganizationAdaptivePolicyAcl_1(organizationId, createOrganizationAdaptivePolicyAclRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#createOrganizationAdaptivePolicyAcl_1");
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
| **createOrganizationAdaptivePolicyAclRequest** | [**CreateOrganizationAdaptivePolicyAclRequest**](CreateOrganizationAdaptivePolicyAclRequest.md)|  | |

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

<a id="createOrganizationAdaptivePolicyGroup_1"></a>
# **createOrganizationAdaptivePolicyGroup_1**
> Object createOrganizationAdaptivePolicyGroup_1(organizationId, createOrganizationAdaptivePolicyGroupRequest)

Creates a new adaptive policy group

Creates a new adaptive policy group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationAdaptivePolicyGroupRequest createOrganizationAdaptivePolicyGroupRequest = new CreateOrganizationAdaptivePolicyGroupRequest(); // CreateOrganizationAdaptivePolicyGroupRequest | 
    try {
      Object result = apiInstance.createOrganizationAdaptivePolicyGroup_1(organizationId, createOrganizationAdaptivePolicyGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#createOrganizationAdaptivePolicyGroup_1");
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
| **createOrganizationAdaptivePolicyGroupRequest** | [**CreateOrganizationAdaptivePolicyGroupRequest**](CreateOrganizationAdaptivePolicyGroupRequest.md)|  | |

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

<a id="createOrganizationAdaptivePolicyPolicy_1"></a>
# **createOrganizationAdaptivePolicyPolicy_1**
> Object createOrganizationAdaptivePolicyPolicy_1(organizationId, createOrganizationAdaptivePolicyPolicyRequest)

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
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationAdaptivePolicyPolicyRequest createOrganizationAdaptivePolicyPolicyRequest = new CreateOrganizationAdaptivePolicyPolicyRequest(); // CreateOrganizationAdaptivePolicyPolicyRequest | 
    try {
      Object result = apiInstance.createOrganizationAdaptivePolicyPolicy_1(organizationId, createOrganizationAdaptivePolicyPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#createOrganizationAdaptivePolicyPolicy_1");
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

<a id="deleteOrganizationAdaptivePolicyAcl_1"></a>
# **deleteOrganizationAdaptivePolicyAcl_1**
> deleteOrganizationAdaptivePolicyAcl_1(organizationId, aclId)

Deletes the specified adaptive policy ACL

Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String aclId = "aclId_example"; // String | 
    try {
      apiInstance.deleteOrganizationAdaptivePolicyAcl_1(organizationId, aclId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#deleteOrganizationAdaptivePolicyAcl_1");
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
| **aclId** | **String**|  | |

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

<a id="deleteOrganizationAdaptivePolicyGroup_1"></a>
# **deleteOrganizationAdaptivePolicyGroup_1**
> deleteOrganizationAdaptivePolicyGroup_1(organizationId, id)

Deletes the specified adaptive policy group and any associated policies and references

Deletes the specified adaptive policy group and any associated policies and references

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganizationAdaptivePolicyGroup_1(organizationId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#deleteOrganizationAdaptivePolicyGroup_1");
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

<a id="deleteOrganizationAdaptivePolicyPolicy_1"></a>
# **deleteOrganizationAdaptivePolicyPolicy_1**
> deleteOrganizationAdaptivePolicyPolicy_1(organizationId, id)

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
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganizationAdaptivePolicyPolicy_1(organizationId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#deleteOrganizationAdaptivePolicyPolicy_1");
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

<a id="getOrganizationAdaptivePolicyAcl_1"></a>
# **getOrganizationAdaptivePolicyAcl_1**
> Object getOrganizationAdaptivePolicyAcl_1(organizationId, aclId)

Returns the adaptive policy ACL information

Returns the adaptive policy ACL information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String aclId = "aclId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationAdaptivePolicyAcl_1(organizationId, aclId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#getOrganizationAdaptivePolicyAcl_1");
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
| **aclId** | **String**|  | |

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

<a id="getOrganizationAdaptivePolicyAcls_1"></a>
# **getOrganizationAdaptivePolicyAcls_1**
> List&lt;Object&gt; getOrganizationAdaptivePolicyAcls_1(organizationId)

List adaptive policy ACLs in a organization

List adaptive policy ACLs in a organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationAdaptivePolicyAcls_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#getOrganizationAdaptivePolicyAcls_1");
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

<a id="getOrganizationAdaptivePolicyGroup_1"></a>
# **getOrganizationAdaptivePolicyGroup_1**
> Object getOrganizationAdaptivePolicyGroup_1(organizationId, id)

Returns an adaptive policy group

Returns an adaptive policy group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationAdaptivePolicyGroup_1(organizationId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#getOrganizationAdaptivePolicyGroup_1");
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

<a id="getOrganizationAdaptivePolicyGroups_1"></a>
# **getOrganizationAdaptivePolicyGroups_1**
> List&lt;Object&gt; getOrganizationAdaptivePolicyGroups_1(organizationId)

List adaptive policy groups in a organization

List adaptive policy groups in a organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationAdaptivePolicyGroups_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#getOrganizationAdaptivePolicyGroups_1");
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

<a id="getOrganizationAdaptivePolicyOverview_1"></a>
# **getOrganizationAdaptivePolicyOverview_1**
> GetOrganizationAdaptivePolicyOverview200Response getOrganizationAdaptivePolicyOverview_1(organizationId)

Returns adaptive policy aggregate statistics for an organization

Returns adaptive policy aggregate statistics for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      GetOrganizationAdaptivePolicyOverview200Response result = apiInstance.getOrganizationAdaptivePolicyOverview_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#getOrganizationAdaptivePolicyOverview_1");
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

[**GetOrganizationAdaptivePolicyOverview200Response**](GetOrganizationAdaptivePolicyOverview200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationAdaptivePolicyPolicies_1"></a>
# **getOrganizationAdaptivePolicyPolicies_1**
> List&lt;Object&gt; getOrganizationAdaptivePolicyPolicies_1(organizationId)

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
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationAdaptivePolicyPolicies_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#getOrganizationAdaptivePolicyPolicies_1");
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

<a id="getOrganizationAdaptivePolicyPolicy_1"></a>
# **getOrganizationAdaptivePolicyPolicy_1**
> Object getOrganizationAdaptivePolicyPolicy_1(organizationId, id)

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
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationAdaptivePolicyPolicy_1(organizationId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#getOrganizationAdaptivePolicyPolicy_1");
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

<a id="getOrganizationAdaptivePolicySettings_1"></a>
# **getOrganizationAdaptivePolicySettings_1**
> Object getOrganizationAdaptivePolicySettings_1(organizationId)

Returns global adaptive policy settings in an organization

Returns global adaptive policy settings in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationAdaptivePolicySettings_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#getOrganizationAdaptivePolicySettings_1");
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

<a id="updateOrganizationAdaptivePolicyAcl_1"></a>
# **updateOrganizationAdaptivePolicyAcl_1**
> Object updateOrganizationAdaptivePolicyAcl_1(organizationId, aclId, updateOrganizationAdaptivePolicyAclRequest)

Updates an adaptive policy ACL

Updates an adaptive policy ACL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String aclId = "aclId_example"; // String | 
    UpdateOrganizationAdaptivePolicyAclRequest updateOrganizationAdaptivePolicyAclRequest = new UpdateOrganizationAdaptivePolicyAclRequest(); // UpdateOrganizationAdaptivePolicyAclRequest | 
    try {
      Object result = apiInstance.updateOrganizationAdaptivePolicyAcl_1(organizationId, aclId, updateOrganizationAdaptivePolicyAclRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#updateOrganizationAdaptivePolicyAcl_1");
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
| **aclId** | **String**|  | |
| **updateOrganizationAdaptivePolicyAclRequest** | [**UpdateOrganizationAdaptivePolicyAclRequest**](UpdateOrganizationAdaptivePolicyAclRequest.md)|  | [optional] |

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

<a id="updateOrganizationAdaptivePolicyGroup_1"></a>
# **updateOrganizationAdaptivePolicyGroup_1**
> Object updateOrganizationAdaptivePolicyGroup_1(organizationId, id, updateOrganizationAdaptivePolicyGroupRequest)

Updates an adaptive policy group

Updates an adaptive policy group. If updating \&quot;Infrastructure\&quot;, only the SGT is allowed. Cannot update \&quot;Unknown\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    UpdateOrganizationAdaptivePolicyGroupRequest updateOrganizationAdaptivePolicyGroupRequest = new UpdateOrganizationAdaptivePolicyGroupRequest(); // UpdateOrganizationAdaptivePolicyGroupRequest | 
    try {
      Object result = apiInstance.updateOrganizationAdaptivePolicyGroup_1(organizationId, id, updateOrganizationAdaptivePolicyGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#updateOrganizationAdaptivePolicyGroup_1");
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
| **updateOrganizationAdaptivePolicyGroupRequest** | [**UpdateOrganizationAdaptivePolicyGroupRequest**](UpdateOrganizationAdaptivePolicyGroupRequest.md)|  | [optional] |

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

<a id="updateOrganizationAdaptivePolicyPolicy_1"></a>
# **updateOrganizationAdaptivePolicyPolicy_1**
> Object updateOrganizationAdaptivePolicyPolicy_1(organizationId, id, updateOrganizationAdaptivePolicyPolicyRequest)

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
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String id = "id_example"; // String | 
    UpdateOrganizationAdaptivePolicyPolicyRequest updateOrganizationAdaptivePolicyPolicyRequest = new UpdateOrganizationAdaptivePolicyPolicyRequest(); // UpdateOrganizationAdaptivePolicyPolicyRequest | 
    try {
      Object result = apiInstance.updateOrganizationAdaptivePolicyPolicy_1(organizationId, id, updateOrganizationAdaptivePolicyPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#updateOrganizationAdaptivePolicyPolicy_1");
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

<a id="updateOrganizationAdaptivePolicySettings_1"></a>
# **updateOrganizationAdaptivePolicySettings_1**
> Object updateOrganizationAdaptivePolicySettings_1(organizationId, updateOrganizationAdaptivePolicySettingsRequest)

Update global adaptive policy settings

Update global adaptive policy settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdaptivePolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdaptivePolicyApi apiInstance = new AdaptivePolicyApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationAdaptivePolicySettingsRequest updateOrganizationAdaptivePolicySettingsRequest = new UpdateOrganizationAdaptivePolicySettingsRequest(); // UpdateOrganizationAdaptivePolicySettingsRequest | 
    try {
      Object result = apiInstance.updateOrganizationAdaptivePolicySettings_1(organizationId, updateOrganizationAdaptivePolicySettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdaptivePolicyApi#updateOrganizationAdaptivePolicySettings_1");
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
| **updateOrganizationAdaptivePolicySettingsRequest** | [**UpdateOrganizationAdaptivePolicySettingsRequest**](UpdateOrganizationAdaptivePolicySettingsRequest.md)|  | [optional] |

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

