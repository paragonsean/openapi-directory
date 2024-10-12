# TransportYunpianApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportYunpianGetCollection**](TransportYunpianApi.md#apiTransportYunpianGetCollection) | **GET** /api/transport-yunpian | Retrieves the collection of TransportYunpian resources. |
| [**apiTransportYunpianIdDelete**](TransportYunpianApi.md#apiTransportYunpianIdDelete) | **DELETE** /api/transport-yunpian/{id} | Removes the TransportYunpian resource. |
| [**apiTransportYunpianIdGet**](TransportYunpianApi.md#apiTransportYunpianIdGet) | **GET** /api/transport-yunpian/{id} | Retrieves a TransportYunpian resource. |
| [**apiTransportYunpianIdPatch**](TransportYunpianApi.md#apiTransportYunpianIdPatch) | **PATCH** /api/transport-yunpian/{id} | Updates the TransportYunpian resource. |
| [**apiTransportYunpianIdPut**](TransportYunpianApi.md#apiTransportYunpianIdPut) | **PUT** /api/transport-yunpian/{id} | Replaces the TransportYunpian resource. |
| [**apiTransportYunpianPost**](TransportYunpianApi.md#apiTransportYunpianPost) | **POST** /api/transport-yunpian | Creates a TransportYunpian resource. |


<a id="apiTransportYunpianGetCollection"></a>
# **apiTransportYunpianGetCollection**
> List&lt;TransportYunpianGet&gt; apiTransportYunpianGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportYunpian resources.

Retrieves the collection of TransportYunpian resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportYunpianApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportYunpianApi apiInstance = new TransportYunpianApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportYunpianGet> result = apiInstance.apiTransportYunpianGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportYunpianApi#apiTransportYunpianGetCollection");
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
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **dataSegmentCode** | **String**|  | [optional] |
| **dataSegmentCode2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **partition** | **String**|  | [optional] |
| **partition2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;TransportYunpianGet&gt;**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportYunpian collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportYunpianIdDelete"></a>
# **apiTransportYunpianIdDelete**
> apiTransportYunpianIdDelete(id)

Removes the TransportYunpian resource.

Removes the TransportYunpian resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportYunpianApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportYunpianApi apiInstance = new TransportYunpianApi(defaultClient);
    String id = "id_example"; // String | TransportYunpian identifier
    try {
      apiInstance.apiTransportYunpianIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportYunpianApi#apiTransportYunpianIdDelete");
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
| **id** | **String**| TransportYunpian identifier | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | TransportYunpian resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportYunpianIdGet"></a>
# **apiTransportYunpianIdGet**
> TransportYunpianGet apiTransportYunpianIdGet(id)

Retrieves a TransportYunpian resource.

Retrieves a TransportYunpian resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportYunpianApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportYunpianApi apiInstance = new TransportYunpianApi(defaultClient);
    String id = "id_example"; // String | TransportYunpian identifier
    try {
      TransportYunpianGet result = apiInstance.apiTransportYunpianIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportYunpianApi#apiTransportYunpianIdGet");
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
| **id** | **String**| TransportYunpian identifier | |

### Return type

[**TransportYunpianGet**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportYunpian resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportYunpianIdPatch"></a>
# **apiTransportYunpianIdPatch**
> TransportYunpianGet apiTransportYunpianIdPatch(id, transportYunpianPatch)

Updates the TransportYunpian resource.

Updates the TransportYunpian resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportYunpianApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportYunpianApi apiInstance = new TransportYunpianApi(defaultClient);
    String id = "id_example"; // String | TransportYunpian identifier
    TransportYunpianPatch transportYunpianPatch = new TransportYunpianPatch(); // TransportYunpianPatch | The updated TransportYunpian resource
    try {
      TransportYunpianGet result = apiInstance.apiTransportYunpianIdPatch(id, transportYunpianPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportYunpianApi#apiTransportYunpianIdPatch");
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
| **id** | **String**| TransportYunpian identifier | |
| **transportYunpianPatch** | [**TransportYunpianPatch**](TransportYunpianPatch.md)| The updated TransportYunpian resource | |

### Return type

[**TransportYunpianGet**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportYunpian resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportYunpianIdPut"></a>
# **apiTransportYunpianIdPut**
> TransportYunpianGet apiTransportYunpianIdPut(id, transportYunpianPut)

Replaces the TransportYunpian resource.

Replaces the TransportYunpian resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportYunpianApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportYunpianApi apiInstance = new TransportYunpianApi(defaultClient);
    String id = "id_example"; // String | TransportYunpian identifier
    TransportYunpianPut transportYunpianPut = new TransportYunpianPut(); // TransportYunpianPut | The updated TransportYunpian resource
    try {
      TransportYunpianGet result = apiInstance.apiTransportYunpianIdPut(id, transportYunpianPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportYunpianApi#apiTransportYunpianIdPut");
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
| **id** | **String**| TransportYunpian identifier | |
| **transportYunpianPut** | [**TransportYunpianPut**](TransportYunpianPut.md)| The updated TransportYunpian resource | |

### Return type

[**TransportYunpianGet**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportYunpian resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportYunpianPost"></a>
# **apiTransportYunpianPost**
> TransportYunpianGet apiTransportYunpianPost(transportYunpianPost)

Creates a TransportYunpian resource.

Creates a TransportYunpian resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportYunpianApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportYunpianApi apiInstance = new TransportYunpianApi(defaultClient);
    TransportYunpianPost transportYunpianPost = new TransportYunpianPost(); // TransportYunpianPost | The new TransportYunpian resource
    try {
      TransportYunpianGet result = apiInstance.apiTransportYunpianPost(transportYunpianPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportYunpianApi#apiTransportYunpianPost");
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
| **transportYunpianPost** | [**TransportYunpianPost**](TransportYunpianPost.md)| The new TransportYunpian resource | |

### Return type

[**TransportYunpianGet**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportYunpian resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

