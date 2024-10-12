# StreamApi

All URIs are relative to *https://visagecloud.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addStreamUsingPOST**](StreamApi.md#addStreamUsingPOST) | **POST** /rest/v1.1/stream/stream | Create new stream with given name |
| [**cleanupStreamUsingPATCH**](StreamApi.md#cleanupStreamUsingPATCH) | **PATCH** /rest/v1.1/stream/cleanup | Cleanup frames older than specified timeframe |
| [**getFrameImageUsingGET**](StreamApi.md#getFrameImageUsingGET) | **GET** /rest/v1.1/stream/frameImage | Get individual frame image |
| [**getLastNAttedanceUsingGET**](StreamApi.md#getLastNAttedanceUsingGET) | **GET** /rest/v1.1/stream/attendance | Get last N recognized individuals from stream |
| [**getLastNFramesUsingGET**](StreamApi.md#getLastNFramesUsingGET) | **GET** /rest/v1.1/stream/frames | Get last processed N frames from stream |
| [**getStreamUsingGET**](StreamApi.md#getStreamUsingGET) | **GET** /rest/v1.1/stream/{streamId} | Get an existing stream with a given ID |
| [**removeStreamUsingDELETE**](StreamApi.md#removeStreamUsingDELETE) | **DELETE** /rest/v1.1/stream/{id} | Delete existing stream |
| [**startStreamUsingPATCH**](StreamApi.md#startStreamUsingPATCH) | **PATCH** /rest/v1.1/stream/start | Start existing stream |
| [**stopStreamUsingPATCH**](StreamApi.md#stopStreamUsingPATCH) | **PATCH** /rest/v1.1/stream/stop | Stop existing stream |
| [**streamsByAccountUsingGET**](StreamApi.md#streamsByAccountUsingGET) | **GET** /rest/v1.1/stream/all | Show status of all streams from account |
| [**updateStreamUsingPATCH**](StreamApi.md#updateStreamUsingPATCH) | **PATCH** /rest/v1.1/stream/{streamId} | Update an existing stream with a given ID |


<a id="addStreamUsingPOST"></a>
# **addStreamUsingPOST**
> RestResponse addStreamUsingPOST(accessKey, secretKey, name, url, method, username, password, skipFramesWithNoFaces, retentionTime, storeOriginalFrames, storeAttendanceFaces, storeAttendanceFrames, isActive, associatedCollections, attributes)

Create new stream with given name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String name = "name_example"; // String | The name of the stream that will be created
    String url = "url_example"; // String | The url of the stream
    String method = "WEBRTC_PULL"; // String | Streaming method
    String username = "username_example"; // String | Username
    String password = "password_example"; // String | Password
    Boolean skipFramesWithNoFaces = true; // Boolean | Boolean value indicating whether you want the original picture to be stored for later retrieval
    Integer retentionTime = 605000; // Integer | Number of seconds for frames to be kept. Default is 605000s (7 days)
    Boolean storeOriginalFrames = false; // Boolean | Boolean value indicating whether you want the original picture to be stored for later retrieval
    Boolean storeAttendanceFaces = false; // Boolean | Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces
    Boolean storeAttendanceFrames = false; // Boolean | Boolean value indicating whether you want to store permanently store frames with a recognized face in them
    Boolean isActive = false; // Boolean | Boolean value indicating whether the stream is currently active or not
    List<String> associatedCollections = Arrays.asList(); // List<String> | List of collection ids which will be used to measure attendance
    String attributes = "attributes_example"; // String | Attributes of the stream
    try {
      RestResponse result = apiInstance.addStreamUsingPOST(accessKey, secretKey, name, url, method, username, password, skipFramesWithNoFaces, retentionTime, storeOriginalFrames, storeAttendanceFaces, storeAttendanceFrames, isActive, associatedCollections, attributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#addStreamUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **name** | **String**| The name of the stream that will be created | |
| **url** | **String**| The url of the stream | |
| **method** | **String**| Streaming method | [optional] [default to WEBRTC_PUSH] [enum: WEBRTC_PULL, WEBRTC_PUSH, INGESTION_ENDPOINT] |
| **username** | **String**| Username | [optional] |
| **password** | **String**| Password | [optional] |
| **skipFramesWithNoFaces** | **Boolean**| Boolean value indicating whether you want the original picture to be stored for later retrieval | [optional] [default to true] |
| **retentionTime** | **Integer**| Number of seconds for frames to be kept. Default is 605000s (7 days) | [optional] [default to 605000] |
| **storeOriginalFrames** | **Boolean**| Boolean value indicating whether you want the original picture to be stored for later retrieval | [optional] [default to false] |
| **storeAttendanceFaces** | **Boolean**| Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces | [optional] [default to false] |
| **storeAttendanceFrames** | **Boolean**| Boolean value indicating whether you want to store permanently store frames with a recognized face in them | [optional] [default to false] |
| **isActive** | **Boolean**| Boolean value indicating whether the stream is currently active or not | [optional] [default to false] |
| **associatedCollections** | [**List&lt;String&gt;**](String.md)| List of collection ids which will be used to measure attendance | [optional] |
| **attributes** | **String**| Attributes of the stream | [optional] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="cleanupStreamUsingPATCH"></a>
# **cleanupStreamUsingPATCH**
> RestResponse cleanupStreamUsingPATCH(accessKey, secretKey, streamId, interval)

Cleanup frames older than specified timeframe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String streamId = "streamId_example"; // String | The id of the stream that will be stopped
    Integer interval = 56; // Integer | Frames older than interval (seconds) will be cleaned up
    try {
      RestResponse result = apiInstance.cleanupStreamUsingPATCH(accessKey, secretKey, streamId, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#cleanupStreamUsingPATCH");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **streamId** | **String**| The id of the stream that will be stopped | |
| **interval** | **Integer**| Frames older than interval (seconds) will be cleaned up | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getFrameImageUsingGET"></a>
# **getFrameImageUsingGET**
> List&lt;byte[]&gt; getFrameImageUsingGET(accessKey, secretKey, streamId, timestamp)

Get individual frame image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String streamId = "streamId_example"; // String | The id of the stream for which the frames will be retrieved
    Long timestamp = 56L; // Long | Timestamp of frame to retrieve
    try {
      List<byte[]> result = apiInstance.getFrameImageUsingGET(accessKey, secretKey, streamId, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#getFrameImageUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **streamId** | **String**| The id of the stream for which the frames will be retrieved | |
| **timestamp** | **Long**| Timestamp of frame to retrieve | |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getLastNAttedanceUsingGET"></a>
# **getLastNAttedanceUsingGET**
> RestResponse getLastNAttedanceUsingGET(accessKey, secretKey, streamIds, count)

Get last N recognized individuals from stream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    List<String> streamIds = Arrays.asList(); // List<String> | The id of the stream for which the frames will be retrieved
    Integer count = 10; // Integer | How many frames to retrieve at a time
    try {
      RestResponse result = apiInstance.getLastNAttedanceUsingGET(accessKey, secretKey, streamIds, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#getLastNAttedanceUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **streamIds** | [**List&lt;String&gt;**](String.md)| The id of the stream for which the frames will be retrieved | [optional] |
| **count** | **Integer**| How many frames to retrieve at a time | [optional] [default to 10] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getLastNFramesUsingGET"></a>
# **getLastNFramesUsingGET**
> RestResponse getLastNFramesUsingGET(accessKey, secretKey, streamId, count, collectionId, labels, attributeFilters)

Get last processed N frames from stream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String streamId = "streamId_example"; // String | The id of the stream for which the frames will be retrieved
    Integer count = 10; // Integer | How many frames to retrieve at a time
    String collectionId = "collectionId_example"; // String | The collection id you want to run recognition against
    List<String> labels = Arrays.asList(); // List<String> | Labels associated with the given picture or picture URL
    List<String> attributeFilters = Arrays.asList(); // List<String> | Filters that will be applied on the recognition operation
    try {
      RestResponse result = apiInstance.getLastNFramesUsingGET(accessKey, secretKey, streamId, count, collectionId, labels, attributeFilters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#getLastNFramesUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **streamId** | **String**| The id of the stream for which the frames will be retrieved | |
| **count** | **Integer**| How many frames to retrieve at a time | [optional] [default to 10] |
| **collectionId** | **String**| The collection id you want to run recognition against | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| Labels associated with the given picture or picture URL | [optional] |
| **attributeFilters** | [**List&lt;String&gt;**](String.md)| Filters that will be applied on the recognition operation | [optional] [enum: NO_FILTER, GENDER_FILTER, AGE_GROUP_FILTER] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getStreamUsingGET"></a>
# **getStreamUsingGET**
> RestResponse getStreamUsingGET(accessKey, secretKey, streamId)

Get an existing stream with a given ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String streamId = "streamId_example"; // String | The id of the stream for which the data will be retrieved
    try {
      RestResponse result = apiInstance.getStreamUsingGET(accessKey, secretKey, streamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#getStreamUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **streamId** | **String**| The id of the stream for which the data will be retrieved | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="removeStreamUsingDELETE"></a>
# **removeStreamUsingDELETE**
> RestResponse removeStreamUsingDELETE(accessKey, secretKey, id)

Delete existing stream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String id = "id_example"; // String | The id of the stream that will be removed
    try {
      RestResponse result = apiInstance.removeStreamUsingDELETE(accessKey, secretKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#removeStreamUsingDELETE");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **id** | **String**| The id of the stream that will be removed | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="startStreamUsingPATCH"></a>
# **startStreamUsingPATCH**
> RestResponse startStreamUsingPATCH(accessKey, secretKey, streamId)

Start existing stream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String streamId = "streamId_example"; // String | The id of the stream that will be started
    try {
      RestResponse result = apiInstance.startStreamUsingPATCH(accessKey, secretKey, streamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#startStreamUsingPATCH");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **streamId** | **String**| The id of the stream that will be started | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="stopStreamUsingPATCH"></a>
# **stopStreamUsingPATCH**
> RestResponse stopStreamUsingPATCH(accessKey, secretKey, streamId)

Stop existing stream

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String streamId = "streamId_example"; // String | The id of the stream that will be stopped
    try {
      RestResponse result = apiInstance.stopStreamUsingPATCH(accessKey, secretKey, streamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#stopStreamUsingPATCH");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **streamId** | **String**| The id of the stream that will be stopped | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="streamsByAccountUsingGET"></a>
# **streamsByAccountUsingGET**
> RestResponse streamsByAccountUsingGET(accessKey, secretKey)

Show status of all streams from account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    try {
      RestResponse result = apiInstance.streamsByAccountUsingGET(accessKey, secretKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamsByAccountUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateStreamUsingPATCH"></a>
# **updateStreamUsingPATCH**
> RestResponse updateStreamUsingPATCH(accessKey, secretKey, streamId, name, url, method, username, password, skipFramesWithNoFaces, retentionTime, storeOriginalFrames, storeAttendanceFaces, storeAttendanceFrames, isActive, associatedCollections, attributes)

Update an existing stream with a given ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String streamId = "streamId_example"; // String | The id of the stream that will be updated
    String name = "name_example"; // String | The name of the stream that will be updated
    String url = "url_example"; // String | The url of the stream
    String method = "WEBRTC_PULL"; // String | Streaming method
    String username = "username_example"; // String | Username
    String password = "password_example"; // String | Password
    Boolean skipFramesWithNoFaces = true; // Boolean | Boolean value indicating whether you want the original picture to be stored for later retrieval
    Integer retentionTime = 56; // Integer | Number of seconds for frames to be kept
    Boolean storeOriginalFrames = true; // Boolean | Boolean value indicating whether you want the original picture to be stored for later retrieval
    Boolean storeAttendanceFaces = true; // Boolean | Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces
    Boolean storeAttendanceFrames = true; // Boolean | Boolean value indicating whether you want to store permanently store frames with a recognized face in them
    Boolean isActive = true; // Boolean | Boolean value indicating whether the stream is currently active or not
    List<String> associatedCollections = Arrays.asList(); // List<String> | List of collection ids which will be used to measure attendance
    String attributes = "attributes_example"; // String | Attributes of the stream
    try {
      RestResponse result = apiInstance.updateStreamUsingPATCH(accessKey, secretKey, streamId, name, url, method, username, password, skipFramesWithNoFaces, retentionTime, storeOriginalFrames, storeAttendanceFaces, storeAttendanceFrames, isActive, associatedCollections, attributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#updateStreamUsingPATCH");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **streamId** | **String**| The id of the stream that will be updated | |
| **name** | **String**| The name of the stream that will be updated | [optional] |
| **url** | **String**| The url of the stream | [optional] |
| **method** | **String**| Streaming method | [optional] [enum: WEBRTC_PULL, WEBRTC_PUSH, INGESTION_ENDPOINT] |
| **username** | **String**| Username | [optional] |
| **password** | **String**| Password | [optional] |
| **skipFramesWithNoFaces** | **Boolean**| Boolean value indicating whether you want the original picture to be stored for later retrieval | [optional] |
| **retentionTime** | **Integer**| Number of seconds for frames to be kept | [optional] |
| **storeOriginalFrames** | **Boolean**| Boolean value indicating whether you want the original picture to be stored for later retrieval | [optional] |
| **storeAttendanceFaces** | **Boolean**| Boolean value indicating whether you want to store permanently store faces clippings of the recognized faces | [optional] |
| **storeAttendanceFrames** | **Boolean**| Boolean value indicating whether you want to store permanently store frames with a recognized face in them | [optional] |
| **isActive** | **Boolean**| Boolean value indicating whether the stream is currently active or not | [optional] |
| **associatedCollections** | [**List&lt;String&gt;**](String.md)| List of collection ids which will be used to measure attendance | [optional] |
| **attributes** | **String**| Attributes of the stream | [optional] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

