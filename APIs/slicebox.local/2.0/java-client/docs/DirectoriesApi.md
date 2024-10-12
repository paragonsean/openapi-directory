# DirectoriesApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**directorywatchesGet**](DirectoriesApi.md#directorywatchesGet) | **GET** /directorywatches |  |
| [**directorywatchesIdDelete**](DirectoriesApi.md#directorywatchesIdDelete) | **DELETE** /directorywatches/{id} |  |
| [**directorywatchesPost**](DirectoriesApi.md#directorywatchesPost) | **POST** /directorywatches |  |


<a id="directorywatchesGet"></a>
# **directorywatchesGet**
> List&lt;WatchedDirectory&gt; directorywatchesGet(startindex, count)



get a list of watch directories. Each watch directory and its sub-directories are watched for incoming DICOM files, which are read and imported into slicebox.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    DirectoriesApi apiInstance = new DirectoriesApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of watched directories
    Long count = 20L; // Long | size of returned slice of watched directories
    try {
      List<WatchedDirectory> result = apiInstance.directorywatchesGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoriesApi#directorywatchesGet");
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
| **startindex** | **Long**| start index of returned slice of watched directories | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of watched directories | [optional] [default to 20] |

### Return type

[**List&lt;WatchedDirectory&gt;**](WatchedDirectory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of watched directories |  -  |

<a id="directorywatchesIdDelete"></a>
# **directorywatchesIdDelete**
> directorywatchesIdDelete(id)



stop watching and remove the directory corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    DirectoriesApi apiInstance = new DirectoriesApi(defaultClient);
    Long id = 56L; // Long | id of directory to stop watching
    try {
      apiInstance.directorywatchesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoriesApi#directorywatchesIdDelete");
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
| **id** | **Long**| id of directory to stop watching | |

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
| **204** | directory watch removed |  -  |

<a id="directorywatchesPost"></a>
# **directorywatchesPost**
> WatchedDirectory directorywatchesPost(watchedDirectory)



add a new directory to watch for incoming DICOM files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    DirectoriesApi apiInstance = new DirectoriesApi(defaultClient);
    WatchedDirectory watchedDirectory = new WatchedDirectory(); // WatchedDirectory | directory to setup a watch for. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    try {
      WatchedDirectory result = apiInstance.directorywatchesPost(watchedDirectory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoriesApi#directorywatchesPost");
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
| **watchedDirectory** | [**WatchedDirectory**](WatchedDirectory.md)| directory to setup a watch for. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] |

### Return type

[**WatchedDirectory**](WatchedDirectory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the directory now being watched |  -  |

