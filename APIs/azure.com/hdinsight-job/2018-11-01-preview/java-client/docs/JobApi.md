# JobApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobGet**](JobApi.md#jobGet) | **GET** /templeton/v1/jobs/{jobId} |  |
| [**jobGetAppState**](JobApi.md#jobGetAppState) | **GET** /ws/v1/cluster/apps/{appId}/state |  |
| [**jobKill**](JobApi.md#jobKill) | **DELETE** /templeton/v1/jobs/{jobId} |  |
| [**jobList**](JobApi.md#jobList) | **GET** /templeton/v1/jobs |  |
| [**jobListAfterJobId**](JobApi.md#jobListAfterJobId) | **GET** /templeton/v1/jobs?op&#x3D;LISTAFTERID |  |
| [**jobSubmitHiveJob**](JobApi.md#jobSubmitHiveJob) | **POST** /templeton/v1/hive |  |
| [**jobSubmitMapReduceJob**](JobApi.md#jobSubmitMapReduceJob) | **POST** /templeton/v1/mapreduce/jar |  |
| [**jobSubmitMapReduceStreamingJob**](JobApi.md#jobSubmitMapReduceStreamingJob) | **POST** /templeton/v1/mapreduce/streaming |  |
| [**jobSubmitPigJob**](JobApi.md#jobSubmitPigJob) | **POST** /templeton/v1/pig |  |
| [**jobSubmitSqoopJob**](JobApi.md#jobSubmitSqoopJob) | **POST** /templeton/v1/sqoop |  |


<a id="jobGet"></a>
# **jobGet**
> JobDetailRootJsonObject jobGet(userName, jobId, fields)



Gets job details from the specified HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    String jobId = "jobId_example"; // String | The id of the job.
    String fields = "*"; // String | If fields set to '*', the request will return full details of the job. Currently the value can only be '*'.
    try {
      JobDetailRootJsonObject result = apiInstance.jobGet(userName, jobId, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobGet");
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
| **userName** | **String**| The user name used for running job. | |
| **jobId** | **String**| The id of the job. | |
| **fields** | **String**| If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;. | [enum: *] |

### Return type

[**JobDetailRootJsonObject**](JobDetailRootJsonObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobGetAppState"></a>
# **jobGetAppState**
> AppState jobGetAppState(appId)



Gets application state from the specified HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String appId = "appId_example"; // String | The id of the job.
    try {
      AppState result = apiInstance.jobGetAppState(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobGetAppState");
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
| **appId** | **String**| The id of the job. | |

### Return type

[**AppState**](AppState.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobKill"></a>
# **jobKill**
> JobDetailRootJsonObject jobKill(userName, jobId)



Initiates cancel on given running job in the specified HDInsight.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    String jobId = "jobId_example"; // String | The id of the job.
    try {
      JobDetailRootJsonObject result = apiInstance.jobKill(userName, jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobKill");
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
| **userName** | **String**| The user name used for running job. | |
| **jobId** | **String**| The id of the job. | |

### Return type

[**JobDetailRootJsonObject**](JobDetailRootJsonObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobList"></a>
# **jobList**
> List&lt;JobListJsonObject&gt; jobList(userName, showall, fields)



Gets the list of jobs from the specified HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    String showall = "true"; // String | If showall is set to 'true', the request will return all jobs the user has permission to view, not only the jobs belonging to the user.
    String fields = "*"; // String | If fields set to '*', the request will return full details of the job. Currently the value can only be '*'.
    try {
      List<JobListJsonObject> result = apiInstance.jobList(userName, showall, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobList");
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
| **userName** | **String**| The user name used for running job. | |
| **showall** | **String**| If showall is set to &#39;true&#39;, the request will return all jobs the user has permission to view, not only the jobs belonging to the user. | [enum: true] |
| **fields** | **String**| If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;. | [enum: *] |

### Return type

[**List&lt;JobListJsonObject&gt;**](JobListJsonObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobListAfterJobId"></a>
# **jobListAfterJobId**
> List&lt;JobListJsonObject&gt; jobListAfterJobId(userName, showall, fields, jobid, numrecords)



Gets numrecords Of Jobs after jobid from the specified HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    String showall = "true"; // String | If showall is set to 'true', the request will return all jobs the user has permission to view, not only the jobs belonging to the user.
    String fields = "*"; // String | If fields set to '*', the request will return full details of the job. Currently the value can only be '*'.
    String jobid = "jobid_example"; // String | JobId from where to list jobs.
    Integer numrecords = 56; // Integer | Number of jobs to fetch.
    try {
      List<JobListJsonObject> result = apiInstance.jobListAfterJobId(userName, showall, fields, jobid, numrecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobListAfterJobId");
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
| **userName** | **String**| The user name used for running job. | |
| **showall** | **String**| If showall is set to &#39;true&#39;, the request will return all jobs the user has permission to view, not only the jobs belonging to the user. | [enum: true] |
| **fields** | **String**| If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;. | [enum: *] |
| **jobid** | **String**| JobId from where to list jobs. | [optional] |
| **numrecords** | **Integer**| Number of jobs to fetch. | [optional] |

### Return type

[**List&lt;JobListJsonObject&gt;**](JobListJsonObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobSubmitHiveJob"></a>
# **jobSubmitHiveJob**
> JobSubmissionJsonResponse jobSubmitHiveJob(userName, content)



Submits a Hive job to an HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    Object content = null; // Object | The content of the Hive job request.
    try {
      JobSubmissionJsonResponse result = apiInstance.jobSubmitHiveJob(userName, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobSubmitHiveJob");
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
| **userName** | **String**| The user name used for running job. | |
| **content** | **Object**| The content of the Hive job request. | |

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/text
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobSubmitMapReduceJob"></a>
# **jobSubmitMapReduceJob**
> JobSubmissionJsonResponse jobSubmitMapReduceJob(userName, content)



Submits a MapReduce job to an HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    Object content = null; // Object | The content of the MapReduce job request.
    try {
      JobSubmissionJsonResponse result = apiInstance.jobSubmitMapReduceJob(userName, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobSubmitMapReduceJob");
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
| **userName** | **String**| The user name used for running job. | |
| **content** | **Object**| The content of the MapReduce job request. | |

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobSubmitMapReduceStreamingJob"></a>
# **jobSubmitMapReduceStreamingJob**
> JobSubmissionJsonResponse jobSubmitMapReduceStreamingJob(userName, content)



Submits a MapReduce streaming job to an HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    Object content = null; // Object | The content of the MapReduce job request.
    try {
      JobSubmissionJsonResponse result = apiInstance.jobSubmitMapReduceStreamingJob(userName, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobSubmitMapReduceStreamingJob");
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
| **userName** | **String**| The user name used for running job. | |
| **content** | **Object**| The content of the MapReduce job request. | |

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobSubmitPigJob"></a>
# **jobSubmitPigJob**
> JobSubmissionJsonResponse jobSubmitPigJob(userName, content)



Submits a Pig job to an HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    Object content = null; // Object | The content of the Pig job request.
    try {
      JobSubmissionJsonResponse result = apiInstance.jobSubmitPigJob(userName, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobSubmitPigJob");
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
| **userName** | **String**| The user name used for running job. | |
| **content** | **Object**| The content of the Pig job request. | |

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="jobSubmitSqoopJob"></a>
# **jobSubmitSqoopJob**
> JobSubmissionJsonResponse jobSubmitSqoopJob(userName, content)



Submits a Sqoop job to an HDInsight cluster.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobApi apiInstance = new JobApi(defaultClient);
    String userName = "userName_example"; // String | The user name used for running job.
    Object content = null; // Object | The content of the Sqoop job request.
    try {
      JobSubmissionJsonResponse result = apiInstance.jobSubmitSqoopJob(userName, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobSubmitSqoopJob");
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
| **userName** | **String**| The user name used for running job. | |
| **content** | **Object**| The content of the Sqoop job request. | |

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

