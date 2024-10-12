# TransportTurboSmsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportTurboSmsGetCollection**](TransportTurboSmsApi.md#apiTransportTurboSmsGetCollection) | **GET** /api/transport-turbo-sms | Retrieves the collection of TransportTurboSms resources. |
| [**apiTransportTurboSmsIdDelete**](TransportTurboSmsApi.md#apiTransportTurboSmsIdDelete) | **DELETE** /api/transport-turbo-sms/{id} | Removes the TransportTurboSms resource. |
| [**apiTransportTurboSmsIdGet**](TransportTurboSmsApi.md#apiTransportTurboSmsIdGet) | **GET** /api/transport-turbo-sms/{id} | Retrieves a TransportTurboSms resource. |
| [**apiTransportTurboSmsIdPatch**](TransportTurboSmsApi.md#apiTransportTurboSmsIdPatch) | **PATCH** /api/transport-turbo-sms/{id} | Updates the TransportTurboSms resource. |
| [**apiTransportTurboSmsIdPut**](TransportTurboSmsApi.md#apiTransportTurboSmsIdPut) | **PUT** /api/transport-turbo-sms/{id} | Replaces the TransportTurboSms resource. |
| [**apiTransportTurboSmsPost**](TransportTurboSmsApi.md#apiTransportTurboSmsPost) | **POST** /api/transport-turbo-sms | Creates a TransportTurboSms resource. |


<a id="apiTransportTurboSmsGetCollection"></a>
# **apiTransportTurboSmsGetCollection**
> List&lt;TransportTurboSmsGet&gt; apiTransportTurboSmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportTurboSms resources.

Retrieves the collection of TransportTurboSms resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTurboSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTurboSmsApi apiInstance = new TransportTurboSmsApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportTurboSmsGet> result = apiInstance.apiTransportTurboSmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTurboSmsApi#apiTransportTurboSmsGetCollection");
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

[**List&lt;TransportTurboSmsGet&gt;**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTurboSms collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTurboSmsIdDelete"></a>
# **apiTransportTurboSmsIdDelete**
> apiTransportTurboSmsIdDelete(id)

Removes the TransportTurboSms resource.

Removes the TransportTurboSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTurboSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTurboSmsApi apiInstance = new TransportTurboSmsApi(defaultClient);
    String id = "id_example"; // String | TransportTurboSms identifier
    try {
      apiInstance.apiTransportTurboSmsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTurboSmsApi#apiTransportTurboSmsIdDelete");
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
| **id** | **String**| TransportTurboSms identifier | |

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
| **204** | TransportTurboSms resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTurboSmsIdGet"></a>
# **apiTransportTurboSmsIdGet**
> TransportTurboSmsGet apiTransportTurboSmsIdGet(id)

Retrieves a TransportTurboSms resource.

Retrieves a TransportTurboSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTurboSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTurboSmsApi apiInstance = new TransportTurboSmsApi(defaultClient);
    String id = "id_example"; // String | TransportTurboSms identifier
    try {
      TransportTurboSmsGet result = apiInstance.apiTransportTurboSmsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTurboSmsApi#apiTransportTurboSmsIdGet");
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
| **id** | **String**| TransportTurboSms identifier | |

### Return type

[**TransportTurboSmsGet**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTurboSms resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTurboSmsIdPatch"></a>
# **apiTransportTurboSmsIdPatch**
> TransportTurboSmsGet apiTransportTurboSmsIdPatch(id, transportTurboSmsPatch)

Updates the TransportTurboSms resource.

Updates the TransportTurboSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTurboSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTurboSmsApi apiInstance = new TransportTurboSmsApi(defaultClient);
    String id = "id_example"; // String | TransportTurboSms identifier
    TransportTurboSmsPatch transportTurboSmsPatch = new TransportTurboSmsPatch(); // TransportTurboSmsPatch | The updated TransportTurboSms resource
    try {
      TransportTurboSmsGet result = apiInstance.apiTransportTurboSmsIdPatch(id, transportTurboSmsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTurboSmsApi#apiTransportTurboSmsIdPatch");
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
| **id** | **String**| TransportTurboSms identifier | |
| **transportTurboSmsPatch** | [**TransportTurboSmsPatch**](TransportTurboSmsPatch.md)| The updated TransportTurboSms resource | |

### Return type

[**TransportTurboSmsGet**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTurboSms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTurboSmsIdPut"></a>
# **apiTransportTurboSmsIdPut**
> TransportTurboSmsGet apiTransportTurboSmsIdPut(id, transportTurboSmsPut)

Replaces the TransportTurboSms resource.

Replaces the TransportTurboSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTurboSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTurboSmsApi apiInstance = new TransportTurboSmsApi(defaultClient);
    String id = "id_example"; // String | TransportTurboSms identifier
    TransportTurboSmsPut transportTurboSmsPut = new TransportTurboSmsPut(); // TransportTurboSmsPut | The updated TransportTurboSms resource
    try {
      TransportTurboSmsGet result = apiInstance.apiTransportTurboSmsIdPut(id, transportTurboSmsPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTurboSmsApi#apiTransportTurboSmsIdPut");
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
| **id** | **String**| TransportTurboSms identifier | |
| **transportTurboSmsPut** | [**TransportTurboSmsPut**](TransportTurboSmsPut.md)| The updated TransportTurboSms resource | |

### Return type

[**TransportTurboSmsGet**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTurboSms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTurboSmsPost"></a>
# **apiTransportTurboSmsPost**
> TransportTurboSmsGet apiTransportTurboSmsPost(transportTurboSmsPost)

Creates a TransportTurboSms resource.

Creates a TransportTurboSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTurboSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTurboSmsApi apiInstance = new TransportTurboSmsApi(defaultClient);
    TransportTurboSmsPost transportTurboSmsPost = new TransportTurboSmsPost(); // TransportTurboSmsPost | The new TransportTurboSms resource
    try {
      TransportTurboSmsGet result = apiInstance.apiTransportTurboSmsPost(transportTurboSmsPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTurboSmsApi#apiTransportTurboSmsPost");
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
| **transportTurboSmsPost** | [**TransportTurboSmsPost**](TransportTurboSmsPost.md)| The new TransportTurboSms resource | |

### Return type

[**TransportTurboSmsGet**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportTurboSms resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

