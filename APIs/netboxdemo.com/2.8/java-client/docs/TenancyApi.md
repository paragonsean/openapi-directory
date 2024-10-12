# TenancyApi

All URIs are relative to *https://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
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


<a id="tenancyTenantGroupsCreate"></a>
# **tenancyTenantGroupsCreate**
> TenantGroup tenancyTenantGroupsCreate(writableTenantGroup)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    WritableTenantGroup writableTenantGroup = new WritableTenantGroup(); // WritableTenantGroup | 
    try {
      TenantGroup result = apiInstance.tenancyTenantGroupsCreate(writableTenantGroup);
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
| **writableTenantGroup** | [**WritableTenantGroup**](WritableTenantGroup.md)|  | |

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> TenancyTenantGroupsList200Response tenancyTenantGroupsList(id, name, slug, description, q, parentId, parent, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, parentIdN, parentN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String description = "description_example"; // String | 
    String q = "q_example"; // String | 
    String parentId = "parentId_example"; // String | 
    String parent = "parent_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String slugN = "slugN_example"; // String | 
    String slugIc = "slugIc_example"; // String | 
    String slugNic = "slugNic_example"; // String | 
    String slugIew = "slugIew_example"; // String | 
    String slugNiew = "slugNiew_example"; // String | 
    String slugIsw = "slugIsw_example"; // String | 
    String slugNisw = "slugNisw_example"; // String | 
    String slugIe = "slugIe_example"; // String | 
    String slugNie = "slugNie_example"; // String | 
    String descriptionN = "descriptionN_example"; // String | 
    String descriptionIc = "descriptionIc_example"; // String | 
    String descriptionNic = "descriptionNic_example"; // String | 
    String descriptionIew = "descriptionIew_example"; // String | 
    String descriptionNiew = "descriptionNiew_example"; // String | 
    String descriptionIsw = "descriptionIsw_example"; // String | 
    String descriptionNisw = "descriptionNisw_example"; // String | 
    String descriptionIe = "descriptionIe_example"; // String | 
    String descriptionNie = "descriptionNie_example"; // String | 
    String parentIdN = "parentIdN_example"; // String | 
    String parentN = "parentN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      TenancyTenantGroupsList200Response result = apiInstance.tenancyTenantGroupsList(id, name, slug, description, q, parentId, parent, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, parentIdN, parentN, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **description** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **parentId** | **String**|  | [optional] |
| **parent** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **slugN** | **String**|  | [optional] |
| **slugIc** | **String**|  | [optional] |
| **slugNic** | **String**|  | [optional] |
| **slugIew** | **String**|  | [optional] |
| **slugNiew** | **String**|  | [optional] |
| **slugIsw** | **String**|  | [optional] |
| **slugNisw** | **String**|  | [optional] |
| **slugIe** | **String**|  | [optional] |
| **slugNie** | **String**|  | [optional] |
| **descriptionN** | **String**|  | [optional] |
| **descriptionIc** | **String**|  | [optional] |
| **descriptionNic** | **String**|  | [optional] |
| **descriptionIew** | **String**|  | [optional] |
| **descriptionNiew** | **String**|  | [optional] |
| **descriptionIsw** | **String**|  | [optional] |
| **descriptionNisw** | **String**|  | [optional] |
| **descriptionIe** | **String**|  | [optional] |
| **descriptionNie** | **String**|  | [optional] |
| **parentIdN** | **String**|  | [optional] |
| **parentN** | **String**|  | [optional] |
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
> TenantGroup tenancyTenantGroupsPartialUpdate(id, writableTenantGroup)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant group.
    WritableTenantGroup writableTenantGroup = new WritableTenantGroup(); // WritableTenantGroup | 
    try {
      TenantGroup result = apiInstance.tenancyTenantGroupsPartialUpdate(id, writableTenantGroup);
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
| **writableTenantGroup** | [**WritableTenantGroup**](WritableTenantGroup.md)|  | |

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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> TenantGroup tenancyTenantGroupsUpdate(id, writableTenantGroup)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tenant group.
    WritableTenantGroup writableTenantGroup = new WritableTenantGroup(); // WritableTenantGroup | 
    try {
      TenantGroup result = apiInstance.tenancyTenantGroupsUpdate(id, writableTenantGroup);
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
| **writableTenantGroup** | [**WritableTenantGroup**](WritableTenantGroup.md)|  | |

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> TenancyTenantsList200Response tenancyTenantsList(id, name, slug, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, groupId, group, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, groupIdN, groupN, tagN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    TenancyApi apiInstance = new TenancyApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String lastUpdated = "lastUpdated_example"; // String | 
    String lastUpdatedGte = "lastUpdatedGte_example"; // String | 
    String lastUpdatedLte = "lastUpdatedLte_example"; // String | 
    String q = "q_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String slugN = "slugN_example"; // String | 
    String slugIc = "slugIc_example"; // String | 
    String slugNic = "slugNic_example"; // String | 
    String slugIew = "slugIew_example"; // String | 
    String slugNiew = "slugNiew_example"; // String | 
    String slugIsw = "slugIsw_example"; // String | 
    String slugNisw = "slugNisw_example"; // String | 
    String slugIe = "slugIe_example"; // String | 
    String slugNie = "slugNie_example"; // String | 
    String groupIdN = "groupIdN_example"; // String | 
    String groupN = "groupN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      TenancyTenantsList200Response result = apiInstance.tenancyTenantsList(id, name, slug, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, groupId, group, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, groupIdN, groupN, tagN, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **lastUpdated** | **String**|  | [optional] |
| **lastUpdatedGte** | **String**|  | [optional] |
| **lastUpdatedLte** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **slugN** | **String**|  | [optional] |
| **slugIc** | **String**|  | [optional] |
| **slugNic** | **String**|  | [optional] |
| **slugIew** | **String**|  | [optional] |
| **slugNiew** | **String**|  | [optional] |
| **slugIsw** | **String**|  | [optional] |
| **slugNisw** | **String**|  | [optional] |
| **slugIe** | **String**|  | [optional] |
| **slugNie** | **String**|  | [optional] |
| **groupIdN** | **String**|  | [optional] |
| **groupN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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

