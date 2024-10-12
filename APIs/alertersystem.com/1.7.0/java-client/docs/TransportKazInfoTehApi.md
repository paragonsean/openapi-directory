# TransportKazInfoTehApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportKazInfoTehGetCollection**](TransportKazInfoTehApi.md#apiTransportKazInfoTehGetCollection) | **GET** /api/transport-kaz-info-teh | Retrieves the collection of TransportKazInfoTeh resources. |
| [**apiTransportKazInfoTehIdDelete**](TransportKazInfoTehApi.md#apiTransportKazInfoTehIdDelete) | **DELETE** /api/transport-kaz-info-teh/{id} | Removes the TransportKazInfoTeh resource. |
| [**apiTransportKazInfoTehIdGet**](TransportKazInfoTehApi.md#apiTransportKazInfoTehIdGet) | **GET** /api/transport-kaz-info-teh/{id} | Retrieves a TransportKazInfoTeh resource. |
| [**apiTransportKazInfoTehIdPatch**](TransportKazInfoTehApi.md#apiTransportKazInfoTehIdPatch) | **PATCH** /api/transport-kaz-info-teh/{id} | Updates the TransportKazInfoTeh resource. |
| [**apiTransportKazInfoTehIdPut**](TransportKazInfoTehApi.md#apiTransportKazInfoTehIdPut) | **PUT** /api/transport-kaz-info-teh/{id} | Replaces the TransportKazInfoTeh resource. |
| [**apiTransportKazInfoTehPost**](TransportKazInfoTehApi.md#apiTransportKazInfoTehPost) | **POST** /api/transport-kaz-info-teh | Creates a TransportKazInfoTeh resource. |


<a id="apiTransportKazInfoTehGetCollection"></a>
# **apiTransportKazInfoTehGetCollection**
> List&lt;TransportKazInfoTehGet&gt; apiTransportKazInfoTehGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportKazInfoTeh resources.

Retrieves the collection of TransportKazInfoTeh resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportKazInfoTehApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportKazInfoTehApi apiInstance = new TransportKazInfoTehApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportKazInfoTehGet> result = apiInstance.apiTransportKazInfoTehGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportKazInfoTehApi#apiTransportKazInfoTehGetCollection");
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

[**List&lt;TransportKazInfoTehGet&gt;**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportKazInfoTeh collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportKazInfoTehIdDelete"></a>
# **apiTransportKazInfoTehIdDelete**
> apiTransportKazInfoTehIdDelete(id)

Removes the TransportKazInfoTeh resource.

Removes the TransportKazInfoTeh resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportKazInfoTehApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportKazInfoTehApi apiInstance = new TransportKazInfoTehApi(defaultClient);
    String id = "id_example"; // String | TransportKazInfoTeh identifier
    try {
      apiInstance.apiTransportKazInfoTehIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportKazInfoTehApi#apiTransportKazInfoTehIdDelete");
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
| **id** | **String**| TransportKazInfoTeh identifier | |

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
| **204** | TransportKazInfoTeh resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportKazInfoTehIdGet"></a>
# **apiTransportKazInfoTehIdGet**
> TransportKazInfoTehGet apiTransportKazInfoTehIdGet(id)

Retrieves a TransportKazInfoTeh resource.

Retrieves a TransportKazInfoTeh resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportKazInfoTehApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportKazInfoTehApi apiInstance = new TransportKazInfoTehApi(defaultClient);
    String id = "id_example"; // String | TransportKazInfoTeh identifier
    try {
      TransportKazInfoTehGet result = apiInstance.apiTransportKazInfoTehIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportKazInfoTehApi#apiTransportKazInfoTehIdGet");
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
| **id** | **String**| TransportKazInfoTeh identifier | |

### Return type

[**TransportKazInfoTehGet**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportKazInfoTeh resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportKazInfoTehIdPatch"></a>
# **apiTransportKazInfoTehIdPatch**
> TransportKazInfoTehGet apiTransportKazInfoTehIdPatch(id, transportKazInfoTehPatch)

Updates the TransportKazInfoTeh resource.

Updates the TransportKazInfoTeh resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportKazInfoTehApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportKazInfoTehApi apiInstance = new TransportKazInfoTehApi(defaultClient);
    String id = "id_example"; // String | TransportKazInfoTeh identifier
    TransportKazInfoTehPatch transportKazInfoTehPatch = new TransportKazInfoTehPatch(); // TransportKazInfoTehPatch | The updated TransportKazInfoTeh resource
    try {
      TransportKazInfoTehGet result = apiInstance.apiTransportKazInfoTehIdPatch(id, transportKazInfoTehPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportKazInfoTehApi#apiTransportKazInfoTehIdPatch");
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
| **id** | **String**| TransportKazInfoTeh identifier | |
| **transportKazInfoTehPatch** | [**TransportKazInfoTehPatch**](TransportKazInfoTehPatch.md)| The updated TransportKazInfoTeh resource | |

### Return type

[**TransportKazInfoTehGet**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportKazInfoTeh resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportKazInfoTehIdPut"></a>
# **apiTransportKazInfoTehIdPut**
> TransportKazInfoTehGet apiTransportKazInfoTehIdPut(id, transportKazInfoTehPut)

Replaces the TransportKazInfoTeh resource.

Replaces the TransportKazInfoTeh resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportKazInfoTehApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportKazInfoTehApi apiInstance = new TransportKazInfoTehApi(defaultClient);
    String id = "id_example"; // String | TransportKazInfoTeh identifier
    TransportKazInfoTehPut transportKazInfoTehPut = new TransportKazInfoTehPut(); // TransportKazInfoTehPut | The updated TransportKazInfoTeh resource
    try {
      TransportKazInfoTehGet result = apiInstance.apiTransportKazInfoTehIdPut(id, transportKazInfoTehPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportKazInfoTehApi#apiTransportKazInfoTehIdPut");
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
| **id** | **String**| TransportKazInfoTeh identifier | |
| **transportKazInfoTehPut** | [**TransportKazInfoTehPut**](TransportKazInfoTehPut.md)| The updated TransportKazInfoTeh resource | |

### Return type

[**TransportKazInfoTehGet**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportKazInfoTeh resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportKazInfoTehPost"></a>
# **apiTransportKazInfoTehPost**
> TransportKazInfoTehGet apiTransportKazInfoTehPost(transportKazInfoTehPost)

Creates a TransportKazInfoTeh resource.

Creates a TransportKazInfoTeh resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportKazInfoTehApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportKazInfoTehApi apiInstance = new TransportKazInfoTehApi(defaultClient);
    TransportKazInfoTehPost transportKazInfoTehPost = new TransportKazInfoTehPost(); // TransportKazInfoTehPost | The new TransportKazInfoTeh resource
    try {
      TransportKazInfoTehGet result = apiInstance.apiTransportKazInfoTehPost(transportKazInfoTehPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportKazInfoTehApi#apiTransportKazInfoTehPost");
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
| **transportKazInfoTehPost** | [**TransportKazInfoTehPost**](TransportKazInfoTehPost.md)| The new TransportKazInfoTeh resource | |

### Return type

[**TransportKazInfoTehGet**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportKazInfoTeh resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

