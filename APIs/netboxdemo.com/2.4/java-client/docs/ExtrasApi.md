# ExtrasApi

All URIs are relative to *http://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extrasChoicesList**](ExtrasApi.md#extrasChoicesList) | **GET** /extras/_choices/ |  |
| [**extrasChoicesRead**](ExtrasApi.md#extrasChoicesRead) | **GET** /extras/_choices/{id}/ |  |
| [**extrasConfigContextsCreate**](ExtrasApi.md#extrasConfigContextsCreate) | **POST** /extras/config-contexts/ |  |
| [**extrasConfigContextsDelete**](ExtrasApi.md#extrasConfigContextsDelete) | **DELETE** /extras/config-contexts/{id}/ |  |
| [**extrasConfigContextsList**](ExtrasApi.md#extrasConfigContextsList) | **GET** /extras/config-contexts/ |  |
| [**extrasConfigContextsPartialUpdate**](ExtrasApi.md#extrasConfigContextsPartialUpdate) | **PATCH** /extras/config-contexts/{id}/ |  |
| [**extrasConfigContextsRead**](ExtrasApi.md#extrasConfigContextsRead) | **GET** /extras/config-contexts/{id}/ |  |
| [**extrasConfigContextsUpdate**](ExtrasApi.md#extrasConfigContextsUpdate) | **PUT** /extras/config-contexts/{id}/ |  |
| [**extrasExportTemplatesCreate**](ExtrasApi.md#extrasExportTemplatesCreate) | **POST** /extras/export-templates/ |  |
| [**extrasExportTemplatesDelete**](ExtrasApi.md#extrasExportTemplatesDelete) | **DELETE** /extras/export-templates/{id}/ |  |
| [**extrasExportTemplatesList**](ExtrasApi.md#extrasExportTemplatesList) | **GET** /extras/export-templates/ |  |
| [**extrasExportTemplatesPartialUpdate**](ExtrasApi.md#extrasExportTemplatesPartialUpdate) | **PATCH** /extras/export-templates/{id}/ |  |
| [**extrasExportTemplatesRead**](ExtrasApi.md#extrasExportTemplatesRead) | **GET** /extras/export-templates/{id}/ |  |
| [**extrasExportTemplatesUpdate**](ExtrasApi.md#extrasExportTemplatesUpdate) | **PUT** /extras/export-templates/{id}/ |  |
| [**extrasGraphsCreate**](ExtrasApi.md#extrasGraphsCreate) | **POST** /extras/graphs/ |  |
| [**extrasGraphsDelete**](ExtrasApi.md#extrasGraphsDelete) | **DELETE** /extras/graphs/{id}/ |  |
| [**extrasGraphsList**](ExtrasApi.md#extrasGraphsList) | **GET** /extras/graphs/ |  |
| [**extrasGraphsPartialUpdate**](ExtrasApi.md#extrasGraphsPartialUpdate) | **PATCH** /extras/graphs/{id}/ |  |
| [**extrasGraphsRead**](ExtrasApi.md#extrasGraphsRead) | **GET** /extras/graphs/{id}/ |  |
| [**extrasGraphsUpdate**](ExtrasApi.md#extrasGraphsUpdate) | **PUT** /extras/graphs/{id}/ |  |
| [**extrasImageAttachmentsCreate**](ExtrasApi.md#extrasImageAttachmentsCreate) | **POST** /extras/image-attachments/ |  |
| [**extrasImageAttachmentsDelete**](ExtrasApi.md#extrasImageAttachmentsDelete) | **DELETE** /extras/image-attachments/{id}/ |  |
| [**extrasImageAttachmentsList**](ExtrasApi.md#extrasImageAttachmentsList) | **GET** /extras/image-attachments/ |  |
| [**extrasImageAttachmentsPartialUpdate**](ExtrasApi.md#extrasImageAttachmentsPartialUpdate) | **PATCH** /extras/image-attachments/{id}/ |  |
| [**extrasImageAttachmentsRead**](ExtrasApi.md#extrasImageAttachmentsRead) | **GET** /extras/image-attachments/{id}/ |  |
| [**extrasImageAttachmentsUpdate**](ExtrasApi.md#extrasImageAttachmentsUpdate) | **PUT** /extras/image-attachments/{id}/ |  |
| [**extrasObjectChangesList**](ExtrasApi.md#extrasObjectChangesList) | **GET** /extras/object-changes/ |  |
| [**extrasObjectChangesRead**](ExtrasApi.md#extrasObjectChangesRead) | **GET** /extras/object-changes/{id}/ |  |
| [**extrasRecentActivityList**](ExtrasApi.md#extrasRecentActivityList) | **GET** /extras/recent-activity/ |  |
| [**extrasRecentActivityRead**](ExtrasApi.md#extrasRecentActivityRead) | **GET** /extras/recent-activity/{id}/ |  |
| [**extrasTagsCreate**](ExtrasApi.md#extrasTagsCreate) | **POST** /extras/tags/ |  |
| [**extrasTagsDelete**](ExtrasApi.md#extrasTagsDelete) | **DELETE** /extras/tags/{id}/ |  |
| [**extrasTagsList**](ExtrasApi.md#extrasTagsList) | **GET** /extras/tags/ |  |
| [**extrasTagsPartialUpdate**](ExtrasApi.md#extrasTagsPartialUpdate) | **PATCH** /extras/tags/{id}/ |  |
| [**extrasTagsRead**](ExtrasApi.md#extrasTagsRead) | **GET** /extras/tags/{id}/ |  |
| [**extrasTagsUpdate**](ExtrasApi.md#extrasTagsUpdate) | **PUT** /extras/tags/{id}/ |  |
| [**extrasTopologyMapsCreate**](ExtrasApi.md#extrasTopologyMapsCreate) | **POST** /extras/topology-maps/ |  |
| [**extrasTopologyMapsDelete**](ExtrasApi.md#extrasTopologyMapsDelete) | **DELETE** /extras/topology-maps/{id}/ |  |
| [**extrasTopologyMapsList**](ExtrasApi.md#extrasTopologyMapsList) | **GET** /extras/topology-maps/ |  |
| [**extrasTopologyMapsPartialUpdate**](ExtrasApi.md#extrasTopologyMapsPartialUpdate) | **PATCH** /extras/topology-maps/{id}/ |  |
| [**extrasTopologyMapsRead**](ExtrasApi.md#extrasTopologyMapsRead) | **GET** /extras/topology-maps/{id}/ |  |
| [**extrasTopologyMapsRender**](ExtrasApi.md#extrasTopologyMapsRender) | **GET** /extras/topology-maps/{id}/render/ |  |
| [**extrasTopologyMapsUpdate**](ExtrasApi.md#extrasTopologyMapsUpdate) | **PUT** /extras/topology-maps/{id}/ |  |


<a id="extrasChoicesList"></a>
# **extrasChoicesList**
> extrasChoicesList()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    try {
      apiInstance.extrasChoicesList();
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasChoicesList");
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

<a id="extrasChoicesRead"></a>
# **extrasChoicesRead**
> extrasChoicesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.extrasChoicesRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasChoicesRead");
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

<a id="extrasConfigContextsCreate"></a>
# **extrasConfigContextsCreate**
> ConfigContext extrasConfigContextsCreate(writableConfigContext)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    WritableConfigContext writableConfigContext = new WritableConfigContext(); // WritableConfigContext | 
    try {
      ConfigContext result = apiInstance.extrasConfigContextsCreate(writableConfigContext);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasConfigContextsCreate");
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
| **writableConfigContext** | [**WritableConfigContext**](WritableConfigContext.md)|  | |

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="extrasConfigContextsDelete"></a>
# **extrasConfigContextsDelete**
> extrasConfigContextsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this config context.
    try {
      apiInstance.extrasConfigContextsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasConfigContextsDelete");
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
| **id** | **Integer**| A unique integer value identifying this config context. | |

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

<a id="extrasConfigContextsList"></a>
# **extrasConfigContextsList**
> ExtrasConfigContextsList200Response extrasConfigContextsList(name, isActive, q, regionId, region, siteId, site, roleId, role, platformId, platform, tenantGroupId, tenantGroup, tenantId, tenant, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String name = "name_example"; // String | 
    String isActive = "isActive_example"; // String | 
    String q = "q_example"; // String | 
    String regionId = "regionId_example"; // String | 
    String region = "region_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String platformId = "platformId_example"; // String | 
    String platform = "platform_example"; // String | 
    String tenantGroupId = "tenantGroupId_example"; // String | 
    String tenantGroup = "tenantGroup_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasConfigContextsList200Response result = apiInstance.extrasConfigContextsList(name, isActive, q, regionId, region, siteId, site, roleId, role, platformId, platform, tenantGroupId, tenantGroup, tenantId, tenant, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasConfigContextsList");
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
| **isActive** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **regionId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **platformId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **tenantGroupId** | **String**|  | [optional] |
| **tenantGroup** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**ExtrasConfigContextsList200Response**](ExtrasConfigContextsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasConfigContextsPartialUpdate"></a>
# **extrasConfigContextsPartialUpdate**
> ConfigContext extrasConfigContextsPartialUpdate(id, writableConfigContext)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this config context.
    WritableConfigContext writableConfigContext = new WritableConfigContext(); // WritableConfigContext | 
    try {
      ConfigContext result = apiInstance.extrasConfigContextsPartialUpdate(id, writableConfigContext);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasConfigContextsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this config context. | |
| **writableConfigContext** | [**WritableConfigContext**](WritableConfigContext.md)|  | |

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasConfigContextsRead"></a>
# **extrasConfigContextsRead**
> ConfigContext extrasConfigContextsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this config context.
    try {
      ConfigContext result = apiInstance.extrasConfigContextsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasConfigContextsRead");
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
| **id** | **Integer**| A unique integer value identifying this config context. | |

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasConfigContextsUpdate"></a>
# **extrasConfigContextsUpdate**
> ConfigContext extrasConfigContextsUpdate(id, writableConfigContext)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this config context.
    WritableConfigContext writableConfigContext = new WritableConfigContext(); // WritableConfigContext | 
    try {
      ConfigContext result = apiInstance.extrasConfigContextsUpdate(id, writableConfigContext);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasConfigContextsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this config context. | |
| **writableConfigContext** | [**WritableConfigContext**](WritableConfigContext.md)|  | |

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasExportTemplatesCreate"></a>
# **extrasExportTemplatesCreate**
> ExportTemplate extrasExportTemplatesCreate(exportTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    ExportTemplate exportTemplate = new ExportTemplate(); // ExportTemplate | 
    try {
      ExportTemplate result = apiInstance.extrasExportTemplatesCreate(exportTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasExportTemplatesCreate");
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
| **exportTemplate** | [**ExportTemplate**](ExportTemplate.md)|  | |

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="extrasExportTemplatesDelete"></a>
# **extrasExportTemplatesDelete**
> extrasExportTemplatesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this export template.
    try {
      apiInstance.extrasExportTemplatesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasExportTemplatesDelete");
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
| **id** | **Integer**| A unique integer value identifying this export template. | |

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

<a id="extrasExportTemplatesList"></a>
# **extrasExportTemplatesList**
> ExtrasExportTemplatesList200Response extrasExportTemplatesList(contentType, name, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String name = "name_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasExportTemplatesList200Response result = apiInstance.extrasExportTemplatesList(contentType, name, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasExportTemplatesList");
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
| **contentType** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**ExtrasExportTemplatesList200Response**](ExtrasExportTemplatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasExportTemplatesPartialUpdate"></a>
# **extrasExportTemplatesPartialUpdate**
> ExportTemplate extrasExportTemplatesPartialUpdate(id, exportTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this export template.
    ExportTemplate exportTemplate = new ExportTemplate(); // ExportTemplate | 
    try {
      ExportTemplate result = apiInstance.extrasExportTemplatesPartialUpdate(id, exportTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasExportTemplatesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this export template. | |
| **exportTemplate** | [**ExportTemplate**](ExportTemplate.md)|  | |

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasExportTemplatesRead"></a>
# **extrasExportTemplatesRead**
> ExportTemplate extrasExportTemplatesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this export template.
    try {
      ExportTemplate result = apiInstance.extrasExportTemplatesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasExportTemplatesRead");
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
| **id** | **Integer**| A unique integer value identifying this export template. | |

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasExportTemplatesUpdate"></a>
# **extrasExportTemplatesUpdate**
> ExportTemplate extrasExportTemplatesUpdate(id, exportTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this export template.
    ExportTemplate exportTemplate = new ExportTemplate(); // ExportTemplate | 
    try {
      ExportTemplate result = apiInstance.extrasExportTemplatesUpdate(id, exportTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasExportTemplatesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this export template. | |
| **exportTemplate** | [**ExportTemplate**](ExportTemplate.md)|  | |

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasGraphsCreate"></a>
# **extrasGraphsCreate**
> Graph extrasGraphsCreate(writableGraph)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    WritableGraph writableGraph = new WritableGraph(); // WritableGraph | 
    try {
      Graph result = apiInstance.extrasGraphsCreate(writableGraph);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasGraphsCreate");
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
| **writableGraph** | [**WritableGraph**](WritableGraph.md)|  | |

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="extrasGraphsDelete"></a>
# **extrasGraphsDelete**
> extrasGraphsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this graph.
    try {
      apiInstance.extrasGraphsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasGraphsDelete");
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
| **id** | **Integer**| A unique integer value identifying this graph. | |

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

<a id="extrasGraphsList"></a>
# **extrasGraphsList**
> ExtrasGraphsList200Response extrasGraphsList(type, name, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String type = "type_example"; // String | 
    String name = "name_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasGraphsList200Response result = apiInstance.extrasGraphsList(type, name, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasGraphsList");
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
| **type** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**ExtrasGraphsList200Response**](ExtrasGraphsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasGraphsPartialUpdate"></a>
# **extrasGraphsPartialUpdate**
> Graph extrasGraphsPartialUpdate(id, writableGraph)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this graph.
    WritableGraph writableGraph = new WritableGraph(); // WritableGraph | 
    try {
      Graph result = apiInstance.extrasGraphsPartialUpdate(id, writableGraph);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasGraphsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this graph. | |
| **writableGraph** | [**WritableGraph**](WritableGraph.md)|  | |

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasGraphsRead"></a>
# **extrasGraphsRead**
> Graph extrasGraphsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this graph.
    try {
      Graph result = apiInstance.extrasGraphsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasGraphsRead");
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
| **id** | **Integer**| A unique integer value identifying this graph. | |

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasGraphsUpdate"></a>
# **extrasGraphsUpdate**
> Graph extrasGraphsUpdate(id, writableGraph)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this graph.
    WritableGraph writableGraph = new WritableGraph(); // WritableGraph | 
    try {
      Graph result = apiInstance.extrasGraphsUpdate(id, writableGraph);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasGraphsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this graph. | |
| **writableGraph** | [**WritableGraph**](WritableGraph.md)|  | |

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasImageAttachmentsCreate"></a>
# **extrasImageAttachmentsCreate**
> ImageAttachment extrasImageAttachmentsCreate(imageAttachment)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    ImageAttachment imageAttachment = new ImageAttachment(); // ImageAttachment | 
    try {
      ImageAttachment result = apiInstance.extrasImageAttachmentsCreate(imageAttachment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasImageAttachmentsCreate");
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
| **imageAttachment** | [**ImageAttachment**](ImageAttachment.md)|  | |

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="extrasImageAttachmentsDelete"></a>
# **extrasImageAttachmentsDelete**
> extrasImageAttachmentsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this image attachment.
    try {
      apiInstance.extrasImageAttachmentsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasImageAttachmentsDelete");
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
| **id** | **Integer**| A unique integer value identifying this image attachment. | |

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

<a id="extrasImageAttachmentsList"></a>
# **extrasImageAttachmentsList**
> ExtrasImageAttachmentsList200Response extrasImageAttachmentsList(limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasImageAttachmentsList200Response result = apiInstance.extrasImageAttachmentsList(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasImageAttachmentsList");
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
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**ExtrasImageAttachmentsList200Response**](ExtrasImageAttachmentsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasImageAttachmentsPartialUpdate"></a>
# **extrasImageAttachmentsPartialUpdate**
> ImageAttachment extrasImageAttachmentsPartialUpdate(id, imageAttachment)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this image attachment.
    ImageAttachment imageAttachment = new ImageAttachment(); // ImageAttachment | 
    try {
      ImageAttachment result = apiInstance.extrasImageAttachmentsPartialUpdate(id, imageAttachment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasImageAttachmentsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this image attachment. | |
| **imageAttachment** | [**ImageAttachment**](ImageAttachment.md)|  | |

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasImageAttachmentsRead"></a>
# **extrasImageAttachmentsRead**
> ImageAttachment extrasImageAttachmentsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this image attachment.
    try {
      ImageAttachment result = apiInstance.extrasImageAttachmentsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasImageAttachmentsRead");
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
| **id** | **Integer**| A unique integer value identifying this image attachment. | |

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasImageAttachmentsUpdate"></a>
# **extrasImageAttachmentsUpdate**
> ImageAttachment extrasImageAttachmentsUpdate(id, imageAttachment)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this image attachment.
    ImageAttachment imageAttachment = new ImageAttachment(); // ImageAttachment | 
    try {
      ImageAttachment result = apiInstance.extrasImageAttachmentsUpdate(id, imageAttachment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasImageAttachmentsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this image attachment. | |
| **imageAttachment** | [**ImageAttachment**](ImageAttachment.md)|  | |

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasObjectChangesList"></a>
# **extrasObjectChangesList**
> ExtrasObjectChangesList200Response extrasObjectChangesList(user, userName, requestId, action, changedObjectType, objectRepr, q, time, limit, offset)



Retrieve a list of recent changes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String user = "user_example"; // String | 
    String userName = "userName_example"; // String | 
    String requestId = "requestId_example"; // String | 
    String action = "action_example"; // String | 
    String changedObjectType = "changedObjectType_example"; // String | 
    String objectRepr = "objectRepr_example"; // String | 
    String q = "q_example"; // String | 
    String time = "time_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasObjectChangesList200Response result = apiInstance.extrasObjectChangesList(user, userName, requestId, action, changedObjectType, objectRepr, q, time, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasObjectChangesList");
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
| **user** | **String**|  | [optional] |
| **userName** | **String**|  | [optional] |
| **requestId** | **String**|  | [optional] |
| **action** | **String**|  | [optional] |
| **changedObjectType** | **String**|  | [optional] |
| **objectRepr** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **time** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**ExtrasObjectChangesList200Response**](ExtrasObjectChangesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasObjectChangesRead"></a>
# **extrasObjectChangesRead**
> ObjectChange extrasObjectChangesRead(id)



Retrieve a list of recent changes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this object change.
    try {
      ObjectChange result = apiInstance.extrasObjectChangesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasObjectChangesRead");
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
| **id** | **Integer**| A unique integer value identifying this object change. | |

### Return type

[**ObjectChange**](ObjectChange.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasRecentActivityList"></a>
# **extrasRecentActivityList**
> ExtrasRecentActivityList200Response extrasRecentActivityList(user, username, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String user = "user_example"; // String | 
    String username = "username_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasRecentActivityList200Response result = apiInstance.extrasRecentActivityList(user, username, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasRecentActivityList");
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
| **user** | **String**|  | [optional] |
| **username** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**ExtrasRecentActivityList200Response**](ExtrasRecentActivityList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasRecentActivityRead"></a>
# **extrasRecentActivityRead**
> UserAction extrasRecentActivityRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this user action.
    try {
      UserAction result = apiInstance.extrasRecentActivityRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasRecentActivityRead");
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
| **id** | **Integer**| A unique integer value identifying this user action. | |

### Return type

[**UserAction**](UserAction.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTagsCreate"></a>
# **extrasTagsCreate**
> Tag extrasTagsCreate(tag)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Tag tag = new Tag(); // Tag | 
    try {
      Tag result = apiInstance.extrasTagsCreate(tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTagsCreate");
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
| **tag** | [**Tag**](Tag.md)|  | |

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="extrasTagsDelete"></a>
# **extrasTagsDelete**
> extrasTagsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this Tag.
    try {
      apiInstance.extrasTagsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTagsDelete");
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
| **id** | **Integer**| A unique integer value identifying this Tag. | |

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

<a id="extrasTagsList"></a>
# **extrasTagsList**
> ExtrasTagsList200Response extrasTagsList(name, slug, q, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String q = "q_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasTagsList200Response result = apiInstance.extrasTagsList(name, slug, q, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTagsList");
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
| **q** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**ExtrasTagsList200Response**](ExtrasTagsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTagsPartialUpdate"></a>
# **extrasTagsPartialUpdate**
> Tag extrasTagsPartialUpdate(id, tag)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this Tag.
    Tag tag = new Tag(); // Tag | 
    try {
      Tag result = apiInstance.extrasTagsPartialUpdate(id, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTagsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this Tag. | |
| **tag** | [**Tag**](Tag.md)|  | |

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTagsRead"></a>
# **extrasTagsRead**
> Tag extrasTagsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this Tag.
    try {
      Tag result = apiInstance.extrasTagsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTagsRead");
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
| **id** | **Integer**| A unique integer value identifying this Tag. | |

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTagsUpdate"></a>
# **extrasTagsUpdate**
> Tag extrasTagsUpdate(id, tag)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this Tag.
    Tag tag = new Tag(); // Tag | 
    try {
      Tag result = apiInstance.extrasTagsUpdate(id, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTagsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this Tag. | |
| **tag** | [**Tag**](Tag.md)|  | |

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTopologyMapsCreate"></a>
# **extrasTopologyMapsCreate**
> TopologyMap extrasTopologyMapsCreate(writableTopologyMap)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    WritableTopologyMap writableTopologyMap = new WritableTopologyMap(); // WritableTopologyMap | 
    try {
      TopologyMap result = apiInstance.extrasTopologyMapsCreate(writableTopologyMap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTopologyMapsCreate");
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
| **writableTopologyMap** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | |

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="extrasTopologyMapsDelete"></a>
# **extrasTopologyMapsDelete**
> extrasTopologyMapsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this topology map.
    try {
      apiInstance.extrasTopologyMapsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTopologyMapsDelete");
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
| **id** | **Integer**| A unique integer value identifying this topology map. | |

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

<a id="extrasTopologyMapsList"></a>
# **extrasTopologyMapsList**
> ExtrasTopologyMapsList200Response extrasTopologyMapsList(name, slug, siteId, site, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasTopologyMapsList200Response result = apiInstance.extrasTopologyMapsList(name, slug, siteId, site, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTopologyMapsList");
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
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**ExtrasTopologyMapsList200Response**](ExtrasTopologyMapsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTopologyMapsPartialUpdate"></a>
# **extrasTopologyMapsPartialUpdate**
> TopologyMap extrasTopologyMapsPartialUpdate(id, writableTopologyMap)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this topology map.
    WritableTopologyMap writableTopologyMap = new WritableTopologyMap(); // WritableTopologyMap | 
    try {
      TopologyMap result = apiInstance.extrasTopologyMapsPartialUpdate(id, writableTopologyMap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTopologyMapsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this topology map. | |
| **writableTopologyMap** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | |

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTopologyMapsRead"></a>
# **extrasTopologyMapsRead**
> TopologyMap extrasTopologyMapsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this topology map.
    try {
      TopologyMap result = apiInstance.extrasTopologyMapsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTopologyMapsRead");
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
| **id** | **Integer**| A unique integer value identifying this topology map. | |

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTopologyMapsRender"></a>
# **extrasTopologyMapsRender**
> TopologyMap extrasTopologyMapsRender(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this topology map.
    try {
      TopologyMap result = apiInstance.extrasTopologyMapsRender(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTopologyMapsRender");
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
| **id** | **Integer**| A unique integer value identifying this topology map. | |

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="extrasTopologyMapsUpdate"></a>
# **extrasTopologyMapsUpdate**
> TopologyMap extrasTopologyMapsUpdate(id, writableTopologyMap)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtrasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this topology map.
    WritableTopologyMap writableTopologyMap = new WritableTopologyMap(); // WritableTopologyMap | 
    try {
      TopologyMap result = apiInstance.extrasTopologyMapsUpdate(id, writableTopologyMap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasTopologyMapsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this topology map. | |
| **writableTopologyMap** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | |

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

