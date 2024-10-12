# JobRunsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobRunsDeleteJobRun**](JobRunsApi.md#jobRunsDeleteJobRun) | **DELETE** /api/v2/jobRuns/{jobRunID} | Delete a JobRun |
| [**jobRunsGetJobRun**](JobRunsApi.md#jobRunsGetJobRun) | **GET** /api/v2/jobRuns/{jobRunID} | Get a JobRun by ID |
| [**jobRunsGetJobRuns**](JobRunsApi.md#jobRunsGetJobRuns) | **GET** /api/v2/jobRuns | Get JobRuns |
| [**jobRunsPostJobRun**](JobRunsApi.md#jobRunsPostJobRun) | **POST** /api/v2/jobRuns | Create a JobRun |
| [**jobRunsPutJobRun**](JobRunsApi.md#jobRunsPutJobRun) | **PUT** /api/v2/jobRuns/{jobRunID} | Update a JobRun |


<a id="jobRunsDeleteJobRun"></a>
# **jobRunsDeleteJobRun**
> jobRunsDeleteJobRun(jobRunID)

Delete a JobRun

Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobRunsApi apiInstance = new JobRunsApi(defaultClient);
    Integer jobRunID = 56; // Integer | The id of the JobRun to delete
    try {
      apiInstance.jobRunsDeleteJobRun(jobRunID);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobRunsApi#jobRunsDeleteJobRun");
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
| **jobRunID** | **Integer**| The id of the JobRun to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="jobRunsGetJobRun"></a>
# **jobRunsGetJobRun**
> BuildSystemSharedDTOJobRun jobRunsGetJobRun(jobRunID, includeActivityRunDetails)

Get a JobRun by ID

Gets a JobRun by ID. When successful, the response is the requested JobRun.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobRunsApi apiInstance = new JobRunsApi(defaultClient);
    Integer jobRunID = 56; // Integer | The ID of the JobRun to get.
    Boolean includeActivityRunDetails = true; // Boolean | Optional. Indicates whether to include ActivityRun details.  Defaults to false.
    try {
      BuildSystemSharedDTOJobRun result = apiInstance.jobRunsGetJobRun(jobRunID, includeActivityRunDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobRunsApi#jobRunsGetJobRun");
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
| **jobRunID** | **Integer**| The ID of the JobRun to get. | |
| **includeActivityRunDetails** | **Boolean**| Optional. Indicates whether to include ActivityRun details.  Defaults to false. | [optional] |

### Return type

[**BuildSystemSharedDTOJobRun**](BuildSystemSharedDTOJobRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="jobRunsGetJobRuns"></a>
# **jobRunsGetJobRuns**
> APIPagedResponseBuildSystemSharedDTOJobRun jobRunsGetJobRuns(limit, offset, includeActivityRunDetails)

Get JobRuns

Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobRunsApi apiInstance = new JobRunsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Boolean includeActivityRunDetails = true; // Boolean | Optional. Indicates whether to include ActivityRun details.  Defaults to false.
    try {
      APIPagedResponseBuildSystemSharedDTOJobRun result = apiInstance.jobRunsGetJobRuns(limit, offset, includeActivityRunDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobRunsApi#jobRunsGetJobRuns");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **includeActivityRunDetails** | **Boolean**| Optional. Indicates whether to include ActivityRun details.  Defaults to false. | [optional] |

### Return type

[**APIPagedResponseBuildSystemSharedDTOJobRun**](APIPagedResponseBuildSystemSharedDTOJobRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="jobRunsPostJobRun"></a>
# **jobRunsPostJobRun**
> Integer jobRunsPostJobRun(buildSystemSharedDTOJobRun)

Create a JobRun

Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on              creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an               appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobRunsApi apiInstance = new JobRunsApi(defaultClient);
    BuildSystemSharedDTOJobRun buildSystemSharedDTOJobRun = new BuildSystemSharedDTOJobRun(); // BuildSystemSharedDTOJobRun | The JobRun to create.  The JobRunID will be assigned on creation of the JobRun.
    try {
      Integer result = apiInstance.jobRunsPostJobRun(buildSystemSharedDTOJobRun);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobRunsApi#jobRunsPostJobRun");
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
| **buildSystemSharedDTOJobRun** | [**BuildSystemSharedDTOJobRun**](BuildSystemSharedDTOJobRun.md)| The JobRun to create.  The JobRunID will be assigned on creation of the JobRun. | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="jobRunsPutJobRun"></a>
# **jobRunsPutJobRun**
> jobRunsPutJobRun(jobRunID, buildSystemSharedDTOJobRun)

Update a JobRun

///               Updates a JobRun.  The body of the PUT is the updated JobRun.              When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobRunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobRunsApi apiInstance = new JobRunsApi(defaultClient);
    Integer jobRunID = 56; // Integer | The id of the JobRun to update
    BuildSystemSharedDTOJobRun buildSystemSharedDTOJobRun = new BuildSystemSharedDTOJobRun(); // BuildSystemSharedDTOJobRun | The updated JobRun
    try {
      apiInstance.jobRunsPutJobRun(jobRunID, buildSystemSharedDTOJobRun);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobRunsApi#jobRunsPutJobRun");
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
| **jobRunID** | **Integer**| The id of the JobRun to update | |
| **buildSystemSharedDTOJobRun** | [**BuildSystemSharedDTOJobRun**](BuildSystemSharedDTOJobRun.md)| The updated JobRun | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

