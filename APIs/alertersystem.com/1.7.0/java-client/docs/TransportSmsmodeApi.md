# TransportSmsmodeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSmsmodeGetCollection**](TransportSmsmodeApi.md#apiTransportSmsmodeGetCollection) | **GET** /api/transport-smsmode | Retrieves the collection of TransportSmsmode resources. |
| [**apiTransportSmsmodeIdDelete**](TransportSmsmodeApi.md#apiTransportSmsmodeIdDelete) | **DELETE** /api/transport-smsmode/{id} | Removes the TransportSmsmode resource. |
| [**apiTransportSmsmodeIdGet**](TransportSmsmodeApi.md#apiTransportSmsmodeIdGet) | **GET** /api/transport-smsmode/{id} | Retrieves a TransportSmsmode resource. |
| [**apiTransportSmsmodeIdPatch**](TransportSmsmodeApi.md#apiTransportSmsmodeIdPatch) | **PATCH** /api/transport-smsmode/{id} | Updates the TransportSmsmode resource. |
| [**apiTransportSmsmodeIdPut**](TransportSmsmodeApi.md#apiTransportSmsmodeIdPut) | **PUT** /api/transport-smsmode/{id} | Replaces the TransportSmsmode resource. |
| [**apiTransportSmsmodePost**](TransportSmsmodeApi.md#apiTransportSmsmodePost) | **POST** /api/transport-smsmode | Creates a TransportSmsmode resource. |


<a id="apiTransportSmsmodeGetCollection"></a>
# **apiTransportSmsmodeGetCollection**
> List&lt;TransportSmsmodeGet&gt; apiTransportSmsmodeGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSmsmode resources.

Retrieves the collection of TransportSmsmode resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsmodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsmodeApi apiInstance = new TransportSmsmodeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSmsmodeGet> result = apiInstance.apiTransportSmsmodeGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsmodeApi#apiTransportSmsmodeGetCollection");
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

[**List&lt;TransportSmsmodeGet&gt;**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsmode collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsmodeIdDelete"></a>
# **apiTransportSmsmodeIdDelete**
> apiTransportSmsmodeIdDelete(id)

Removes the TransportSmsmode resource.

Removes the TransportSmsmode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsmodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsmodeApi apiInstance = new TransportSmsmodeApi(defaultClient);
    String id = "id_example"; // String | TransportSmsmode identifier
    try {
      apiInstance.apiTransportSmsmodeIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsmodeApi#apiTransportSmsmodeIdDelete");
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
| **id** | **String**| TransportSmsmode identifier | |

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
| **204** | TransportSmsmode resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsmodeIdGet"></a>
# **apiTransportSmsmodeIdGet**
> TransportSmsmodeGet apiTransportSmsmodeIdGet(id)

Retrieves a TransportSmsmode resource.

Retrieves a TransportSmsmode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsmodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsmodeApi apiInstance = new TransportSmsmodeApi(defaultClient);
    String id = "id_example"; // String | TransportSmsmode identifier
    try {
      TransportSmsmodeGet result = apiInstance.apiTransportSmsmodeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsmodeApi#apiTransportSmsmodeIdGet");
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
| **id** | **String**| TransportSmsmode identifier | |

### Return type

[**TransportSmsmodeGet**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsmode resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsmodeIdPatch"></a>
# **apiTransportSmsmodeIdPatch**
> TransportSmsmodeGet apiTransportSmsmodeIdPatch(id, transportSmsmodePatch)

Updates the TransportSmsmode resource.

Updates the TransportSmsmode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsmodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsmodeApi apiInstance = new TransportSmsmodeApi(defaultClient);
    String id = "id_example"; // String | TransportSmsmode identifier
    TransportSmsmodePatch transportSmsmodePatch = new TransportSmsmodePatch(); // TransportSmsmodePatch | The updated TransportSmsmode resource
    try {
      TransportSmsmodeGet result = apiInstance.apiTransportSmsmodeIdPatch(id, transportSmsmodePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsmodeApi#apiTransportSmsmodeIdPatch");
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
| **id** | **String**| TransportSmsmode identifier | |
| **transportSmsmodePatch** | [**TransportSmsmodePatch**](TransportSmsmodePatch.md)| The updated TransportSmsmode resource | |

### Return type

[**TransportSmsmodeGet**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsmode resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsmodeIdPut"></a>
# **apiTransportSmsmodeIdPut**
> TransportSmsmodeGet apiTransportSmsmodeIdPut(id, transportSmsmodePut)

Replaces the TransportSmsmode resource.

Replaces the TransportSmsmode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsmodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsmodeApi apiInstance = new TransportSmsmodeApi(defaultClient);
    String id = "id_example"; // String | TransportSmsmode identifier
    TransportSmsmodePut transportSmsmodePut = new TransportSmsmodePut(); // TransportSmsmodePut | The updated TransportSmsmode resource
    try {
      TransportSmsmodeGet result = apiInstance.apiTransportSmsmodeIdPut(id, transportSmsmodePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsmodeApi#apiTransportSmsmodeIdPut");
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
| **id** | **String**| TransportSmsmode identifier | |
| **transportSmsmodePut** | [**TransportSmsmodePut**](TransportSmsmodePut.md)| The updated TransportSmsmode resource | |

### Return type

[**TransportSmsmodeGet**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsmode resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsmodePost"></a>
# **apiTransportSmsmodePost**
> TransportSmsmodeGet apiTransportSmsmodePost(transportSmsmodePost)

Creates a TransportSmsmode resource.

Creates a TransportSmsmode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsmodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsmodeApi apiInstance = new TransportSmsmodeApi(defaultClient);
    TransportSmsmodePost transportSmsmodePost = new TransportSmsmodePost(); // TransportSmsmodePost | The new TransportSmsmode resource
    try {
      TransportSmsmodeGet result = apiInstance.apiTransportSmsmodePost(transportSmsmodePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsmodeApi#apiTransportSmsmodePost");
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
| **transportSmsmodePost** | [**TransportSmsmodePost**](TransportSmsmodePost.md)| The new TransportSmsmode resource | |

### Return type

[**TransportSmsmodeGet**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSmsmode resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

