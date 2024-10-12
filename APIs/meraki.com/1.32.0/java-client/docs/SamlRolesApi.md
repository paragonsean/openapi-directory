# SamlRolesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationSamlRole_1**](SamlRolesApi.md#createOrganizationSamlRole_1) | **POST** /organizations/{organizationId}/samlRoles | Create a SAML role |
| [**deleteOrganizationSamlRole_1**](SamlRolesApi.md#deleteOrganizationSamlRole_1) | **DELETE** /organizations/{organizationId}/samlRoles/{samlRoleId} | Remove a SAML role |
| [**getOrganizationSamlRole_1**](SamlRolesApi.md#getOrganizationSamlRole_1) | **GET** /organizations/{organizationId}/samlRoles/{samlRoleId} | Return a SAML role |
| [**getOrganizationSamlRoles_1**](SamlRolesApi.md#getOrganizationSamlRoles_1) | **GET** /organizations/{organizationId}/samlRoles | List the SAML roles for this organization |
| [**updateOrganizationSamlRole_1**](SamlRolesApi.md#updateOrganizationSamlRole_1) | **PUT** /organizations/{organizationId}/samlRoles/{samlRoleId} | Update a SAML role |


<a id="createOrganizationSamlRole_1"></a>
# **createOrganizationSamlRole_1**
> Object createOrganizationSamlRole_1(organizationId, createOrganizationSamlRoleRequest)

Create a SAML role

Create a SAML role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlRolesApi apiInstance = new SamlRolesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationSamlRoleRequest createOrganizationSamlRoleRequest = new CreateOrganizationSamlRoleRequest(); // CreateOrganizationSamlRoleRequest | 
    try {
      Object result = apiInstance.createOrganizationSamlRole_1(organizationId, createOrganizationSamlRoleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlRolesApi#createOrganizationSamlRole_1");
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
| **createOrganizationSamlRoleRequest** | [**CreateOrganizationSamlRoleRequest**](CreateOrganizationSamlRoleRequest.md)|  | |

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

<a id="deleteOrganizationSamlRole_1"></a>
# **deleteOrganizationSamlRole_1**
> deleteOrganizationSamlRole_1(organizationId, samlRoleId)

Remove a SAML role

Remove a SAML role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlRolesApi apiInstance = new SamlRolesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String samlRoleId = "samlRoleId_example"; // String | 
    try {
      apiInstance.deleteOrganizationSamlRole_1(organizationId, samlRoleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlRolesApi#deleteOrganizationSamlRole_1");
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
| **samlRoleId** | **String**|  | |

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

<a id="getOrganizationSamlRole_1"></a>
# **getOrganizationSamlRole_1**
> Object getOrganizationSamlRole_1(organizationId, samlRoleId)

Return a SAML role

Return a SAML role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlRolesApi apiInstance = new SamlRolesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String samlRoleId = "samlRoleId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationSamlRole_1(organizationId, samlRoleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlRolesApi#getOrganizationSamlRole_1");
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
| **samlRoleId** | **String**|  | |

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

<a id="getOrganizationSamlRoles_1"></a>
# **getOrganizationSamlRoles_1**
> List&lt;Object&gt; getOrganizationSamlRoles_1(organizationId)

List the SAML roles for this organization

List the SAML roles for this organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlRolesApi apiInstance = new SamlRolesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationSamlRoles_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlRolesApi#getOrganizationSamlRoles_1");
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

<a id="updateOrganizationSamlRole_1"></a>
# **updateOrganizationSamlRole_1**
> UpdateOrganizationSamlRole200Response updateOrganizationSamlRole_1(organizationId, samlRoleId, updateOrganizationSamlRoleRequest)

Update a SAML role

Update a SAML role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlRolesApi apiInstance = new SamlRolesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String samlRoleId = "samlRoleId_example"; // String | 
    UpdateOrganizationSamlRoleRequest updateOrganizationSamlRoleRequest = new UpdateOrganizationSamlRoleRequest(); // UpdateOrganizationSamlRoleRequest | 
    try {
      UpdateOrganizationSamlRole200Response result = apiInstance.updateOrganizationSamlRole_1(organizationId, samlRoleId, updateOrganizationSamlRoleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlRolesApi#updateOrganizationSamlRole_1");
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
| **samlRoleId** | **String**|  | |
| **updateOrganizationSamlRoleRequest** | [**UpdateOrganizationSamlRoleRequest**](UpdateOrganizationSamlRoleRequest.md)|  | [optional] |

### Return type

[**UpdateOrganizationSamlRole200Response**](UpdateOrganizationSamlRole200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

