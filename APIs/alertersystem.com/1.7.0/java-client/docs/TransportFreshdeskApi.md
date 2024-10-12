# TransportFreshdeskApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportFreshdeskGetCollection**](TransportFreshdeskApi.md#apiTransportFreshdeskGetCollection) | **GET** /api/transport-freshdesk | Retrieves the collection of TransportFreshdesk resources. |
| [**apiTransportFreshdeskIdDelete**](TransportFreshdeskApi.md#apiTransportFreshdeskIdDelete) | **DELETE** /api/transport-freshdesk/{id} | Removes the TransportFreshdesk resource. |
| [**apiTransportFreshdeskIdGet**](TransportFreshdeskApi.md#apiTransportFreshdeskIdGet) | **GET** /api/transport-freshdesk/{id} | Retrieves a TransportFreshdesk resource. |
| [**apiTransportFreshdeskIdPatch**](TransportFreshdeskApi.md#apiTransportFreshdeskIdPatch) | **PATCH** /api/transport-freshdesk/{id} | Updates the TransportFreshdesk resource. |
| [**apiTransportFreshdeskIdPut**](TransportFreshdeskApi.md#apiTransportFreshdeskIdPut) | **PUT** /api/transport-freshdesk/{id} | Replaces the TransportFreshdesk resource. |
| [**apiTransportFreshdeskPost**](TransportFreshdeskApi.md#apiTransportFreshdeskPost) | **POST** /api/transport-freshdesk | Creates a TransportFreshdesk resource. |


<a id="apiTransportFreshdeskGetCollection"></a>
# **apiTransportFreshdeskGetCollection**
> List&lt;TransportFreshdeskGet&gt; apiTransportFreshdeskGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportFreshdesk resources.

Retrieves the collection of TransportFreshdesk resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreshdeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreshdeskApi apiInstance = new TransportFreshdeskApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportFreshdeskGet> result = apiInstance.apiTransportFreshdeskGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreshdeskApi#apiTransportFreshdeskGetCollection");
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

[**List&lt;TransportFreshdeskGet&gt;**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFreshdesk collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreshdeskIdDelete"></a>
# **apiTransportFreshdeskIdDelete**
> apiTransportFreshdeskIdDelete(id)

Removes the TransportFreshdesk resource.

Removes the TransportFreshdesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreshdeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreshdeskApi apiInstance = new TransportFreshdeskApi(defaultClient);
    String id = "id_example"; // String | TransportFreshdesk identifier
    try {
      apiInstance.apiTransportFreshdeskIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreshdeskApi#apiTransportFreshdeskIdDelete");
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
| **id** | **String**| TransportFreshdesk identifier | |

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
| **204** | TransportFreshdesk resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreshdeskIdGet"></a>
# **apiTransportFreshdeskIdGet**
> TransportFreshdeskGet apiTransportFreshdeskIdGet(id)

Retrieves a TransportFreshdesk resource.

Retrieves a TransportFreshdesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreshdeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreshdeskApi apiInstance = new TransportFreshdeskApi(defaultClient);
    String id = "id_example"; // String | TransportFreshdesk identifier
    try {
      TransportFreshdeskGet result = apiInstance.apiTransportFreshdeskIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreshdeskApi#apiTransportFreshdeskIdGet");
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
| **id** | **String**| TransportFreshdesk identifier | |

### Return type

[**TransportFreshdeskGet**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFreshdesk resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreshdeskIdPatch"></a>
# **apiTransportFreshdeskIdPatch**
> TransportFreshdeskGet apiTransportFreshdeskIdPatch(id, transportFreshdeskPatch)

Updates the TransportFreshdesk resource.

Updates the TransportFreshdesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreshdeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreshdeskApi apiInstance = new TransportFreshdeskApi(defaultClient);
    String id = "id_example"; // String | TransportFreshdesk identifier
    TransportFreshdeskPatch transportFreshdeskPatch = new TransportFreshdeskPatch(); // TransportFreshdeskPatch | The updated TransportFreshdesk resource
    try {
      TransportFreshdeskGet result = apiInstance.apiTransportFreshdeskIdPatch(id, transportFreshdeskPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreshdeskApi#apiTransportFreshdeskIdPatch");
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
| **id** | **String**| TransportFreshdesk identifier | |
| **transportFreshdeskPatch** | [**TransportFreshdeskPatch**](TransportFreshdeskPatch.md)| The updated TransportFreshdesk resource | |

### Return type

[**TransportFreshdeskGet**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFreshdesk resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreshdeskIdPut"></a>
# **apiTransportFreshdeskIdPut**
> TransportFreshdeskGet apiTransportFreshdeskIdPut(id, transportFreshdeskPut)

Replaces the TransportFreshdesk resource.

Replaces the TransportFreshdesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreshdeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreshdeskApi apiInstance = new TransportFreshdeskApi(defaultClient);
    String id = "id_example"; // String | TransportFreshdesk identifier
    TransportFreshdeskPut transportFreshdeskPut = new TransportFreshdeskPut(); // TransportFreshdeskPut | The updated TransportFreshdesk resource
    try {
      TransportFreshdeskGet result = apiInstance.apiTransportFreshdeskIdPut(id, transportFreshdeskPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreshdeskApi#apiTransportFreshdeskIdPut");
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
| **id** | **String**| TransportFreshdesk identifier | |
| **transportFreshdeskPut** | [**TransportFreshdeskPut**](TransportFreshdeskPut.md)| The updated TransportFreshdesk resource | |

### Return type

[**TransportFreshdeskGet**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFreshdesk resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreshdeskPost"></a>
# **apiTransportFreshdeskPost**
> TransportFreshdeskGet apiTransportFreshdeskPost(transportFreshdeskPost)

Creates a TransportFreshdesk resource.

Creates a TransportFreshdesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreshdeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreshdeskApi apiInstance = new TransportFreshdeskApi(defaultClient);
    TransportFreshdeskPost transportFreshdeskPost = new TransportFreshdeskPost(); // TransportFreshdeskPost | The new TransportFreshdesk resource
    try {
      TransportFreshdeskGet result = apiInstance.apiTransportFreshdeskPost(transportFreshdeskPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreshdeskApi#apiTransportFreshdeskPost");
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
| **transportFreshdeskPost** | [**TransportFreshdeskPost**](TransportFreshdeskPost.md)| The new TransportFreshdesk resource | |

### Return type

[**TransportFreshdeskGet**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportFreshdesk resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

