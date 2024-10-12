# TransportOrangeSmsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportOrangeSmsGetCollection**](TransportOrangeSmsApi.md#apiTransportOrangeSmsGetCollection) | **GET** /api/transport-orange-sms | Retrieves the collection of TransportOrangeSms resources. |
| [**apiTransportOrangeSmsIdDelete**](TransportOrangeSmsApi.md#apiTransportOrangeSmsIdDelete) | **DELETE** /api/transport-orange-sms/{id} | Removes the TransportOrangeSms resource. |
| [**apiTransportOrangeSmsIdGet**](TransportOrangeSmsApi.md#apiTransportOrangeSmsIdGet) | **GET** /api/transport-orange-sms/{id} | Retrieves a TransportOrangeSms resource. |
| [**apiTransportOrangeSmsIdPatch**](TransportOrangeSmsApi.md#apiTransportOrangeSmsIdPatch) | **PATCH** /api/transport-orange-sms/{id} | Updates the TransportOrangeSms resource. |
| [**apiTransportOrangeSmsIdPut**](TransportOrangeSmsApi.md#apiTransportOrangeSmsIdPut) | **PUT** /api/transport-orange-sms/{id} | Replaces the TransportOrangeSms resource. |
| [**apiTransportOrangeSmsPost**](TransportOrangeSmsApi.md#apiTransportOrangeSmsPost) | **POST** /api/transport-orange-sms | Creates a TransportOrangeSms resource. |


<a id="apiTransportOrangeSmsGetCollection"></a>
# **apiTransportOrangeSmsGetCollection**
> List&lt;TransportOrangeSmsGet&gt; apiTransportOrangeSmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportOrangeSms resources.

Retrieves the collection of TransportOrangeSms resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOrangeSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOrangeSmsApi apiInstance = new TransportOrangeSmsApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportOrangeSmsGet> result = apiInstance.apiTransportOrangeSmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOrangeSmsApi#apiTransportOrangeSmsGetCollection");
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

[**List&lt;TransportOrangeSmsGet&gt;**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOrangeSms collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOrangeSmsIdDelete"></a>
# **apiTransportOrangeSmsIdDelete**
> apiTransportOrangeSmsIdDelete(id)

Removes the TransportOrangeSms resource.

Removes the TransportOrangeSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOrangeSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOrangeSmsApi apiInstance = new TransportOrangeSmsApi(defaultClient);
    String id = "id_example"; // String | TransportOrangeSms identifier
    try {
      apiInstance.apiTransportOrangeSmsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOrangeSmsApi#apiTransportOrangeSmsIdDelete");
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
| **id** | **String**| TransportOrangeSms identifier | |

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
| **204** | TransportOrangeSms resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOrangeSmsIdGet"></a>
# **apiTransportOrangeSmsIdGet**
> TransportOrangeSmsGet apiTransportOrangeSmsIdGet(id)

Retrieves a TransportOrangeSms resource.

Retrieves a TransportOrangeSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOrangeSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOrangeSmsApi apiInstance = new TransportOrangeSmsApi(defaultClient);
    String id = "id_example"; // String | TransportOrangeSms identifier
    try {
      TransportOrangeSmsGet result = apiInstance.apiTransportOrangeSmsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOrangeSmsApi#apiTransportOrangeSmsIdGet");
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
| **id** | **String**| TransportOrangeSms identifier | |

### Return type

[**TransportOrangeSmsGet**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOrangeSms resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOrangeSmsIdPatch"></a>
# **apiTransportOrangeSmsIdPatch**
> TransportOrangeSmsGet apiTransportOrangeSmsIdPatch(id, transportOrangeSmsPatch)

Updates the TransportOrangeSms resource.

Updates the TransportOrangeSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOrangeSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOrangeSmsApi apiInstance = new TransportOrangeSmsApi(defaultClient);
    String id = "id_example"; // String | TransportOrangeSms identifier
    TransportOrangeSmsPatch transportOrangeSmsPatch = new TransportOrangeSmsPatch(); // TransportOrangeSmsPatch | The updated TransportOrangeSms resource
    try {
      TransportOrangeSmsGet result = apiInstance.apiTransportOrangeSmsIdPatch(id, transportOrangeSmsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOrangeSmsApi#apiTransportOrangeSmsIdPatch");
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
| **id** | **String**| TransportOrangeSms identifier | |
| **transportOrangeSmsPatch** | [**TransportOrangeSmsPatch**](TransportOrangeSmsPatch.md)| The updated TransportOrangeSms resource | |

### Return type

[**TransportOrangeSmsGet**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOrangeSms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOrangeSmsIdPut"></a>
# **apiTransportOrangeSmsIdPut**
> TransportOrangeSmsGet apiTransportOrangeSmsIdPut(id, transportOrangeSmsPut)

Replaces the TransportOrangeSms resource.

Replaces the TransportOrangeSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOrangeSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOrangeSmsApi apiInstance = new TransportOrangeSmsApi(defaultClient);
    String id = "id_example"; // String | TransportOrangeSms identifier
    TransportOrangeSmsPut transportOrangeSmsPut = new TransportOrangeSmsPut(); // TransportOrangeSmsPut | The updated TransportOrangeSms resource
    try {
      TransportOrangeSmsGet result = apiInstance.apiTransportOrangeSmsIdPut(id, transportOrangeSmsPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOrangeSmsApi#apiTransportOrangeSmsIdPut");
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
| **id** | **String**| TransportOrangeSms identifier | |
| **transportOrangeSmsPut** | [**TransportOrangeSmsPut**](TransportOrangeSmsPut.md)| The updated TransportOrangeSms resource | |

### Return type

[**TransportOrangeSmsGet**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOrangeSms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOrangeSmsPost"></a>
# **apiTransportOrangeSmsPost**
> TransportOrangeSmsGet apiTransportOrangeSmsPost(transportOrangeSmsPost)

Creates a TransportOrangeSms resource.

Creates a TransportOrangeSms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOrangeSmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOrangeSmsApi apiInstance = new TransportOrangeSmsApi(defaultClient);
    TransportOrangeSmsPost transportOrangeSmsPost = new TransportOrangeSmsPost(); // TransportOrangeSmsPost | The new TransportOrangeSms resource
    try {
      TransportOrangeSmsGet result = apiInstance.apiTransportOrangeSmsPost(transportOrangeSmsPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOrangeSmsApi#apiTransportOrangeSmsPost");
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
| **transportOrangeSmsPost** | [**TransportOrangeSmsPost**](TransportOrangeSmsPost.md)| The new TransportOrangeSms resource | |

### Return type

[**TransportOrangeSmsGet**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportOrangeSms resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

