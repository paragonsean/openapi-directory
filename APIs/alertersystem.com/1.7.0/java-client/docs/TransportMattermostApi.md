# TransportMattermostApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportMattermostGetCollection**](TransportMattermostApi.md#apiTransportMattermostGetCollection) | **GET** /api/transport-mattermost | Retrieves the collection of TransportMattermost resources. |
| [**apiTransportMattermostIdDelete**](TransportMattermostApi.md#apiTransportMattermostIdDelete) | **DELETE** /api/transport-mattermost/{id} | Removes the TransportMattermost resource. |
| [**apiTransportMattermostIdGet**](TransportMattermostApi.md#apiTransportMattermostIdGet) | **GET** /api/transport-mattermost/{id} | Retrieves a TransportMattermost resource. |
| [**apiTransportMattermostIdPatch**](TransportMattermostApi.md#apiTransportMattermostIdPatch) | **PATCH** /api/transport-mattermost/{id} | Updates the TransportMattermost resource. |
| [**apiTransportMattermostIdPut**](TransportMattermostApi.md#apiTransportMattermostIdPut) | **PUT** /api/transport-mattermost/{id} | Replaces the TransportMattermost resource. |
| [**apiTransportMattermostPost**](TransportMattermostApi.md#apiTransportMattermostPost) | **POST** /api/transport-mattermost | Creates a TransportMattermost resource. |


<a id="apiTransportMattermostGetCollection"></a>
# **apiTransportMattermostGetCollection**
> List&lt;TransportMattermostGet&gt; apiTransportMattermostGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportMattermost resources.

Retrieves the collection of TransportMattermost resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMattermostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMattermostApi apiInstance = new TransportMattermostApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportMattermostGet> result = apiInstance.apiTransportMattermostGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMattermostApi#apiTransportMattermostGetCollection");
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

[**List&lt;TransportMattermostGet&gt;**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMattermost collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMattermostIdDelete"></a>
# **apiTransportMattermostIdDelete**
> apiTransportMattermostIdDelete(id)

Removes the TransportMattermost resource.

Removes the TransportMattermost resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMattermostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMattermostApi apiInstance = new TransportMattermostApi(defaultClient);
    String id = "id_example"; // String | TransportMattermost identifier
    try {
      apiInstance.apiTransportMattermostIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMattermostApi#apiTransportMattermostIdDelete");
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
| **id** | **String**| TransportMattermost identifier | |

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
| **204** | TransportMattermost resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMattermostIdGet"></a>
# **apiTransportMattermostIdGet**
> TransportMattermostGet apiTransportMattermostIdGet(id)

Retrieves a TransportMattermost resource.

Retrieves a TransportMattermost resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMattermostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMattermostApi apiInstance = new TransportMattermostApi(defaultClient);
    String id = "id_example"; // String | TransportMattermost identifier
    try {
      TransportMattermostGet result = apiInstance.apiTransportMattermostIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMattermostApi#apiTransportMattermostIdGet");
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
| **id** | **String**| TransportMattermost identifier | |

### Return type

[**TransportMattermostGet**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMattermost resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMattermostIdPatch"></a>
# **apiTransportMattermostIdPatch**
> TransportMattermostGet apiTransportMattermostIdPatch(id, transportMattermostPatch)

Updates the TransportMattermost resource.

Updates the TransportMattermost resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMattermostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMattermostApi apiInstance = new TransportMattermostApi(defaultClient);
    String id = "id_example"; // String | TransportMattermost identifier
    TransportMattermostPatch transportMattermostPatch = new TransportMattermostPatch(); // TransportMattermostPatch | The updated TransportMattermost resource
    try {
      TransportMattermostGet result = apiInstance.apiTransportMattermostIdPatch(id, transportMattermostPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMattermostApi#apiTransportMattermostIdPatch");
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
| **id** | **String**| TransportMattermost identifier | |
| **transportMattermostPatch** | [**TransportMattermostPatch**](TransportMattermostPatch.md)| The updated TransportMattermost resource | |

### Return type

[**TransportMattermostGet**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMattermost resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMattermostIdPut"></a>
# **apiTransportMattermostIdPut**
> TransportMattermostGet apiTransportMattermostIdPut(id, transportMattermostPut)

Replaces the TransportMattermost resource.

Replaces the TransportMattermost resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMattermostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMattermostApi apiInstance = new TransportMattermostApi(defaultClient);
    String id = "id_example"; // String | TransportMattermost identifier
    TransportMattermostPut transportMattermostPut = new TransportMattermostPut(); // TransportMattermostPut | The updated TransportMattermost resource
    try {
      TransportMattermostGet result = apiInstance.apiTransportMattermostIdPut(id, transportMattermostPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMattermostApi#apiTransportMattermostIdPut");
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
| **id** | **String**| TransportMattermost identifier | |
| **transportMattermostPut** | [**TransportMattermostPut**](TransportMattermostPut.md)| The updated TransportMattermost resource | |

### Return type

[**TransportMattermostGet**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMattermost resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMattermostPost"></a>
# **apiTransportMattermostPost**
> TransportMattermostGet apiTransportMattermostPost(transportMattermostPost)

Creates a TransportMattermost resource.

Creates a TransportMattermost resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMattermostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMattermostApi apiInstance = new TransportMattermostApi(defaultClient);
    TransportMattermostPost transportMattermostPost = new TransportMattermostPost(); // TransportMattermostPost | The new TransportMattermost resource
    try {
      TransportMattermostGet result = apiInstance.apiTransportMattermostPost(transportMattermostPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMattermostApi#apiTransportMattermostPost");
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
| **transportMattermostPost** | [**TransportMattermostPost**](TransportMattermostPost.md)| The new TransportMattermost resource | |

### Return type

[**TransportMattermostGet**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportMattermost resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

