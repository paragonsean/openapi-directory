# QshowApi

All URIs are relative to *https://quotes.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**qshowDelete**](QshowApi.md#qshowDelete) | **DELETE** /qshow |  |
| [**qshowGet**](QshowApi.md#qshowGet) | **GET** /qshow |  |
| [**qshowListGet**](QshowApi.md#qshowListGet) | **GET** /qshow/list |  |
| [**qshowPatch**](QshowApi.md#qshowPatch) | **PATCH** /qshow |  |
| [**qshowPut**](QshowApi.md#qshowPut) | **PUT** /qshow |  |
| [**qshowQuotesAddPost**](QshowApi.md#qshowQuotesAddPost) | **POST** /qshow/quotes/add |  |
| [**qshowQuotesGet**](QshowApi.md#qshowQuotesGet) | **GET** /qshow/quotes |  |
| [**qshowQuotesRemovePost**](QshowApi.md#qshowQuotesRemovePost) | **POST** /qshow/quotes/remove |  |


<a id="qshowDelete"></a>
# **qshowDelete**
> qshowDelete(id)



Delete a qshow. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QshowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QshowApi apiInstance = new QshowApi(defaultClient);
    String id = "id_example"; // String | Qshow ID
    try {
      apiInstance.qshowDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling QshowApi#qshowDelete");
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
| **id** | **String**| Qshow ID | |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="qshowGet"></a>
# **qshowGet**
> qshowGet(id)



Gets a details about a qshow. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QshowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QshowApi apiInstance = new QshowApi(defaultClient);
    String id = "id_example"; // String | Qshow ID
    try {
      apiInstance.qshowGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling QshowApi#qshowGet");
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
| **id** | **String**| Qshow ID | |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="qshowListGet"></a>
# **qshowListGet**
> qshowListGet(start, _public)



Get the list of Qshows in They Said So platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QshowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QshowApi apiInstance = new QshowApi(defaultClient);
    Integer start = 0; // Integer | Response is paged. This parameter controls where response starts the listing at
    Boolean _public = false; // Boolean | Should include public qshows or not in the list
    try {
      apiInstance.qshowListGet(start, _public);
    } catch (ApiException e) {
      System.err.println("Exception when calling QshowApi#qshowListGet");
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
| **start** | **Integer**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0] |
| **_public** | **Boolean**| Should include public qshows or not in the list | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qshowPatch"></a>
# **qshowPatch**
> qshowPatch(id, title, description, tags)



Update an existing qshow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QshowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QshowApi apiInstance = new QshowApi(defaultClient);
    String id = "id_example"; // String | Qshow ID
    String title = "title_example"; // String | Qshow title
    String description = "description_example"; // String | Qshow description
    List<String> tags = Arrays.asList(); // List<String> | Tags for the qshow
    try {
      apiInstance.qshowPatch(id, title, description, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling QshowApi#qshowPatch");
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
| **id** | **String**| Qshow ID | |
| **title** | **String**| Qshow title | [optional] |
| **description** | **String**| Qshow description | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tags for the qshow | [optional] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="qshowPut"></a>
# **qshowPut**
> qshowPut(title, description, tags)



Create and add a new qshow to your private collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QshowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QshowApi apiInstance = new QshowApi(defaultClient);
    String title = "title_example"; // String | Qshow title
    String description = "description_example"; // String | Qshow description
    List<String> tags = Arrays.asList(); // List<String> | Tags for the qshow
    try {
      apiInstance.qshowPut(title, description, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling QshowApi#qshowPut");
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
| **title** | **String**| Qshow title | |
| **description** | **String**| Qshow description | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tags for the qshow | [optional] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qshowQuotesAddPost"></a>
# **qshowQuotesAddPost**
> qshowQuotesAddPost(id, quoteid)



Add a quote to a given Qshow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QshowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QshowApi apiInstance = new QshowApi(defaultClient);
    String id = "id_example"; // String | Qshow ID
    String quoteid = "quoteid_example"; // String | Quote ID to add the qshow collection
    try {
      apiInstance.qshowQuotesAddPost(id, quoteid);
    } catch (ApiException e) {
      System.err.println("Exception when calling QshowApi#qshowQuotesAddPost");
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
| **id** | **String**| Qshow ID | |
| **quoteid** | **String**| Quote ID to add the qshow collection | |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="qshowQuotesGet"></a>
# **qshowQuotesGet**
> qshowQuotesGet(id)



Get the quotes in a given Qshow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QshowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QshowApi apiInstance = new QshowApi(defaultClient);
    String id = "id_example"; // String | Qshow ID
    try {
      apiInstance.qshowQuotesGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling QshowApi#qshowQuotesGet");
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
| **id** | **String**| Qshow ID | |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="qshowQuotesRemovePost"></a>
# **qshowQuotesRemovePost**
> qshowQuotesRemovePost(id, quoteid)



Remove a quote to a given Qshow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QshowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QshowApi apiInstance = new QshowApi(defaultClient);
    String id = "id_example"; // String | Qshow ID
    String quoteid = "quoteid_example"; // String | Quote ID to remove from the qshow collection
    try {
      apiInstance.qshowQuotesRemovePost(id, quoteid);
    } catch (ApiException e) {
      System.err.println("Exception when calling QshowApi#qshowQuotesRemovePost");
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
| **id** | **String**| Qshow ID | |
| **quoteid** | **String**| Quote ID to remove from the qshow collection | |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

