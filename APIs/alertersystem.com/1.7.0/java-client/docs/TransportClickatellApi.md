# TransportClickatellApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportClickatellGetCollection**](TransportClickatellApi.md#apiTransportClickatellGetCollection) | **GET** /api/transport-clickatell | Retrieves the collection of TransportClickatell resources. |
| [**apiTransportClickatellIdDelete**](TransportClickatellApi.md#apiTransportClickatellIdDelete) | **DELETE** /api/transport-clickatell/{id} | Removes the TransportClickatell resource. |
| [**apiTransportClickatellIdGet**](TransportClickatellApi.md#apiTransportClickatellIdGet) | **GET** /api/transport-clickatell/{id} | Retrieves a TransportClickatell resource. |
| [**apiTransportClickatellIdPatch**](TransportClickatellApi.md#apiTransportClickatellIdPatch) | **PATCH** /api/transport-clickatell/{id} | Updates the TransportClickatell resource. |
| [**apiTransportClickatellIdPut**](TransportClickatellApi.md#apiTransportClickatellIdPut) | **PUT** /api/transport-clickatell/{id} | Replaces the TransportClickatell resource. |
| [**apiTransportClickatellPost**](TransportClickatellApi.md#apiTransportClickatellPost) | **POST** /api/transport-clickatell | Creates a TransportClickatell resource. |


<a id="apiTransportClickatellGetCollection"></a>
# **apiTransportClickatellGetCollection**
> List&lt;TransportClickatellGet&gt; apiTransportClickatellGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportClickatell resources.

Retrieves the collection of TransportClickatell resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickatellApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickatellApi apiInstance = new TransportClickatellApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportClickatellGet> result = apiInstance.apiTransportClickatellGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickatellApi#apiTransportClickatellGetCollection");
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

[**List&lt;TransportClickatellGet&gt;**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportClickatell collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickatellIdDelete"></a>
# **apiTransportClickatellIdDelete**
> apiTransportClickatellIdDelete(id)

Removes the TransportClickatell resource.

Removes the TransportClickatell resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickatellApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickatellApi apiInstance = new TransportClickatellApi(defaultClient);
    String id = "id_example"; // String | TransportClickatell identifier
    try {
      apiInstance.apiTransportClickatellIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickatellApi#apiTransportClickatellIdDelete");
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
| **id** | **String**| TransportClickatell identifier | |

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
| **204** | TransportClickatell resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickatellIdGet"></a>
# **apiTransportClickatellIdGet**
> TransportClickatellGet apiTransportClickatellIdGet(id)

Retrieves a TransportClickatell resource.

Retrieves a TransportClickatell resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickatellApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickatellApi apiInstance = new TransportClickatellApi(defaultClient);
    String id = "id_example"; // String | TransportClickatell identifier
    try {
      TransportClickatellGet result = apiInstance.apiTransportClickatellIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickatellApi#apiTransportClickatellIdGet");
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
| **id** | **String**| TransportClickatell identifier | |

### Return type

[**TransportClickatellGet**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportClickatell resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickatellIdPatch"></a>
# **apiTransportClickatellIdPatch**
> TransportClickatellGet apiTransportClickatellIdPatch(id, transportClickatellPatch)

Updates the TransportClickatell resource.

Updates the TransportClickatell resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickatellApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickatellApi apiInstance = new TransportClickatellApi(defaultClient);
    String id = "id_example"; // String | TransportClickatell identifier
    TransportClickatellPatch transportClickatellPatch = new TransportClickatellPatch(); // TransportClickatellPatch | The updated TransportClickatell resource
    try {
      TransportClickatellGet result = apiInstance.apiTransportClickatellIdPatch(id, transportClickatellPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickatellApi#apiTransportClickatellIdPatch");
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
| **id** | **String**| TransportClickatell identifier | |
| **transportClickatellPatch** | [**TransportClickatellPatch**](TransportClickatellPatch.md)| The updated TransportClickatell resource | |

### Return type

[**TransportClickatellGet**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportClickatell resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickatellIdPut"></a>
# **apiTransportClickatellIdPut**
> TransportClickatellGet apiTransportClickatellIdPut(id, transportClickatellPut)

Replaces the TransportClickatell resource.

Replaces the TransportClickatell resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickatellApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickatellApi apiInstance = new TransportClickatellApi(defaultClient);
    String id = "id_example"; // String | TransportClickatell identifier
    TransportClickatellPut transportClickatellPut = new TransportClickatellPut(); // TransportClickatellPut | The updated TransportClickatell resource
    try {
      TransportClickatellGet result = apiInstance.apiTransportClickatellIdPut(id, transportClickatellPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickatellApi#apiTransportClickatellIdPut");
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
| **id** | **String**| TransportClickatell identifier | |
| **transportClickatellPut** | [**TransportClickatellPut**](TransportClickatellPut.md)| The updated TransportClickatell resource | |

### Return type

[**TransportClickatellGet**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportClickatell resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportClickatellPost"></a>
# **apiTransportClickatellPost**
> TransportClickatellGet apiTransportClickatellPost(transportClickatellPost)

Creates a TransportClickatell resource.

Creates a TransportClickatell resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportClickatellApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportClickatellApi apiInstance = new TransportClickatellApi(defaultClient);
    TransportClickatellPost transportClickatellPost = new TransportClickatellPost(); // TransportClickatellPost | The new TransportClickatell resource
    try {
      TransportClickatellGet result = apiInstance.apiTransportClickatellPost(transportClickatellPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportClickatellApi#apiTransportClickatellPost");
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
| **transportClickatellPost** | [**TransportClickatellPost**](TransportClickatellPost.md)| The new TransportClickatell resource | |

### Return type

[**TransportClickatellGet**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportClickatell resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

