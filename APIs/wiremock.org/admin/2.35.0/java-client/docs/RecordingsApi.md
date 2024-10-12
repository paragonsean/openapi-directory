# RecordingsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminRecordingsSnapshotPost**](RecordingsApi.md#adminRecordingsSnapshotPost) | **POST** /__admin/recordings/snapshot | Take a snapshot recording |
| [**adminRecordingsStartPost**](RecordingsApi.md#adminRecordingsStartPost) | **POST** /__admin/recordings/start | Start recording |
| [**adminRecordingsStatusGet**](RecordingsApi.md#adminRecordingsStatusGet) | **GET** /__admin/recordings/status | Get recording status |
| [**adminRecordingsStopPost**](RecordingsApi.md#adminRecordingsStopPost) | **POST** /__admin/recordings/stop | Stop recording |


<a id="adminRecordingsSnapshotPost"></a>
# **adminRecordingsSnapshotPost**
> AdminMappingsGet200Response adminRecordingsSnapshotPost(adminRecordingsSnapshotPostRequest)

Take a snapshot recording

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RecordingsApi apiInstance = new RecordingsApi(defaultClient);
    AdminRecordingsSnapshotPostRequest adminRecordingsSnapshotPostRequest = new AdminRecordingsSnapshotPostRequest(); // AdminRecordingsSnapshotPostRequest | 
    try {
      AdminMappingsGet200Response result = apiInstance.adminRecordingsSnapshotPost(adminRecordingsSnapshotPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordingsApi#adminRecordingsSnapshotPost");
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
| **adminRecordingsSnapshotPostRequest** | [**AdminRecordingsSnapshotPostRequest**](AdminRecordingsSnapshotPostRequest.md)|  | |

### Return type

[**AdminMappingsGet200Response**](AdminMappingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully took a snapshot recording |  -  |

<a id="adminRecordingsStartPost"></a>
# **adminRecordingsStartPost**
> adminRecordingsStartPost(adminRecordingsStartPostRequest)

Start recording

Begin recording stub mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RecordingsApi apiInstance = new RecordingsApi(defaultClient);
    AdminRecordingsStartPostRequest adminRecordingsStartPostRequest = new AdminRecordingsStartPostRequest(); // AdminRecordingsStartPostRequest | 
    try {
      apiInstance.adminRecordingsStartPost(adminRecordingsStartPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordingsApi#adminRecordingsStartPost");
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
| **adminRecordingsStartPostRequest** | [**AdminRecordingsStartPostRequest**](AdminRecordingsStartPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully started recording |  -  |

<a id="adminRecordingsStatusGet"></a>
# **adminRecordingsStatusGet**
> AdminRecordingsStatusGet200Response adminRecordingsStatusGet()

Get recording status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RecordingsApi apiInstance = new RecordingsApi(defaultClient);
    try {
      AdminRecordingsStatusGet200Response result = apiInstance.adminRecordingsStatusGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordingsApi#adminRecordingsStatusGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminRecordingsStatusGet200Response**](AdminRecordingsStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully got the record status |  -  |

<a id="adminRecordingsStopPost"></a>
# **adminRecordingsStopPost**
> AdminMappingsGet200Response adminRecordingsStopPost()

Stop recording

End recording of stub mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RecordingsApi apiInstance = new RecordingsApi(defaultClient);
    try {
      AdminMappingsGet200Response result = apiInstance.adminRecordingsStopPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordingsApi#adminRecordingsStopPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminMappingsGet200Response**](AdminMappingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully stopped recording |  -  |

