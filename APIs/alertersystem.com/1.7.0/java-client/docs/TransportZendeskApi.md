# TransportZendeskApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportZendeskGetCollection**](TransportZendeskApi.md#apiTransportZendeskGetCollection) | **GET** /api/transport-zendesk | Retrieves the collection of TransportZendesk resources. |
| [**apiTransportZendeskIdDelete**](TransportZendeskApi.md#apiTransportZendeskIdDelete) | **DELETE** /api/transport-zendesk/{id} | Removes the TransportZendesk resource. |
| [**apiTransportZendeskIdGet**](TransportZendeskApi.md#apiTransportZendeskIdGet) | **GET** /api/transport-zendesk/{id} | Retrieves a TransportZendesk resource. |
| [**apiTransportZendeskIdPatch**](TransportZendeskApi.md#apiTransportZendeskIdPatch) | **PATCH** /api/transport-zendesk/{id} | Updates the TransportZendesk resource. |
| [**apiTransportZendeskIdPut**](TransportZendeskApi.md#apiTransportZendeskIdPut) | **PUT** /api/transport-zendesk/{id} | Replaces the TransportZendesk resource. |
| [**apiTransportZendeskPost**](TransportZendeskApi.md#apiTransportZendeskPost) | **POST** /api/transport-zendesk | Creates a TransportZendesk resource. |


<a id="apiTransportZendeskGetCollection"></a>
# **apiTransportZendeskGetCollection**
> List&lt;TransportZendeskGet&gt; apiTransportZendeskGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportZendesk resources.

Retrieves the collection of TransportZendesk resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZendeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZendeskApi apiInstance = new TransportZendeskApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportZendeskGet> result = apiInstance.apiTransportZendeskGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZendeskApi#apiTransportZendeskGetCollection");
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

[**List&lt;TransportZendeskGet&gt;**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportZendesk collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZendeskIdDelete"></a>
# **apiTransportZendeskIdDelete**
> apiTransportZendeskIdDelete(id)

Removes the TransportZendesk resource.

Removes the TransportZendesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZendeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZendeskApi apiInstance = new TransportZendeskApi(defaultClient);
    String id = "id_example"; // String | TransportZendesk identifier
    try {
      apiInstance.apiTransportZendeskIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZendeskApi#apiTransportZendeskIdDelete");
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
| **id** | **String**| TransportZendesk identifier | |

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
| **204** | TransportZendesk resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZendeskIdGet"></a>
# **apiTransportZendeskIdGet**
> TransportZendeskGet apiTransportZendeskIdGet(id)

Retrieves a TransportZendesk resource.

Retrieves a TransportZendesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZendeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZendeskApi apiInstance = new TransportZendeskApi(defaultClient);
    String id = "id_example"; // String | TransportZendesk identifier
    try {
      TransportZendeskGet result = apiInstance.apiTransportZendeskIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZendeskApi#apiTransportZendeskIdGet");
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
| **id** | **String**| TransportZendesk identifier | |

### Return type

[**TransportZendeskGet**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportZendesk resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZendeskIdPatch"></a>
# **apiTransportZendeskIdPatch**
> TransportZendeskGet apiTransportZendeskIdPatch(id, transportZendeskPatch)

Updates the TransportZendesk resource.

Updates the TransportZendesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZendeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZendeskApi apiInstance = new TransportZendeskApi(defaultClient);
    String id = "id_example"; // String | TransportZendesk identifier
    TransportZendeskPatch transportZendeskPatch = new TransportZendeskPatch(); // TransportZendeskPatch | The updated TransportZendesk resource
    try {
      TransportZendeskGet result = apiInstance.apiTransportZendeskIdPatch(id, transportZendeskPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZendeskApi#apiTransportZendeskIdPatch");
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
| **id** | **String**| TransportZendesk identifier | |
| **transportZendeskPatch** | [**TransportZendeskPatch**](TransportZendeskPatch.md)| The updated TransportZendesk resource | |

### Return type

[**TransportZendeskGet**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportZendesk resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZendeskIdPut"></a>
# **apiTransportZendeskIdPut**
> TransportZendeskGet apiTransportZendeskIdPut(id, transportZendeskPut)

Replaces the TransportZendesk resource.

Replaces the TransportZendesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZendeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZendeskApi apiInstance = new TransportZendeskApi(defaultClient);
    String id = "id_example"; // String | TransportZendesk identifier
    TransportZendeskPut transportZendeskPut = new TransportZendeskPut(); // TransportZendeskPut | The updated TransportZendesk resource
    try {
      TransportZendeskGet result = apiInstance.apiTransportZendeskIdPut(id, transportZendeskPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZendeskApi#apiTransportZendeskIdPut");
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
| **id** | **String**| TransportZendesk identifier | |
| **transportZendeskPut** | [**TransportZendeskPut**](TransportZendeskPut.md)| The updated TransportZendesk resource | |

### Return type

[**TransportZendeskGet**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportZendesk resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZendeskPost"></a>
# **apiTransportZendeskPost**
> TransportZendeskGet apiTransportZendeskPost(transportZendeskPost)

Creates a TransportZendesk resource.

Creates a TransportZendesk resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZendeskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZendeskApi apiInstance = new TransportZendeskApi(defaultClient);
    TransportZendeskPost transportZendeskPost = new TransportZendeskPost(); // TransportZendeskPost | The new TransportZendesk resource
    try {
      TransportZendeskGet result = apiInstance.apiTransportZendeskPost(transportZendeskPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZendeskApi#apiTransportZendeskPost");
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
| **transportZendeskPost** | [**TransportZendeskPost**](TransportZendeskPost.md)| The new TransportZendesk resource | |

### Return type

[**TransportZendeskGet**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportZendesk resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

