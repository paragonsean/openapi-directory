# PartitionApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPartitionGetCollection**](PartitionApi.md#apiPartitionGetCollection) | **GET** /api/partition | Retrieves the collection of Partition resources. |
| [**apiPartitionIdDelete**](PartitionApi.md#apiPartitionIdDelete) | **DELETE** /api/partition/{id} | Removes the Partition resource. |
| [**apiPartitionIdGet**](PartitionApi.md#apiPartitionIdGet) | **GET** /api/partition/{id} | Retrieves a Partition resource. |
| [**apiPartitionIdPatch**](PartitionApi.md#apiPartitionIdPatch) | **PATCH** /api/partition/{id} | Updates the Partition resource. |
| [**apiPartitionIdPut**](PartitionApi.md#apiPartitionIdPut) | **PUT** /api/partition/{id} | Replaces the Partition resource. |
| [**apiPartitionPost**](PartitionApi.md#apiPartitionPost) | **POST** /api/partition | Creates a Partition resource. |


<a id="apiPartitionGetCollection"></a>
# **apiPartitionGetCollection**
> List&lt;PartitionGet&gt; apiPartitionGetCollection(page, dataSegmentCode, dataSegmentCode2, properties)

Retrieves the collection of Partition resources.

Retrieves the collection of Partition resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PartitionApi apiInstance = new PartitionApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<PartitionGet> result = apiInstance.apiPartitionGetCollection(page, dataSegmentCode, dataSegmentCode2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartitionApi#apiPartitionGetCollection");
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
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;PartitionGet&gt;**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Partition collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiPartitionIdDelete"></a>
# **apiPartitionIdDelete**
> apiPartitionIdDelete(id)

Removes the Partition resource.

Removes the Partition resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PartitionApi apiInstance = new PartitionApi(defaultClient);
    String id = "id_example"; // String | Partition identifier
    try {
      apiInstance.apiPartitionIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartitionApi#apiPartitionIdDelete");
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
| **id** | **String**| Partition identifier | |

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
| **204** | Partition resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiPartitionIdGet"></a>
# **apiPartitionIdGet**
> PartitionGet apiPartitionIdGet(id)

Retrieves a Partition resource.

Retrieves a Partition resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PartitionApi apiInstance = new PartitionApi(defaultClient);
    String id = "id_example"; // String | Partition identifier
    try {
      PartitionGet result = apiInstance.apiPartitionIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartitionApi#apiPartitionIdGet");
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
| **id** | **String**| Partition identifier | |

### Return type

[**PartitionGet**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Partition resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiPartitionIdPatch"></a>
# **apiPartitionIdPatch**
> PartitionGet apiPartitionIdPatch(id, partitionPatch)

Updates the Partition resource.

Updates the Partition resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PartitionApi apiInstance = new PartitionApi(defaultClient);
    String id = "id_example"; // String | Partition identifier
    PartitionPatch partitionPatch = new PartitionPatch(); // PartitionPatch | The updated Partition resource
    try {
      PartitionGet result = apiInstance.apiPartitionIdPatch(id, partitionPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartitionApi#apiPartitionIdPatch");
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
| **id** | **String**| Partition identifier | |
| **partitionPatch** | [**PartitionPatch**](PartitionPatch.md)| The updated Partition resource | |

### Return type

[**PartitionGet**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Partition resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiPartitionIdPut"></a>
# **apiPartitionIdPut**
> PartitionGet apiPartitionIdPut(id, partitionPut)

Replaces the Partition resource.

Replaces the Partition resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PartitionApi apiInstance = new PartitionApi(defaultClient);
    String id = "id_example"; // String | Partition identifier
    PartitionPut partitionPut = new PartitionPut(); // PartitionPut | The updated Partition resource
    try {
      PartitionGet result = apiInstance.apiPartitionIdPut(id, partitionPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartitionApi#apiPartitionIdPut");
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
| **id** | **String**| Partition identifier | |
| **partitionPut** | [**PartitionPut**](PartitionPut.md)| The updated Partition resource | |

### Return type

[**PartitionGet**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Partition resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiPartitionPost"></a>
# **apiPartitionPost**
> PartitionGet apiPartitionPost(partitionPost)

Creates a Partition resource.

Creates a Partition resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PartitionApi apiInstance = new PartitionApi(defaultClient);
    PartitionPost partitionPost = new PartitionPost(); // PartitionPost | The new Partition resource
    try {
      PartitionGet result = apiInstance.apiPartitionPost(partitionPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartitionApi#apiPartitionPost");
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
| **partitionPost** | [**PartitionPost**](PartitionPost.md)| The new Partition resource | |

### Return type

[**PartitionGet**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Partition resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

