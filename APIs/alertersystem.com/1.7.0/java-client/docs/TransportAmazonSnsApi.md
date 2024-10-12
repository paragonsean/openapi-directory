# TransportAmazonSnsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportAmazonSnsGetCollection**](TransportAmazonSnsApi.md#apiTransportAmazonSnsGetCollection) | **GET** /api/transport-amazon-sns | Retrieves the collection of TransportAmazonSns resources. |
| [**apiTransportAmazonSnsIdDelete**](TransportAmazonSnsApi.md#apiTransportAmazonSnsIdDelete) | **DELETE** /api/transport-amazon-sns/{id} | Removes the TransportAmazonSns resource. |
| [**apiTransportAmazonSnsIdGet**](TransportAmazonSnsApi.md#apiTransportAmazonSnsIdGet) | **GET** /api/transport-amazon-sns/{id} | Retrieves a TransportAmazonSns resource. |
| [**apiTransportAmazonSnsIdPatch**](TransportAmazonSnsApi.md#apiTransportAmazonSnsIdPatch) | **PATCH** /api/transport-amazon-sns/{id} | Updates the TransportAmazonSns resource. |
| [**apiTransportAmazonSnsIdPut**](TransportAmazonSnsApi.md#apiTransportAmazonSnsIdPut) | **PUT** /api/transport-amazon-sns/{id} | Replaces the TransportAmazonSns resource. |
| [**apiTransportAmazonSnsPost**](TransportAmazonSnsApi.md#apiTransportAmazonSnsPost) | **POST** /api/transport-amazon-sns | Creates a TransportAmazonSns resource. |


<a id="apiTransportAmazonSnsGetCollection"></a>
# **apiTransportAmazonSnsGetCollection**
> List&lt;TransportAmazonSnsGet&gt; apiTransportAmazonSnsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportAmazonSns resources.

Retrieves the collection of TransportAmazonSns resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAmazonSnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAmazonSnsApi apiInstance = new TransportAmazonSnsApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportAmazonSnsGet> result = apiInstance.apiTransportAmazonSnsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAmazonSnsApi#apiTransportAmazonSnsGetCollection");
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

[**List&lt;TransportAmazonSnsGet&gt;**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAmazonSns collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAmazonSnsIdDelete"></a>
# **apiTransportAmazonSnsIdDelete**
> apiTransportAmazonSnsIdDelete(id)

Removes the TransportAmazonSns resource.

Removes the TransportAmazonSns resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAmazonSnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAmazonSnsApi apiInstance = new TransportAmazonSnsApi(defaultClient);
    String id = "id_example"; // String | TransportAmazonSns identifier
    try {
      apiInstance.apiTransportAmazonSnsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAmazonSnsApi#apiTransportAmazonSnsIdDelete");
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
| **id** | **String**| TransportAmazonSns identifier | |

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
| **204** | TransportAmazonSns resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAmazonSnsIdGet"></a>
# **apiTransportAmazonSnsIdGet**
> TransportAmazonSnsGet apiTransportAmazonSnsIdGet(id)

Retrieves a TransportAmazonSns resource.

Retrieves a TransportAmazonSns resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAmazonSnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAmazonSnsApi apiInstance = new TransportAmazonSnsApi(defaultClient);
    String id = "id_example"; // String | TransportAmazonSns identifier
    try {
      TransportAmazonSnsGet result = apiInstance.apiTransportAmazonSnsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAmazonSnsApi#apiTransportAmazonSnsIdGet");
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
| **id** | **String**| TransportAmazonSns identifier | |

### Return type

[**TransportAmazonSnsGet**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAmazonSns resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAmazonSnsIdPatch"></a>
# **apiTransportAmazonSnsIdPatch**
> TransportAmazonSnsGet apiTransportAmazonSnsIdPatch(id, transportAmazonSnsPatch)

Updates the TransportAmazonSns resource.

Updates the TransportAmazonSns resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAmazonSnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAmazonSnsApi apiInstance = new TransportAmazonSnsApi(defaultClient);
    String id = "id_example"; // String | TransportAmazonSns identifier
    TransportAmazonSnsPatch transportAmazonSnsPatch = new TransportAmazonSnsPatch(); // TransportAmazonSnsPatch | The updated TransportAmazonSns resource
    try {
      TransportAmazonSnsGet result = apiInstance.apiTransportAmazonSnsIdPatch(id, transportAmazonSnsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAmazonSnsApi#apiTransportAmazonSnsIdPatch");
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
| **id** | **String**| TransportAmazonSns identifier | |
| **transportAmazonSnsPatch** | [**TransportAmazonSnsPatch**](TransportAmazonSnsPatch.md)| The updated TransportAmazonSns resource | |

### Return type

[**TransportAmazonSnsGet**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAmazonSns resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAmazonSnsIdPut"></a>
# **apiTransportAmazonSnsIdPut**
> TransportAmazonSnsGet apiTransportAmazonSnsIdPut(id, transportAmazonSnsPut)

Replaces the TransportAmazonSns resource.

Replaces the TransportAmazonSns resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAmazonSnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAmazonSnsApi apiInstance = new TransportAmazonSnsApi(defaultClient);
    String id = "id_example"; // String | TransportAmazonSns identifier
    TransportAmazonSnsPut transportAmazonSnsPut = new TransportAmazonSnsPut(); // TransportAmazonSnsPut | The updated TransportAmazonSns resource
    try {
      TransportAmazonSnsGet result = apiInstance.apiTransportAmazonSnsIdPut(id, transportAmazonSnsPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAmazonSnsApi#apiTransportAmazonSnsIdPut");
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
| **id** | **String**| TransportAmazonSns identifier | |
| **transportAmazonSnsPut** | [**TransportAmazonSnsPut**](TransportAmazonSnsPut.md)| The updated TransportAmazonSns resource | |

### Return type

[**TransportAmazonSnsGet**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAmazonSns resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAmazonSnsPost"></a>
# **apiTransportAmazonSnsPost**
> TransportAmazonSnsGet apiTransportAmazonSnsPost(transportAmazonSnsPost)

Creates a TransportAmazonSns resource.

Creates a TransportAmazonSns resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAmazonSnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAmazonSnsApi apiInstance = new TransportAmazonSnsApi(defaultClient);
    TransportAmazonSnsPost transportAmazonSnsPost = new TransportAmazonSnsPost(); // TransportAmazonSnsPost | The new TransportAmazonSns resource
    try {
      TransportAmazonSnsGet result = apiInstance.apiTransportAmazonSnsPost(transportAmazonSnsPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAmazonSnsApi#apiTransportAmazonSnsPost");
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
| **transportAmazonSnsPost** | [**TransportAmazonSnsPost**](TransportAmazonSnsPost.md)| The new TransportAmazonSns resource | |

### Return type

[**TransportAmazonSnsGet**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportAmazonSns resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

