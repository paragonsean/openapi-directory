# MediaObjectApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiMediaObjectGetCollection**](MediaObjectApi.md#apiMediaObjectGetCollection) | **GET** /api/media-object | Retrieves the collection of MediaObject resources. |
| [**apiMediaObjectIdDelete**](MediaObjectApi.md#apiMediaObjectIdDelete) | **DELETE** /api/media-object/{id} | Removes the MediaObject resource. |
| [**apiMediaObjectIdGet**](MediaObjectApi.md#apiMediaObjectIdGet) | **GET** /api/media-object/{id} | Retrieves a MediaObject resource. |
| [**apiMediaObjectPost**](MediaObjectApi.md#apiMediaObjectPost) | **POST** /api/media-object | Creates a MediaObject resource. |


<a id="apiMediaObjectGetCollection"></a>
# **apiMediaObjectGetCollection**
> List&lt;MediaObjectGet&gt; apiMediaObjectGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of MediaObject resources.

Retrieves the collection of MediaObject resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaObjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MediaObjectApi apiInstance = new MediaObjectApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<MediaObjectGet> result = apiInstance.apiMediaObjectGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaObjectApi#apiMediaObjectGetCollection");
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

[**List&lt;MediaObjectGet&gt;**](MediaObjectGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MediaObject collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiMediaObjectIdDelete"></a>
# **apiMediaObjectIdDelete**
> apiMediaObjectIdDelete(id)

Removes the MediaObject resource.

Removes the MediaObject resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaObjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MediaObjectApi apiInstance = new MediaObjectApi(defaultClient);
    String id = "id_example"; // String | MediaObject identifier
    try {
      apiInstance.apiMediaObjectIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaObjectApi#apiMediaObjectIdDelete");
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
| **id** | **String**| MediaObject identifier | |

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
| **204** | MediaObject resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiMediaObjectIdGet"></a>
# **apiMediaObjectIdGet**
> MediaObjectGet apiMediaObjectIdGet(id)

Retrieves a MediaObject resource.

Retrieves a MediaObject resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaObjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MediaObjectApi apiInstance = new MediaObjectApi(defaultClient);
    String id = "id_example"; // String | MediaObject identifier
    try {
      MediaObjectGet result = apiInstance.apiMediaObjectIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaObjectApi#apiMediaObjectIdGet");
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
| **id** | **String**| MediaObject identifier | |

### Return type

[**MediaObjectGet**](MediaObjectGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MediaObject resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiMediaObjectPost"></a>
# **apiMediaObjectPost**
> MediaObjectGet apiMediaObjectPost(dataSegmentCode, _file, keywords, partition)

Creates a MediaObject resource.

Creates a MediaObject resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaObjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MediaObjectApi apiInstance = new MediaObjectApi(defaultClient);
    String dataSegmentCode = "dataSegmentCode_example"; // String | User-provided string on which to segment and filter data. Max 50 characters.
    File _file = new File("/path/to/file"); // File | 
    String keywords = "keywords_example"; // String | A string of keywords that can be used to search for a resource. Max 100 characters.
    String partition = "partition_example"; // String | The unique id of the partition. Can be just the id or an IRI.
    try {
      MediaObjectGet result = apiInstance.apiMediaObjectPost(dataSegmentCode, _file, keywords, partition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaObjectApi#apiMediaObjectPost");
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
| **dataSegmentCode** | **String**| User-provided string on which to segment and filter data. Max 50 characters. | [optional] |
| **_file** | **File**|  | [optional] |
| **keywords** | **String**| A string of keywords that can be used to search for a resource. Max 100 characters. | [optional] |
| **partition** | **String**| The unique id of the partition. Can be just the id or an IRI. | [optional] |

### Return type

[**MediaObjectGet**](MediaObjectGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | MediaObject resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

