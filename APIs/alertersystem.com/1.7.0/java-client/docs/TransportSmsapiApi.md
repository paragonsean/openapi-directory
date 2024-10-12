# TransportSmsapiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSmsapiGetCollection**](TransportSmsapiApi.md#apiTransportSmsapiGetCollection) | **GET** /api/transport-smsapi | Retrieves the collection of TransportSmsapi resources. |
| [**apiTransportSmsapiIdDelete**](TransportSmsapiApi.md#apiTransportSmsapiIdDelete) | **DELETE** /api/transport-smsapi/{id} | Removes the TransportSmsapi resource. |
| [**apiTransportSmsapiIdGet**](TransportSmsapiApi.md#apiTransportSmsapiIdGet) | **GET** /api/transport-smsapi/{id} | Retrieves a TransportSmsapi resource. |
| [**apiTransportSmsapiIdPatch**](TransportSmsapiApi.md#apiTransportSmsapiIdPatch) | **PATCH** /api/transport-smsapi/{id} | Updates the TransportSmsapi resource. |
| [**apiTransportSmsapiIdPut**](TransportSmsapiApi.md#apiTransportSmsapiIdPut) | **PUT** /api/transport-smsapi/{id} | Replaces the TransportSmsapi resource. |
| [**apiTransportSmsapiPost**](TransportSmsapiApi.md#apiTransportSmsapiPost) | **POST** /api/transport-smsapi | Creates a TransportSmsapi resource. |


<a id="apiTransportSmsapiGetCollection"></a>
# **apiTransportSmsapiGetCollection**
> List&lt;TransportSmsapiGet&gt; apiTransportSmsapiGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSmsapi resources.

Retrieves the collection of TransportSmsapi resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsapiApi apiInstance = new TransportSmsapiApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSmsapiGet> result = apiInstance.apiTransportSmsapiGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsapiApi#apiTransportSmsapiGetCollection");
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

[**List&lt;TransportSmsapiGet&gt;**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsapi collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsapiIdDelete"></a>
# **apiTransportSmsapiIdDelete**
> apiTransportSmsapiIdDelete(id)

Removes the TransportSmsapi resource.

Removes the TransportSmsapi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsapiApi apiInstance = new TransportSmsapiApi(defaultClient);
    String id = "id_example"; // String | TransportSmsapi identifier
    try {
      apiInstance.apiTransportSmsapiIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsapiApi#apiTransportSmsapiIdDelete");
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
| **id** | **String**| TransportSmsapi identifier | |

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
| **204** | TransportSmsapi resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsapiIdGet"></a>
# **apiTransportSmsapiIdGet**
> TransportSmsapiGet apiTransportSmsapiIdGet(id)

Retrieves a TransportSmsapi resource.

Retrieves a TransportSmsapi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsapiApi apiInstance = new TransportSmsapiApi(defaultClient);
    String id = "id_example"; // String | TransportSmsapi identifier
    try {
      TransportSmsapiGet result = apiInstance.apiTransportSmsapiIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsapiApi#apiTransportSmsapiIdGet");
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
| **id** | **String**| TransportSmsapi identifier | |

### Return type

[**TransportSmsapiGet**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsapi resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsapiIdPatch"></a>
# **apiTransportSmsapiIdPatch**
> TransportSmsapiGet apiTransportSmsapiIdPatch(id, transportSmsapiPatch)

Updates the TransportSmsapi resource.

Updates the TransportSmsapi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsapiApi apiInstance = new TransportSmsapiApi(defaultClient);
    String id = "id_example"; // String | TransportSmsapi identifier
    TransportSmsapiPatch transportSmsapiPatch = new TransportSmsapiPatch(); // TransportSmsapiPatch | The updated TransportSmsapi resource
    try {
      TransportSmsapiGet result = apiInstance.apiTransportSmsapiIdPatch(id, transportSmsapiPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsapiApi#apiTransportSmsapiIdPatch");
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
| **id** | **String**| TransportSmsapi identifier | |
| **transportSmsapiPatch** | [**TransportSmsapiPatch**](TransportSmsapiPatch.md)| The updated TransportSmsapi resource | |

### Return type

[**TransportSmsapiGet**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsapi resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsapiIdPut"></a>
# **apiTransportSmsapiIdPut**
> TransportSmsapiGet apiTransportSmsapiIdPut(id, transportSmsapiPut)

Replaces the TransportSmsapi resource.

Replaces the TransportSmsapi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsapiApi apiInstance = new TransportSmsapiApi(defaultClient);
    String id = "id_example"; // String | TransportSmsapi identifier
    TransportSmsapiPut transportSmsapiPut = new TransportSmsapiPut(); // TransportSmsapiPut | The updated TransportSmsapi resource
    try {
      TransportSmsapiGet result = apiInstance.apiTransportSmsapiIdPut(id, transportSmsapiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsapiApi#apiTransportSmsapiIdPut");
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
| **id** | **String**| TransportSmsapi identifier | |
| **transportSmsapiPut** | [**TransportSmsapiPut**](TransportSmsapiPut.md)| The updated TransportSmsapi resource | |

### Return type

[**TransportSmsapiGet**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsapi resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsapiPost"></a>
# **apiTransportSmsapiPost**
> TransportSmsapiGet apiTransportSmsapiPost(transportSmsapiPost)

Creates a TransportSmsapi resource.

Creates a TransportSmsapi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsapiApi apiInstance = new TransportSmsapiApi(defaultClient);
    TransportSmsapiPost transportSmsapiPost = new TransportSmsapiPost(); // TransportSmsapiPost | The new TransportSmsapi resource
    try {
      TransportSmsapiGet result = apiInstance.apiTransportSmsapiPost(transportSmsapiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsapiApi#apiTransportSmsapiPost");
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
| **transportSmsapiPost** | [**TransportSmsapiPost**](TransportSmsapiPost.md)| The new TransportSmsapi resource | |

### Return type

[**TransportSmsapiGet**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSmsapi resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

