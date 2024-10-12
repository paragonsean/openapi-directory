# TransportVonageApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportVonageGetCollection**](TransportVonageApi.md#apiTransportVonageGetCollection) | **GET** /api/transport-vonage | Retrieves the collection of TransportVonage resources. |
| [**apiTransportVonageIdDelete**](TransportVonageApi.md#apiTransportVonageIdDelete) | **DELETE** /api/transport-vonage/{id} | Removes the TransportVonage resource. |
| [**apiTransportVonageIdGet**](TransportVonageApi.md#apiTransportVonageIdGet) | **GET** /api/transport-vonage/{id} | Retrieves a TransportVonage resource. |
| [**apiTransportVonageIdPatch**](TransportVonageApi.md#apiTransportVonageIdPatch) | **PATCH** /api/transport-vonage/{id} | Updates the TransportVonage resource. |
| [**apiTransportVonageIdPut**](TransportVonageApi.md#apiTransportVonageIdPut) | **PUT** /api/transport-vonage/{id} | Replaces the TransportVonage resource. |
| [**apiTransportVonagePost**](TransportVonageApi.md#apiTransportVonagePost) | **POST** /api/transport-vonage | Creates a TransportVonage resource. |


<a id="apiTransportVonageGetCollection"></a>
# **apiTransportVonageGetCollection**
> List&lt;TransportVonageGet&gt; apiTransportVonageGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportVonage resources.

Retrieves the collection of TransportVonage resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportVonageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportVonageApi apiInstance = new TransportVonageApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportVonageGet> result = apiInstance.apiTransportVonageGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportVonageApi#apiTransportVonageGetCollection");
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

[**List&lt;TransportVonageGet&gt;**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportVonage collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportVonageIdDelete"></a>
# **apiTransportVonageIdDelete**
> apiTransportVonageIdDelete(id)

Removes the TransportVonage resource.

Removes the TransportVonage resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportVonageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportVonageApi apiInstance = new TransportVonageApi(defaultClient);
    String id = "id_example"; // String | TransportVonage identifier
    try {
      apiInstance.apiTransportVonageIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportVonageApi#apiTransportVonageIdDelete");
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
| **id** | **String**| TransportVonage identifier | |

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
| **204** | TransportVonage resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportVonageIdGet"></a>
# **apiTransportVonageIdGet**
> TransportVonageGet apiTransportVonageIdGet(id)

Retrieves a TransportVonage resource.

Retrieves a TransportVonage resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportVonageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportVonageApi apiInstance = new TransportVonageApi(defaultClient);
    String id = "id_example"; // String | TransportVonage identifier
    try {
      TransportVonageGet result = apiInstance.apiTransportVonageIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportVonageApi#apiTransportVonageIdGet");
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
| **id** | **String**| TransportVonage identifier | |

### Return type

[**TransportVonageGet**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportVonage resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportVonageIdPatch"></a>
# **apiTransportVonageIdPatch**
> TransportVonageGet apiTransportVonageIdPatch(id, transportVonagePatch)

Updates the TransportVonage resource.

Updates the TransportVonage resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportVonageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportVonageApi apiInstance = new TransportVonageApi(defaultClient);
    String id = "id_example"; // String | TransportVonage identifier
    TransportVonagePatch transportVonagePatch = new TransportVonagePatch(); // TransportVonagePatch | The updated TransportVonage resource
    try {
      TransportVonageGet result = apiInstance.apiTransportVonageIdPatch(id, transportVonagePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportVonageApi#apiTransportVonageIdPatch");
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
| **id** | **String**| TransportVonage identifier | |
| **transportVonagePatch** | [**TransportVonagePatch**](TransportVonagePatch.md)| The updated TransportVonage resource | |

### Return type

[**TransportVonageGet**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportVonage resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportVonageIdPut"></a>
# **apiTransportVonageIdPut**
> TransportVonageGet apiTransportVonageIdPut(id, transportVonagePut)

Replaces the TransportVonage resource.

Replaces the TransportVonage resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportVonageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportVonageApi apiInstance = new TransportVonageApi(defaultClient);
    String id = "id_example"; // String | TransportVonage identifier
    TransportVonagePut transportVonagePut = new TransportVonagePut(); // TransportVonagePut | The updated TransportVonage resource
    try {
      TransportVonageGet result = apiInstance.apiTransportVonageIdPut(id, transportVonagePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportVonageApi#apiTransportVonageIdPut");
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
| **id** | **String**| TransportVonage identifier | |
| **transportVonagePut** | [**TransportVonagePut**](TransportVonagePut.md)| The updated TransportVonage resource | |

### Return type

[**TransportVonageGet**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportVonage resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportVonagePost"></a>
# **apiTransportVonagePost**
> TransportVonageGet apiTransportVonagePost(transportVonagePost)

Creates a TransportVonage resource.

Creates a TransportVonage resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportVonageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportVonageApi apiInstance = new TransportVonageApi(defaultClient);
    TransportVonagePost transportVonagePost = new TransportVonagePost(); // TransportVonagePost | The new TransportVonage resource
    try {
      TransportVonageGet result = apiInstance.apiTransportVonagePost(transportVonagePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportVonageApi#apiTransportVonagePost");
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
| **transportVonagePost** | [**TransportVonagePost**](TransportVonagePost.md)| The new TransportVonage resource | |

### Return type

[**TransportVonageGet**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportVonage resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

