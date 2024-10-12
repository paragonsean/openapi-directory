# QueriesApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryDistinctColumnNameGet**](QueriesApi.md#queryDistinctColumnNameGet) | **GET** /query/distinct/{column_name} |  |
| [**queryGet**](QueriesApi.md#queryGet) | **GET** /query/ |  |
| [**queryPkGet**](QueriesApi.md#queryPkGet) | **GET** /query/{pk} |  |
| [**queryRelatedColumnNameGet**](QueriesApi.md#queryRelatedColumnNameGet) | **GET** /query/related/{column_name} |  |
| [**savedQueryDelete**](QueriesApi.md#savedQueryDelete) | **DELETE** /saved_query/ |  |
| [**savedQueryDistinctColumnNameGet**](QueriesApi.md#savedQueryDistinctColumnNameGet) | **GET** /saved_query/distinct/{column_name} |  |
| [**savedQueryExportGet**](QueriesApi.md#savedQueryExportGet) | **GET** /saved_query/export/ |  |
| [**savedQueryGet**](QueriesApi.md#savedQueryGet) | **GET** /saved_query/ |  |
| [**savedQueryImportPost**](QueriesApi.md#savedQueryImportPost) | **POST** /saved_query/import/ |  |
| [**savedQueryInfoGet**](QueriesApi.md#savedQueryInfoGet) | **GET** /saved_query/_info |  |
| [**savedQueryPkDelete**](QueriesApi.md#savedQueryPkDelete) | **DELETE** /saved_query/{pk} |  |
| [**savedQueryPkGet**](QueriesApi.md#savedQueryPkGet) | **GET** /saved_query/{pk} |  |
| [**savedQueryPkPut**](QueriesApi.md#savedQueryPkPut) | **PUT** /saved_query/{pk} |  |
| [**savedQueryPost**](QueriesApi.md#savedQueryPost) | **POST** /saved_query/ |  |
| [**savedQueryRelatedColumnNameGet**](QueriesApi.md#savedQueryRelatedColumnNameGet) | **GET** /saved_query/related/{column_name} |  |


<a id="queryDistinctColumnNameGet"></a>
# **queryDistinctColumnNameGet**
> DistincResponseSchema queryDistinctColumnNameGet(columnName, q)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    String columnName = "columnName_example"; // String | 
    GetRelatedSchema q = new GetRelatedSchema(); // GetRelatedSchema | 
    try {
      DistincResponseSchema result = apiInstance.queryDistinctColumnNameGet(columnName, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#queryDistinctColumnNameGet");
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

[**DistincResponseSchema**](DistincResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Distinct field data |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="queryGet"></a>
# **queryGet**
> QueryGet200Response queryGet(q)



Get a list of queries, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    GetListSchema q = new GetListSchema(); // GetListSchema | 
    try {
      QueryGet200Response result = apiInstance.queryGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#queryGet");
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

[**QueryGet200Response**](QueryGet200Response.md)

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

<a id="queryPkGet"></a>
# **queryPkGet**
> QueryPkGet200Response queryPkGet(pk, q)



Get query detail information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    Integer pk = 56; // Integer | 
    GetItemSchema q = new GetItemSchema(); // GetItemSchema | 
    try {
      QueryPkGet200Response result = apiInstance.queryPkGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#queryPkGet");
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

[**QueryPkGet200Response**](QueryPkGet200Response.md)

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

<a id="queryRelatedColumnNameGet"></a>
# **queryRelatedColumnNameGet**
> RelatedResponseSchema queryRelatedColumnNameGet(columnName, q)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    String columnName = "columnName_example"; // String | 
    GetRelatedSchema q = new GetRelatedSchema(); // GetRelatedSchema | 
    try {
      RelatedResponseSchema result = apiInstance.queryRelatedColumnNameGet(columnName, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#queryRelatedColumnNameGet");
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

<a id="savedQueryDelete"></a>
# **savedQueryDelete**
> AnnotationLayerGet400Response savedQueryDelete(q)



Deletes multiple saved queries in a bulk operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      AnnotationLayerGet400Response result = apiInstance.savedQueryDelete(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryDelete");
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
| **200** | Saved queries bulk delete |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="savedQueryDistinctColumnNameGet"></a>
# **savedQueryDistinctColumnNameGet**
> DistincResponseSchema savedQueryDistinctColumnNameGet(columnName, q)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    String columnName = "columnName_example"; // String | 
    GetRelatedSchema q = new GetRelatedSchema(); // GetRelatedSchema | 
    try {
      DistincResponseSchema result = apiInstance.savedQueryDistinctColumnNameGet(columnName, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryDistinctColumnNameGet");
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

[**DistincResponseSchema**](DistincResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Distinct field data |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="savedQueryExportGet"></a>
# **savedQueryExportGet**
> File savedQueryExportGet(q)



Exports multiple saved queries and downloads them as YAML files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      File result = apiInstance.savedQueryExportGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryExportGet");
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
| **200** | A zip file with saved query(ies) and database(s) as YAML |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="savedQueryGet"></a>
# **savedQueryGet**
> SavedQueryGet200Response savedQueryGet(q)



Get a list of saved queries, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    GetListSchema q = new GetListSchema(); // GetListSchema | 
    try {
      SavedQueryGet200Response result = apiInstance.savedQueryGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryGet");
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

[**SavedQueryGet200Response**](SavedQueryGet200Response.md)

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

<a id="savedQueryImportPost"></a>
# **savedQueryImportPost**
> AnnotationLayerGet400Response savedQueryImportPost(formData, overwrite, passwords)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    File formData = new File("/path/to/file"); // File | upload file (ZIP)
    Boolean overwrite = true; // Boolean | overwrite existing saved queries?
    String passwords = "passwords_example"; // String | JSON map of passwords for each file
    try {
      AnnotationLayerGet400Response result = apiInstance.savedQueryImportPost(formData, overwrite, passwords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryImportPost");
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
| **overwrite** | **Boolean**| overwrite existing saved queries? | [optional] |
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
| **200** | Saved Query import result |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="savedQueryInfoGet"></a>
# **savedQueryInfoGet**
> AnnotationLayerInfoGet200Response savedQueryInfoGet(q)



Get metadata information about this API resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    GetInfoSchema q = new GetInfoSchema(); // GetInfoSchema | 
    try {
      AnnotationLayerInfoGet200Response result = apiInstance.savedQueryInfoGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryInfoGet");
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

<a id="savedQueryPkDelete"></a>
# **savedQueryPkDelete**
> AnnotationLayerGet400Response savedQueryPkDelete(pk)



Delete saved query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    Integer pk = 56; // Integer | 
    try {
      AnnotationLayerGet400Response result = apiInstance.savedQueryPkDelete(pk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryPkDelete");
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
| **200** | Item deleted |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="savedQueryPkGet"></a>
# **savedQueryPkGet**
> SavedQueryPkGet200Response savedQueryPkGet(pk, q)



Get a saved query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    Integer pk = 56; // Integer | 
    GetItemSchema q = new GetItemSchema(); // GetItemSchema | 
    try {
      SavedQueryPkGet200Response result = apiInstance.savedQueryPkGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryPkGet");
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

[**SavedQueryPkGet200Response**](SavedQueryPkGet200Response.md)

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

<a id="savedQueryPkPut"></a>
# **savedQueryPkPut**
> SavedQueryPkPut200Response savedQueryPkPut(pk, savedQueryRestApiPut)



Update a saved query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    Integer pk = 56; // Integer | 
    SavedQueryRestApiPut savedQueryRestApiPut = new SavedQueryRestApiPut(); // SavedQueryRestApiPut | Model schema
    try {
      SavedQueryPkPut200Response result = apiInstance.savedQueryPkPut(pk, savedQueryRestApiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryPkPut");
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
| **savedQueryRestApiPut** | [**SavedQueryRestApiPut**](SavedQueryRestApiPut.md)| Model schema | |

### Return type

[**SavedQueryPkPut200Response**](SavedQueryPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item changed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="savedQueryPost"></a>
# **savedQueryPost**
> SavedQueryPost201Response savedQueryPost(savedQueryRestApiPost)



Create a saved query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    SavedQueryRestApiPost savedQueryRestApiPost = new SavedQueryRestApiPost(); // SavedQueryRestApiPost | Model schema
    try {
      SavedQueryPost201Response result = apiInstance.savedQueryPost(savedQueryRestApiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryPost");
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
| **savedQueryRestApiPost** | [**SavedQueryRestApiPost**](SavedQueryRestApiPost.md)| Model schema | |

### Return type

[**SavedQueryPost201Response**](SavedQueryPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Item inserted |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="savedQueryRelatedColumnNameGet"></a>
# **savedQueryRelatedColumnNameGet**
> RelatedResponseSchema savedQueryRelatedColumnNameGet(columnName, q)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    String columnName = "columnName_example"; // String | 
    GetRelatedSchema q = new GetRelatedSchema(); // GetRelatedSchema | 
    try {
      RelatedResponseSchema result = apiInstance.savedQueryRelatedColumnNameGet(columnName, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#savedQueryRelatedColumnNameGet");
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

