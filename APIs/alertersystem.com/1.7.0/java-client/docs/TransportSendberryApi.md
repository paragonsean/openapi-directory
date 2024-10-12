# TransportSendberryApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSendberryGetCollection**](TransportSendberryApi.md#apiTransportSendberryGetCollection) | **GET** /api/transport-sendberry | Retrieves the collection of TransportSendberry resources. |
| [**apiTransportSendberryIdDelete**](TransportSendberryApi.md#apiTransportSendberryIdDelete) | **DELETE** /api/transport-sendberry/{id} | Removes the TransportSendberry resource. |
| [**apiTransportSendberryIdGet**](TransportSendberryApi.md#apiTransportSendberryIdGet) | **GET** /api/transport-sendberry/{id} | Retrieves a TransportSendberry resource. |
| [**apiTransportSendberryIdPatch**](TransportSendberryApi.md#apiTransportSendberryIdPatch) | **PATCH** /api/transport-sendberry/{id} | Updates the TransportSendberry resource. |
| [**apiTransportSendberryIdPut**](TransportSendberryApi.md#apiTransportSendberryIdPut) | **PUT** /api/transport-sendberry/{id} | Replaces the TransportSendberry resource. |
| [**apiTransportSendberryPost**](TransportSendberryApi.md#apiTransportSendberryPost) | **POST** /api/transport-sendberry | Creates a TransportSendberry resource. |


<a id="apiTransportSendberryGetCollection"></a>
# **apiTransportSendberryGetCollection**
> List&lt;TransportSendberryGet&gt; apiTransportSendberryGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSendberry resources.

Retrieves the collection of TransportSendberry resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendberryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendberryApi apiInstance = new TransportSendberryApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSendberryGet> result = apiInstance.apiTransportSendberryGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendberryApi#apiTransportSendberryGetCollection");
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

[**List&lt;TransportSendberryGet&gt;**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSendberry collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendberryIdDelete"></a>
# **apiTransportSendberryIdDelete**
> apiTransportSendberryIdDelete(id)

Removes the TransportSendberry resource.

Removes the TransportSendberry resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendberryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendberryApi apiInstance = new TransportSendberryApi(defaultClient);
    String id = "id_example"; // String | TransportSendberry identifier
    try {
      apiInstance.apiTransportSendberryIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendberryApi#apiTransportSendberryIdDelete");
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
| **id** | **String**| TransportSendberry identifier | |

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
| **204** | TransportSendberry resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendberryIdGet"></a>
# **apiTransportSendberryIdGet**
> TransportSendberryGet apiTransportSendberryIdGet(id)

Retrieves a TransportSendberry resource.

Retrieves a TransportSendberry resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendberryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendberryApi apiInstance = new TransportSendberryApi(defaultClient);
    String id = "id_example"; // String | TransportSendberry identifier
    try {
      TransportSendberryGet result = apiInstance.apiTransportSendberryIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendberryApi#apiTransportSendberryIdGet");
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
| **id** | **String**| TransportSendberry identifier | |

### Return type

[**TransportSendberryGet**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSendberry resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendberryIdPatch"></a>
# **apiTransportSendberryIdPatch**
> TransportSendberryGet apiTransportSendberryIdPatch(id, transportSendberryPatch)

Updates the TransportSendberry resource.

Updates the TransportSendberry resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendberryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendberryApi apiInstance = new TransportSendberryApi(defaultClient);
    String id = "id_example"; // String | TransportSendberry identifier
    TransportSendberryPatch transportSendberryPatch = new TransportSendberryPatch(); // TransportSendberryPatch | The updated TransportSendberry resource
    try {
      TransportSendberryGet result = apiInstance.apiTransportSendberryIdPatch(id, transportSendberryPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendberryApi#apiTransportSendberryIdPatch");
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
| **id** | **String**| TransportSendberry identifier | |
| **transportSendberryPatch** | [**TransportSendberryPatch**](TransportSendberryPatch.md)| The updated TransportSendberry resource | |

### Return type

[**TransportSendberryGet**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSendberry resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendberryIdPut"></a>
# **apiTransportSendberryIdPut**
> TransportSendberryGet apiTransportSendberryIdPut(id, transportSendberryPut)

Replaces the TransportSendberry resource.

Replaces the TransportSendberry resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendberryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendberryApi apiInstance = new TransportSendberryApi(defaultClient);
    String id = "id_example"; // String | TransportSendberry identifier
    TransportSendberryPut transportSendberryPut = new TransportSendberryPut(); // TransportSendberryPut | The updated TransportSendberry resource
    try {
      TransportSendberryGet result = apiInstance.apiTransportSendberryIdPut(id, transportSendberryPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendberryApi#apiTransportSendberryIdPut");
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
| **id** | **String**| TransportSendberry identifier | |
| **transportSendberryPut** | [**TransportSendberryPut**](TransportSendberryPut.md)| The updated TransportSendberry resource | |

### Return type

[**TransportSendberryGet**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSendberry resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendberryPost"></a>
# **apiTransportSendberryPost**
> TransportSendberryGet apiTransportSendberryPost(transportSendberryPost)

Creates a TransportSendberry resource.

Creates a TransportSendberry resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendberryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendberryApi apiInstance = new TransportSendberryApi(defaultClient);
    TransportSendberryPost transportSendberryPost = new TransportSendberryPost(); // TransportSendberryPost | The new TransportSendberry resource
    try {
      TransportSendberryGet result = apiInstance.apiTransportSendberryPost(transportSendberryPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendberryApi#apiTransportSendberryPost");
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
| **transportSendberryPost** | [**TransportSendberryPost**](TransportSendberryPost.md)| The new TransportSendberry resource | |

### Return type

[**TransportSendberryGet**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSendberry resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

