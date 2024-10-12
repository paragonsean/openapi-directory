# TransportTermiiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportTermiiGetCollection**](TransportTermiiApi.md#apiTransportTermiiGetCollection) | **GET** /api/transport-termii | Retrieves the collection of TransportTermii resources. |
| [**apiTransportTermiiIdDelete**](TransportTermiiApi.md#apiTransportTermiiIdDelete) | **DELETE** /api/transport-termii/{id} | Removes the TransportTermii resource. |
| [**apiTransportTermiiIdGet**](TransportTermiiApi.md#apiTransportTermiiIdGet) | **GET** /api/transport-termii/{id} | Retrieves a TransportTermii resource. |
| [**apiTransportTermiiIdPatch**](TransportTermiiApi.md#apiTransportTermiiIdPatch) | **PATCH** /api/transport-termii/{id} | Updates the TransportTermii resource. |
| [**apiTransportTermiiIdPut**](TransportTermiiApi.md#apiTransportTermiiIdPut) | **PUT** /api/transport-termii/{id} | Replaces the TransportTermii resource. |
| [**apiTransportTermiiPost**](TransportTermiiApi.md#apiTransportTermiiPost) | **POST** /api/transport-termii | Creates a TransportTermii resource. |


<a id="apiTransportTermiiGetCollection"></a>
# **apiTransportTermiiGetCollection**
> List&lt;TransportTermiiGet&gt; apiTransportTermiiGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportTermii resources.

Retrieves the collection of TransportTermii resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTermiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTermiiApi apiInstance = new TransportTermiiApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportTermiiGet> result = apiInstance.apiTransportTermiiGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTermiiApi#apiTransportTermiiGetCollection");
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

[**List&lt;TransportTermiiGet&gt;**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTermii collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTermiiIdDelete"></a>
# **apiTransportTermiiIdDelete**
> apiTransportTermiiIdDelete(id)

Removes the TransportTermii resource.

Removes the TransportTermii resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTermiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTermiiApi apiInstance = new TransportTermiiApi(defaultClient);
    String id = "id_example"; // String | TransportTermii identifier
    try {
      apiInstance.apiTransportTermiiIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTermiiApi#apiTransportTermiiIdDelete");
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
| **id** | **String**| TransportTermii identifier | |

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
| **204** | TransportTermii resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTermiiIdGet"></a>
# **apiTransportTermiiIdGet**
> TransportTermiiGet apiTransportTermiiIdGet(id)

Retrieves a TransportTermii resource.

Retrieves a TransportTermii resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTermiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTermiiApi apiInstance = new TransportTermiiApi(defaultClient);
    String id = "id_example"; // String | TransportTermii identifier
    try {
      TransportTermiiGet result = apiInstance.apiTransportTermiiIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTermiiApi#apiTransportTermiiIdGet");
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
| **id** | **String**| TransportTermii identifier | |

### Return type

[**TransportTermiiGet**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTermii resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTermiiIdPatch"></a>
# **apiTransportTermiiIdPatch**
> TransportTermiiGet apiTransportTermiiIdPatch(id, transportTermiiPatch)

Updates the TransportTermii resource.

Updates the TransportTermii resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTermiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTermiiApi apiInstance = new TransportTermiiApi(defaultClient);
    String id = "id_example"; // String | TransportTermii identifier
    TransportTermiiPatch transportTermiiPatch = new TransportTermiiPatch(); // TransportTermiiPatch | The updated TransportTermii resource
    try {
      TransportTermiiGet result = apiInstance.apiTransportTermiiIdPatch(id, transportTermiiPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTermiiApi#apiTransportTermiiIdPatch");
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
| **id** | **String**| TransportTermii identifier | |
| **transportTermiiPatch** | [**TransportTermiiPatch**](TransportTermiiPatch.md)| The updated TransportTermii resource | |

### Return type

[**TransportTermiiGet**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTermii resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTermiiIdPut"></a>
# **apiTransportTermiiIdPut**
> TransportTermiiGet apiTransportTermiiIdPut(id, transportTermiiPut)

Replaces the TransportTermii resource.

Replaces the TransportTermii resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTermiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTermiiApi apiInstance = new TransportTermiiApi(defaultClient);
    String id = "id_example"; // String | TransportTermii identifier
    TransportTermiiPut transportTermiiPut = new TransportTermiiPut(); // TransportTermiiPut | The updated TransportTermii resource
    try {
      TransportTermiiGet result = apiInstance.apiTransportTermiiIdPut(id, transportTermiiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTermiiApi#apiTransportTermiiIdPut");
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
| **id** | **String**| TransportTermii identifier | |
| **transportTermiiPut** | [**TransportTermiiPut**](TransportTermiiPut.md)| The updated TransportTermii resource | |

### Return type

[**TransportTermiiGet**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTermii resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTermiiPost"></a>
# **apiTransportTermiiPost**
> TransportTermiiGet apiTransportTermiiPost(transportTermiiPost)

Creates a TransportTermii resource.

Creates a TransportTermii resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTermiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTermiiApi apiInstance = new TransportTermiiApi(defaultClient);
    TransportTermiiPost transportTermiiPost = new TransportTermiiPost(); // TransportTermiiPost | The new TransportTermii resource
    try {
      TransportTermiiGet result = apiInstance.apiTransportTermiiPost(transportTermiiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTermiiApi#apiTransportTermiiPost");
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
| **transportTermiiPost** | [**TransportTermiiPost**](TransportTermiiPost.md)| The new TransportTermii resource | |

### Return type

[**TransportTermiiGet**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportTermii resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

