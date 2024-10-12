# RecordingsApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRecordingDownloadById**](RecordingsApi.md#getRecordingDownloadById) | **GET** /trainings/{trainingKey}/recordings/{recordingId} | Get Download for Online Recordings |
| [**getRecordingsForTraining**](RecordingsApi.md#getRecordingsForTraining) | **GET** /trainings/{trainingKey}/recordings | Get Online Recordings for Training |


<a id="getRecordingDownloadById"></a>
# **getRecordingDownloadById**
> getRecordingDownloadById(authorization, trainingKey, recordingId)

Get Download for Online Recordings

This call provides the download for the given recording by returning a 302 redirect to the original file.

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
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    RecordingsApi apiInstance = new RecordingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long trainingKey = 56L; // Long | The key of the training
    Long recordingId = 56L; // Long | the unique id of the recording
    try {
      apiInstance.getRecordingDownloadById(authorization, trainingKey, recordingId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordingsApi#getRecordingDownloadById");
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
| **authorization** | **String**| Access token | |
| **trainingKey** | **Long**| The key of the training | |
| **recordingId** | **Long**| the unique id of the recording | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirected to download |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getRecordingsForTraining"></a>
# **getRecordingsForTraining**
> RecordingsListForTraining getRecordingsForTraining(authorization, trainingKey)

Get Online Recordings for Training

This call retrieves information on all online recordings for a given training. If there are none, it returns an empty list.

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
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    RecordingsApi apiInstance = new RecordingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long trainingKey = 56L; // Long | The key of the training
    try {
      RecordingsListForTraining result = apiInstance.getRecordingsForTraining(authorization, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordingsApi#getRecordingsForTraining");
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
| **authorization** | **String**| Access token | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

[**RecordingsListForTraining**](RecordingsListForTraining.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

