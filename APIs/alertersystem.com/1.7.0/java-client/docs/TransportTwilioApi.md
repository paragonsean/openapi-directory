# TransportTwilioApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportTwilioGetCollection**](TransportTwilioApi.md#apiTransportTwilioGetCollection) | **GET** /api/transport-twilio | Retrieves the collection of TransportTwilio resources. |
| [**apiTransportTwilioIdDelete**](TransportTwilioApi.md#apiTransportTwilioIdDelete) | **DELETE** /api/transport-twilio/{id} | Removes the TransportTwilio resource. |
| [**apiTransportTwilioIdGet**](TransportTwilioApi.md#apiTransportTwilioIdGet) | **GET** /api/transport-twilio/{id} | Retrieves a TransportTwilio resource. |
| [**apiTransportTwilioIdPatch**](TransportTwilioApi.md#apiTransportTwilioIdPatch) | **PATCH** /api/transport-twilio/{id} | Updates the TransportTwilio resource. |
| [**apiTransportTwilioIdPut**](TransportTwilioApi.md#apiTransportTwilioIdPut) | **PUT** /api/transport-twilio/{id} | Replaces the TransportTwilio resource. |
| [**apiTransportTwilioPost**](TransportTwilioApi.md#apiTransportTwilioPost) | **POST** /api/transport-twilio | Creates a TransportTwilio resource. |


<a id="apiTransportTwilioGetCollection"></a>
# **apiTransportTwilioGetCollection**
> List&lt;TransportTwilioGet&gt; apiTransportTwilioGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportTwilio resources.

Retrieves the collection of TransportTwilio resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwilioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwilioApi apiInstance = new TransportTwilioApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportTwilioGet> result = apiInstance.apiTransportTwilioGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwilioApi#apiTransportTwilioGetCollection");
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

[**List&lt;TransportTwilioGet&gt;**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTwilio collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwilioIdDelete"></a>
# **apiTransportTwilioIdDelete**
> apiTransportTwilioIdDelete(id)

Removes the TransportTwilio resource.

Removes the TransportTwilio resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwilioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwilioApi apiInstance = new TransportTwilioApi(defaultClient);
    String id = "id_example"; // String | TransportTwilio identifier
    try {
      apiInstance.apiTransportTwilioIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwilioApi#apiTransportTwilioIdDelete");
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
| **id** | **String**| TransportTwilio identifier | |

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
| **204** | TransportTwilio resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwilioIdGet"></a>
# **apiTransportTwilioIdGet**
> TransportTwilioGet apiTransportTwilioIdGet(id)

Retrieves a TransportTwilio resource.

Retrieves a TransportTwilio resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwilioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwilioApi apiInstance = new TransportTwilioApi(defaultClient);
    String id = "id_example"; // String | TransportTwilio identifier
    try {
      TransportTwilioGet result = apiInstance.apiTransportTwilioIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwilioApi#apiTransportTwilioIdGet");
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
| **id** | **String**| TransportTwilio identifier | |

### Return type

[**TransportTwilioGet**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTwilio resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwilioIdPatch"></a>
# **apiTransportTwilioIdPatch**
> TransportTwilioGet apiTransportTwilioIdPatch(id, transportTwilioPatch)

Updates the TransportTwilio resource.

Updates the TransportTwilio resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwilioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwilioApi apiInstance = new TransportTwilioApi(defaultClient);
    String id = "id_example"; // String | TransportTwilio identifier
    TransportTwilioPatch transportTwilioPatch = new TransportTwilioPatch(); // TransportTwilioPatch | The updated TransportTwilio resource
    try {
      TransportTwilioGet result = apiInstance.apiTransportTwilioIdPatch(id, transportTwilioPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwilioApi#apiTransportTwilioIdPatch");
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
| **id** | **String**| TransportTwilio identifier | |
| **transportTwilioPatch** | [**TransportTwilioPatch**](TransportTwilioPatch.md)| The updated TransportTwilio resource | |

### Return type

[**TransportTwilioGet**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTwilio resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwilioIdPut"></a>
# **apiTransportTwilioIdPut**
> TransportTwilioGet apiTransportTwilioIdPut(id, transportTwilioPut)

Replaces the TransportTwilio resource.

Replaces the TransportTwilio resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwilioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwilioApi apiInstance = new TransportTwilioApi(defaultClient);
    String id = "id_example"; // String | TransportTwilio identifier
    TransportTwilioPut transportTwilioPut = new TransportTwilioPut(); // TransportTwilioPut | The updated TransportTwilio resource
    try {
      TransportTwilioGet result = apiInstance.apiTransportTwilioIdPut(id, transportTwilioPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwilioApi#apiTransportTwilioIdPut");
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
| **id** | **String**| TransportTwilio identifier | |
| **transportTwilioPut** | [**TransportTwilioPut**](TransportTwilioPut.md)| The updated TransportTwilio resource | |

### Return type

[**TransportTwilioGet**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTwilio resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTwilioPost"></a>
# **apiTransportTwilioPost**
> TransportTwilioGet apiTransportTwilioPost(transportTwilioPost)

Creates a TransportTwilio resource.

Creates a TransportTwilio resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTwilioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTwilioApi apiInstance = new TransportTwilioApi(defaultClient);
    TransportTwilioPost transportTwilioPost = new TransportTwilioPost(); // TransportTwilioPost | The new TransportTwilio resource
    try {
      TransportTwilioGet result = apiInstance.apiTransportTwilioPost(transportTwilioPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTwilioApi#apiTransportTwilioPost");
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
| **transportTwilioPost** | [**TransportTwilioPost**](TransportTwilioPost.md)| The new TransportTwilio resource | |

### Return type

[**TransportTwilioGet**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportTwilio resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

