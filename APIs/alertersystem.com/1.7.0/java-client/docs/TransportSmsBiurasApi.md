# TransportSmsBiurasApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSmsBiurasGetCollection**](TransportSmsBiurasApi.md#apiTransportSmsBiurasGetCollection) | **GET** /api/transport-sms-biuras | Retrieves the collection of TransportSmsBiuras resources. |
| [**apiTransportSmsBiurasIdDelete**](TransportSmsBiurasApi.md#apiTransportSmsBiurasIdDelete) | **DELETE** /api/transport-sms-biuras/{id} | Removes the TransportSmsBiuras resource. |
| [**apiTransportSmsBiurasIdGet**](TransportSmsBiurasApi.md#apiTransportSmsBiurasIdGet) | **GET** /api/transport-sms-biuras/{id} | Retrieves a TransportSmsBiuras resource. |
| [**apiTransportSmsBiurasIdPatch**](TransportSmsBiurasApi.md#apiTransportSmsBiurasIdPatch) | **PATCH** /api/transport-sms-biuras/{id} | Updates the TransportSmsBiuras resource. |
| [**apiTransportSmsBiurasIdPut**](TransportSmsBiurasApi.md#apiTransportSmsBiurasIdPut) | **PUT** /api/transport-sms-biuras/{id} | Replaces the TransportSmsBiuras resource. |
| [**apiTransportSmsBiurasPost**](TransportSmsBiurasApi.md#apiTransportSmsBiurasPost) | **POST** /api/transport-sms-biuras | Creates a TransportSmsBiuras resource. |


<a id="apiTransportSmsBiurasGetCollection"></a>
# **apiTransportSmsBiurasGetCollection**
> List&lt;TransportSmsBiurasGet&gt; apiTransportSmsBiurasGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSmsBiuras resources.

Retrieves the collection of TransportSmsBiuras resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsBiurasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsBiurasApi apiInstance = new TransportSmsBiurasApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSmsBiurasGet> result = apiInstance.apiTransportSmsBiurasGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsBiurasApi#apiTransportSmsBiurasGetCollection");
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

[**List&lt;TransportSmsBiurasGet&gt;**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsBiuras collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsBiurasIdDelete"></a>
# **apiTransportSmsBiurasIdDelete**
> apiTransportSmsBiurasIdDelete(id)

Removes the TransportSmsBiuras resource.

Removes the TransportSmsBiuras resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsBiurasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsBiurasApi apiInstance = new TransportSmsBiurasApi(defaultClient);
    String id = "id_example"; // String | TransportSmsBiuras identifier
    try {
      apiInstance.apiTransportSmsBiurasIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsBiurasApi#apiTransportSmsBiurasIdDelete");
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
| **id** | **String**| TransportSmsBiuras identifier | |

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
| **204** | TransportSmsBiuras resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsBiurasIdGet"></a>
# **apiTransportSmsBiurasIdGet**
> TransportSmsBiurasGet apiTransportSmsBiurasIdGet(id)

Retrieves a TransportSmsBiuras resource.

Retrieves a TransportSmsBiuras resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsBiurasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsBiurasApi apiInstance = new TransportSmsBiurasApi(defaultClient);
    String id = "id_example"; // String | TransportSmsBiuras identifier
    try {
      TransportSmsBiurasGet result = apiInstance.apiTransportSmsBiurasIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsBiurasApi#apiTransportSmsBiurasIdGet");
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
| **id** | **String**| TransportSmsBiuras identifier | |

### Return type

[**TransportSmsBiurasGet**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsBiuras resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsBiurasIdPatch"></a>
# **apiTransportSmsBiurasIdPatch**
> TransportSmsBiurasGet apiTransportSmsBiurasIdPatch(id, transportSmsBiurasPatch)

Updates the TransportSmsBiuras resource.

Updates the TransportSmsBiuras resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsBiurasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsBiurasApi apiInstance = new TransportSmsBiurasApi(defaultClient);
    String id = "id_example"; // String | TransportSmsBiuras identifier
    TransportSmsBiurasPatch transportSmsBiurasPatch = new TransportSmsBiurasPatch(); // TransportSmsBiurasPatch | The updated TransportSmsBiuras resource
    try {
      TransportSmsBiurasGet result = apiInstance.apiTransportSmsBiurasIdPatch(id, transportSmsBiurasPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsBiurasApi#apiTransportSmsBiurasIdPatch");
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
| **id** | **String**| TransportSmsBiuras identifier | |
| **transportSmsBiurasPatch** | [**TransportSmsBiurasPatch**](TransportSmsBiurasPatch.md)| The updated TransportSmsBiuras resource | |

### Return type

[**TransportSmsBiurasGet**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsBiuras resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsBiurasIdPut"></a>
# **apiTransportSmsBiurasIdPut**
> TransportSmsBiurasGet apiTransportSmsBiurasIdPut(id, transportSmsBiurasPut)

Replaces the TransportSmsBiuras resource.

Replaces the TransportSmsBiuras resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsBiurasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsBiurasApi apiInstance = new TransportSmsBiurasApi(defaultClient);
    String id = "id_example"; // String | TransportSmsBiuras identifier
    TransportSmsBiurasPut transportSmsBiurasPut = new TransportSmsBiurasPut(); // TransportSmsBiurasPut | The updated TransportSmsBiuras resource
    try {
      TransportSmsBiurasGet result = apiInstance.apiTransportSmsBiurasIdPut(id, transportSmsBiurasPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsBiurasApi#apiTransportSmsBiurasIdPut");
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
| **id** | **String**| TransportSmsBiuras identifier | |
| **transportSmsBiurasPut** | [**TransportSmsBiurasPut**](TransportSmsBiurasPut.md)| The updated TransportSmsBiuras resource | |

### Return type

[**TransportSmsBiurasGet**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsBiuras resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsBiurasPost"></a>
# **apiTransportSmsBiurasPost**
> TransportSmsBiurasGet apiTransportSmsBiurasPost(transportSmsBiurasPost)

Creates a TransportSmsBiuras resource.

Creates a TransportSmsBiuras resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsBiurasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsBiurasApi apiInstance = new TransportSmsBiurasApi(defaultClient);
    TransportSmsBiurasPost transportSmsBiurasPost = new TransportSmsBiurasPost(); // TransportSmsBiurasPost | The new TransportSmsBiuras resource
    try {
      TransportSmsBiurasGet result = apiInstance.apiTransportSmsBiurasPost(transportSmsBiurasPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsBiurasApi#apiTransportSmsBiurasPost");
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
| **transportSmsBiurasPost** | [**TransportSmsBiurasPost**](TransportSmsBiurasPost.md)| The new TransportSmsBiuras resource | |

### Return type

[**TransportSmsBiurasGet**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSmsBiuras resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

