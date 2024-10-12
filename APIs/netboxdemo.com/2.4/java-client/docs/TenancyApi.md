# TenancyApi

All URIs are relative to *http://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tenancyChoicesList**](TenancyApi.md#tenancyChoicesList) | **GET** /tenancy/_choices/ |  |
| [**tenancyChoicesRead**](TenancyApi.md#tenancyChoicesRead) | **GET** /tenancy/_choices/{id}/ |  |
| [**tenancyTenantGroupsCreate**](TenancyApi.md#tenancyTenantGroupsCreate) | **POST** /tenancy/tenant-groups/ |  |
| [**tenancyTenantGroupsDelete**](TenancyApi.md#tenancyTenantGroupsDelete) | **DELETE** /tenancy/tenant-groups/{id}/ |  |
| [**tenancyTenantGroupsList**](TenancyApi.md#tenancyTenantGroupsList) | **GET** /tenancy/tenant-groups/ |  |
| [**tenancyTenantGroupsPartialUpdate**](TenancyApi.md#tenancyTenantGroupsPartialUpdate) | **PATCH** /tenancy/tenant-groups/{id}/ |  |
| [**tenancyTenantGroupsRead**](TenancyApi.md#tenancyTenantGroupsRead) | **GET** /tenancy/tenant-groups/{id}/ |  |
| [**tenancyTenantGroupsUpdate**](TenancyApi.md#tenancyTenantGroupsUpdate) | **PUT** /tenancy/tenant-groups/{id}/ |  |
| [**tenancyTenantsCreate**](TenancyApi.md#tenancyTenantsCreate) | **POST** /tenancy/tenants/ |  |
| [**tenancyTenantsDelete**](TenancyApi.md#tenancyTenantsDelete) | **DELETE** /tenancy/tenants/{id}/ |  |
| [**tenancyTenantsList**](TenancyApi.md#tenancyTenantsList) | **GET** /tenancy/tenants/ |  |
| [**tenancyTenantsPartialUpdate**](TenancyApi.md#tenancyTenantsPartialUpdate) | **PATCH** /tenancy/tenants/{id}/ |  |
| [**tenancyTenantsRead**](TenancyApi.md#tenancyTenantsRead) | **GET** /tenancy/tenants/{id}/ |  |
| [**tenancyTenantsUpdate**](TenancyApi.md#tenancyTenantsUpdate) | **PUT** /tenancy/tenants/{id}/ |  |


<a id="tenancyChoicesList"></a>
# **tenancyChoicesList**
> tenancyChoicesList()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    try {
      apiInstance.tenancyChoicesList();
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyChoicesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyChoicesRead"></a>
# **tenancyChoicesRead**
> tenancyChoicesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.tenancyChoicesRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyChoicesRead");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyTenantGroupsCreate"></a>
# **tenancyTenantGroupsCreate**
> TenantGroup tenancyTenantGroupsCreate(tenantGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    TenantGroup tenantGroup = new TenantGroup(); // TenantGroup | 
    try {
      TenantGroup result = apiInstance.tenancyTenantGroupsCreate(tenantGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantGroupsCreate");
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
| **tenantGroup** | [**TenantGroup**](TenantGroup.md)|  | |

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="tenancyTenantGroupsDelete"></a>
# **tenancyTenantGroupsDelete**
> tenancyTenantGroupsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant group.
    try {
      apiInstance.tenancyTenantGroupsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantGroupsDelete");
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
| **id** | **Integer**| A unique integer value identifying this tenant group. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="tenancyTenantGroupsList"></a>
# **tenancyTenantGroupsList**
> TenancyTenantGroupsList200Response tenancyTenantGroupsList(name, slug, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      TenancyTenantGroupsList200Response result = apiInstance.tenancyTenantGroupsList(name, slug, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantGroupsList");
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
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**TenancyTenantGroupsList200Response**](TenancyTenantGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyTenantGroupsPartialUpdate"></a>
# **tenancyTenantGroupsPartialUpdate**
> TenantGroup tenancyTenantGroupsPartialUpdate(id, tenantGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant group.
    TenantGroup tenantGroup = new TenantGroup(); // TenantGroup | 
    try {
      TenantGroup result = apiInstance.tenancyTenantGroupsPartialUpdate(id, tenantGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantGroupsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this tenant group. | |
| **tenantGroup** | [**TenantGroup**](TenantGroup.md)|  | |

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyTenantGroupsRead"></a>
# **tenancyTenantGroupsRead**
> TenantGroup tenancyTenantGroupsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant group.
    try {
      TenantGroup result = apiInstance.tenancyTenantGroupsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantGroupsRead");
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
| **id** | **Integer**| A unique integer value identifying this tenant group. | |

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyTenantGroupsUpdate"></a>
# **tenancyTenantGroupsUpdate**
> TenantGroup tenancyTenantGroupsUpdate(id, tenantGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant group.
    TenantGroup tenantGroup = new TenantGroup(); // TenantGroup | 
    try {
      TenantGroup result = apiInstance.tenancyTenantGroupsUpdate(id, tenantGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantGroupsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this tenant group. | |
| **tenantGroup** | [**TenantGroup**](TenantGroup.md)|  | |

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyTenantsCreate"></a>
# **tenancyTenantsCreate**
> Tenant tenancyTenantsCreate(writableTenant)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    WritableTenant writableTenant = new WritableTenant(); // WritableTenant | 
    try {
      Tenant result = apiInstance.tenancyTenantsCreate(writableTenant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantsCreate");
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
| **writableTenant** | [**WritableTenant**](WritableTenant.md)|  | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="tenancyTenantsDelete"></a>
# **tenancyTenantsDelete**
> tenancyTenantsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant.
    try {
      apiInstance.tenancyTenantsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantsDelete");
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
| **id** | **Integer**| A unique integer value identifying this tenant. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="tenancyTenantsList"></a>
# **tenancyTenantsList**
> TenancyTenantsList200Response tenancyTenantsList(name, idIn, q, groupId, group, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    String name = "name_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      TenancyTenantsList200Response result = apiInstance.tenancyTenantsList(name, idIn, q, groupId, group, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantsList");
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
| **name** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**TenancyTenantsList200Response**](TenancyTenantsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyTenantsPartialUpdate"></a>
# **tenancyTenantsPartialUpdate**
> Tenant tenancyTenantsPartialUpdate(id, writableTenant)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant.
    WritableTenant writableTenant = new WritableTenant(); // WritableTenant | 
    try {
      Tenant result = apiInstance.tenancyTenantsPartialUpdate(id, writableTenant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this tenant. | |
| **writableTenant** | [**WritableTenant**](WritableTenant.md)|  | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyTenantsRead"></a>
# **tenancyTenantsRead**
> Tenant tenancyTenantsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant.
    try {
      Tenant result = apiInstance.tenancyTenantsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantsRead");
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
| **id** | **Integer**| A unique integer value identifying this tenant. | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="tenancyTenantsUpdate"></a>
# **tenancyTenantsUpdate**
> Tenant tenancyTenantsUpdate(id, writableTenant)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant.
    WritableTenant writableTenant = new WritableTenant(); // WritableTenant | 
    try {
      Tenant result = apiInstance.tenancyTenantsUpdate(id, writableTenant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenancyApi#tenancyTenantsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this tenant. | |
| **writableTenant** | [**WritableTenant**](WritableTenant.md)|  | |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

