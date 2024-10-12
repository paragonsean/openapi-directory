# TransportLightSmsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportLightSmsGetCollection**](TransportLightSmsApi.md#apiTransportLightSmsGetCollection) | **GET** /api/transport-light-sms | Retrieves the collection of TransportLightSms resources. |
| [**apiTransportLightSmsIdDelete**](TransportLightSmsApi.md#apiTransportLightSmsIdDelete) | **DELETE** /api/transport-light-sms/{id} | Removes the TransportLightSms resource. |
| [**apiTransportLightSmsIdGet**](TransportLightSmsApi.md#apiTransportLightSmsIdGet) | **GET** /api/transport-light-sms/{id} | Retrieves a TransportLightSms resource. |
| [**apiTransportLightSmsIdPatch**](TransportLightSmsApi.md#apiTransportLightSmsIdPatch) | **PATCH** /api/transport-light-sms/{id} | Updates the TransportLightSms resource. |
| [**apiTransportLightSmsIdPut**](TransportLightSmsApi.md#apiTransportLightSmsIdPut) | **PUT** /api/transport-light-sms/{id} | Replaces the TransportLightSms resource. |
| [**apiTransportLightSmsPost**](TransportLightSmsApi.md#apiTransportLightSmsPost) | **POST** /api/transport-light-sms | Creates a TransportLightSms resource. |


<a id="apiTransportLightSmsGetCollection"></a>
# **apiTransportLightSmsGetCollection**
> List&lt;TransportLightSmsGet&gt; apiTransportLightSmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportLightSms resources.

Retrieves the collection of TransportLightSms resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLightSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLightSmsApi apiInstance = new TransportLightSmsApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportLightSmsGet> result = apiInstance.apiTransportLightSmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLightSmsApi#apiTransportLightSmsGetCollection");
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

[**List&lt;TransportLightSmsGet&gt;**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLightSms collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLightSmsIdDelete"></a>
# **apiTransportLightSmsIdDelete**
> apiTransportLightSmsIdDelete(id)

Removes the TransportLightSms resource.

Removes the TransportLightSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLightSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLightSmsApi apiInstance = new TransportLightSmsApi(defaultClient);
    String id = "id_example"; // String | TransportLightSms identifier
    try {
      apiInstance.apiTransportLightSmsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLightSmsApi#apiTransportLightSmsIdDelete");
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
| **id** | **String**| TransportLightSms identifier | |

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
| **204** | TransportLightSms resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLightSmsIdGet"></a>
# **apiTransportLightSmsIdGet**
> TransportLightSmsGet apiTransportLightSmsIdGet(id)

Retrieves a TransportLightSms resource.

Retrieves a TransportLightSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLightSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLightSmsApi apiInstance = new TransportLightSmsApi(defaultClient);
    String id = "id_example"; // String | TransportLightSms identifier
    try {
      TransportLightSmsGet result = apiInstance.apiTransportLightSmsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLightSmsApi#apiTransportLightSmsIdGet");
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
| **id** | **String**| TransportLightSms identifier | |

### Return type

[**TransportLightSmsGet**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLightSms resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLightSmsIdPatch"></a>
# **apiTransportLightSmsIdPatch**
> TransportLightSmsGet apiTransportLightSmsIdPatch(id, transportLightSmsPatch)

Updates the TransportLightSms resource.

Updates the TransportLightSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLightSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLightSmsApi apiInstance = new TransportLightSmsApi(defaultClient);
    String id = "id_example"; // String | TransportLightSms identifier
    TransportLightSmsPatch transportLightSmsPatch = new TransportLightSmsPatch(); // TransportLightSmsPatch | The updated TransportLightSms resource
    try {
      TransportLightSmsGet result = apiInstance.apiTransportLightSmsIdPatch(id, transportLightSmsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLightSmsApi#apiTransportLightSmsIdPatch");
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
| **id** | **String**| TransportLightSms identifier | |
| **transportLightSmsPatch** | [**TransportLightSmsPatch**](TransportLightSmsPatch.md)| The updated TransportLightSms resource | |

### Return type

[**TransportLightSmsGet**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLightSms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLightSmsIdPut"></a>
# **apiTransportLightSmsIdPut**
> TransportLightSmsGet apiTransportLightSmsIdPut(id, transportLightSmsPut)

Replaces the TransportLightSms resource.

Replaces the TransportLightSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLightSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLightSmsApi apiInstance = new TransportLightSmsApi(defaultClient);
    String id = "id_example"; // String | TransportLightSms identifier
    TransportLightSmsPut transportLightSmsPut = new TransportLightSmsPut(); // TransportLightSmsPut | The updated TransportLightSms resource
    try {
      TransportLightSmsGet result = apiInstance.apiTransportLightSmsIdPut(id, transportLightSmsPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLightSmsApi#apiTransportLightSmsIdPut");
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
| **id** | **String**| TransportLightSms identifier | |
| **transportLightSmsPut** | [**TransportLightSmsPut**](TransportLightSmsPut.md)| The updated TransportLightSms resource | |

### Return type

[**TransportLightSmsGet**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLightSms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLightSmsPost"></a>
# **apiTransportLightSmsPost**
> TransportLightSmsGet apiTransportLightSmsPost(transportLightSmsPost)

Creates a TransportLightSms resource.

Creates a TransportLightSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLightSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLightSmsApi apiInstance = new TransportLightSmsApi(defaultClient);
    TransportLightSmsPost transportLightSmsPost = new TransportLightSmsPost(); // TransportLightSmsPost | The new TransportLightSms resource
    try {
      TransportLightSmsGet result = apiInstance.apiTransportLightSmsPost(transportLightSmsPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLightSmsApi#apiTransportLightSmsPost");
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
| **transportLightSmsPost** | [**TransportLightSmsPost**](TransportLightSmsPost.md)| The new TransportLightSms resource | |

### Return type

[**TransportLightSmsGet**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportLightSms resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

