# TransportSendinblueApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSendinblueGetCollection**](TransportSendinblueApi.md#apiTransportSendinblueGetCollection) | **GET** /api/transport-sendinblue | Retrieves the collection of TransportSendinblue resources. |
| [**apiTransportSendinblueIdDelete**](TransportSendinblueApi.md#apiTransportSendinblueIdDelete) | **DELETE** /api/transport-sendinblue/{id} | Removes the TransportSendinblue resource. |
| [**apiTransportSendinblueIdGet**](TransportSendinblueApi.md#apiTransportSendinblueIdGet) | **GET** /api/transport-sendinblue/{id} | Retrieves a TransportSendinblue resource. |
| [**apiTransportSendinblueIdPatch**](TransportSendinblueApi.md#apiTransportSendinblueIdPatch) | **PATCH** /api/transport-sendinblue/{id} | Updates the TransportSendinblue resource. |
| [**apiTransportSendinblueIdPut**](TransportSendinblueApi.md#apiTransportSendinblueIdPut) | **PUT** /api/transport-sendinblue/{id} | Replaces the TransportSendinblue resource. |
| [**apiTransportSendinbluePost**](TransportSendinblueApi.md#apiTransportSendinbluePost) | **POST** /api/transport-sendinblue | Creates a TransportSendinblue resource. |


<a id="apiTransportSendinblueGetCollection"></a>
# **apiTransportSendinblueGetCollection**
> List&lt;TransportSendinblueGet&gt; apiTransportSendinblueGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSendinblue resources.

Retrieves the collection of TransportSendinblue resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendinblueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendinblueApi apiInstance = new TransportSendinblueApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSendinblueGet> result = apiInstance.apiTransportSendinblueGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendinblueApi#apiTransportSendinblueGetCollection");
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

[**List&lt;TransportSendinblueGet&gt;**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSendinblue collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendinblueIdDelete"></a>
# **apiTransportSendinblueIdDelete**
> apiTransportSendinblueIdDelete(id)

Removes the TransportSendinblue resource.

Removes the TransportSendinblue resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendinblueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendinblueApi apiInstance = new TransportSendinblueApi(defaultClient);
    String id = "id_example"; // String | TransportSendinblue identifier
    try {
      apiInstance.apiTransportSendinblueIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendinblueApi#apiTransportSendinblueIdDelete");
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
| **id** | **String**| TransportSendinblue identifier | |

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
| **204** | TransportSendinblue resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendinblueIdGet"></a>
# **apiTransportSendinblueIdGet**
> TransportSendinblueGet apiTransportSendinblueIdGet(id)

Retrieves a TransportSendinblue resource.

Retrieves a TransportSendinblue resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendinblueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendinblueApi apiInstance = new TransportSendinblueApi(defaultClient);
    String id = "id_example"; // String | TransportSendinblue identifier
    try {
      TransportSendinblueGet result = apiInstance.apiTransportSendinblueIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendinblueApi#apiTransportSendinblueIdGet");
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
| **id** | **String**| TransportSendinblue identifier | |

### Return type

[**TransportSendinblueGet**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSendinblue resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendinblueIdPatch"></a>
# **apiTransportSendinblueIdPatch**
> TransportSendinblueGet apiTransportSendinblueIdPatch(id, transportSendinbluePatch)

Updates the TransportSendinblue resource.

Updates the TransportSendinblue resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendinblueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendinblueApi apiInstance = new TransportSendinblueApi(defaultClient);
    String id = "id_example"; // String | TransportSendinblue identifier
    TransportSendinbluePatch transportSendinbluePatch = new TransportSendinbluePatch(); // TransportSendinbluePatch | The updated TransportSendinblue resource
    try {
      TransportSendinblueGet result = apiInstance.apiTransportSendinblueIdPatch(id, transportSendinbluePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendinblueApi#apiTransportSendinblueIdPatch");
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
| **id** | **String**| TransportSendinblue identifier | |
| **transportSendinbluePatch** | [**TransportSendinbluePatch**](TransportSendinbluePatch.md)| The updated TransportSendinblue resource | |

### Return type

[**TransportSendinblueGet**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSendinblue resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendinblueIdPut"></a>
# **apiTransportSendinblueIdPut**
> TransportSendinblueGet apiTransportSendinblueIdPut(id, transportSendinbluePut)

Replaces the TransportSendinblue resource.

Replaces the TransportSendinblue resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendinblueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendinblueApi apiInstance = new TransportSendinblueApi(defaultClient);
    String id = "id_example"; // String | TransportSendinblue identifier
    TransportSendinbluePut transportSendinbluePut = new TransportSendinbluePut(); // TransportSendinbluePut | The updated TransportSendinblue resource
    try {
      TransportSendinblueGet result = apiInstance.apiTransportSendinblueIdPut(id, transportSendinbluePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendinblueApi#apiTransportSendinblueIdPut");
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
| **id** | **String**| TransportSendinblue identifier | |
| **transportSendinbluePut** | [**TransportSendinbluePut**](TransportSendinbluePut.md)| The updated TransportSendinblue resource | |

### Return type

[**TransportSendinblueGet**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSendinblue resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSendinbluePost"></a>
# **apiTransportSendinbluePost**
> TransportSendinblueGet apiTransportSendinbluePost(transportSendinbluePost)

Creates a TransportSendinblue resource.

Creates a TransportSendinblue resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSendinblueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSendinblueApi apiInstance = new TransportSendinblueApi(defaultClient);
    TransportSendinbluePost transportSendinbluePost = new TransportSendinbluePost(); // TransportSendinbluePost | The new TransportSendinblue resource
    try {
      TransportSendinblueGet result = apiInstance.apiTransportSendinbluePost(transportSendinbluePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSendinblueApi#apiTransportSendinbluePost");
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
| **transportSendinbluePost** | [**TransportSendinbluePost**](TransportSendinbluePost.md)| The new TransportSendinblue resource | |

### Return type

[**TransportSendinblueGet**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSendinblue resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

