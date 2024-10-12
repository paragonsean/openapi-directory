# PolicyObjectsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationPolicyObject_1**](PolicyObjectsApi.md#createOrganizationPolicyObject_1) | **POST** /organizations/{organizationId}/policyObjects | Creates a new Policy Object. |
| [**createOrganizationPolicyObjectsGroup_1**](PolicyObjectsApi.md#createOrganizationPolicyObjectsGroup_1) | **POST** /organizations/{organizationId}/policyObjects/groups | Creates a new Policy Object Group. |
| [**deleteOrganizationPolicyObject_1**](PolicyObjectsApi.md#deleteOrganizationPolicyObject_1) | **DELETE** /organizations/{organizationId}/policyObjects/{policyObjectId} | Deletes a Policy Object. |
| [**deleteOrganizationPolicyObjectsGroup_1**](PolicyObjectsApi.md#deleteOrganizationPolicyObjectsGroup_1) | **DELETE** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Deletes a Policy Object Group. |
| [**getOrganizationPolicyObject_1**](PolicyObjectsApi.md#getOrganizationPolicyObject_1) | **GET** /organizations/{organizationId}/policyObjects/{policyObjectId} | Shows details of a Policy Object. |
| [**getOrganizationPolicyObjectsGroup_1**](PolicyObjectsApi.md#getOrganizationPolicyObjectsGroup_1) | **GET** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Shows details of a Policy Object Group. |
| [**getOrganizationPolicyObjectsGroups_1**](PolicyObjectsApi.md#getOrganizationPolicyObjectsGroups_1) | **GET** /organizations/{organizationId}/policyObjects/groups | Lists Policy Object Groups belonging to the organization. |
| [**getOrganizationPolicyObjects_1**](PolicyObjectsApi.md#getOrganizationPolicyObjects_1) | **GET** /organizations/{organizationId}/policyObjects | Lists Policy Objects belonging to the organization. |
| [**updateOrganizationPolicyObject_1**](PolicyObjectsApi.md#updateOrganizationPolicyObject_1) | **PUT** /organizations/{organizationId}/policyObjects/{policyObjectId} | Updates a Policy Object. |
| [**updateOrganizationPolicyObjectsGroup_1**](PolicyObjectsApi.md#updateOrganizationPolicyObjectsGroup_1) | **PUT** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Updates a Policy Object Group. |


<a id="createOrganizationPolicyObject_1"></a>
# **createOrganizationPolicyObject_1**
> Object createOrganizationPolicyObject_1(organizationId, createOrganizationPolicyObjectRequest)

Creates a new Policy Object.

Creates a new Policy Object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationPolicyObjectRequest createOrganizationPolicyObjectRequest = new CreateOrganizationPolicyObjectRequest(); // CreateOrganizationPolicyObjectRequest | 
    try {
      Object result = apiInstance.createOrganizationPolicyObject_1(organizationId, createOrganizationPolicyObjectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#createOrganizationPolicyObject_1");
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
| **createOrganizationPolicyObjectRequest** | [**CreateOrganizationPolicyObjectRequest**](CreateOrganizationPolicyObjectRequest.md)|  | |

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

<a id="createOrganizationPolicyObjectsGroup_1"></a>
# **createOrganizationPolicyObjectsGroup_1**
> Object createOrganizationPolicyObjectsGroup_1(organizationId, createOrganizationPolicyObjectsGroupRequest)

Creates a new Policy Object Group.

Creates a new Policy Object Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationPolicyObjectsGroupRequest createOrganizationPolicyObjectsGroupRequest = new CreateOrganizationPolicyObjectsGroupRequest(); // CreateOrganizationPolicyObjectsGroupRequest | 
    try {
      Object result = apiInstance.createOrganizationPolicyObjectsGroup_1(organizationId, createOrganizationPolicyObjectsGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#createOrganizationPolicyObjectsGroup_1");
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
| **createOrganizationPolicyObjectsGroupRequest** | [**CreateOrganizationPolicyObjectsGroupRequest**](CreateOrganizationPolicyObjectsGroupRequest.md)|  | |

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

<a id="deleteOrganizationPolicyObject_1"></a>
# **deleteOrganizationPolicyObject_1**
> deleteOrganizationPolicyObject_1(organizationId, policyObjectId)

Deletes a Policy Object.

Deletes a Policy Object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String policyObjectId = "policyObjectId_example"; // String | 
    try {
      apiInstance.deleteOrganizationPolicyObject_1(organizationId, policyObjectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#deleteOrganizationPolicyObject_1");
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
| **policyObjectId** | **String**|  | |

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

<a id="deleteOrganizationPolicyObjectsGroup_1"></a>
# **deleteOrganizationPolicyObjectsGroup_1**
> deleteOrganizationPolicyObjectsGroup_1(organizationId, policyObjectGroupId)

Deletes a Policy Object Group.

Deletes a Policy Object Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String policyObjectGroupId = "policyObjectGroupId_example"; // String | 
    try {
      apiInstance.deleteOrganizationPolicyObjectsGroup_1(organizationId, policyObjectGroupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#deleteOrganizationPolicyObjectsGroup_1");
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
| **policyObjectGroupId** | **String**|  | |

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

<a id="getOrganizationPolicyObject_1"></a>
# **getOrganizationPolicyObject_1**
> Object getOrganizationPolicyObject_1(organizationId, policyObjectId)

Shows details of a Policy Object.

Shows details of a Policy Object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String policyObjectId = "policyObjectId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationPolicyObject_1(organizationId, policyObjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#getOrganizationPolicyObject_1");
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
| **policyObjectId** | **String**|  | |

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

<a id="getOrganizationPolicyObjectsGroup_1"></a>
# **getOrganizationPolicyObjectsGroup_1**
> Object getOrganizationPolicyObjectsGroup_1(organizationId, policyObjectGroupId)

Shows details of a Policy Object Group.

Shows details of a Policy Object Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String policyObjectGroupId = "policyObjectGroupId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationPolicyObjectsGroup_1(organizationId, policyObjectGroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#getOrganizationPolicyObjectsGroup_1");
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
| **policyObjectGroupId** | **String**|  | |

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

<a id="getOrganizationPolicyObjectsGroups_1"></a>
# **getOrganizationPolicyObjectsGroups_1**
> List&lt;Object&gt; getOrganizationPolicyObjectsGroups_1(organizationId, perPage, startingAfter, endingBefore)

Lists Policy Object Groups belonging to the organization.

Lists Policy Object Groups belonging to the organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<Object> result = apiInstance.getOrganizationPolicyObjectsGroups_1(organizationId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#getOrganizationPolicyObjectsGroups_1");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationPolicyObjects_1"></a>
# **getOrganizationPolicyObjects_1**
> List&lt;Object&gt; getOrganizationPolicyObjects_1(organizationId, perPage, startingAfter, endingBefore)

Lists Policy Objects belonging to the organization.

Lists Policy Objects belonging to the organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<Object> result = apiInstance.getOrganizationPolicyObjects_1(organizationId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#getOrganizationPolicyObjects_1");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="updateOrganizationPolicyObject_1"></a>
# **updateOrganizationPolicyObject_1**
> Object updateOrganizationPolicyObject_1(organizationId, policyObjectId, updateOrganizationPolicyObjectRequest)

Updates a Policy Object.

Updates a Policy Object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String policyObjectId = "policyObjectId_example"; // String | 
    UpdateOrganizationPolicyObjectRequest updateOrganizationPolicyObjectRequest = new UpdateOrganizationPolicyObjectRequest(); // UpdateOrganizationPolicyObjectRequest | 
    try {
      Object result = apiInstance.updateOrganizationPolicyObject_1(organizationId, policyObjectId, updateOrganizationPolicyObjectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#updateOrganizationPolicyObject_1");
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
| **policyObjectId** | **String**|  | |
| **updateOrganizationPolicyObjectRequest** | [**UpdateOrganizationPolicyObjectRequest**](UpdateOrganizationPolicyObjectRequest.md)|  | [optional] |

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

<a id="updateOrganizationPolicyObjectsGroup_1"></a>
# **updateOrganizationPolicyObjectsGroup_1**
> Object updateOrganizationPolicyObjectsGroup_1(organizationId, policyObjectGroupId, updateOrganizationPolicyObjectsGroupRequest)

Updates a Policy Object Group.

Updates a Policy Object Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyObjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PolicyObjectsApi apiInstance = new PolicyObjectsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String policyObjectGroupId = "policyObjectGroupId_example"; // String | 
    UpdateOrganizationPolicyObjectsGroupRequest updateOrganizationPolicyObjectsGroupRequest = new UpdateOrganizationPolicyObjectsGroupRequest(); // UpdateOrganizationPolicyObjectsGroupRequest | 
    try {
      Object result = apiInstance.updateOrganizationPolicyObjectsGroup_1(organizationId, policyObjectGroupId, updateOrganizationPolicyObjectsGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyObjectsApi#updateOrganizationPolicyObjectsGroup_1");
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
| **policyObjectGroupId** | **String**|  | |
| **updateOrganizationPolicyObjectsGroupRequest** | [**UpdateOrganizationPolicyObjectsGroupRequest**](UpdateOrganizationPolicyObjectsGroupRequest.md)|  | [optional] |

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

