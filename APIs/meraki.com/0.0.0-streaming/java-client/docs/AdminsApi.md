# AdminsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationAdmin**](AdminsApi.md#createOrganizationAdmin) | **POST** /organizations/{organizationId}/admins | Create a new dashboard administrator |
| [**deleteOrganizationAdmin**](AdminsApi.md#deleteOrganizationAdmin) | **DELETE** /organizations/{organizationId}/admins/{adminId} | Revoke all access for a dashboard administrator within this organization |
| [**getOrganizationAdmins**](AdminsApi.md#getOrganizationAdmins) | **GET** /organizations/{organizationId}/admins | List the dashboard administrators in this organization |
| [**updateOrganizationAdmin**](AdminsApi.md#updateOrganizationAdmin) | **PUT** /organizations/{organizationId}/admins/{adminId} | Update an administrator |


<a id="createOrganizationAdmin"></a>
# **createOrganizationAdmin**
> Object createOrganizationAdmin(organizationId, createOrganizationAdminRequest)

Create a new dashboard administrator

Create a new dashboard administrator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdminsApi apiInstance = new AdminsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationAdminRequest createOrganizationAdminRequest = new CreateOrganizationAdminRequest(); // CreateOrganizationAdminRequest | 
    try {
      Object result = apiInstance.createOrganizationAdmin(organizationId, createOrganizationAdminRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminsApi#createOrganizationAdmin");
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
| **createOrganizationAdminRequest** | [**CreateOrganizationAdminRequest**](CreateOrganizationAdminRequest.md)|  | |

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

<a id="deleteOrganizationAdmin"></a>
# **deleteOrganizationAdmin**
> deleteOrganizationAdmin(organizationId, adminId)

Revoke all access for a dashboard administrator within this organization

Revoke all access for a dashboard administrator within this organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdminsApi apiInstance = new AdminsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String adminId = "adminId_example"; // String | 
    try {
      apiInstance.deleteOrganizationAdmin(organizationId, adminId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminsApi#deleteOrganizationAdmin");
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
| **adminId** | **String**|  | |

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

<a id="getOrganizationAdmins"></a>
# **getOrganizationAdmins**
> List&lt;Object&gt; getOrganizationAdmins(organizationId)

List the dashboard administrators in this organization

List the dashboard administrators in this organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdminsApi apiInstance = new AdminsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationAdmins(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminsApi#getOrganizationAdmins");
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

<a id="updateOrganizationAdmin"></a>
# **updateOrganizationAdmin**
> Object updateOrganizationAdmin(organizationId, adminId, updateOrganizationAdminRequest)

Update an administrator

Update an administrator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AdminsApi apiInstance = new AdminsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String adminId = "adminId_example"; // String | 
    UpdateOrganizationAdminRequest updateOrganizationAdminRequest = new UpdateOrganizationAdminRequest(); // UpdateOrganizationAdminRequest | 
    try {
      Object result = apiInstance.updateOrganizationAdmin(organizationId, adminId, updateOrganizationAdminRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminsApi#updateOrganizationAdmin");
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
| **adminId** | **String**|  | |
| **updateOrganizationAdminRequest** | [**UpdateOrganizationAdminRequest**](UpdateOrganizationAdminRequest.md)|  | [optional] |

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

