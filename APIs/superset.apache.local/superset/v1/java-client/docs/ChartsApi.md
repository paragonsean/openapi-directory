# ChartsApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartDataCacheKeyGet**](ChartsApi.md#chartDataCacheKeyGet) | **GET** /chart/data/{cache_key} |  |
| [**chartDataPost**](ChartsApi.md#chartDataPost) | **POST** /chart/data |  |
| [**chartDelete**](ChartsApi.md#chartDelete) | **DELETE** /chart/ |  |
| [**chartExportGet**](ChartsApi.md#chartExportGet) | **GET** /chart/export/ |  |
| [**chartFavoriteStatusGet**](ChartsApi.md#chartFavoriteStatusGet) | **GET** /chart/favorite_status/ |  |
| [**chartGet**](ChartsApi.md#chartGet) | **GET** /chart/ |  |
| [**chartImportPost**](ChartsApi.md#chartImportPost) | **POST** /chart/import/ |  |
| [**chartInfoGet**](ChartsApi.md#chartInfoGet) | **GET** /chart/_info |  |
| [**chartPkCacheScreenshotGet**](ChartsApi.md#chartPkCacheScreenshotGet) | **GET** /chart/{pk}/cache_screenshot/ |  |
| [**chartPkDataGet**](ChartsApi.md#chartPkDataGet) | **GET** /chart/{pk}/data/ |  |
| [**chartPkDelete**](ChartsApi.md#chartPkDelete) | **DELETE** /chart/{pk} |  |
| [**chartPkGet**](ChartsApi.md#chartPkGet) | **GET** /chart/{pk} |  |
| [**chartPkPut**](ChartsApi.md#chartPkPut) | **PUT** /chart/{pk} |  |
| [**chartPkScreenshotDigestGet**](ChartsApi.md#chartPkScreenshotDigestGet) | **GET** /chart/{pk}/screenshot/{digest}/ |  |
| [**chartPkThumbnailDigestGet**](ChartsApi.md#chartPkThumbnailDigestGet) | **GET** /chart/{pk}/thumbnail/{digest}/ |  |
| [**chartPost**](ChartsApi.md#chartPost) | **POST** /chart/ |  |
| [**chartRelatedColumnNameGet**](ChartsApi.md#chartRelatedColumnNameGet) | **GET** /chart/related/{column_name} |  |


<a id="chartDataCacheKeyGet"></a>
# **chartDataCacheKeyGet**
> ChartDataResponseSchema chartDataCacheKeyGet(cacheKey)



Takes a query context cache key and returns payload data response for the given query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    String cacheKey = "cacheKey_example"; // String | 
    try {
      ChartDataResponseSchema result = apiInstance.chartDataCacheKeyGet(cacheKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartDataCacheKeyGet");
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
| **cacheKey** | **String**|  | |

### Return type

[**ChartDataResponseSchema**](ChartDataResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query result |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="chartDataPost"></a>
# **chartDataPost**
> ChartDataResponseSchema chartDataPost(chartDataQueryContextSchema)



Takes a query context constructed in the client and returns payload data response for the given query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    ChartDataQueryContextSchema chartDataQueryContextSchema = new ChartDataQueryContextSchema(); // ChartDataQueryContextSchema | A query context consists of a datasource from which to fetch data and one or many query objects.
    try {
      ChartDataResponseSchema result = apiInstance.chartDataPost(chartDataQueryContextSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartDataPost");
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
| **chartDataQueryContextSchema** | [**ChartDataQueryContextSchema**](ChartDataQueryContextSchema.md)| A query context consists of a datasource from which to fetch data and one or many query objects. | |

### Return type

[**ChartDataResponseSchema**](ChartDataResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query result |  -  |
| **202** | Async job details |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Fatal error |  -  |

<a id="chartDelete"></a>
# **chartDelete**
> AnnotationLayerGet400Response chartDelete(q)



Deletes multiple Charts in a bulk operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      AnnotationLayerGet400Response result = apiInstance.chartDelete(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartDelete");
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
| **200** | Charts bulk delete |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="chartExportGet"></a>
# **chartExportGet**
> File chartExportGet(q)



Exports multiple charts and downloads them as YAML files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      File result = apiInstance.chartExportGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartExportGet");
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

[**File**](File.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A zip file with chart(s), dataset(s) and database(s) as YAML |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="chartFavoriteStatusGet"></a>
# **chartFavoriteStatusGet**
> GetFavStarIdsSchema chartFavoriteStatusGet(q)



Check favorited dashboards for current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      GetFavStarIdsSchema result = apiInstance.chartFavoriteStatusGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartFavoriteStatusGet");
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

<a id="chartGet"></a>
# **chartGet**
> ChartGet200Response chartGet(q)



Get a list of charts, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    GetListSchema q = new GetListSchema(); // GetListSchema | 
    try {
      ChartGet200Response result = apiInstance.chartGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartGet");
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

[**ChartGet200Response**](ChartGet200Response.md)

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

<a id="chartImportPost"></a>
# **chartImportPost**
> AnnotationLayerGet400Response chartImportPost(formData, overwrite, passwords)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    File formData = new File("/path/to/file"); // File | upload file (ZIP)
    Boolean overwrite = true; // Boolean | overwrite existing databases?
    String passwords = "passwords_example"; // String | JSON map of passwords for each file
    try {
      AnnotationLayerGet400Response result = apiInstance.chartImportPost(formData, overwrite, passwords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartImportPost");
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
| **formData** | **File**| upload file (ZIP) | [optional] |
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
| **200** | Chart import result |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="chartInfoGet"></a>
# **chartInfoGet**
> AnnotationLayerInfoGet200Response chartInfoGet(q)



Several metadata information about chart API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    GetInfoSchema q = new GetInfoSchema(); // GetInfoSchema | 
    try {
      AnnotationLayerInfoGet200Response result = apiInstance.chartInfoGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartInfoGet");
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

<a id="chartPkCacheScreenshotGet"></a>
# **chartPkCacheScreenshotGet**
> ChartCacheScreenshotResponseSchema chartPkCacheScreenshotGet(pk, q)



Compute and cache a screenshot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    Integer pk = 56; // Integer | 
    ScreenshotQuerySchema q = new ScreenshotQuerySchema(); // ScreenshotQuerySchema | 
    try {
      ChartCacheScreenshotResponseSchema result = apiInstance.chartPkCacheScreenshotGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartPkCacheScreenshotGet");
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
| **q** | [**ScreenshotQuerySchema**](.md)|  | [optional] |

### Return type

[**ChartCacheScreenshotResponseSchema**](ChartCacheScreenshotResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Chart async result |  -  |
| **302** | Redirects to the current digest |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="chartPkDataGet"></a>
# **chartPkDataGet**
> ChartDataResponseSchema chartPkDataGet(pk, format, type)



Takes a chart ID and uses the query context stored when the chart was saved to return payload data response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    Integer pk = 56; // Integer | The chart ID
    String format = "format_example"; // String | The format in which the data should be returned
    String type = "type_example"; // String | The type in which the data should be returned
    try {
      ChartDataResponseSchema result = apiInstance.chartPkDataGet(pk, format, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartPkDataGet");
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
| **pk** | **Integer**| The chart ID | |
| **format** | **String**| The format in which the data should be returned | [optional] |
| **type** | **String**| The type in which the data should be returned | [optional] |

### Return type

[**ChartDataResponseSchema**](ChartDataResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query result |  -  |
| **202** | Async job details |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Fatal error |  -  |

<a id="chartPkDelete"></a>
# **chartPkDelete**
> AnnotationLayerGet400Response chartPkDelete(pk)



Deletes a Chart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    Integer pk = 56; // Integer | 
    try {
      AnnotationLayerGet400Response result = apiInstance.chartPkDelete(pk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartPkDelete");
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
| **200** | Chart delete |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="chartPkGet"></a>
# **chartPkGet**
> ChartPkGet200Response chartPkGet(pk, q)



Get a chart detail information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    Integer pk = 56; // Integer | 
    GetItemSchema q = new GetItemSchema(); // GetItemSchema | 
    try {
      ChartPkGet200Response result = apiInstance.chartPkGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartPkGet");
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
| **q** | [**GetItemSchema**](.md)|  | [optional] |

### Return type

[**ChartPkGet200Response**](ChartPkGet200Response.md)

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
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="chartPkPut"></a>
# **chartPkPut**
> ChartPkPut200Response chartPkPut(pk, chartRestApiPut)



Changes a Chart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    Integer pk = 56; // Integer | 
    ChartRestApiPut chartRestApiPut = new ChartRestApiPut(); // ChartRestApiPut | Chart schema
    try {
      ChartPkPut200Response result = apiInstance.chartPkPut(pk, chartRestApiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartPkPut");
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
| **chartRestApiPut** | [**ChartRestApiPut**](ChartRestApiPut.md)| Chart schema | |

### Return type

[**ChartPkPut200Response**](ChartPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Chart changed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="chartPkScreenshotDigestGet"></a>
# **chartPkScreenshotDigestGet**
> File chartPkScreenshotDigestGet(pk, digest)



Get a computed screenshot from cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    Integer pk = 56; // Integer | 
    String digest = "digest_example"; // String | 
    try {
      File result = apiInstance.chartPkScreenshotDigestGet(pk, digest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartPkScreenshotDigestGet");
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
| **digest** | **String**|  | |

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
| **200** | Chart thumbnail image |  -  |
| **302** | Redirects to the current digest |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="chartPkThumbnailDigestGet"></a>
# **chartPkThumbnailDigestGet**
> File chartPkThumbnailDigestGet(pk, digest)



Compute or get already computed chart thumbnail from cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    Integer pk = 56; // Integer | 
    String digest = "digest_example"; // String | 
    try {
      File result = apiInstance.chartPkThumbnailDigestGet(pk, digest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartPkThumbnailDigestGet");
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
| **digest** | **String**|  | |

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
| **200** | Chart thumbnail image |  -  |
| **302** | Redirects to the current digest |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="chartPost"></a>
# **chartPost**
> ChartPost201Response chartPost(chartRestApiPost)



Create a new Chart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    ChartRestApiPost chartRestApiPost = new ChartRestApiPost(); // ChartRestApiPost | Chart schema
    try {
      ChartPost201Response result = apiInstance.chartPost(chartRestApiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartPost");
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
| **chartRestApiPost** | [**ChartRestApiPost**](ChartRestApiPost.md)| Chart schema | |

### Return type

[**ChartPost201Response**](ChartPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Chart added |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="chartRelatedColumnNameGet"></a>
# **chartRelatedColumnNameGet**
> RelatedResponseSchema chartRelatedColumnNameGet(columnName, q)



Get a list of all possible owners for a chart. Use &#x60;owners&#x60; has the &#x60;column_name&#x60; parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    ChartsApi apiInstance = new ChartsApi(defaultClient);
    String columnName = "columnName_example"; // String | 
    GetRelatedSchema q = new GetRelatedSchema(); // GetRelatedSchema | 
    try {
      RelatedResponseSchema result = apiInstance.chartRelatedColumnNameGet(columnName, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsApi#chartRelatedColumnNameGet");
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

