# JobMonitoringApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMonitoringSubscription**](JobMonitoringApi.md#createMonitoringSubscription) | **POST** /job_monitoring/subscription | Create an email subscription to the job monitoring page |
| [**deleteMonitoringSubscription**](JobMonitoringApi.md#deleteMonitoringSubscription) | **DELETE** /job_monitoring/subscription/{subscription_id} | Delete a monitoring page email subscription |
| [**getJobMonitoringInfo**](JobMonitoringApi.md#getJobMonitoringInfo) | **GET** /job_monitoring | Get job monitoring information |
| [**getJobMonitoringInfoCsvDownloadLink**](JobMonitoringApi.md#getJobMonitoringInfoCsvDownloadLink) | **GET** /job_monitoring/csv_download_link | Download job monitoring information as a CSV file |
| [**getMonitoringJobCountByJobState**](JobMonitoringApi.md#getMonitoringJobCountByJobState) | **GET** /job_monitoring/summary_by_job_state | Get job monitoring summary information separated by job state |
| [**getMonitoringJobCountByJobType**](JobMonitoringApi.md#getMonitoringJobCountByJobType) | **GET** /job_monitoring/summary_by_job_type | Get job monitoring summary information separated by job type |
| [**getMonitoringSubscription**](JobMonitoringApi.md#getMonitoringSubscription) | **GET** /job_monitoring/subscription/{subscription_id} | Get a specific monitoring email subscription by id |
| [**getMonitoringSubscriptions**](JobMonitoringApi.md#getMonitoringSubscriptions) | **GET** /job_monitoring/subscription | Returns all email subscriptions for the monitoring page |
| [**updateMonitoringSubscription**](JobMonitoringApi.md#updateMonitoringSubscription) | **PATCH** /job_monitoring/subscription/{subscription_id} | Update a monitoring email subscription |


<a id="createMonitoringSubscription"></a>
# **createMonitoringSubscription**
> MonitoringSubscriptionSummary createMonitoringSubscription(monitoringEmailSubscriptionRequest)

Create an email subscription to the job monitoring page

Creates an email subscription to the job monitoring page, which provides information on jobs based on their type (active, in progress, canceled, scheduled, or succeeded). Users can choose which job states to include in the subscription. The email summarizes the job counts by type in the body, and includes the option to include CSV attachments for every job state selected.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    MonitoringEmailSubscriptionRequest monitoringEmailSubscriptionRequest = new MonitoringEmailSubscriptionRequest(); // MonitoringEmailSubscriptionRequest | All information required to create a job-monitoring email subscription.
    try {
      MonitoringSubscriptionSummary result = apiInstance.createMonitoringSubscription(monitoringEmailSubscriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#createMonitoringSubscription");
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
| **monitoringEmailSubscriptionRequest** | [**MonitoringEmailSubscriptionRequest**](MonitoringEmailSubscriptionRequest.md)| All information required to create a job-monitoring email subscription. | |

### Return type

[**MonitoringSubscriptionSummary**](MonitoringSubscriptionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the email subscription. |  -  |

<a id="deleteMonitoringSubscription"></a>
# **deleteMonitoringSubscription**
> deleteMonitoringSubscription(subscriptionId)

Delete a monitoring page email subscription

Deletes the specified monitoring page email subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | ID of the monitoring subscription to delete.
    try {
      apiInstance.deleteMonitoringSubscription(subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#deleteMonitoringSubscription");
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
| **subscriptionId** | **String**| ID of the monitoring subscription to delete. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Monitoring email subscription was successfully deleted. |  -  |

<a id="getJobMonitoringInfo"></a>
# **getJobMonitoringInfo**
> JobMonitoringResponse getJobMonitoringInfo(limit, jobEventStatus, jobType, shouldIncludeLogRelatedJob, isFirstFull, objectType, objectName, nodeName, effectiveSlaDomainId, isOnDemand, lastUpdateTime, afterId, sortBy, sortOrder)

Get job monitoring information

Get the job summary for protection and recovery jobs that are currently running, scheduled to run, or completed in the past 24 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    Integer limit = 56; // Integer | Maximum number of entries to retrieve. The default value is 25. Value needs to be a positive number.
    List<String> jobEventStatus = Arrays.asList(); // List<String> | Filters results by the current event status of the job. The filters should be separated by ','.
    String jobType = "Archival"; // String | Filters results by job type.
    Boolean shouldIncludeLogRelatedJob = true; // Boolean | A Boolean that specifies whether or not to include log- related jobs. Default value is 'false'.
    Boolean isFirstFull = true; // Boolean | Filter results by first full status.
    String objectType = "AppBlueprint"; // String | Filters results by a specified object type.
    String objectName = "objectName_example"; // String | Filters results by the provided value for object_name, using infix search.
    String nodeName = "nodeName_example"; // String | Filter results by node name.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filters results by the provided sla doimain id.
    Boolean isOnDemand = true; // Boolean | Filters results according to their on-demand status.
    OffsetDateTime lastUpdateTime = OffsetDateTime.now(); // OffsetDateTime | All rows updated at or after this time will be returned.
    String afterId = "afterId_example"; // String | Fetches all rows after given row cursor.
    String sortBy = "StartTime"; // String | The column by which to sort the entries.
    String sortOrder = "asc"; // String | The sorting order.
    try {
      JobMonitoringResponse result = apiInstance.getJobMonitoringInfo(limit, jobEventStatus, jobType, shouldIncludeLogRelatedJob, isFirstFull, objectType, objectName, nodeName, effectiveSlaDomainId, isOnDemand, lastUpdateTime, afterId, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#getJobMonitoringInfo");
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
| **limit** | **Integer**| Maximum number of entries to retrieve. The default value is 25. Value needs to be a positive number. | [optional] |
| **jobEventStatus** | [**List&lt;String&gt;**](String.md)| Filters results by the current event status of the job. The filters should be separated by &#39;,&#39;. | [optional] |
| **jobType** | **String**| Filters results by job type. | [optional] [enum: Archival, Backup, Conversion, Recovery, Replication, Index, LogBackup, LogArchival, LogReplication, LogShipping] |
| **shouldIncludeLogRelatedJob** | **Boolean**| A Boolean that specifies whether or not to include log- related jobs. Default value is &#39;false&#39;. | [optional] |
| **isFirstFull** | **Boolean**| Filter results by first full status. | [optional] |
| **objectType** | **String**| Filters results by a specified object type. | [optional] [enum: AppBlueprint, Ec2Instance, Hdfs, HypervVirtualMachine, LinuxFileset, ManagedVolume, Mssql, NutanixVirtualMachine, OracleDatabase, SapHanaDatabase, ShareFileset, StorageArrayVolumeGroup, VcdVapp, VmwareVirtualMachine, WindowsFileset, WindowsVolumeGroup] |
| **objectName** | **String**| Filters results by the provided value for object_name, using infix search. | [optional] |
| **nodeName** | **String**| Filter results by node name. | [optional] |
| **effectiveSlaDomainId** | **String**| Filters results by the provided sla doimain id. | [optional] |
| **isOnDemand** | **Boolean**| Filters results according to their on-demand status. | [optional] |
| **lastUpdateTime** | **OffsetDateTime**| All rows updated at or after this time will be returned. | [optional] |
| **afterId** | **String**| Fetches all rows after given row cursor. | [optional] |
| **sortBy** | **String**| The column by which to sort the entries. | [optional] [enum: StartTime, JobStatus, JobType, ObjectType, SlaDomainName, EndTime, ObjectLogicalSize, DataTransferred, Duration, ObjectName] |
| **sortOrder** | **String**| The sorting order. | [optional] [enum: asc, desc] |

### Return type

[**JobMonitoringResponse**](JobMonitoringResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns job information. |  -  |

<a id="getJobMonitoringInfoCsvDownloadLink"></a>
# **getJobMonitoringInfoCsvDownloadLink**
> JobMonitoringCsvDownloadResponse getJobMonitoringInfoCsvDownloadLink(jobMonitoringState, jobEventStatus, jobType, shouldIncludeLogRelatedJob, objectType, objectName)

Download job monitoring information as a CSV file

Download the job summary for protection and recovery jobs that are currently running, scheduled to run, or completed in the past 24 hours as a CSV file. This is a synchronous operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    String jobMonitoringState = "Failure"; // String | State of the jobs in the CSV.
    String jobEventStatus = "Failure"; // String | Filters results by the current event status of the job.
    String jobType = "Archival"; // String | Filters results by job type.
    Boolean shouldIncludeLogRelatedJob = true; // Boolean | A Boolean that specifies whether or not to include log- related jobs. Default value is 'false'.
    String objectType = "AppBlueprint"; // String | Filters results by a specified object type.
    String objectName = "objectName_example"; // String | Filters results by the provided value for object_name, using infix search.
    try {
      JobMonitoringCsvDownloadResponse result = apiInstance.getJobMonitoringInfoCsvDownloadLink(jobMonitoringState, jobEventStatus, jobType, shouldIncludeLogRelatedJob, objectType, objectName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#getJobMonitoringInfoCsvDownloadLink");
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
| **jobMonitoringState** | **String**| State of the jobs in the CSV. | [enum: Failure, Scheduled, Success, Active, Canceled] |
| **jobEventStatus** | **String**| Filters results by the current event status of the job. | [optional] [enum: Failure, Success, Queued, Scheduled, Active, Canceling, Canceled, SuccessfulWithWarnings, CancelingScheduled] |
| **jobType** | **String**| Filters results by job type. | [optional] [enum: Archival, Backup, Conversion, Recovery, Replication, Index, LogBackup, LogArchival, LogReplication, LogShipping] |
| **shouldIncludeLogRelatedJob** | **Boolean**| A Boolean that specifies whether or not to include log- related jobs. Default value is &#39;false&#39;. | [optional] |
| **objectType** | **String**| Filters results by a specified object type. | [optional] [enum: AppBlueprint, Ec2Instance, Hdfs, HypervVirtualMachine, LinuxFileset, ManagedVolume, Mssql, NutanixVirtualMachine, OracleDatabase, SapHanaDatabase, ShareFileset, StorageArrayVolumeGroup, VcdVapp, VmwareVirtualMachine, WindowsFileset, WindowsVolumeGroup] |
| **objectName** | **String**| Filters results by the provided value for object_name, using infix search. | [optional] |

### Return type

[**JobMonitoringCsvDownloadResponse**](JobMonitoringCsvDownloadResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Download link of the requested CSV file. |  -  |

<a id="getMonitoringJobCountByJobState"></a>
# **getMonitoringJobCountByJobState**
> JobMonitoringSummaryByState getMonitoringJobCountByJobState(jobTypes)

Get job monitoring summary information separated by job state

Get job summary separated by job state for all running jobs, jobs that have been scheduled and jobs that are complete, for protection and recovery jobs in the past 24 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    List<String> jobTypes = Arrays.asList(); // List<String> | Filter by a comma separated list of job types.
    try {
      JobMonitoringSummaryByState result = apiInstance.getMonitoringJobCountByJobState(jobTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#getMonitoringJobCountByJobState");
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
| **jobTypes** | [**List&lt;String&gt;**](String.md)| Filter by a comma separated list of job types. | [optional] |

### Return type

[**JobMonitoringSummaryByState**](JobMonitoringSummaryByState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information about the job counts for the events that match the query parameters. |  -  |

<a id="getMonitoringJobCountByJobType"></a>
# **getMonitoringJobCountByJobType**
> JobMonitoringSummaryByType getMonitoringJobCountByJobType(jobMonitoringState)

Get job monitoring summary information separated by job type

Get job summaries for protection and recovery jobs, separated by job type, that have been scheduled, are currently running, or completed in the past 24 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    String jobMonitoringState = "Failure"; // String | Filter by job state.
    try {
      JobMonitoringSummaryByType result = apiInstance.getMonitoringJobCountByJobType(jobMonitoringState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#getMonitoringJobCountByJobType");
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
| **jobMonitoringState** | **String**| Filter by job state. | [enum: Failure, Scheduled, Success, Active, Canceled] |

### Return type

[**JobMonitoringSummaryByType**](JobMonitoringSummaryByType.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information about the job counts for the events that match the query parameters. |  -  |

<a id="getMonitoringSubscription"></a>
# **getMonitoringSubscription**
> MonitoringSubscriptionSummary getMonitoringSubscription(subscriptionId)

Get a specific monitoring email subscription by id

Returns a summary of the provided monitoring subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | ID of the monitoring subscription to acquire.
    try {
      MonitoringSubscriptionSummary result = apiInstance.getMonitoringSubscription(subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#getMonitoringSubscription");
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
| **subscriptionId** | **String**| ID of the monitoring subscription to acquire. | |

### Return type

[**MonitoringSubscriptionSummary**](MonitoringSubscriptionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the email subscription. |  -  |

<a id="getMonitoringSubscriptions"></a>
# **getMonitoringSubscriptions**
> List&lt;MonitoringSubscriptionSummary&gt; getMonitoringSubscriptions()

Returns all email subscriptions for the monitoring page

Return all unarchived email subscriptions for monitoring page in a list of summaries sorted by creation time (earliest created first). Each summary contains information for each subscription -- Time attributes - when to send the email -- Email addresses - who to send the email -- Attachments - what attachments should the email include -- Job states - which job states to include in the email (Failure, Scheduled, Success, Active, Canceled). -- Id - the tring that identifies the subscription -- Status - the status of the subscription (Active, Suspended, or Unknown) -- Owner - information about the owner of the subscription -- user id - unique id used to identify the owner -- user name - human-readable name of user the time schedule to send the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    try {
      List<MonitoringSubscriptionSummary> result = apiInstance.getMonitoringSubscriptions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#getMonitoringSubscriptions");
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

[**List&lt;MonitoringSubscriptionSummary&gt;**](MonitoringSubscriptionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of email subscriptions for the monitoring page. |  -  |

<a id="updateMonitoringSubscription"></a>
# **updateMonitoringSubscription**
> MonitoringSubscriptionSummary updateMonitoringSubscription(subscriptionId, monitoringEmailSubscriptionUpdate)

Update a monitoring email subscription

Updates the monitoring email subscription with the subscription ID provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    JobMonitoringApi apiInstance = new JobMonitoringApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | ID of the monitoring subscription.
    MonitoringEmailSubscriptionUpdate monitoringEmailSubscriptionUpdate = new MonitoringEmailSubscriptionUpdate(); // MonitoringEmailSubscriptionUpdate | Information required to update a monitoring subscription.
    try {
      MonitoringSubscriptionSummary result = apiInstance.updateMonitoringSubscription(subscriptionId, monitoringEmailSubscriptionUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobMonitoringApi#updateMonitoringSubscription");
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
| **subscriptionId** | **String**| ID of the monitoring subscription. | |
| **monitoringEmailSubscriptionUpdate** | [**MonitoringEmailSubscriptionUpdate**](MonitoringEmailSubscriptionUpdate.md)| Information required to update a monitoring subscription. | |

### Return type

[**MonitoringSubscriptionSummary**](MonitoringSubscriptionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the email subscription. |  -  |

