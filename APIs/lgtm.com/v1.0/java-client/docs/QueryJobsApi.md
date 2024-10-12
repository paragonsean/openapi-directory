# QueryJobsApi

All URIs are relative to *https://lgtm.com/api/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createQueryJob**](QueryJobsApi.md#createQueryJob) | **POST** /queryjobs | Run a CodeQL query on one or more projects |
| [**getQueryJob**](QueryJobsApi.md#getQueryJob) | **GET** /queryjobs/{queryjob-id} | Get the status of a query job |
| [**getQueryJobResultsForProject**](QueryJobsApi.md#getQueryJobResultsForProject) | **GET** /queryjobs/{queryjob-id}/results/{project-id} | Fetch the results of a query job for a specific project |
| [**getQueryJobResultsOverview**](QueryJobsApi.md#getQueryJobResultsOverview) | **GET** /queryjobs/{queryjob-id}/results | Provide a summary of results for the projects in the query job |


<a id="createQueryJob"></a>
# **createQueryJob**
> Operation createQueryJob(language, body, projectId, projectsList)

Run a CodeQL query on one or more projects

Submit a query to run on one or more projects on LGTM. The query is included in the body of the request. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    QueryJobsApi apiInstance = new QueryJobsApi(defaultClient);
    String language = "language_example"; // String | The [language](https://lgtm.com/help/lgtm/analysis-faqs#which-languages-are-supported) you want to analyze. 
    String body = select "hello", "world"; // String | The query to run.
    List<Long> projectId = Arrays.asList(); // List<Long> | The identifier of the project to analyze. Either `project-id` or `projects-list` must be specified.
    String projectsList = "projectsList_example"; // String | Name of the list containing the projects to analyze. Either `project-id` or `projects-list` must be specified.
    try {
      Operation result = apiInstance.createQueryJob(language, body, projectId, projectsList);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryJobsApi#createQueryJob");
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
| **language** | **String**| The [language](https://lgtm.com/help/lgtm/analysis-faqs#which-languages-are-supported) you want to analyze.  | |
| **body** | **String**| The query to run. | |
| **projectId** | [**List&lt;Long&gt;**](Long.md)| The identifier of the project to analyze. Either &#x60;project-id&#x60; or &#x60;projects-list&#x60; must be specified. | [optional] |
| **projectsList** | **String**| Name of the list containing the projects to analyze. Either &#x60;project-id&#x60; or &#x60;projects-list&#x60; must be specified. | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. Query submitted. Tracking data returned. |  -  |

<a id="getQueryJob"></a>
# **getQueryJob**
> Queryjob getQueryJob(queryjobId)

Get the status of a query job

Get the status of a query job using the query job identifier for the task.  When you create a query job, the response includes a task result URL of the form: &#x60;/queryjobs/{queryjob-id}&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    QueryJobsApi apiInstance = new QueryJobsApi(defaultClient);
    String queryjobId = "queryjobId_example"; // String | The identifier of the query job, from the `task-result` given in the response to the initial `POST /queryjobs` request.
    try {
      Queryjob result = apiInstance.getQueryJob(queryjobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryJobsApi#getQueryJob");
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
| **queryjobId** | **String**| The identifier of the query job, from the &#x60;task-result&#x60; given in the response to the initial &#x60;POST /queryjobs&#x60; request. | |

### Return type

[**Queryjob**](Queryjob.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Requested data returned. |  -  |

<a id="getQueryJobResultsForProject"></a>
# **getQueryJobResultsForProject**
> QueryjobProjectResults getQueryJobResultsForProject(queryjobId, projectId, start, limit, nofilter)

Fetch the results of a query job for a specific project

Fetch the results for a specific project. The endpoint succeeds only if the query was successful,  and returns a &#x60;404&#x60; error otherwise.  By default, the endpoint provides only results that are within the source tree. To obtain all results, specify the &#x60;nofilter&#x60; parameter. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    QueryJobsApi apiInstance = new QueryJobsApi(defaultClient);
    String queryjobId = "queryjobId_example"; // String | The identifier of the query job, from the `task-result` given in the response to the initial `POST /queryjobs` request.
    String projectId = "projectId_example"; // String | The identifier for the project.
    Integer start = 56; // Integer | Start point for the page of results.
    Integer limit = 100; // Integer | The maximum number of results to display (less than 100).
    Boolean nofilter = false; // Boolean | Include results that are not part of the source tree. These results are filtered out by default.
    try {
      QueryjobProjectResults result = apiInstance.getQueryJobResultsForProject(queryjobId, projectId, start, limit, nofilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryJobsApi#getQueryJobResultsForProject");
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
| **queryjobId** | **String**| The identifier of the query job, from the &#x60;task-result&#x60; given in the response to the initial &#x60;POST /queryjobs&#x60; request. | |
| **projectId** | **String**| The identifier for the project. | |
| **start** | **Integer**| Start point for the page of results. | [optional] |
| **limit** | **Integer**| The maximum number of results to display (less than 100). | [optional] [default to 100] |
| **nofilter** | **Boolean**| Include results that are not part of the source tree. These results are filtered out by default. | [optional] [default to false] |

### Return type

[**QueryjobProjectResults**](QueryjobProjectResults.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The result contains three items: column headers, data, and pagination information. |  -  |

<a id="getQueryJobResultsOverview"></a>
# **getQueryJobResultsOverview**
> QueryjobResultsOverview getQueryJobResultsOverview(queryjobId, start, limit, filter)

Provide a summary of results for the projects in the query job

This endpoint provides a summary of the results generated by completed query runs for each  project specified in the the POST /queryjobs endpoint.  For completed query jobs, the summary includes:    * The number of results for successful query runs.   * Error information for failed query runs.  No information is included in the response for any project for which the query  run is still in progress. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    QueryJobsApi apiInstance = new QueryJobsApi(defaultClient);
    String queryjobId = "queryjobId_example"; // String | The identifier of the query job, from the `task-result` given in the response to the initial `POST /queryjobs` request.
    String start = "start_example"; // String | An opaque identifier generated by the API used for pagination.  This identifier will be included as part of the response for this endpoint whenever more than one page of results is available.  
    Integer limit = 100; // Integer | The number of results to return. Useful for pagination.
    String filter = "filter_example"; // String | Only return a subset of results. Legal values are `w-results`, `wo-results`, `error`.
    try {
      QueryjobResultsOverview result = apiInstance.getQueryJobResultsOverview(queryjobId, start, limit, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryJobsApi#getQueryJobResultsOverview");
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
| **queryjobId** | **String**| The identifier of the query job, from the &#x60;task-result&#x60; given in the response to the initial &#x60;POST /queryjobs&#x60; request. | |
| **start** | **String**| An opaque identifier generated by the API used for pagination.  This identifier will be included as part of the response for this endpoint whenever more than one page of results is available.   | [optional] |
| **limit** | **Integer**| The number of results to return. Useful for pagination. | [optional] [default to 100] |
| **filter** | **String**| Only return a subset of results. Legal values are &#x60;w-results&#x60;, &#x60;wo-results&#x60;, &#x60;error&#x60;. | [optional] |

### Return type

[**QueryjobResultsOverview**](QueryjobResultsOverview.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Requested data returned. |  -  |

