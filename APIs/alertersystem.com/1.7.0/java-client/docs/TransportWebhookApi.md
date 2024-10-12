# TransportWebhookApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportWebhookGetCollection**](TransportWebhookApi.md#apiTransportWebhookGetCollection) | **GET** /api/transport-webhook | Retrieves the collection of TransportWebhook resources. |
| [**apiTransportWebhookIdDelete**](TransportWebhookApi.md#apiTransportWebhookIdDelete) | **DELETE** /api/transport-webhook/{id} | Removes the TransportWebhook resource. |
| [**apiTransportWebhookIdGet**](TransportWebhookApi.md#apiTransportWebhookIdGet) | **GET** /api/transport-webhook/{id} | Retrieves a TransportWebhook resource. |
| [**apiTransportWebhookIdPatch**](TransportWebhookApi.md#apiTransportWebhookIdPatch) | **PATCH** /api/transport-webhook/{id} | Updates the TransportWebhook resource. |
| [**apiTransportWebhookIdPut**](TransportWebhookApi.md#apiTransportWebhookIdPut) | **PUT** /api/transport-webhook/{id} | Replaces the TransportWebhook resource. |
| [**apiTransportWebhookPost**](TransportWebhookApi.md#apiTransportWebhookPost) | **POST** /api/transport-webhook | Creates a TransportWebhook resource. |


<a id="apiTransportWebhookGetCollection"></a>
# **apiTransportWebhookGetCollection**
> List&lt;TransportWebhookGet&gt; apiTransportWebhookGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportWebhook resources.

Retrieves the collection of TransportWebhook resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportWebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportWebhookApi apiInstance = new TransportWebhookApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportWebhookGet> result = apiInstance.apiTransportWebhookGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportWebhookApi#apiTransportWebhookGetCollection");
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

[**List&lt;TransportWebhookGet&gt;**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportWebhook collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportWebhookIdDelete"></a>
# **apiTransportWebhookIdDelete**
> apiTransportWebhookIdDelete(id)

Removes the TransportWebhook resource.

Removes the TransportWebhook resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportWebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportWebhookApi apiInstance = new TransportWebhookApi(defaultClient);
    String id = "id_example"; // String | TransportWebhook identifier
    try {
      apiInstance.apiTransportWebhookIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportWebhookApi#apiTransportWebhookIdDelete");
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
| **id** | **String**| TransportWebhook identifier | |

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
| **204** | TransportWebhook resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportWebhookIdGet"></a>
# **apiTransportWebhookIdGet**
> TransportWebhookGet apiTransportWebhookIdGet(id)

Retrieves a TransportWebhook resource.

Retrieves a TransportWebhook resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportWebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportWebhookApi apiInstance = new TransportWebhookApi(defaultClient);
    String id = "id_example"; // String | TransportWebhook identifier
    try {
      TransportWebhookGet result = apiInstance.apiTransportWebhookIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportWebhookApi#apiTransportWebhookIdGet");
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
| **id** | **String**| TransportWebhook identifier | |

### Return type

[**TransportWebhookGet**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportWebhook resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportWebhookIdPatch"></a>
# **apiTransportWebhookIdPatch**
> TransportWebhookGet apiTransportWebhookIdPatch(id, transportWebhookPatch)

Updates the TransportWebhook resource.

Updates the TransportWebhook resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportWebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportWebhookApi apiInstance = new TransportWebhookApi(defaultClient);
    String id = "id_example"; // String | TransportWebhook identifier
    TransportWebhookPatch transportWebhookPatch = new TransportWebhookPatch(); // TransportWebhookPatch | The updated TransportWebhook resource
    try {
      TransportWebhookGet result = apiInstance.apiTransportWebhookIdPatch(id, transportWebhookPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportWebhookApi#apiTransportWebhookIdPatch");
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
| **id** | **String**| TransportWebhook identifier | |
| **transportWebhookPatch** | [**TransportWebhookPatch**](TransportWebhookPatch.md)| The updated TransportWebhook resource | |

### Return type

[**TransportWebhookGet**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportWebhook resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportWebhookIdPut"></a>
# **apiTransportWebhookIdPut**
> TransportWebhookGet apiTransportWebhookIdPut(id, transportWebhookPut)

Replaces the TransportWebhook resource.

Replaces the TransportWebhook resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportWebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportWebhookApi apiInstance = new TransportWebhookApi(defaultClient);
    String id = "id_example"; // String | TransportWebhook identifier
    TransportWebhookPut transportWebhookPut = new TransportWebhookPut(); // TransportWebhookPut | The updated TransportWebhook resource
    try {
      TransportWebhookGet result = apiInstance.apiTransportWebhookIdPut(id, transportWebhookPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportWebhookApi#apiTransportWebhookIdPut");
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
| **id** | **String**| TransportWebhook identifier | |
| **transportWebhookPut** | [**TransportWebhookPut**](TransportWebhookPut.md)| The updated TransportWebhook resource | |

### Return type

[**TransportWebhookGet**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportWebhook resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportWebhookPost"></a>
# **apiTransportWebhookPost**
> TransportWebhookGet apiTransportWebhookPost(transportWebhookPost)

Creates a TransportWebhook resource.

Creates a TransportWebhook resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportWebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportWebhookApi apiInstance = new TransportWebhookApi(defaultClient);
    TransportWebhookPost transportWebhookPost = new TransportWebhookPost(); // TransportWebhookPost | The new TransportWebhook resource
    try {
      TransportWebhookGet result = apiInstance.apiTransportWebhookPost(transportWebhookPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportWebhookApi#apiTransportWebhookPost");
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
| **transportWebhookPost** | [**TransportWebhookPost**](TransportWebhookPost.md)| The new TransportWebhook resource | |

### Return type

[**TransportWebhookGet**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportWebhook resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

