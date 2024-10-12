# TransportSmsFactorApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSmsFactorGetCollection**](TransportSmsFactorApi.md#apiTransportSmsFactorGetCollection) | **GET** /api/transport-sms-factor | Retrieves the collection of TransportSmsFactor resources. |
| [**apiTransportSmsFactorIdDelete**](TransportSmsFactorApi.md#apiTransportSmsFactorIdDelete) | **DELETE** /api/transport-sms-factor/{id} | Removes the TransportSmsFactor resource. |
| [**apiTransportSmsFactorIdGet**](TransportSmsFactorApi.md#apiTransportSmsFactorIdGet) | **GET** /api/transport-sms-factor/{id} | Retrieves a TransportSmsFactor resource. |
| [**apiTransportSmsFactorIdPatch**](TransportSmsFactorApi.md#apiTransportSmsFactorIdPatch) | **PATCH** /api/transport-sms-factor/{id} | Updates the TransportSmsFactor resource. |
| [**apiTransportSmsFactorIdPut**](TransportSmsFactorApi.md#apiTransportSmsFactorIdPut) | **PUT** /api/transport-sms-factor/{id} | Replaces the TransportSmsFactor resource. |
| [**apiTransportSmsFactorPost**](TransportSmsFactorApi.md#apiTransportSmsFactorPost) | **POST** /api/transport-sms-factor | Creates a TransportSmsFactor resource. |


<a id="apiTransportSmsFactorGetCollection"></a>
# **apiTransportSmsFactorGetCollection**
> List&lt;TransportSmsFactorGet&gt; apiTransportSmsFactorGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSmsFactor resources.

Retrieves the collection of TransportSmsFactor resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsFactorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsFactorApi apiInstance = new TransportSmsFactorApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSmsFactorGet> result = apiInstance.apiTransportSmsFactorGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsFactorApi#apiTransportSmsFactorGetCollection");
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

[**List&lt;TransportSmsFactorGet&gt;**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsFactor collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsFactorIdDelete"></a>
# **apiTransportSmsFactorIdDelete**
> apiTransportSmsFactorIdDelete(id)

Removes the TransportSmsFactor resource.

Removes the TransportSmsFactor resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsFactorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsFactorApi apiInstance = new TransportSmsFactorApi(defaultClient);
    String id = "id_example"; // String | TransportSmsFactor identifier
    try {
      apiInstance.apiTransportSmsFactorIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsFactorApi#apiTransportSmsFactorIdDelete");
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
| **id** | **String**| TransportSmsFactor identifier | |

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
| **204** | TransportSmsFactor resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsFactorIdGet"></a>
# **apiTransportSmsFactorIdGet**
> TransportSmsFactorGet apiTransportSmsFactorIdGet(id)

Retrieves a TransportSmsFactor resource.

Retrieves a TransportSmsFactor resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsFactorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsFactorApi apiInstance = new TransportSmsFactorApi(defaultClient);
    String id = "id_example"; // String | TransportSmsFactor identifier
    try {
      TransportSmsFactorGet result = apiInstance.apiTransportSmsFactorIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsFactorApi#apiTransportSmsFactorIdGet");
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
| **id** | **String**| TransportSmsFactor identifier | |

### Return type

[**TransportSmsFactorGet**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsFactor resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsFactorIdPatch"></a>
# **apiTransportSmsFactorIdPatch**
> TransportSmsFactorGet apiTransportSmsFactorIdPatch(id, transportSmsFactorPatch)

Updates the TransportSmsFactor resource.

Updates the TransportSmsFactor resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsFactorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsFactorApi apiInstance = new TransportSmsFactorApi(defaultClient);
    String id = "id_example"; // String | TransportSmsFactor identifier
    TransportSmsFactorPatch transportSmsFactorPatch = new TransportSmsFactorPatch(); // TransportSmsFactorPatch | The updated TransportSmsFactor resource
    try {
      TransportSmsFactorGet result = apiInstance.apiTransportSmsFactorIdPatch(id, transportSmsFactorPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsFactorApi#apiTransportSmsFactorIdPatch");
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
| **id** | **String**| TransportSmsFactor identifier | |
| **transportSmsFactorPatch** | [**TransportSmsFactorPatch**](TransportSmsFactorPatch.md)| The updated TransportSmsFactor resource | |

### Return type

[**TransportSmsFactorGet**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsFactor resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsFactorIdPut"></a>
# **apiTransportSmsFactorIdPut**
> TransportSmsFactorGet apiTransportSmsFactorIdPut(id, transportSmsFactorPut)

Replaces the TransportSmsFactor resource.

Replaces the TransportSmsFactor resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsFactorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsFactorApi apiInstance = new TransportSmsFactorApi(defaultClient);
    String id = "id_example"; // String | TransportSmsFactor identifier
    TransportSmsFactorPut transportSmsFactorPut = new TransportSmsFactorPut(); // TransportSmsFactorPut | The updated TransportSmsFactor resource
    try {
      TransportSmsFactorGet result = apiInstance.apiTransportSmsFactorIdPut(id, transportSmsFactorPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsFactorApi#apiTransportSmsFactorIdPut");
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
| **id** | **String**| TransportSmsFactor identifier | |
| **transportSmsFactorPut** | [**TransportSmsFactorPut**](TransportSmsFactorPut.md)| The updated TransportSmsFactor resource | |

### Return type

[**TransportSmsFactorGet**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsFactor resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmsFactorPost"></a>
# **apiTransportSmsFactorPost**
> TransportSmsFactorGet apiTransportSmsFactorPost(transportSmsFactorPost)

Creates a TransportSmsFactor resource.

Creates a TransportSmsFactor resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmsFactorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmsFactorApi apiInstance = new TransportSmsFactorApi(defaultClient);
    TransportSmsFactorPost transportSmsFactorPost = new TransportSmsFactorPost(); // TransportSmsFactorPost | The new TransportSmsFactor resource
    try {
      TransportSmsFactorGet result = apiInstance.apiTransportSmsFactorPost(transportSmsFactorPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmsFactorApi#apiTransportSmsFactorPost");
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
| **transportSmsFactorPost** | [**TransportSmsFactorPost**](TransportSmsFactorPost.md)| The new TransportSmsFactor resource | |

### Return type

[**TransportSmsFactorGet**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSmsFactor resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

