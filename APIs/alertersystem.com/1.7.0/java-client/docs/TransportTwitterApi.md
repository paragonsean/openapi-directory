# TransportTwitterApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportTwitterGetCollection**](TransportTwitterApi.md#apiTransportTwitterGetCollection) | **GET** /api/transport-twitter | Retrieves the collection of TransportTwitter resources. |
| [**apiTransportTwitterIdDelete**](TransportTwitterApi.md#apiTransportTwitterIdDelete) | **DELETE** /api/transport-twitter/{id} | Removes the TransportTwitter resource. |
| [**apiTransportTwitterIdGet**](TransportTwitterApi.md#apiTransportTwitterIdGet) | **GET** /api/transport-twitter/{id} | Retrieves a TransportTwitter resource. |
| [**apiTransportTwitterIdPatch**](TransportTwitterApi.md#apiTransportTwitterIdPatch) | **PATCH** /api/transport-twitter/{id} | Updates the TransportTwitter resource. |
| [**apiTransportTwitterIdPut**](TransportTwitterApi.md#apiTransportTwitterIdPut) | **PUT** /api/transport-twitter/{id} | Replaces the TransportTwitter resource. |
| [**apiTransportTwitterPost**](TransportTwitterApi.md#apiTransportTwitterPost) | **POST** /api/transport-twitter | Creates a TransportTwitter resource. |


<a id="apiTransportTwitterGetCollection"></a>
# **apiTransportTwitterGetCollection**
> List&lt;TransportTwitterGet&gt; apiTransportTwitterGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportTwitter resources.

Retrieves the collection of TransportTwitter resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwitterApi apiInstance = new TransportTwitterApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportTwitterGet> result = apiInstance.apiTransportTwitterGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwitterApi#apiTransportTwitterGetCollection");
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

[**List&lt;TransportTwitterGet&gt;**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTwitter collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwitterIdDelete"></a>
# **apiTransportTwitterIdDelete**
> apiTransportTwitterIdDelete(id)

Removes the TransportTwitter resource.

Removes the TransportTwitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwitterApi apiInstance = new TransportTwitterApi(defaultClient);
    String id = "id_example"; // String | TransportTwitter identifier
    try {
      apiInstance.apiTransportTwitterIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwitterApi#apiTransportTwitterIdDelete");
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
| **id** | **String**| TransportTwitter identifier | |

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
| **204** | TransportTwitter resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwitterIdGet"></a>
# **apiTransportTwitterIdGet**
> TransportTwitterGet apiTransportTwitterIdGet(id)

Retrieves a TransportTwitter resource.

Retrieves a TransportTwitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwitterApi apiInstance = new TransportTwitterApi(defaultClient);
    String id = "id_example"; // String | TransportTwitter identifier
    try {
      TransportTwitterGet result = apiInstance.apiTransportTwitterIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwitterApi#apiTransportTwitterIdGet");
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
| **id** | **String**| TransportTwitter identifier | |

### Return type

[**TransportTwitterGet**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTwitter resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwitterIdPatch"></a>
# **apiTransportTwitterIdPatch**
> TransportTwitterGet apiTransportTwitterIdPatch(id, transportTwitterPatch)

Updates the TransportTwitter resource.

Updates the TransportTwitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwitterApi apiInstance = new TransportTwitterApi(defaultClient);
    String id = "id_example"; // String | TransportTwitter identifier
    TransportTwitterPatch transportTwitterPatch = new TransportTwitterPatch(); // TransportTwitterPatch | The updated TransportTwitter resource
    try {
      TransportTwitterGet result = apiInstance.apiTransportTwitterIdPatch(id, transportTwitterPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwitterApi#apiTransportTwitterIdPatch");
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
| **id** | **String**| TransportTwitter identifier | |
| **transportTwitterPatch** | [**TransportTwitterPatch**](TransportTwitterPatch.md)| The updated TransportTwitter resource | |

### Return type

[**TransportTwitterGet**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTwitter resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwitterIdPut"></a>
# **apiTransportTwitterIdPut**
> TransportTwitterGet apiTransportTwitterIdPut(id, transportTwitterPut)

Replaces the TransportTwitter resource.

Replaces the TransportTwitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwitterApi apiInstance = new TransportTwitterApi(defaultClient);
    String id = "id_example"; // String | TransportTwitter identifier
    TransportTwitterPut transportTwitterPut = new TransportTwitterPut(); // TransportTwitterPut | The updated TransportTwitter resource
    try {
      TransportTwitterGet result = apiInstance.apiTransportTwitterIdPut(id, transportTwitterPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwitterApi#apiTransportTwitterIdPut");
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
| **id** | **String**| TransportTwitter identifier | |
| **transportTwitterPut** | [**TransportTwitterPut**](TransportTwitterPut.md)| The updated TransportTwitter resource | |

### Return type

[**TransportTwitterGet**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTwitter resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwitterPost"></a>
# **apiTransportTwitterPost**
> TransportTwitterGet apiTransportTwitterPost(transportTwitterPost)

Creates a TransportTwitter resource.

Creates a TransportTwitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwitterApi apiInstance = new TransportTwitterApi(defaultClient);
    TransportTwitterPost transportTwitterPost = new TransportTwitterPost(); // TransportTwitterPost | The new TransportTwitter resource
    try {
      TransportTwitterGet result = apiInstance.apiTransportTwitterPost(transportTwitterPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwitterApi#apiTransportTwitterPost");
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
| **transportTwitterPost** | [**TransportTwitterPost**](TransportTwitterPost.md)| The new TransportTwitter resource | |

### Return type

[**TransportTwitterGet**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportTwitter resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

