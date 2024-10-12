# TransportEngagespotApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportEngagespotGetCollection**](TransportEngagespotApi.md#apiTransportEngagespotGetCollection) | **GET** /api/transport-engagespot | Retrieves the collection of TransportEngagespot resources. |
| [**apiTransportEngagespotIdDelete**](TransportEngagespotApi.md#apiTransportEngagespotIdDelete) | **DELETE** /api/transport-engagespot/{id} | Removes the TransportEngagespot resource. |
| [**apiTransportEngagespotIdGet**](TransportEngagespotApi.md#apiTransportEngagespotIdGet) | **GET** /api/transport-engagespot/{id} | Retrieves a TransportEngagespot resource. |
| [**apiTransportEngagespotIdPatch**](TransportEngagespotApi.md#apiTransportEngagespotIdPatch) | **PATCH** /api/transport-engagespot/{id} | Updates the TransportEngagespot resource. |
| [**apiTransportEngagespotIdPut**](TransportEngagespotApi.md#apiTransportEngagespotIdPut) | **PUT** /api/transport-engagespot/{id} | Replaces the TransportEngagespot resource. |
| [**apiTransportEngagespotPost**](TransportEngagespotApi.md#apiTransportEngagespotPost) | **POST** /api/transport-engagespot | Creates a TransportEngagespot resource. |


<a id="apiTransportEngagespotGetCollection"></a>
# **apiTransportEngagespotGetCollection**
> List&lt;TransportEngagespotGet&gt; apiTransportEngagespotGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportEngagespot resources.

Retrieves the collection of TransportEngagespot resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEngagespotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEngagespotApi apiInstance = new TransportEngagespotApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportEngagespotGet> result = apiInstance.apiTransportEngagespotGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEngagespotApi#apiTransportEngagespotGetCollection");
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

[**List&lt;TransportEngagespotGet&gt;**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEngagespot collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEngagespotIdDelete"></a>
# **apiTransportEngagespotIdDelete**
> apiTransportEngagespotIdDelete(id)

Removes the TransportEngagespot resource.

Removes the TransportEngagespot resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEngagespotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEngagespotApi apiInstance = new TransportEngagespotApi(defaultClient);
    String id = "id_example"; // String | TransportEngagespot identifier
    try {
      apiInstance.apiTransportEngagespotIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEngagespotApi#apiTransportEngagespotIdDelete");
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
| **id** | **String**| TransportEngagespot identifier | |

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
| **204** | TransportEngagespot resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEngagespotIdGet"></a>
# **apiTransportEngagespotIdGet**
> TransportEngagespotGet apiTransportEngagespotIdGet(id)

Retrieves a TransportEngagespot resource.

Retrieves a TransportEngagespot resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEngagespotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEngagespotApi apiInstance = new TransportEngagespotApi(defaultClient);
    String id = "id_example"; // String | TransportEngagespot identifier
    try {
      TransportEngagespotGet result = apiInstance.apiTransportEngagespotIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEngagespotApi#apiTransportEngagespotIdGet");
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
| **id** | **String**| TransportEngagespot identifier | |

### Return type

[**TransportEngagespotGet**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEngagespot resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEngagespotIdPatch"></a>
# **apiTransportEngagespotIdPatch**
> TransportEngagespotGet apiTransportEngagespotIdPatch(id, transportEngagespotPatch)

Updates the TransportEngagespot resource.

Updates the TransportEngagespot resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEngagespotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEngagespotApi apiInstance = new TransportEngagespotApi(defaultClient);
    String id = "id_example"; // String | TransportEngagespot identifier
    TransportEngagespotPatch transportEngagespotPatch = new TransportEngagespotPatch(); // TransportEngagespotPatch | The updated TransportEngagespot resource
    try {
      TransportEngagespotGet result = apiInstance.apiTransportEngagespotIdPatch(id, transportEngagespotPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEngagespotApi#apiTransportEngagespotIdPatch");
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
| **id** | **String**| TransportEngagespot identifier | |
| **transportEngagespotPatch** | [**TransportEngagespotPatch**](TransportEngagespotPatch.md)| The updated TransportEngagespot resource | |

### Return type

[**TransportEngagespotGet**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEngagespot resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEngagespotIdPut"></a>
# **apiTransportEngagespotIdPut**
> TransportEngagespotGet apiTransportEngagespotIdPut(id, transportEngagespotPut)

Replaces the TransportEngagespot resource.

Replaces the TransportEngagespot resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEngagespotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEngagespotApi apiInstance = new TransportEngagespotApi(defaultClient);
    String id = "id_example"; // String | TransportEngagespot identifier
    TransportEngagespotPut transportEngagespotPut = new TransportEngagespotPut(); // TransportEngagespotPut | The updated TransportEngagespot resource
    try {
      TransportEngagespotGet result = apiInstance.apiTransportEngagespotIdPut(id, transportEngagespotPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEngagespotApi#apiTransportEngagespotIdPut");
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
| **id** | **String**| TransportEngagespot identifier | |
| **transportEngagespotPut** | [**TransportEngagespotPut**](TransportEngagespotPut.md)| The updated TransportEngagespot resource | |

### Return type

[**TransportEngagespotGet**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEngagespot resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEngagespotPost"></a>
# **apiTransportEngagespotPost**
> TransportEngagespotGet apiTransportEngagespotPost(transportEngagespotPost)

Creates a TransportEngagespot resource.

Creates a TransportEngagespot resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEngagespotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEngagespotApi apiInstance = new TransportEngagespotApi(defaultClient);
    TransportEngagespotPost transportEngagespotPost = new TransportEngagespotPost(); // TransportEngagespotPost | The new TransportEngagespot resource
    try {
      TransportEngagespotGet result = apiInstance.apiTransportEngagespotPost(transportEngagespotPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEngagespotApi#apiTransportEngagespotPost");
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
| **transportEngagespotPost** | [**TransportEngagespotPost**](TransportEngagespotPost.md)| The new TransportEngagespot resource | |

### Return type

[**TransportEngagespotGet**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportEngagespot resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

