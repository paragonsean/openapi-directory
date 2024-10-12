# DashboardsApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dashboardDelete**](DashboardsApi.md#dashboardDelete) | **DELETE** /dashboard/ |  |
| [**dashboardExportGet**](DashboardsApi.md#dashboardExportGet) | **GET** /dashboard/export/ |  |
| [**dashboardFavoriteStatusGet**](DashboardsApi.md#dashboardFavoriteStatusGet) | **GET** /dashboard/favorite_status/ |  |
| [**dashboardGet**](DashboardsApi.md#dashboardGet) | **GET** /dashboard/ |  |
| [**dashboardIdOrSlugChartsGet**](DashboardsApi.md#dashboardIdOrSlugChartsGet) | **GET** /dashboard/{id_or_slug}/charts |  |
| [**dashboardIdOrSlugDatasetsGet**](DashboardsApi.md#dashboardIdOrSlugDatasetsGet) | **GET** /dashboard/{id_or_slug}/datasets |  |
| [**dashboardIdOrSlugGet**](DashboardsApi.md#dashboardIdOrSlugGet) | **GET** /dashboard/{id_or_slug} |  |
| [**dashboardImportPost**](DashboardsApi.md#dashboardImportPost) | **POST** /dashboard/import/ |  |
| [**dashboardInfoGet**](DashboardsApi.md#dashboardInfoGet) | **GET** /dashboard/_info |  |
| [**dashboardPkDelete**](DashboardsApi.md#dashboardPkDelete) | **DELETE** /dashboard/{pk} |  |
| [**dashboardPkPut**](DashboardsApi.md#dashboardPkPut) | **PUT** /dashboard/{pk} |  |
| [**dashboardPkThumbnailDigestGet**](DashboardsApi.md#dashboardPkThumbnailDigestGet) | **GET** /dashboard/{pk}/thumbnail/{digest}/ |  |
| [**dashboardPost**](DashboardsApi.md#dashboardPost) | **POST** /dashboard/ |  |
| [**dashboardRelatedColumnNameGet**](DashboardsApi.md#dashboardRelatedColumnNameGet) | **GET** /dashboard/related/{column_name} |  |


<a id="dashboardDelete"></a>
# **dashboardDelete**
> AnnotationLayerGet400Response dashboardDelete(q)



Deletes multiple Dashboards in a bulk operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      AnnotationLayerGet400Response result = apiInstance.dashboardDelete(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardDelete");
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
| **q** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard bulk delete |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardExportGet"></a>
# **dashboardExportGet**
> String dashboardExportGet(q)



Exports multiple Dashboards and downloads them as YAML files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      String result = apiInstance.dashboardExportGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardExportGet");
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
| **q** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

**String**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard export |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardFavoriteStatusGet"></a>
# **dashboardFavoriteStatusGet**
> GetFavStarIdsSchema dashboardFavoriteStatusGet(q)



Check favorited dashboards for current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      GetFavStarIdsSchema result = apiInstance.dashboardFavoriteStatusGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardFavoriteStatusGet");
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
| **q** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**GetFavStarIdsSchema**](GetFavStarIdsSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | None |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardGet"></a>
# **dashboardGet**
> DashboardGet200Response dashboardGet(q)



Get a list of dashboards, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    GetListSchema q = new GetListSchema(); // GetListSchema | 
    try {
      DashboardGet200Response result = apiInstance.dashboardGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardGet");
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
| **q** | [**GetListSchema**](.md)|  | [optional] |

### Return type

[**DashboardGet200Response**](DashboardGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Items from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardIdOrSlugChartsGet"></a>
# **dashboardIdOrSlugChartsGet**
> DashboardIdOrSlugChartsGet200Response dashboardIdOrSlugChartsGet(idOrSlug)



Get the chart definitions for a given dashboard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String idOrSlug = "idOrSlug_example"; // String | 
    try {
      DashboardIdOrSlugChartsGet200Response result = apiInstance.dashboardIdOrSlugChartsGet(idOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardIdOrSlugChartsGet");
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
| **idOrSlug** | **String**|  | |

### Return type

[**DashboardIdOrSlugChartsGet200Response**](DashboardIdOrSlugChartsGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard chart definitions |  -  |
| **302** | Redirects to the current digest |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="dashboardIdOrSlugDatasetsGet"></a>
# **dashboardIdOrSlugDatasetsGet**
> DashboardIdOrSlugDatasetsGet200Response dashboardIdOrSlugDatasetsGet(idOrSlug)



Returns a list of a dashboard&#39;s datasets. Each dataset includes only the information necessary to render the dashboard&#39;s charts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String idOrSlug = "idOrSlug_example"; // String | Either the id of the dashboard, or its slug
    try {
      DashboardIdOrSlugDatasetsGet200Response result = apiInstance.dashboardIdOrSlugDatasetsGet(idOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardIdOrSlugDatasetsGet");
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
| **idOrSlug** | **String**| Either the id of the dashboard, or its slug | |

### Return type

[**DashboardIdOrSlugDatasetsGet200Response**](DashboardIdOrSlugDatasetsGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard dataset definitions |  -  |
| **302** | Redirects to the current digest |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="dashboardIdOrSlugGet"></a>
# **dashboardIdOrSlugGet**
> DashboardIdOrSlugGet200Response dashboardIdOrSlugGet(idOrSlug)



Get a dashboard detail information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String idOrSlug = "idOrSlug_example"; // String | Either the id of the dashboard, or its slug
    try {
      DashboardIdOrSlugGet200Response result = apiInstance.dashboardIdOrSlugGet(idOrSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardIdOrSlugGet");
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
| **idOrSlug** | **String**| Either the id of the dashboard, or its slug | |

### Return type

[**DashboardIdOrSlugGet200Response**](DashboardIdOrSlugGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard |  -  |
| **302** | Redirects to the current digest |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="dashboardImportPost"></a>
# **dashboardImportPost**
> AnnotationLayerGet400Response dashboardImportPost(formData, overwrite, passwords)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    File formData = new File("/path/to/file"); // File | upload file (ZIP or JSON)
    Boolean overwrite = true; // Boolean | overwrite existing databases?
    String passwords = "passwords_example"; // String | JSON map of passwords for each file
    try {
      AnnotationLayerGet400Response result = apiInstance.dashboardImportPost(formData, overwrite, passwords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardImportPost");
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
| **formData** | **File**| upload file (ZIP or JSON) | [optional] |
| **overwrite** | **Boolean**| overwrite existing databases? | [optional] |
| **passwords** | **String**| JSON map of passwords for each file | [optional] |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard import result |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardInfoGet"></a>
# **dashboardInfoGet**
> AnnotationLayerInfoGet200Response dashboardInfoGet(q)



Several metadata information about dashboard API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    GetInfoSchema q = new GetInfoSchema(); // GetInfoSchema | 
    try {
      AnnotationLayerInfoGet200Response result = apiInstance.dashboardInfoGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardInfoGet");
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
| **q** | [**GetInfoSchema**](.md)|  | [optional] |

### Return type

[**AnnotationLayerInfoGet200Response**](AnnotationLayerInfoGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardPkDelete"></a>
# **dashboardPkDelete**
> AnnotationLayerGet400Response dashboardPkDelete(pk)



Deletes a Dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    Integer pk = 56; // Integer | 
    try {
      AnnotationLayerGet400Response result = apiInstance.dashboardPkDelete(pk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardPkDelete");
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
| **pk** | **Integer**|  | |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardPkPut"></a>
# **dashboardPkPut**
> DashboardPkPut200Response dashboardPkPut(pk, dashboardRestApiPut)



Changes a Dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    Integer pk = 56; // Integer | 
    DashboardRestApiPut dashboardRestApiPut = new DashboardRestApiPut(); // DashboardRestApiPut | Dashboard schema
    try {
      DashboardPkPut200Response result = apiInstance.dashboardPkPut(pk, dashboardRestApiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardPkPut");
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
| **pk** | **Integer**|  | |
| **dashboardRestApiPut** | [**DashboardRestApiPut**](DashboardRestApiPut.md)| Dashboard schema | |

### Return type

[**DashboardPkPut200Response**](DashboardPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard changed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardPkThumbnailDigestGet"></a>
# **dashboardPkThumbnailDigestGet**
> File dashboardPkThumbnailDigestGet(pk, digest, q)



Compute async or get already computed dashboard thumbnail from cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    Integer pk = 56; // Integer | 
    String digest = "digest_example"; // String | A hex digest that makes this dashboard unique
    ThumbnailQuerySchema q = new ThumbnailQuerySchema(); // ThumbnailQuerySchema | 
    try {
      File result = apiInstance.dashboardPkThumbnailDigestGet(pk, digest, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardPkThumbnailDigestGet");
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
| **pk** | **Integer**|  | |
| **digest** | **String**| A hex digest that makes this dashboard unique | |
| **q** | [**ThumbnailQuerySchema**](.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dashboard thumbnail image |  -  |
| **202** | Thumbnail does not exist on cache, fired async to compute |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardPost"></a>
# **dashboardPost**
> DashboardPost201Response dashboardPost(dashboardRestApiPost)



Create a new Dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    DashboardRestApiPost dashboardRestApiPost = new DashboardRestApiPost(); // DashboardRestApiPost | Dashboard schema
    try {
      DashboardPost201Response result = apiInstance.dashboardPost(dashboardRestApiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardPost");
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
| **dashboardRestApiPost** | [**DashboardRestApiPost**](DashboardRestApiPost.md)| Dashboard schema | |

### Return type

[**DashboardPost201Response**](DashboardPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Dashboard added |  -  |
| **302** | Redirects to the current digest |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="dashboardRelatedColumnNameGet"></a>
# **dashboardRelatedColumnNameGet**
> RelatedResponseSchema dashboardRelatedColumnNameGet(columnName, q)



Get a list of all possible owners for a dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DashboardsApi apiInstance = new DashboardsApi(defaultClient);
    String columnName = "columnName_example"; // String | 
    GetRelatedSchema q = new GetRelatedSchema(); // GetRelatedSchema | 
    try {
      RelatedResponseSchema result = apiInstance.dashboardRelatedColumnNameGet(columnName, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardsApi#dashboardRelatedColumnNameGet");
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
| **columnName** | **String**|  | |
| **q** | [**GetRelatedSchema**](.md)|  | [optional] |

### Return type

[**RelatedResponseSchema**](RelatedResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related column data |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

