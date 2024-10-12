# LiveApi

All URIs are relative to *https://ws.api.video*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dELETELiveStreamsLiveStreamId**](LiveApi.md#dELETELiveStreamsLiveStreamId) | **DELETE** /live-streams/{liveStreamId} | Delete a live stream |
| [**dELETELiveStreamsLiveStreamIdThumbnail**](LiveApi.md#dELETELiveStreamsLiveStreamIdThumbnail) | **DELETE** /live-streams/{liveStreamId}/thumbnail | Delete a thumbnail |
| [**gETLiveStreams**](LiveApi.md#gETLiveStreams) | **GET** /live-streams | List all live streams |
| [**gETLiveStreamsLiveStreamId**](LiveApi.md#gETLiveStreamsLiveStreamId) | **GET** /live-streams/{liveStreamId} | Show live stream |
| [**pATCHLiveStreamsLiveStreamId**](LiveApi.md#pATCHLiveStreamsLiveStreamId) | **PATCH** /live-streams/{liveStreamId} | Update a live stream |
| [**pOSTLiveStreams**](LiveApi.md#pOSTLiveStreams) | **POST** /live-streams | Create live stream |
| [**pOSTLiveStreamsLiveStreamIdThumbnail**](LiveApi.md#pOSTLiveStreamsLiveStreamIdThumbnail) | **POST** /live-streams/{liveStreamId}/thumbnail | Upload a thumbnail |


<a id="dELETELiveStreamsLiveStreamId"></a>
# **dELETELiveStreamsLiveStreamId**
> dELETELiveStreamsLiveStreamId(liveStreamId)

Delete a live stream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LiveApi apiInstance = new LiveApi(defaultClient);
    String liveStreamId = "li400mYKSgQ6xs7taUeSaEKr"; // String | The unique ID for the live stream that you want to remove.
    try {
      apiInstance.dELETELiveStreamsLiveStreamId(liveStreamId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveApi#dELETELiveStreamsLiveStreamId");
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
| **liveStreamId** | **String**| The unique ID for the live stream that you want to remove. | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="dELETELiveStreamsLiveStreamIdThumbnail"></a>
# **dELETELiveStreamsLiveStreamIdThumbnail**
> LiveStream dELETELiveStreamsLiveStreamIdThumbnail(liveStreamId)

Delete a thumbnail

Send the unique identifier for a live stream to delete it from the system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LiveApi apiInstance = new LiveApi(defaultClient);
    String liveStreamId = "li400mYKSgQ6xs7taUeSaEKr"; // String | The unique identifier for the live stream you want to delete. 
    try {
      LiveStream result = apiInstance.dELETELiveStreamsLiveStreamIdThumbnail(liveStreamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveApi#dELETELiveStreamsLiveStreamIdThumbnail");
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
| **liveStreamId** | **String**| The unique identifier for the live stream you want to delete.  | |

### Return type

[**LiveStream**](LiveStream.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="gETLiveStreams"></a>
# **gETLiveStreams**
> LiveStreamListResponse gETLiveStreams().streamKey(streamKey).name(name).sortBy(sortBy).sortOrder(sortOrder).currentPage(currentPage).pageSize(pageSize).execute();

List all live streams

With no parameters added to the url, this will return all livestreams. Query by name or key to limit the list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LiveApi apiInstance = new LiveApi(defaultClient);
    String streamKey = "30087931-229e-42cf-b5f9-e91bcc1f7332"; // String | The unique stream key that allows you to stream videos.
    String name = "My Video"; // String | You can filter live streams by their name or a part of their name.
    String sortBy = "createdAt"; // String | Allowed: createdAt, publishedAt, name. createdAt - the time a livestream was created using the specified streamKey. publishedAt - the time a livestream was published using the specified streamKey. name - the name of the livestream. If you choose one of the time based options, the time is presented in ISO-8601 format.
    String sortOrder = "asc"; // String | Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. For title, it is 0-9 and A-Z ascending and Z-A, 9-0 descending.
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      LiveStreamListResponse result = apiInstance.gETLiveStreams()
            .streamKey(streamKey)
            .name(name)
            .sortBy(sortBy)
            .sortOrder(sortOrder)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveApi#gETLiveStreams");
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
| **streamKey** | **String**| The unique stream key that allows you to stream videos. | [optional] |
| **name** | **String**| You can filter live streams by their name or a part of their name. | [optional] |
| **sortBy** | **String**| Allowed: createdAt, publishedAt, name. createdAt - the time a livestream was created using the specified streamKey. publishedAt - the time a livestream was published using the specified streamKey. name - the name of the livestream. If you choose one of the time based options, the time is presented in ISO-8601 format. | [optional] |
| **sortOrder** | **String**| Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. For title, it is 0-9 and A-Z ascending and Z-A, 9-0 descending. | [optional] [enum: asc, desc] |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**LiveStreamListResponse**](LiveStreamListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="gETLiveStreamsLiveStreamId"></a>
# **gETLiveStreamsLiveStreamId**
> LiveStream gETLiveStreamsLiveStreamId(liveStreamId)

Show live stream

Supply a LivestreamId, and you&#39;ll get all the details for streaming into, and watching the livestream. Tutorials that use the [show livestream endpoint](https://api.video/blog/endpoints/live-stream-status).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LiveApi apiInstance = new LiveApi(defaultClient);
    String liveStreamId = "li400mYKSgQ6xs7taUeSaEKr"; // String | The unique ID for the live stream you want to watch.
    try {
      LiveStream result = apiInstance.gETLiveStreamsLiveStreamId(liveStreamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveApi#gETLiveStreamsLiveStreamId");
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
| **liveStreamId** | **String**| The unique ID for the live stream you want to watch. | |

### Return type

[**LiveStream**](LiveStream.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="pATCHLiveStreamsLiveStreamId"></a>
# **pATCHLiveStreamsLiveStreamId**
> LiveStream pATCHLiveStreamsLiveStreamId(liveStreamId, liveStreamUpdatePayload)

Update a live stream

Use this endpoint to update the player, or to turn recording on/off (saving a copy of the livestream). NOTE: If the livestream is actively streaming, changing the recording status will only affect the NEXT stream.    The public&#x3D;false &#39;private livestream&#39; is available as a BETA feature, and should be limited to livestreams of 3,000 viewers or fewer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LiveApi apiInstance = new LiveApi(defaultClient);
    String liveStreamId = "li400mYKSgQ6xs7taUeSaEKr"; // String | The unique ID for the live stream that you want to update information for such as player details, or whether you want the recording on or off.
    LiveStreamUpdatePayload liveStreamUpdatePayload = new LiveStreamUpdatePayload(); // LiveStreamUpdatePayload | 
    try {
      LiveStream result = apiInstance.pATCHLiveStreamsLiveStreamId(liveStreamId, liveStreamUpdatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveApi#pATCHLiveStreamsLiveStreamId");
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
| **liveStreamId** | **String**| The unique ID for the live stream that you want to update information for such as player details, or whether you want the recording on or off. | |
| **liveStreamUpdatePayload** | [**LiveStreamUpdatePayload**](LiveStreamUpdatePayload.md)|  | [optional] |

### Return type

[**LiveStream**](LiveStream.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="pOSTLiveStreams"></a>
# **pOSTLiveStreams**
> LiveStream pOSTLiveStreams(liveStreamCreatePayload)

Create live stream

A live stream will give you the &#39;connection point&#39; to RTMP your video stream to api.video. It will also give you the details for viewers to watch the same livestream.  The public&#x3D;false &#39;private livestream&#39; is available as a BETA feature, and should be limited to livestreams of 3,000 viewers or fewer. See our [Live Stream Tutorial](https://api.video/blog/tutorials/live-stream-tutorial) for a walkthrough of this API with OBS. Your RTMP endpoint for the livestream is rtmp://broadcast.api.video/s/{streamKey} Tutorials that [create live streams](https://api.video/blog/endpoints/live-create).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LiveApi apiInstance = new LiveApi(defaultClient);
    LiveStreamCreatePayload liveStreamCreatePayload = new LiveStreamCreatePayload(); // LiveStreamCreatePayload | 
    try {
      LiveStream result = apiInstance.pOSTLiveStreams(liveStreamCreatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveApi#pOSTLiveStreams");
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
| **liveStreamCreatePayload** | [**LiveStreamCreatePayload**](LiveStreamCreatePayload.md)|  | [optional] |

### Return type

[**LiveStream**](LiveStream.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="pOSTLiveStreamsLiveStreamIdThumbnail"></a>
# **pOSTLiveStreamsLiveStreamIdThumbnail**
> LiveStream pOSTLiveStreamsLiveStreamIdThumbnail(liveStreamId, _file)

Upload a thumbnail

Upload an image to use as a backdrop for your livestream. Tutorials that [update live stream thumbnails](https://api.video/blog/endpoints/live-upload-a-thumbnail).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LiveApi apiInstance = new LiveApi(defaultClient);
    String liveStreamId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique ID for the live stream you want to upload.
    File _file = new File("/path/to/file"); // File | The image to be added as a thumbnail.
    try {
      LiveStream result = apiInstance.pOSTLiveStreamsLiveStreamIdThumbnail(liveStreamId, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveApi#pOSTLiveStreamsLiveStreamIdThumbnail");
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
| **liveStreamId** | **String**| The unique ID for the live stream you want to upload. | |
| **_file** | **File**| The image to be added as a thumbnail. | |

### Return type

[**LiveStream**](LiveStream.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

