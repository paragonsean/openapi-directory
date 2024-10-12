# TransportEsendexApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportEsendexGetCollection**](TransportEsendexApi.md#apiTransportEsendexGetCollection) | **GET** /api/transport-esendex | Retrieves the collection of TransportEsendex resources. |
| [**apiTransportEsendexIdDelete**](TransportEsendexApi.md#apiTransportEsendexIdDelete) | **DELETE** /api/transport-esendex/{id} | Removes the TransportEsendex resource. |
| [**apiTransportEsendexIdGet**](TransportEsendexApi.md#apiTransportEsendexIdGet) | **GET** /api/transport-esendex/{id} | Retrieves a TransportEsendex resource. |
| [**apiTransportEsendexIdPatch**](TransportEsendexApi.md#apiTransportEsendexIdPatch) | **PATCH** /api/transport-esendex/{id} | Updates the TransportEsendex resource. |
| [**apiTransportEsendexIdPut**](TransportEsendexApi.md#apiTransportEsendexIdPut) | **PUT** /api/transport-esendex/{id} | Replaces the TransportEsendex resource. |
| [**apiTransportEsendexPost**](TransportEsendexApi.md#apiTransportEsendexPost) | **POST** /api/transport-esendex | Creates a TransportEsendex resource. |


<a id="apiTransportEsendexGetCollection"></a>
# **apiTransportEsendexGetCollection**
> List&lt;TransportEsendexGet&gt; apiTransportEsendexGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportEsendex resources.

Retrieves the collection of TransportEsendex resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEsendexApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEsendexApi apiInstance = new TransportEsendexApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportEsendexGet> result = apiInstance.apiTransportEsendexGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEsendexApi#apiTransportEsendexGetCollection");
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

[**List&lt;TransportEsendexGet&gt;**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEsendex collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEsendexIdDelete"></a>
# **apiTransportEsendexIdDelete**
> apiTransportEsendexIdDelete(id)

Removes the TransportEsendex resource.

Removes the TransportEsendex resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEsendexApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEsendexApi apiInstance = new TransportEsendexApi(defaultClient);
    String id = "id_example"; // String | TransportEsendex identifier
    try {
      apiInstance.apiTransportEsendexIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEsendexApi#apiTransportEsendexIdDelete");
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
| **id** | **String**| TransportEsendex identifier | |

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
| **204** | TransportEsendex resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEsendexIdGet"></a>
# **apiTransportEsendexIdGet**
> TransportEsendexGet apiTransportEsendexIdGet(id)

Retrieves a TransportEsendex resource.

Retrieves a TransportEsendex resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEsendexApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEsendexApi apiInstance = new TransportEsendexApi(defaultClient);
    String id = "id_example"; // String | TransportEsendex identifier
    try {
      TransportEsendexGet result = apiInstance.apiTransportEsendexIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEsendexApi#apiTransportEsendexIdGet");
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
| **id** | **String**| TransportEsendex identifier | |

### Return type

[**TransportEsendexGet**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEsendex resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEsendexIdPatch"></a>
# **apiTransportEsendexIdPatch**
> TransportEsendexGet apiTransportEsendexIdPatch(id, transportEsendexPatch)

Updates the TransportEsendex resource.

Updates the TransportEsendex resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEsendexApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEsendexApi apiInstance = new TransportEsendexApi(defaultClient);
    String id = "id_example"; // String | TransportEsendex identifier
    TransportEsendexPatch transportEsendexPatch = new TransportEsendexPatch(); // TransportEsendexPatch | The updated TransportEsendex resource
    try {
      TransportEsendexGet result = apiInstance.apiTransportEsendexIdPatch(id, transportEsendexPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEsendexApi#apiTransportEsendexIdPatch");
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
| **id** | **String**| TransportEsendex identifier | |
| **transportEsendexPatch** | [**TransportEsendexPatch**](TransportEsendexPatch.md)| The updated TransportEsendex resource | |

### Return type

[**TransportEsendexGet**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEsendex resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEsendexIdPut"></a>
# **apiTransportEsendexIdPut**
> TransportEsendexGet apiTransportEsendexIdPut(id, transportEsendexPut)

Replaces the TransportEsendex resource.

Replaces the TransportEsendex resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEsendexApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEsendexApi apiInstance = new TransportEsendexApi(defaultClient);
    String id = "id_example"; // String | TransportEsendex identifier
    TransportEsendexPut transportEsendexPut = new TransportEsendexPut(); // TransportEsendexPut | The updated TransportEsendex resource
    try {
      TransportEsendexGet result = apiInstance.apiTransportEsendexIdPut(id, transportEsendexPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEsendexApi#apiTransportEsendexIdPut");
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
| **id** | **String**| TransportEsendex identifier | |
| **transportEsendexPut** | [**TransportEsendexPut**](TransportEsendexPut.md)| The updated TransportEsendex resource | |

### Return type

[**TransportEsendexGet**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEsendex resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEsendexPost"></a>
# **apiTransportEsendexPost**
> TransportEsendexGet apiTransportEsendexPost(transportEsendexPost)

Creates a TransportEsendex resource.

Creates a TransportEsendex resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEsendexApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEsendexApi apiInstance = new TransportEsendexApi(defaultClient);
    TransportEsendexPost transportEsendexPost = new TransportEsendexPost(); // TransportEsendexPost | The new TransportEsendex resource
    try {
      TransportEsendexGet result = apiInstance.apiTransportEsendexPost(transportEsendexPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEsendexApi#apiTransportEsendexPost");
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
| **transportEsendexPost** | [**TransportEsendexPost**](TransportEsendexPost.md)| The new TransportEsendex resource | |

### Return type

[**TransportEsendexGet**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportEsendex resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

