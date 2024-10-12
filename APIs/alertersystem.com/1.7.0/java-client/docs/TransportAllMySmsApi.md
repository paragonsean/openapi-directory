# TransportAllMySmsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportAllMySmsGetCollection**](TransportAllMySmsApi.md#apiTransportAllMySmsGetCollection) | **GET** /api/transport-all-my-sms | Retrieves the collection of TransportAllMySms resources. |
| [**apiTransportAllMySmsIdDelete**](TransportAllMySmsApi.md#apiTransportAllMySmsIdDelete) | **DELETE** /api/transport-all-my-sms/{id} | Removes the TransportAllMySms resource. |
| [**apiTransportAllMySmsIdGet**](TransportAllMySmsApi.md#apiTransportAllMySmsIdGet) | **GET** /api/transport-all-my-sms/{id} | Retrieves a TransportAllMySms resource. |
| [**apiTransportAllMySmsIdPatch**](TransportAllMySmsApi.md#apiTransportAllMySmsIdPatch) | **PATCH** /api/transport-all-my-sms/{id} | Updates the TransportAllMySms resource. |
| [**apiTransportAllMySmsIdPut**](TransportAllMySmsApi.md#apiTransportAllMySmsIdPut) | **PUT** /api/transport-all-my-sms/{id} | Replaces the TransportAllMySms resource. |
| [**apiTransportAllMySmsPost**](TransportAllMySmsApi.md#apiTransportAllMySmsPost) | **POST** /api/transport-all-my-sms | Creates a TransportAllMySms resource. |


<a id="apiTransportAllMySmsGetCollection"></a>
# **apiTransportAllMySmsGetCollection**
> List&lt;TransportAllMySmsGet&gt; apiTransportAllMySmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportAllMySms resources.

Retrieves the collection of TransportAllMySms resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAllMySmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAllMySmsApi apiInstance = new TransportAllMySmsApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportAllMySmsGet> result = apiInstance.apiTransportAllMySmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAllMySmsApi#apiTransportAllMySmsGetCollection");
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

[**List&lt;TransportAllMySmsGet&gt;**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAllMySms collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAllMySmsIdDelete"></a>
# **apiTransportAllMySmsIdDelete**
> apiTransportAllMySmsIdDelete(id)

Removes the TransportAllMySms resource.

Removes the TransportAllMySms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAllMySmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAllMySmsApi apiInstance = new TransportAllMySmsApi(defaultClient);
    String id = "id_example"; // String | TransportAllMySms identifier
    try {
      apiInstance.apiTransportAllMySmsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAllMySmsApi#apiTransportAllMySmsIdDelete");
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
| **id** | **String**| TransportAllMySms identifier | |

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
| **204** | TransportAllMySms resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAllMySmsIdGet"></a>
# **apiTransportAllMySmsIdGet**
> TransportAllMySmsGet apiTransportAllMySmsIdGet(id)

Retrieves a TransportAllMySms resource.

Retrieves a TransportAllMySms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAllMySmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAllMySmsApi apiInstance = new TransportAllMySmsApi(defaultClient);
    String id = "id_example"; // String | TransportAllMySms identifier
    try {
      TransportAllMySmsGet result = apiInstance.apiTransportAllMySmsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAllMySmsApi#apiTransportAllMySmsIdGet");
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
| **id** | **String**| TransportAllMySms identifier | |

### Return type

[**TransportAllMySmsGet**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAllMySms resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAllMySmsIdPatch"></a>
# **apiTransportAllMySmsIdPatch**
> TransportAllMySmsGet apiTransportAllMySmsIdPatch(id, transportAllMySmsPatch)

Updates the TransportAllMySms resource.

Updates the TransportAllMySms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAllMySmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAllMySmsApi apiInstance = new TransportAllMySmsApi(defaultClient);
    String id = "id_example"; // String | TransportAllMySms identifier
    TransportAllMySmsPatch transportAllMySmsPatch = new TransportAllMySmsPatch(); // TransportAllMySmsPatch | The updated TransportAllMySms resource
    try {
      TransportAllMySmsGet result = apiInstance.apiTransportAllMySmsIdPatch(id, transportAllMySmsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAllMySmsApi#apiTransportAllMySmsIdPatch");
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
| **id** | **String**| TransportAllMySms identifier | |
| **transportAllMySmsPatch** | [**TransportAllMySmsPatch**](TransportAllMySmsPatch.md)| The updated TransportAllMySms resource | |

### Return type

[**TransportAllMySmsGet**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAllMySms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAllMySmsIdPut"></a>
# **apiTransportAllMySmsIdPut**
> TransportAllMySmsGet apiTransportAllMySmsIdPut(id, transportAllMySmsPut)

Replaces the TransportAllMySms resource.

Replaces the TransportAllMySms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAllMySmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAllMySmsApi apiInstance = new TransportAllMySmsApi(defaultClient);
    String id = "id_example"; // String | TransportAllMySms identifier
    TransportAllMySmsPut transportAllMySmsPut = new TransportAllMySmsPut(); // TransportAllMySmsPut | The updated TransportAllMySms resource
    try {
      TransportAllMySmsGet result = apiInstance.apiTransportAllMySmsIdPut(id, transportAllMySmsPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAllMySmsApi#apiTransportAllMySmsIdPut");
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
| **id** | **String**| TransportAllMySms identifier | |
| **transportAllMySmsPut** | [**TransportAllMySmsPut**](TransportAllMySmsPut.md)| The updated TransportAllMySms resource | |

### Return type

[**TransportAllMySmsGet**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAllMySms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAllMySmsPost"></a>
# **apiTransportAllMySmsPost**
> TransportAllMySmsGet apiTransportAllMySmsPost(transportAllMySmsPost)

Creates a TransportAllMySms resource.

Creates a TransportAllMySms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAllMySmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAllMySmsApi apiInstance = new TransportAllMySmsApi(defaultClient);
    TransportAllMySmsPost transportAllMySmsPost = new TransportAllMySmsPost(); // TransportAllMySmsPost | The new TransportAllMySms resource
    try {
      TransportAllMySmsGet result = apiInstance.apiTransportAllMySmsPost(transportAllMySmsPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAllMySmsApi#apiTransportAllMySmsPost");
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
| **transportAllMySmsPost** | [**TransportAllMySmsPost**](TransportAllMySmsPost.md)| The new TransportAllMySms resource | |

### Return type

[**TransportAllMySmsGet**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportAllMySms resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

