# JobApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1JobsPausePost**](JobApi.md#apiV1JobsPausePost) | **POST** /api/v1/jobs/pause | Pause job queue |
| [**apiV1JobsResumePost**](JobApi.md#apiV1JobsResumePost) | **POST** /api/v1/jobs/resume | Resume job queue |
| [**getJobs**](JobApi.md#getJobs) | **GET** /api/v1/jobs/{state} | List instance jobs |


<a id="apiV1JobsPausePost"></a>
# **apiV1JobsPausePost**
> apiV1JobsPausePost()

Pause job queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    try {
      apiInstance.apiV1JobsPausePost();
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#apiV1JobsPausePost");
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

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="apiV1JobsResumePost"></a>
# **apiV1JobsResumePost**
> apiV1JobsResumePost()

Resume job queue

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    try {
      apiInstance.apiV1JobsResumePost();
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#apiV1JobsResumePost");
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

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="getJobs"></a>
# **getJobs**
> GetJobs200Response getJobs(state, jobType, start, count, sort)

List instance jobs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String state = ""; // String | The state of the job ('' for for no filter)
    String jobType = "activitypub-follow"; // String | job type
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      GetJobs200Response result = apiInstance.getJobs(state, jobType, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#getJobs");
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
| **state** | **String**| The state of the job (&#39;&#39; for for no filter) | [enum: , active, completed, failed, waiting, delayed] |
| **jobType** | **String**| job type | [optional] [enum: activitypub-follow, activitypub-http-broadcast, activitypub-http-fetcher, activitypub-http-unicast, email, video-transcoding, video-file-import, video-import, videos-views-stats, activitypub-refresher, video-redundancy, video-live-ending, video-channel-import] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**GetJobs200Response**](GetJobs200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

