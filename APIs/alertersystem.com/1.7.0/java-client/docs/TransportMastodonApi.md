# TransportMastodonApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportMastodonGetCollection**](TransportMastodonApi.md#apiTransportMastodonGetCollection) | **GET** /api/transport-mastodon | Retrieves the collection of TransportMastodon resources. |
| [**apiTransportMastodonIdDelete**](TransportMastodonApi.md#apiTransportMastodonIdDelete) | **DELETE** /api/transport-mastodon/{id} | Removes the TransportMastodon resource. |
| [**apiTransportMastodonIdGet**](TransportMastodonApi.md#apiTransportMastodonIdGet) | **GET** /api/transport-mastodon/{id} | Retrieves a TransportMastodon resource. |
| [**apiTransportMastodonIdPatch**](TransportMastodonApi.md#apiTransportMastodonIdPatch) | **PATCH** /api/transport-mastodon/{id} | Updates the TransportMastodon resource. |
| [**apiTransportMastodonIdPut**](TransportMastodonApi.md#apiTransportMastodonIdPut) | **PUT** /api/transport-mastodon/{id} | Replaces the TransportMastodon resource. |
| [**apiTransportMastodonPost**](TransportMastodonApi.md#apiTransportMastodonPost) | **POST** /api/transport-mastodon | Creates a TransportMastodon resource. |


<a id="apiTransportMastodonGetCollection"></a>
# **apiTransportMastodonGetCollection**
> List&lt;TransportMastodonGet&gt; apiTransportMastodonGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportMastodon resources.

Retrieves the collection of TransportMastodon resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMastodonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMastodonApi apiInstance = new TransportMastodonApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportMastodonGet> result = apiInstance.apiTransportMastodonGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMastodonApi#apiTransportMastodonGetCollection");
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

[**List&lt;TransportMastodonGet&gt;**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMastodon collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMastodonIdDelete"></a>
# **apiTransportMastodonIdDelete**
> apiTransportMastodonIdDelete(id)

Removes the TransportMastodon resource.

Removes the TransportMastodon resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMastodonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMastodonApi apiInstance = new TransportMastodonApi(defaultClient);
    String id = "id_example"; // String | TransportMastodon identifier
    try {
      apiInstance.apiTransportMastodonIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMastodonApi#apiTransportMastodonIdDelete");
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
| **id** | **String**| TransportMastodon identifier | |

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
| **204** | TransportMastodon resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMastodonIdGet"></a>
# **apiTransportMastodonIdGet**
> TransportMastodonGet apiTransportMastodonIdGet(id)

Retrieves a TransportMastodon resource.

Retrieves a TransportMastodon resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMastodonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMastodonApi apiInstance = new TransportMastodonApi(defaultClient);
    String id = "id_example"; // String | TransportMastodon identifier
    try {
      TransportMastodonGet result = apiInstance.apiTransportMastodonIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMastodonApi#apiTransportMastodonIdGet");
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
| **id** | **String**| TransportMastodon identifier | |

### Return type

[**TransportMastodonGet**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMastodon resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMastodonIdPatch"></a>
# **apiTransportMastodonIdPatch**
> TransportMastodonGet apiTransportMastodonIdPatch(id, transportMastodonPatch)

Updates the TransportMastodon resource.

Updates the TransportMastodon resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMastodonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMastodonApi apiInstance = new TransportMastodonApi(defaultClient);
    String id = "id_example"; // String | TransportMastodon identifier
    TransportMastodonPatch transportMastodonPatch = new TransportMastodonPatch(); // TransportMastodonPatch | The updated TransportMastodon resource
    try {
      TransportMastodonGet result = apiInstance.apiTransportMastodonIdPatch(id, transportMastodonPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMastodonApi#apiTransportMastodonIdPatch");
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
| **id** | **String**| TransportMastodon identifier | |
| **transportMastodonPatch** | [**TransportMastodonPatch**](TransportMastodonPatch.md)| The updated TransportMastodon resource | |

### Return type

[**TransportMastodonGet**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMastodon resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMastodonIdPut"></a>
# **apiTransportMastodonIdPut**
> TransportMastodonGet apiTransportMastodonIdPut(id, transportMastodonPut)

Replaces the TransportMastodon resource.

Replaces the TransportMastodon resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMastodonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMastodonApi apiInstance = new TransportMastodonApi(defaultClient);
    String id = "id_example"; // String | TransportMastodon identifier
    TransportMastodonPut transportMastodonPut = new TransportMastodonPut(); // TransportMastodonPut | The updated TransportMastodon resource
    try {
      TransportMastodonGet result = apiInstance.apiTransportMastodonIdPut(id, transportMastodonPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMastodonApi#apiTransportMastodonIdPut");
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
| **id** | **String**| TransportMastodon identifier | |
| **transportMastodonPut** | [**TransportMastodonPut**](TransportMastodonPut.md)| The updated TransportMastodon resource | |

### Return type

[**TransportMastodonGet**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMastodon resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMastodonPost"></a>
# **apiTransportMastodonPost**
> TransportMastodonGet apiTransportMastodonPost(transportMastodonPost)

Creates a TransportMastodon resource.

Creates a TransportMastodon resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMastodonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMastodonApi apiInstance = new TransportMastodonApi(defaultClient);
    TransportMastodonPost transportMastodonPost = new TransportMastodonPost(); // TransportMastodonPost | The new TransportMastodon resource
    try {
      TransportMastodonGet result = apiInstance.apiTransportMastodonPost(transportMastodonPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMastodonApi#apiTransportMastodonPost");
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
| **transportMastodonPost** | [**TransportMastodonPost**](TransportMastodonPost.md)| The new TransportMastodon resource | |

### Return type

[**TransportMastodonGet**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportMastodon resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

