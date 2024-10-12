# TransportClickSendApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportClickSendGetCollection**](TransportClickSendApi.md#apiTransportClickSendGetCollection) | **GET** /api/transport-click-send | Retrieves the collection of TransportClickSend resources. |
| [**apiTransportClickSendIdDelete**](TransportClickSendApi.md#apiTransportClickSendIdDelete) | **DELETE** /api/transport-click-send/{id} | Removes the TransportClickSend resource. |
| [**apiTransportClickSendIdGet**](TransportClickSendApi.md#apiTransportClickSendIdGet) | **GET** /api/transport-click-send/{id} | Retrieves a TransportClickSend resource. |
| [**apiTransportClickSendIdPatch**](TransportClickSendApi.md#apiTransportClickSendIdPatch) | **PATCH** /api/transport-click-send/{id} | Updates the TransportClickSend resource. |
| [**apiTransportClickSendIdPut**](TransportClickSendApi.md#apiTransportClickSendIdPut) | **PUT** /api/transport-click-send/{id} | Replaces the TransportClickSend resource. |
| [**apiTransportClickSendPost**](TransportClickSendApi.md#apiTransportClickSendPost) | **POST** /api/transport-click-send | Creates a TransportClickSend resource. |


<a id="apiTransportClickSendGetCollection"></a>
# **apiTransportClickSendGetCollection**
> List&lt;TransportClickSendGet&gt; apiTransportClickSendGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportClickSend resources.

Retrieves the collection of TransportClickSend resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickSendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickSendApi apiInstance = new TransportClickSendApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportClickSendGet> result = apiInstance.apiTransportClickSendGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickSendApi#apiTransportClickSendGetCollection");
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

[**List&lt;TransportClickSendGet&gt;**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportClickSend collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickSendIdDelete"></a>
# **apiTransportClickSendIdDelete**
> apiTransportClickSendIdDelete(id)

Removes the TransportClickSend resource.

Removes the TransportClickSend resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickSendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickSendApi apiInstance = new TransportClickSendApi(defaultClient);
    String id = "id_example"; // String | TransportClickSend identifier
    try {
      apiInstance.apiTransportClickSendIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickSendApi#apiTransportClickSendIdDelete");
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
| **id** | **String**| TransportClickSend identifier | |

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
| **204** | TransportClickSend resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickSendIdGet"></a>
# **apiTransportClickSendIdGet**
> TransportClickSendGet apiTransportClickSendIdGet(id)

Retrieves a TransportClickSend resource.

Retrieves a TransportClickSend resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickSendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickSendApi apiInstance = new TransportClickSendApi(defaultClient);
    String id = "id_example"; // String | TransportClickSend identifier
    try {
      TransportClickSendGet result = apiInstance.apiTransportClickSendIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickSendApi#apiTransportClickSendIdGet");
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
| **id** | **String**| TransportClickSend identifier | |

### Return type

[**TransportClickSendGet**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportClickSend resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickSendIdPatch"></a>
# **apiTransportClickSendIdPatch**
> TransportClickSendGet apiTransportClickSendIdPatch(id, transportClickSendPatch)

Updates the TransportClickSend resource.

Updates the TransportClickSend resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickSendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickSendApi apiInstance = new TransportClickSendApi(defaultClient);
    String id = "id_example"; // String | TransportClickSend identifier
    TransportClickSendPatch transportClickSendPatch = new TransportClickSendPatch(); // TransportClickSendPatch | The updated TransportClickSend resource
    try {
      TransportClickSendGet result = apiInstance.apiTransportClickSendIdPatch(id, transportClickSendPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickSendApi#apiTransportClickSendIdPatch");
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
| **id** | **String**| TransportClickSend identifier | |
| **transportClickSendPatch** | [**TransportClickSendPatch**](TransportClickSendPatch.md)| The updated TransportClickSend resource | |

### Return type

[**TransportClickSendGet**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportClickSend resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickSendIdPut"></a>
# **apiTransportClickSendIdPut**
> TransportClickSendGet apiTransportClickSendIdPut(id, transportClickSendPut)

Replaces the TransportClickSend resource.

Replaces the TransportClickSend resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickSendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickSendApi apiInstance = new TransportClickSendApi(defaultClient);
    String id = "id_example"; // String | TransportClickSend identifier
    TransportClickSendPut transportClickSendPut = new TransportClickSendPut(); // TransportClickSendPut | The updated TransportClickSend resource
    try {
      TransportClickSendGet result = apiInstance.apiTransportClickSendIdPut(id, transportClickSendPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickSendApi#apiTransportClickSendIdPut");
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
| **id** | **String**| TransportClickSend identifier | |
| **transportClickSendPut** | [**TransportClickSendPut**](TransportClickSendPut.md)| The updated TransportClickSend resource | |

### Return type

[**TransportClickSendGet**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportClickSend resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickSendPost"></a>
# **apiTransportClickSendPost**
> TransportClickSendGet apiTransportClickSendPost(transportClickSendPost)

Creates a TransportClickSend resource.

Creates a TransportClickSend resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickSendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickSendApi apiInstance = new TransportClickSendApi(defaultClient);
    TransportClickSendPost transportClickSendPost = new TransportClickSendPost(); // TransportClickSendPost | The new TransportClickSend resource
    try {
      TransportClickSendGet result = apiInstance.apiTransportClickSendPost(transportClickSendPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickSendApi#apiTransportClickSendPost");
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
| **transportClickSendPost** | [**TransportClickSendPost**](TransportClickSendPost.md)| The new TransportClickSend resource | |

### Return type

[**TransportClickSendGet**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportClickSend resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

