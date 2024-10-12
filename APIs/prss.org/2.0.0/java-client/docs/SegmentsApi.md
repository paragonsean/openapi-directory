# SegmentsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2SegmentsGet**](SegmentsApi.md#apiV2SegmentsGet) | **GET** /api/v2/segments | Returns the segments matching the query parameters. |
| [**apiV2SegmentsIdContentGet**](SegmentsApi.md#apiV2SegmentsIdContentGet) | **GET** /api/v2/segments/{id}/content | UNDER DEVELOPMENT - Returns the audio content segment matching the given ID. |
| [**apiV2SegmentsIdDelete**](SegmentsApi.md#apiV2SegmentsIdDelete) | **DELETE** /api/v2/segments/{id} | Deletes the segment with the given ID. |
| [**apiV2SegmentsIdGet**](SegmentsApi.md#apiV2SegmentsIdGet) | **GET** /api/v2/segments/{id} | Returns the segment matching the given ID. |
| [**apiV2SegmentsPost**](SegmentsApi.md#apiV2SegmentsPost) | **POST** /api/v2/segments | Creates a new segment. |


<a id="apiV2SegmentsGet"></a>
# **apiV2SegmentsGet**
> List&lt;Segment&gt; apiV2SegmentsGet(episodeId, segmentNumber, pageStart, pageSize, orderById)

Returns the segments matching the query parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SegmentsApi apiInstance = new SegmentsApi(defaultClient);
    Long episodeId = 56L; // Long | The ID of the episode that owns the segment.
    Integer segmentNumber = 56; // Integer | 
    Integer pageStart = 0; // Integer | The start page of the results to return. The first item is indexed at 0.
    Integer pageSize = 500; // Integer | The number of items to return. Must be between 0 and 500, inclusive.
    String orderById = "asc"; // String | The sort order of the list of segments, based on segment ID. If unspecified, the segments are returned in random order. If using paging to iterate through the results, sort order should be specified.
    try {
      List<Segment> result = apiInstance.apiV2SegmentsGet(episodeId, segmentNumber, pageStart, pageSize, orderById);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentsApi#apiV2SegmentsGet");
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
| **episodeId** | **Long**| The ID of the episode that owns the segment. | |
| **segmentNumber** | **Integer**|  | [optional] |
| **pageStart** | **Integer**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0] |
| **pageSize** | **Integer**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500] |
| **orderById** | **String**| The sort order of the list of segments, based on segment ID. If unspecified, the segments are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] [enum: asc, desc] |

### Return type

[**List&lt;Segment&gt;**](Segment.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The segments matching the query parameters |  -  |
| **403** | Authorization failed, or the user is not permitted to view this episode or its segments. |  -  |
| **404** | The episode cannot be found. |  -  |

<a id="apiV2SegmentsIdContentGet"></a>
# **apiV2SegmentsIdContentGet**
> File apiV2SegmentsIdContentGet(id)

UNDER DEVELOPMENT - Returns the audio content segment matching the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SegmentsApi apiInstance = new SegmentsApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      File result = apiInstance.apiV2SegmentsIdContentGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentsApi#apiV2SegmentsIdContentGet");
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
| **id** | **Long**|  | |

### Return type

[**File**](File.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The audio content of the requested segment. |  -  |
| **404** | The segment isn&#39;t found or the user doesn&#39;t have permission to get it. |  -  |

<a id="apiV2SegmentsIdDelete"></a>
# **apiV2SegmentsIdDelete**
> apiV2SegmentsIdDelete(id)

Deletes the segment with the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SegmentsApi apiInstance = new SegmentsApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.apiV2SegmentsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentsApi#apiV2SegmentsIdDelete");
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
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The segment was deleted. |  -  |
| **403** | Authorization failed, or the user is not permitted to delete the segment. |  -  |
| **404** | The segment or the episode that owns the segment cannot be found. |  -  |

<a id="apiV2SegmentsIdGet"></a>
# **apiV2SegmentsIdGet**
> Segment apiV2SegmentsIdGet(id)

Returns the segment matching the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SegmentsApi apiInstance = new SegmentsApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      Segment result = apiInstance.apiV2SegmentsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentsApi#apiV2SegmentsIdGet");
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
| **id** | **Long**|  | |

### Return type

[**Segment**](Segment.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The segment with the given ID. |  -  |
| **403** | Authorization failed, or the user is not permitted to view the segment. |  -  |
| **404** | The segment information cannot be found. |  -  |

<a id="apiV2SegmentsPost"></a>
# **apiV2SegmentsPost**
> Segment apiV2SegmentsPost(cdDriveUri, episodeId, segmentNumber, inCue, outCue)

Creates a new segment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SegmentsApi apiInstance = new SegmentsApi(defaultClient);
    String cdDriveUri = "cdDriveUri_example"; // String | The URI to the segment content in CD Drive. Format should be 'cddrive:id:{value}' or 'cddrive://{path}'.
    Long episodeId = 56L; // Long | The ID of the episode that owns the segment.
    Integer segmentNumber = 56; // Integer | The segment number of the segment.
    String inCue = "inCue_example"; // String | The incue for the segment. Defaults to the program segment incue.
    String outCue = "outCue_example"; // String | The outcue for the segment. Defaults to the program segment outcue.
    try {
      Segment result = apiInstance.apiV2SegmentsPost(cdDriveUri, episodeId, segmentNumber, inCue, outCue);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentsApi#apiV2SegmentsPost");
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
| **cdDriveUri** | **String**| The URI to the segment content in CD Drive. Format should be &#39;cddrive:id:{value}&#39; or &#39;cddrive://{path}&#39;. | |
| **episodeId** | **Long**| The ID of the episode that owns the segment. | |
| **segmentNumber** | **Integer**| The segment number of the segment. | |
| **inCue** | **String**| The incue for the segment. Defaults to the program segment incue. | [optional] |
| **outCue** | **String**| The outcue for the segment. Defaults to the program segment outcue. | [optional] |

### Return type

[**Segment**](Segment.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created segment with fields populated. |  -  |
| **400** | The request is missing required data or invalid. |  -  |
| **403** | Authorization failed, or the user is not permitted to create the segment. |  -  |
| **404** | The information for creating the segment cannot be found. |  -  |

