# TransportPagerDutyApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportPagerDutyGetCollection**](TransportPagerDutyApi.md#apiTransportPagerDutyGetCollection) | **GET** /api/transport-pager-duty | Retrieves the collection of TransportPagerDuty resources. |
| [**apiTransportPagerDutyIdDelete**](TransportPagerDutyApi.md#apiTransportPagerDutyIdDelete) | **DELETE** /api/transport-pager-duty/{id} | Removes the TransportPagerDuty resource. |
| [**apiTransportPagerDutyIdGet**](TransportPagerDutyApi.md#apiTransportPagerDutyIdGet) | **GET** /api/transport-pager-duty/{id} | Retrieves a TransportPagerDuty resource. |
| [**apiTransportPagerDutyIdPatch**](TransportPagerDutyApi.md#apiTransportPagerDutyIdPatch) | **PATCH** /api/transport-pager-duty/{id} | Updates the TransportPagerDuty resource. |
| [**apiTransportPagerDutyIdPut**](TransportPagerDutyApi.md#apiTransportPagerDutyIdPut) | **PUT** /api/transport-pager-duty/{id} | Replaces the TransportPagerDuty resource. |
| [**apiTransportPagerDutyPost**](TransportPagerDutyApi.md#apiTransportPagerDutyPost) | **POST** /api/transport-pager-duty | Creates a TransportPagerDuty resource. |


<a id="apiTransportPagerDutyGetCollection"></a>
# **apiTransportPagerDutyGetCollection**
> List&lt;TransportPagerDutyGet&gt; apiTransportPagerDutyGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportPagerDuty resources.

Retrieves the collection of TransportPagerDuty resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerDutyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerDutyApi apiInstance = new TransportPagerDutyApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportPagerDutyGet> result = apiInstance.apiTransportPagerDutyGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerDutyApi#apiTransportPagerDutyGetCollection");
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

[**List&lt;TransportPagerDutyGet&gt;**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPagerDuty collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerDutyIdDelete"></a>
# **apiTransportPagerDutyIdDelete**
> apiTransportPagerDutyIdDelete(id)

Removes the TransportPagerDuty resource.

Removes the TransportPagerDuty resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerDutyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerDutyApi apiInstance = new TransportPagerDutyApi(defaultClient);
    String id = "id_example"; // String | TransportPagerDuty identifier
    try {
      apiInstance.apiTransportPagerDutyIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerDutyApi#apiTransportPagerDutyIdDelete");
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
| **id** | **String**| TransportPagerDuty identifier | |

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
| **204** | TransportPagerDuty resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerDutyIdGet"></a>
# **apiTransportPagerDutyIdGet**
> TransportPagerDutyGet apiTransportPagerDutyIdGet(id)

Retrieves a TransportPagerDuty resource.

Retrieves a TransportPagerDuty resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerDutyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerDutyApi apiInstance = new TransportPagerDutyApi(defaultClient);
    String id = "id_example"; // String | TransportPagerDuty identifier
    try {
      TransportPagerDutyGet result = apiInstance.apiTransportPagerDutyIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerDutyApi#apiTransportPagerDutyIdGet");
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
| **id** | **String**| TransportPagerDuty identifier | |

### Return type

[**TransportPagerDutyGet**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPagerDuty resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerDutyIdPatch"></a>
# **apiTransportPagerDutyIdPatch**
> TransportPagerDutyGet apiTransportPagerDutyIdPatch(id, transportPagerDutyPatch)

Updates the TransportPagerDuty resource.

Updates the TransportPagerDuty resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerDutyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerDutyApi apiInstance = new TransportPagerDutyApi(defaultClient);
    String id = "id_example"; // String | TransportPagerDuty identifier
    TransportPagerDutyPatch transportPagerDutyPatch = new TransportPagerDutyPatch(); // TransportPagerDutyPatch | The updated TransportPagerDuty resource
    try {
      TransportPagerDutyGet result = apiInstance.apiTransportPagerDutyIdPatch(id, transportPagerDutyPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerDutyApi#apiTransportPagerDutyIdPatch");
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
| **id** | **String**| TransportPagerDuty identifier | |
| **transportPagerDutyPatch** | [**TransportPagerDutyPatch**](TransportPagerDutyPatch.md)| The updated TransportPagerDuty resource | |

### Return type

[**TransportPagerDutyGet**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPagerDuty resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerDutyIdPut"></a>
# **apiTransportPagerDutyIdPut**
> TransportPagerDutyGet apiTransportPagerDutyIdPut(id, transportPagerDutyPut)

Replaces the TransportPagerDuty resource.

Replaces the TransportPagerDuty resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerDutyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerDutyApi apiInstance = new TransportPagerDutyApi(defaultClient);
    String id = "id_example"; // String | TransportPagerDuty identifier
    TransportPagerDutyPut transportPagerDutyPut = new TransportPagerDutyPut(); // TransportPagerDutyPut | The updated TransportPagerDuty resource
    try {
      TransportPagerDutyGet result = apiInstance.apiTransportPagerDutyIdPut(id, transportPagerDutyPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerDutyApi#apiTransportPagerDutyIdPut");
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
| **id** | **String**| TransportPagerDuty identifier | |
| **transportPagerDutyPut** | [**TransportPagerDutyPut**](TransportPagerDutyPut.md)| The updated TransportPagerDuty resource | |

### Return type

[**TransportPagerDutyGet**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPagerDuty resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerDutyPost"></a>
# **apiTransportPagerDutyPost**
> TransportPagerDutyGet apiTransportPagerDutyPost(transportPagerDutyPost)

Creates a TransportPagerDuty resource.

Creates a TransportPagerDuty resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerDutyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerDutyApi apiInstance = new TransportPagerDutyApi(defaultClient);
    TransportPagerDutyPost transportPagerDutyPost = new TransportPagerDutyPost(); // TransportPagerDutyPost | The new TransportPagerDuty resource
    try {
      TransportPagerDutyGet result = apiInstance.apiTransportPagerDutyPost(transportPagerDutyPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerDutyApi#apiTransportPagerDutyPost");
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
| **transportPagerDutyPost** | [**TransportPagerDutyPost**](TransportPagerDutyPost.md)| The new TransportPagerDuty resource | |

### Return type

[**TransportPagerDutyGet**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportPagerDuty resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

