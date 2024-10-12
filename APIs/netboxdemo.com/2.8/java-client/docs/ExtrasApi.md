# ExtrasApi

All URIs are relative to *https://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extrasConfigContextsCreate**](ExtrasApi.md#extrasConfigContextsCreate) | **POST** /extras/config-contexts/ |  |
| [**extrasConfigContextsDelete**](ExtrasApi.md#extrasConfigContextsDelete) | **DELETE** /extras/config-contexts/{id}/ |  |
| [**extrasConfigContextsList**](ExtrasApi.md#extrasConfigContextsList) | **GET** /extras/config-contexts/ |  |
| [**extrasConfigContextsPartialUpdate**](ExtrasApi.md#extrasConfigContextsPartialUpdate) | **PATCH** /extras/config-contexts/{id}/ |  |
| [**extrasConfigContextsRead**](ExtrasApi.md#extrasConfigContextsRead) | **GET** /extras/config-contexts/{id}/ |  |
| [**extrasConfigContextsUpdate**](ExtrasApi.md#extrasConfigContextsUpdate) | **PUT** /extras/config-contexts/{id}/ |  |
| [**extrasCustomFieldChoicesList**](ExtrasApi.md#extrasCustomFieldChoicesList) | **GET** /extras/_custom_field_choices/ |  |
| [**extrasCustomFieldChoicesRead**](ExtrasApi.md#extrasCustomFieldChoicesRead) | **GET** /extras/_custom_field_choices/{id}/ |  |
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
| [**extrasReportsList**](ExtrasApi.md#extrasReportsList) | **GET** /extras/reports/ |  |
| [**extrasReportsRead**](ExtrasApi.md#extrasReportsRead) | **GET** /extras/reports/{id}/ |  |
| [**extrasReportsRun**](ExtrasApi.md#extrasReportsRun) | **POST** /extras/reports/{id}/run/ |  |
| [**extrasScriptsList**](ExtrasApi.md#extrasScriptsList) | **GET** /extras/scripts/ |  |
| [**extrasScriptsRead**](ExtrasApi.md#extrasScriptsRead) | **GET** /extras/scripts/{id}/ |  |
| [**extrasTagsCreate**](ExtrasApi.md#extrasTagsCreate) | **POST** /extras/tags/ |  |
| [**extrasTagsDelete**](ExtrasApi.md#extrasTagsDelete) | **DELETE** /extras/tags/{id}/ |  |
| [**extrasTagsList**](ExtrasApi.md#extrasTagsList) | **GET** /extras/tags/ |  |
| [**extrasTagsPartialUpdate**](ExtrasApi.md#extrasTagsPartialUpdate) | **PATCH** /extras/tags/{id}/ |  |
| [**extrasTagsRead**](ExtrasApi.md#extrasTagsRead) | **GET** /extras/tags/{id}/ |  |
| [**extrasTagsUpdate**](ExtrasApi.md#extrasTagsUpdate) | **PUT** /extras/tags/{id}/ |  |


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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> ExtrasConfigContextsList200Response extrasConfigContextsList(id, name, isActive, q, regionId, region, siteId, site, roleId, role, platformId, platform, clusterGroupId, clusterGroup, clusterId, tenantGroupId, tenantGroup, tenantId, tenant, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, regionIdN, regionN, siteIdN, siteN, roleIdN, roleN, platformIdN, platformN, clusterGroupIdN, clusterGroupN, clusterIdN, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, tagN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
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
    String clusterGroupId = "clusterGroupId_example"; // String | 
    String clusterGroup = "clusterGroup_example"; // String | 
    String clusterId = "clusterId_example"; // String | 
    String tenantGroupId = "tenantGroupId_example"; // String | 
    String tenantGroup = "tenantGroup_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
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
    String regionIdN = "regionIdN_example"; // String | 
    String regionN = "regionN_example"; // String | 
    String siteIdN = "siteIdN_example"; // String | 
    String siteN = "siteN_example"; // String | 
    String roleIdN = "roleIdN_example"; // String | 
    String roleN = "roleN_example"; // String | 
    String platformIdN = "platformIdN_example"; // String | 
    String platformN = "platformN_example"; // String | 
    String clusterGroupIdN = "clusterGroupIdN_example"; // String | 
    String clusterGroupN = "clusterGroupN_example"; // String | 
    String clusterIdN = "clusterIdN_example"; // String | 
    String tenantGroupIdN = "tenantGroupIdN_example"; // String | 
    String tenantGroupN = "tenantGroupN_example"; // String | 
    String tenantIdN = "tenantIdN_example"; // String | 
    String tenantN = "tenantN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasConfigContextsList200Response result = apiInstance.extrasConfigContextsList(id, name, isActive, q, regionId, region, siteId, site, roleId, role, platformId, platform, clusterGroupId, clusterGroup, clusterId, tenantGroupId, tenantGroup, tenantId, tenant, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, regionIdN, regionN, siteIdN, siteN, roleIdN, roleN, platformIdN, platformN, clusterGroupIdN, clusterGroupN, clusterIdN, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, tagN, limit, offset);
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
| **id** | **String**|  | [optional] |
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
| **clusterGroupId** | **String**|  | [optional] |
| **clusterGroup** | **String**|  | [optional] |
| **clusterId** | **String**|  | [optional] |
| **tenantGroupId** | **String**|  | [optional] |
| **tenantGroup** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
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
| **regionIdN** | **String**|  | [optional] |
| **regionN** | **String**|  | [optional] |
| **siteIdN** | **String**|  | [optional] |
| **siteN** | **String**|  | [optional] |
| **roleIdN** | **String**|  | [optional] |
| **roleN** | **String**|  | [optional] |
| **platformIdN** | **String**|  | [optional] |
| **platformN** | **String**|  | [optional] |
| **clusterGroupIdN** | **String**|  | [optional] |
| **clusterGroupN** | **String**|  | [optional] |
| **clusterIdN** | **String**|  | [optional] |
| **tenantGroupIdN** | **String**|  | [optional] |
| **tenantGroupN** | **String**|  | [optional] |
| **tenantIdN** | **String**|  | [optional] |
| **tenantN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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

<a id="extrasCustomFieldChoicesList"></a>
# **extrasCustomFieldChoicesList**
> extrasCustomFieldChoicesList()





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    try {
      apiInstance.extrasCustomFieldChoicesList();
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasCustomFieldChoicesList");
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

<a id="extrasCustomFieldChoicesRead"></a>
# **extrasCustomFieldChoicesRead**
> extrasCustomFieldChoicesRead(id)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.extrasCustomFieldChoicesRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasCustomFieldChoicesRead");
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

<a id="extrasExportTemplatesCreate"></a>
# **extrasExportTemplatesCreate**
> ExportTemplate extrasExportTemplatesCreate(writableExportTemplate)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    WritableExportTemplate writableExportTemplate = new WritableExportTemplate(); // WritableExportTemplate | 
    try {
      ExportTemplate result = apiInstance.extrasExportTemplatesCreate(writableExportTemplate);
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
| **writableExportTemplate** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | |

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> ExtrasExportTemplatesList200Response extrasExportTemplatesList(id, contentType, name, templateLanguage, idN, idLte, idLt, idGte, idGt, contentTypeN, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, templateLanguageN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    String contentType = "contentType_example"; // String | 
    String name = "name_example"; // String | 
    String templateLanguage = "templateLanguage_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String contentTypeN = "contentTypeN_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String templateLanguageN = "templateLanguageN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasExportTemplatesList200Response result = apiInstance.extrasExportTemplatesList(id, contentType, name, templateLanguage, idN, idLte, idLt, idGte, idGt, contentTypeN, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, templateLanguageN, limit, offset);
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
| **id** | **String**|  | [optional] |
| **contentType** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **templateLanguage** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **contentTypeN** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **templateLanguageN** | **String**|  | [optional] |
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
> ExportTemplate extrasExportTemplatesPartialUpdate(id, writableExportTemplate)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this export template.
    WritableExportTemplate writableExportTemplate = new WritableExportTemplate(); // WritableExportTemplate | 
    try {
      ExportTemplate result = apiInstance.extrasExportTemplatesPartialUpdate(id, writableExportTemplate);
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
| **writableExportTemplate** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | |

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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> ExportTemplate extrasExportTemplatesUpdate(id, writableExportTemplate)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this export template.
    WritableExportTemplate writableExportTemplate = new WritableExportTemplate(); // WritableExportTemplate | 
    try {
      ExportTemplate result = apiInstance.extrasExportTemplatesUpdate(id, writableExportTemplate);
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
| **writableExportTemplate** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | |

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
> Graph extrasGraphsCreate(graph)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Graph graph = new Graph(); // Graph | 
    try {
      Graph result = apiInstance.extrasGraphsCreate(graph);
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
| **graph** | [**Graph**](Graph.md)|  | |

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> ExtrasGraphsList200Response extrasGraphsList(id, type, name, templateLanguage, idN, idLte, idLt, idGte, idGt, typeN, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, templateLanguageN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    String type = "type_example"; // String | 
    String name = "name_example"; // String | 
    String templateLanguage = "templateLanguage_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String typeN = "typeN_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String templateLanguageN = "templateLanguageN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasGraphsList200Response result = apiInstance.extrasGraphsList(id, type, name, templateLanguage, idN, idLte, idLt, idGte, idGt, typeN, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, templateLanguageN, limit, offset);
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
| **id** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **templateLanguage** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **typeN** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **templateLanguageN** | **String**|  | [optional] |
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
> Graph extrasGraphsPartialUpdate(id, graph)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this graph.
    Graph graph = new Graph(); // Graph | 
    try {
      Graph result = apiInstance.extrasGraphsPartialUpdate(id, graph);
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
| **graph** | [**Graph**](Graph.md)|  | |

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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> Graph extrasGraphsUpdate(id, graph)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this graph.
    Graph graph = new Graph(); // Graph | 
    try {
      Graph result = apiInstance.extrasGraphsUpdate(id, graph);
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
| **graph** | [**Graph**](Graph.md)|  | |

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> ExtrasObjectChangesList200Response extrasObjectChangesList(id, user, userName, requestId, action, changedObjectType, changedObjectId, objectRepr, q, time, idN, idLte, idLt, idGte, idGt, userN, userNameN, userNameIc, userNameNic, userNameIew, userNameNiew, userNameIsw, userNameNisw, userNameIe, userNameNie, actionN, changedObjectTypeN, changedObjectIdN, changedObjectIdLte, changedObjectIdLt, changedObjectIdGte, changedObjectIdGt, objectReprN, objectReprIc, objectReprNic, objectReprIew, objectReprNiew, objectReprIsw, objectReprNisw, objectReprIe, objectReprNie, limit, offset)



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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    String user = "user_example"; // String | 
    String userName = "userName_example"; // String | 
    String requestId = "requestId_example"; // String | 
    String action = "action_example"; // String | 
    String changedObjectType = "changedObjectType_example"; // String | 
    String changedObjectId = "changedObjectId_example"; // String | 
    String objectRepr = "objectRepr_example"; // String | 
    String q = "q_example"; // String | 
    String time = "time_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String userN = "userN_example"; // String | 
    String userNameN = "userNameN_example"; // String | 
    String userNameIc = "userNameIc_example"; // String | 
    String userNameNic = "userNameNic_example"; // String | 
    String userNameIew = "userNameIew_example"; // String | 
    String userNameNiew = "userNameNiew_example"; // String | 
    String userNameIsw = "userNameIsw_example"; // String | 
    String userNameNisw = "userNameNisw_example"; // String | 
    String userNameIe = "userNameIe_example"; // String | 
    String userNameNie = "userNameNie_example"; // String | 
    String actionN = "actionN_example"; // String | 
    String changedObjectTypeN = "changedObjectTypeN_example"; // String | 
    String changedObjectIdN = "changedObjectIdN_example"; // String | 
    String changedObjectIdLte = "changedObjectIdLte_example"; // String | 
    String changedObjectIdLt = "changedObjectIdLt_example"; // String | 
    String changedObjectIdGte = "changedObjectIdGte_example"; // String | 
    String changedObjectIdGt = "changedObjectIdGt_example"; // String | 
    String objectReprN = "objectReprN_example"; // String | 
    String objectReprIc = "objectReprIc_example"; // String | 
    String objectReprNic = "objectReprNic_example"; // String | 
    String objectReprIew = "objectReprIew_example"; // String | 
    String objectReprNiew = "objectReprNiew_example"; // String | 
    String objectReprIsw = "objectReprIsw_example"; // String | 
    String objectReprNisw = "objectReprNisw_example"; // String | 
    String objectReprIe = "objectReprIe_example"; // String | 
    String objectReprNie = "objectReprNie_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasObjectChangesList200Response result = apiInstance.extrasObjectChangesList(id, user, userName, requestId, action, changedObjectType, changedObjectId, objectRepr, q, time, idN, idLte, idLt, idGte, idGt, userN, userNameN, userNameIc, userNameNic, userNameIew, userNameNiew, userNameIsw, userNameNisw, userNameIe, userNameNie, actionN, changedObjectTypeN, changedObjectIdN, changedObjectIdLte, changedObjectIdLt, changedObjectIdGte, changedObjectIdGt, objectReprN, objectReprIc, objectReprNic, objectReprIew, objectReprNiew, objectReprIsw, objectReprNisw, objectReprIe, objectReprNie, limit, offset);
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
| **id** | **String**|  | [optional] |
| **user** | **String**|  | [optional] |
| **userName** | **String**|  | [optional] |
| **requestId** | **String**|  | [optional] |
| **action** | **String**|  | [optional] |
| **changedObjectType** | **String**|  | [optional] |
| **changedObjectId** | **String**|  | [optional] |
| **objectRepr** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **time** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **userN** | **String**|  | [optional] |
| **userNameN** | **String**|  | [optional] |
| **userNameIc** | **String**|  | [optional] |
| **userNameNic** | **String**|  | [optional] |
| **userNameIew** | **String**|  | [optional] |
| **userNameNiew** | **String**|  | [optional] |
| **userNameIsw** | **String**|  | [optional] |
| **userNameNisw** | **String**|  | [optional] |
| **userNameIe** | **String**|  | [optional] |
| **userNameNie** | **String**|  | [optional] |
| **actionN** | **String**|  | [optional] |
| **changedObjectTypeN** | **String**|  | [optional] |
| **changedObjectIdN** | **String**|  | [optional] |
| **changedObjectIdLte** | **String**|  | [optional] |
| **changedObjectIdLt** | **String**|  | [optional] |
| **changedObjectIdGte** | **String**|  | [optional] |
| **changedObjectIdGt** | **String**|  | [optional] |
| **objectReprN** | **String**|  | [optional] |
| **objectReprIc** | **String**|  | [optional] |
| **objectReprNic** | **String**|  | [optional] |
| **objectReprIew** | **String**|  | [optional] |
| **objectReprNiew** | **String**|  | [optional] |
| **objectReprIsw** | **String**|  | [optional] |
| **objectReprNisw** | **String**|  | [optional] |
| **objectReprIe** | **String**|  | [optional] |
| **objectReprNie** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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

<a id="extrasReportsList"></a>
# **extrasReportsList**
> extrasReportsList()



Compile all reports and their related results (if any). Result data is deferred in the list view.

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    try {
      apiInstance.extrasReportsList();
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasReportsList");
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

<a id="extrasReportsRead"></a>
# **extrasReportsRead**
> extrasReportsRead(id)



Retrieve a single Report identified as \&quot;&lt;module&gt;.&lt;report&gt;\&quot;.

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.extrasReportsRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasReportsRead");
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

<a id="extrasReportsRun"></a>
# **extrasReportsRun**
> extrasReportsRun(id)



Run a Report and create a new ReportResult, overwriting any previous result for the Report.

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.extrasReportsRun(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasReportsRun");
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
| **201** |  |  -  |

<a id="extrasScriptsList"></a>
# **extrasScriptsList**
> extrasScriptsList()





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    try {
      apiInstance.extrasScriptsList();
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasScriptsList");
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

<a id="extrasScriptsRead"></a>
# **extrasScriptsRead**
> extrasScriptsRead(id)





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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.extrasScriptsRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtrasApi#extrasScriptsRead");
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tag.
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
| **id** | **Integer**| A unique integer value identifying this tag. | |

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
> ExtrasTagsList200Response extrasTagsList(id, name, slug, color, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, colorN, colorIc, colorNic, colorIew, colorNiew, colorIsw, colorNisw, colorIe, colorNie, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String color = "color_example"; // String | 
    String q = "q_example"; // String | 
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
    String colorN = "colorN_example"; // String | 
    String colorIc = "colorIc_example"; // String | 
    String colorNic = "colorNic_example"; // String | 
    String colorIew = "colorIew_example"; // String | 
    String colorNiew = "colorNiew_example"; // String | 
    String colorIsw = "colorIsw_example"; // String | 
    String colorNisw = "colorNisw_example"; // String | 
    String colorIe = "colorIe_example"; // String | 
    String colorNie = "colorNie_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      ExtrasTagsList200Response result = apiInstance.extrasTagsList(id, name, slug, color, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, colorN, colorIc, colorNic, colorIew, colorNiew, colorIsw, colorNisw, colorIe, colorNie, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **color** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
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
| **colorN** | **String**|  | [optional] |
| **colorIc** | **String**|  | [optional] |
| **colorNic** | **String**|  | [optional] |
| **colorIew** | **String**|  | [optional] |
| **colorNiew** | **String**|  | [optional] |
| **colorIsw** | **String**|  | [optional] |
| **colorNisw** | **String**|  | [optional] |
| **colorIe** | **String**|  | [optional] |
| **colorNie** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tag.
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
| **id** | **Integer**| A unique integer value identifying this tag. | |
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tag.
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
| **id** | **Integer**| A unique integer value identifying this tag. | |

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExtrasApi apiInstance = new ExtrasApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this tag.
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
| **id** | **Integer**| A unique integer value identifying this tag. | |
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

