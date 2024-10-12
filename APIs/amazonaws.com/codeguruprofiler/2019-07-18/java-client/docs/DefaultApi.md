# DefaultApi

All URIs are relative to *http://codeguru-profiler.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addNotificationChannels**](DefaultApi.md#addNotificationChannels) | **POST** /profilingGroups/{profilingGroupName}/notificationConfiguration |  |
| [**batchGetFrameMetricData**](DefaultApi.md#batchGetFrameMetricData) | **POST** /profilingGroups/{profilingGroupName}/frames/-/metrics |  |
| [**configureAgent**](DefaultApi.md#configureAgent) | **POST** /profilingGroups/{profilingGroupName}/configureAgent |  |
| [**createProfilingGroup**](DefaultApi.md#createProfilingGroup) | **POST** /profilingGroups#clientToken |  |
| [**deleteProfilingGroup**](DefaultApi.md#deleteProfilingGroup) | **DELETE** /profilingGroups/{profilingGroupName} |  |
| [**describeProfilingGroup**](DefaultApi.md#describeProfilingGroup) | **GET** /profilingGroups/{profilingGroupName} |  |
| [**getFindingsReportAccountSummary**](DefaultApi.md#getFindingsReportAccountSummary) | **GET** /internal/findingsReports |  |
| [**getNotificationConfiguration**](DefaultApi.md#getNotificationConfiguration) | **GET** /profilingGroups/{profilingGroupName}/notificationConfiguration |  |
| [**getPolicy**](DefaultApi.md#getPolicy) | **GET** /profilingGroups/{profilingGroupName}/policy |  |
| [**getProfile**](DefaultApi.md#getProfile) | **GET** /profilingGroups/{profilingGroupName}/profile |  |
| [**getRecommendations**](DefaultApi.md#getRecommendations) | **GET** /internal/profilingGroups/{profilingGroupName}/recommendations#endTime&amp;startTime |  |
| [**listFindingsReports**](DefaultApi.md#listFindingsReports) | **GET** /internal/profilingGroups/{profilingGroupName}/findingsReports#endTime&amp;startTime |  |
| [**listProfileTimes**](DefaultApi.md#listProfileTimes) | **GET** /profilingGroups/{profilingGroupName}/profileTimes#endTime&amp;period&amp;startTime |  |
| [**listProfilingGroups**](DefaultApi.md#listProfilingGroups) | **GET** /profilingGroups |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} |  |
| [**postAgentProfile**](DefaultApi.md#postAgentProfile) | **POST** /profilingGroups/{profilingGroupName}/agentProfile#Content-Type |  |
| [**putPermission**](DefaultApi.md#putPermission) | **PUT** /profilingGroups/{profilingGroupName}/policy/{actionGroup} |  |
| [**removeNotificationChannel**](DefaultApi.md#removeNotificationChannel) | **DELETE** /profilingGroups/{profilingGroupName}/notificationConfiguration/{channelId} |  |
| [**removePermission**](DefaultApi.md#removePermission) | **DELETE** /profilingGroups/{profilingGroupName}/policy/{actionGroup}#revisionId |  |
| [**submitFeedback**](DefaultApi.md#submitFeedback) | **POST** /internal/profilingGroups/{profilingGroupName}/anomalies/{anomalyInstanceId}/feedback |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} |  |
| [**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys |  |
| [**updateProfilingGroup**](DefaultApi.md#updateProfilingGroup) | **PUT** /profilingGroups/{profilingGroupName} |  |


<a id="addNotificationChannels"></a>
# **addNotificationChannels**
> AddNotificationChannelsResponse addNotificationChannels(profilingGroupName, addNotificationChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Add up to 2 anomaly notifications channels for a profiling group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group that we are setting up notifications for.
    AddNotificationChannelsRequest addNotificationChannelsRequest = new AddNotificationChannelsRequest(); // AddNotificationChannelsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AddNotificationChannelsResponse result = apiInstance.addNotificationChannels(profilingGroupName, addNotificationChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addNotificationChannels");
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
| **profilingGroupName** | **String**| The name of the profiling group that we are setting up notifications for. | |
| **addNotificationChannelsRequest** | [**AddNotificationChannelsRequest**](AddNotificationChannelsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AddNotificationChannelsResponse**](AddNotificationChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceQuotaExceededException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | ThrottlingException |  -  |
| **485** | ResourceNotFoundException |  -  |

<a id="batchGetFrameMetricData"></a>
# **batchGetFrameMetricData**
> BatchGetFrameMetricDataResponse batchGetFrameMetricData(profilingGroupName, batchGetFrameMetricDataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, endTime, period, startTime, targetResolution)



 Returns the time series of values for a requested list of frame metrics from a time period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String |  The name of the profiling group associated with the the frame metrics used to return the time series values. 
    BatchGetFrameMetricDataRequest batchGetFrameMetricDataRequest = new BatchGetFrameMetricDataRequest(); // BatchGetFrameMetricDataRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime |  The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    String period = "period_example"; // String |  The duration of the frame metrics used to return the time series values. Specify using the ISO 8601 format. The maximum period duration is one day (<code>PT24H</code> or <code>P1D</code>). 
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime |  The start time of the time period for the frame metrics used to return the time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    String targetResolution = "PT5M"; // String | <p>The requested resolution of time steps for the returned time series of values. If the requested target resolution is not available due to data not being retained we provide a best effort result by falling back to the most granular available resolution after the target resolution. There are 3 valid values. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>
    try {
      BatchGetFrameMetricDataResponse result = apiInstance.batchGetFrameMetricData(profilingGroupName, batchGetFrameMetricDataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, endTime, period, startTime, targetResolution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchGetFrameMetricData");
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
| **profilingGroupName** | **String**|  The name of the profiling group associated with the the frame metrics used to return the time series values.  | |
| **batchGetFrameMetricDataRequest** | [**BatchGetFrameMetricDataRequest**](BatchGetFrameMetricDataRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **endTime** | **OffsetDateTime**|  The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.  | [optional] |
| **period** | **String**|  The duration of the frame metrics used to return the time series values. Specify using the ISO 8601 format. The maximum period duration is one day (&lt;code&gt;PT24H&lt;/code&gt; or &lt;code&gt;P1D&lt;/code&gt;).  | [optional] |
| **startTime** | **OffsetDateTime**|  The start time of the time period for the frame metrics used to return the time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.  | [optional] |
| **targetResolution** | **String**| &lt;p&gt;The requested resolution of time steps for the returned time series of values. If the requested target resolution is not available due to data not being retained we provide a best effort result by falling back to the most granular available resolution after the target resolution. There are 3 valid values. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;P1D&lt;/code&gt; — 1 day &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PT1H&lt;/code&gt; — 1 hour &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PT5M&lt;/code&gt; — 5 minutes &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] [enum: PT5M, PT1H, P1D] |

### Return type

[**BatchGetFrameMetricDataResponse**](BatchGetFrameMetricDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="configureAgent"></a>
# **configureAgent**
> ConfigureAgentResponse configureAgent(profilingGroupName, configureAgentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Used by profiler agents to report their current state and to receive remote configuration updates. For example, &lt;code&gt;ConfigureAgent&lt;/code&gt; can be used to tell an agent whether to profile or not and for how long to return profiling data. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String |  The name of the profiling group for which the configured agent is collecting profiling data. 
    ConfigureAgentRequest configureAgentRequest = new ConfigureAgentRequest(); // ConfigureAgentRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ConfigureAgentResponse result = apiInstance.configureAgent(profilingGroupName, configureAgentRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#configureAgent");
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
| **profilingGroupName** | **String**|  The name of the profiling group for which the configured agent is collecting profiling data.  | |
| **configureAgentRequest** | [**ConfigureAgentRequest**](ConfigureAgentRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ConfigureAgentResponse**](ConfigureAgentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="createProfilingGroup"></a>
# **createProfilingGroup**
> CreateProfilingGroupResponse createProfilingGroup(clientToken, createProfilingGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a profiling group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String clientToken = "clientToken_example"; // String |  Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental creation of duplicate profiling groups if there are failures and retries. 
    CreateProfilingGroupRequest createProfilingGroupRequest = new CreateProfilingGroupRequest(); // CreateProfilingGroupRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateProfilingGroupResponse result = apiInstance.createProfilingGroup(clientToken, createProfilingGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createProfilingGroup");
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
| **clientToken** | **String**|  Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental creation of duplicate profiling groups if there are failures and retries.  | |
| **createProfilingGroupRequest** | [**CreateProfilingGroupRequest**](CreateProfilingGroupRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateProfilingGroupResponse**](CreateProfilingGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ServiceQuotaExceededException |  -  |
| **481** | InternalServerException |  -  |
| **482** | ConflictException |  -  |
| **483** | ValidationException |  -  |
| **484** | ThrottlingException |  -  |

<a id="deleteProfilingGroup"></a>
# **deleteProfilingGroup**
> Object deleteProfilingGroup(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a profiling group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group to delete.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteProfilingGroup(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteProfilingGroup");
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
| **profilingGroupName** | **String**| The name of the profiling group to delete. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ConflictException |  -  |
| **482** | ValidationException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ResourceNotFoundException |  -  |

<a id="describeProfilingGroup"></a>
# **describeProfilingGroup**
> DescribeProfilingGroupResponse describeProfilingGroup(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\&quot;&gt; &lt;code&gt;ProfilingGroupDescription&lt;/code&gt; &lt;/a&gt; object that contains information about the requested profiling group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String |  The name of the profiling group to get information about. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeProfilingGroupResponse result = apiInstance.describeProfilingGroup(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeProfilingGroup");
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
| **profilingGroupName** | **String**|  The name of the profiling group to get information about.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeProfilingGroupResponse**](DescribeProfilingGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="getFindingsReportAccountSummary"></a>
# **getFindingsReportAccountSummary**
> GetFindingsReportAccountSummaryResponse getFindingsReportAccountSummary(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, dailyReportsOnly, maxResults, nextToken)



 Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html\&quot;&gt; &lt;code&gt;FindingsReportSummary&lt;/code&gt; &lt;/a&gt; objects that contain analysis results for all profiling groups in your AWS account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean dailyReportsOnly = true; // Boolean | A <code>Boolean</code> value indicating whether to only return reports from daily profiles. If set to <code>True</code>, only analysis data from daily profiles is returned. If set to <code>False</code>, analysis data is returned from smaller time windows (for example, one hour).
    Integer maxResults = 56; // Integer | The maximum number of results returned by <code> GetFindingsReportAccountSummary</code> in paginated output. When this parameter is used, <code>GetFindingsReportAccountSummary</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>GetFindingsReportAccountSummary</code> request with the returned <code>nextToken</code> value.
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>GetFindingsReportAccountSummary</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
    try {
      GetFindingsReportAccountSummaryResponse result = apiInstance.getFindingsReportAccountSummary(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, dailyReportsOnly, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFindingsReportAccountSummary");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **dailyReportsOnly** | **Boolean**| A &lt;code&gt;Boolean&lt;/code&gt; value indicating whether to only return reports from daily profiles. If set to &lt;code&gt;True&lt;/code&gt;, only analysis data from daily profiles is returned. If set to &lt;code&gt;False&lt;/code&gt;, analysis data is returned from smaller time windows (for example, one hour). | [optional] |
| **maxResults** | **Integer**| The maximum number of results returned by &lt;code&gt; GetFindingsReportAccountSummary&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;GetFindingsReportAccountSummary&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;GetFindingsReportAccountSummary&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;GetFindingsReportAccountSummary&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

[**GetFindingsReportAccountSummaryResponse**](GetFindingsReportAccountSummaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |

<a id="getNotificationConfiguration"></a>
# **getNotificationConfiguration**
> GetNotificationConfigurationResponse getNotificationConfiguration(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Get the current configuration for anomaly notifications for a profiling group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group we want to get the notification configuration for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetNotificationConfigurationResponse result = apiInstance.getNotificationConfiguration(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getNotificationConfiguration");
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
| **profilingGroupName** | **String**| The name of the profiling group we want to get the notification configuration for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetNotificationConfigurationResponse**](GetNotificationConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="getPolicy"></a>
# **getPolicy**
> GetPolicyResponse getPolicy(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Returns the JSON-formatted resource-based policy on a profiling group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetPolicyResponse result = apiInstance.getPolicy(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPolicy");
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
| **profilingGroupName** | **String**| The name of the profiling group. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetPolicyResponse**](GetPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ThrottlingException |  -  |
| **482** | ResourceNotFoundException |  -  |

<a id="getProfile"></a>
# **getProfile**
> GetProfileResponse getProfile(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, accept, endTime, maxDepth, period, startTime)



&lt;p&gt; Gets the aggregated profile of a profiling group for a specified time range. Amazon CodeGuru Profiler collects posted agent profiles for a profiling group into aggregated profiles. &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;note&amp;gt; &amp;lt;p&amp;gt; Because aggregated profiles expire over time &amp;lt;code&amp;gt;GetProfile&amp;lt;/code&amp;gt; is not idempotent. &amp;lt;/p&amp;gt; &amp;lt;/note&amp;gt; &amp;lt;p&amp;gt; Specify the time range for the requested aggregated profile using 1 or 2 of the following parameters: &amp;lt;code&amp;gt;startTime&amp;lt;/code&amp;gt;, &amp;lt;code&amp;gt;endTime&amp;lt;/code&amp;gt;, &amp;lt;code&amp;gt;period&amp;lt;/code&amp;gt;. The maximum time range allowed is 7 days. If you specify all 3 parameters, an exception is thrown. If you specify only &amp;lt;code&amp;gt;period&amp;lt;/code&amp;gt;, the latest aggregated profile is returned. &amp;lt;/p&amp;gt; &amp;lt;p&amp;gt; Aggregated profiles are available with aggregation periods of 5 minutes, 1 hour, and 1 day, aligned to UTC. The aggregation period of an aggregated profile determines how long it is retained. For more information, see &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html&amp;quot;&amp;gt; &amp;lt;code&amp;gt;AggregatedProfileTime&amp;lt;/code&amp;gt; &amp;lt;/a&amp;gt;. The aggregated profile&#39;s aggregation period determines how long it is retained by CodeGuru Profiler. &amp;lt;/p&amp;gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If the aggregation period is 5 minutes, the aggregated profile is retained for 15 days. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If the aggregation period is 1 hour, the aggregated profile is retained for 60 days. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If the aggregation period is 1 day, the aggregated profile is retained for 3 years. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ul&amp;gt; &amp;lt;p&amp;gt;There are two use cases for calling &amp;lt;code&amp;gt;GetProfile&amp;lt;/code&amp;gt;.&amp;lt;/p&amp;gt; &amp;lt;ol&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If you want to return an aggregated profile that already exists, use &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfileTimes.html&amp;quot;&amp;gt; &amp;lt;code&amp;gt;ListProfileTimes&amp;lt;/code&amp;gt; &amp;lt;/a&amp;gt; to view the time ranges of existing aggregated profiles. Use them in a &amp;lt;code&amp;gt;GetProfile&amp;lt;/code&amp;gt; request to return a specific, existing aggregated profile. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; If you want to return an aggregated profile for a time range that doesn&#39;t align with an existing aggregated profile, then CodeGuru Profiler makes a best effort to combine existing aggregated profiles from the requested time range and return them as one aggregated profile. &amp;lt;/p&amp;gt; &amp;lt;p&amp;gt; If aggregated profiles do not exist for the full time range requested, then aggregated profiles for a smaller time range are returned. For example, if the requested time range is from 00:00 to 00:20, and the existing aggregated profiles are from 00:15 and 00:25, then the aggregated profiles from 00:15 to 00:20 are returned. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ol&amp;gt; &lt;/code&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group to get.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String accept = "accept_example"; // String | <p> The format of the returned profiling data. The format maps to the <code>Accept</code> and <code>Content-Type</code> headers of the HTTP request. You can specify one of the following: or the default . </p> <pre><code> &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;application/json&lt;/code&gt; — standard JSON format &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;application/x-amzn-ion&lt;/code&gt; — the Amazon Ion data format. For more information, see &lt;a href=&quot;http://amzn.github.io/ion-docs/&quot;&gt;Amazon Ion&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; </code></pre>
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | <p> The end time of the requested profile. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p> <p> If you specify <code>endTime</code>, then you must also specify <code>period</code> or <code>startTime</code>, but not both. </p>
    Integer maxDepth = 56; // Integer |  The maximum depth of the stacks in the code that is represented in the aggregated profile. For example, if CodeGuru Profiler finds a method <code>A</code>, which calls method <code>B</code>, which calls method <code>C</code>, which calls method <code>D</code>, then the depth is 4. If the <code>maxDepth</code> is set to 2, then the aggregated profile contains representations of methods <code>A</code> and <code>B</code>. 
    String period = "period_example"; // String | <p> Used with <code>startTime</code> or <code>endTime</code> to specify the time range for the returned aggregated profile. Specify using the ISO 8601 format. For example, <code>P1DT1H1M1S</code>. </p> <pre><code> &lt;p&gt; To get the latest aggregated profile, specify only &lt;code&gt;period&lt;/code&gt;. &lt;/p&gt; </code></pre>
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | <p>The start time of the profile to get. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p> <pre><code> &lt;p&gt; If you specify &lt;code&gt;startTime&lt;/code&gt;, then you must also specify &lt;code&gt;period&lt;/code&gt; or &lt;code&gt;endTime&lt;/code&gt;, but not both. &lt;/p&gt; </code></pre>
    try {
      GetProfileResponse result = apiInstance.getProfile(profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, accept, endTime, maxDepth, period, startTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProfile");
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
| **profilingGroupName** | **String**| The name of the profiling group to get. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **accept** | **String**| &lt;p&gt; The format of the returned profiling data. The format maps to the &lt;code&gt;Accept&lt;/code&gt; and &lt;code&gt;Content-Type&lt;/code&gt; headers of the HTTP request. You can specify one of the following: or the default . &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;code&amp;gt;application/json&amp;lt;/code&amp;gt; — standard JSON format &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;code&amp;gt;application/x-amzn-ion&amp;lt;/code&amp;gt; — the Amazon Ion data format. For more information, see &amp;lt;a href&#x3D;&amp;quot;http://amzn.github.io/ion-docs/&amp;quot;&amp;gt;Amazon Ion&amp;lt;/a&amp;gt;. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ul&amp;gt; &lt;/code&gt;&lt;/pre&gt; | [optional] |
| **endTime** | **OffsetDateTime**| &lt;p&gt; The end time of the requested profile. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. &lt;/p&gt; &lt;p&gt; If you specify &lt;code&gt;endTime&lt;/code&gt;, then you must also specify &lt;code&gt;period&lt;/code&gt; or &lt;code&gt;startTime&lt;/code&gt;, but not both. &lt;/p&gt; | [optional] |
| **maxDepth** | **Integer**|  The maximum depth of the stacks in the code that is represented in the aggregated profile. For example, if CodeGuru Profiler finds a method &lt;code&gt;A&lt;/code&gt;, which calls method &lt;code&gt;B&lt;/code&gt;, which calls method &lt;code&gt;C&lt;/code&gt;, which calls method &lt;code&gt;D&lt;/code&gt;, then the depth is 4. If the &lt;code&gt;maxDepth&lt;/code&gt; is set to 2, then the aggregated profile contains representations of methods &lt;code&gt;A&lt;/code&gt; and &lt;code&gt;B&lt;/code&gt;.  | [optional] |
| **period** | **String**| &lt;p&gt; Used with &lt;code&gt;startTime&lt;/code&gt; or &lt;code&gt;endTime&lt;/code&gt; to specify the time range for the returned aggregated profile. Specify using the ISO 8601 format. For example, &lt;code&gt;P1DT1H1M1S&lt;/code&gt;. &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;p&amp;gt; To get the latest aggregated profile, specify only &amp;lt;code&amp;gt;period&amp;lt;/code&amp;gt;. &amp;lt;/p&amp;gt; &lt;/code&gt;&lt;/pre&gt; | [optional] |
| **startTime** | **OffsetDateTime**| &lt;p&gt;The start time of the profile to get. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.&lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;p&amp;gt; If you specify &amp;lt;code&amp;gt;startTime&amp;lt;/code&amp;gt;, then you must also specify &amp;lt;code&amp;gt;period&amp;lt;/code&amp;gt; or &amp;lt;code&amp;gt;endTime&amp;lt;/code&amp;gt;, but not both. &amp;lt;/p&amp;gt; &lt;/code&gt;&lt;/pre&gt; | [optional] |

### Return type

[**GetProfileResponse**](GetProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="getRecommendations"></a>
# **getRecommendations**
> GetRecommendationsResponse getRecommendations(endTime, profilingGroupName, startTime, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, locale)



 Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation.html\&quot;&gt; &lt;code&gt;Recommendation&lt;/code&gt; &lt;/a&gt; objects that contain recommendations for a profiling group for a given time period. A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Anomaly.html\&quot;&gt; &lt;code&gt;Anomaly&lt;/code&gt; &lt;/a&gt; objects that contains details about anomalies detected in the profiling group for the same time period is also returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime |  The start time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    String profilingGroupName = "profilingGroupName_example"; // String |  The name of the profiling group to get analysis data about. 
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime |  The end time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String locale = "locale_example"; // String | <p> The language used to provide analysis. Specify using a string that is one of the following <code>BCP 47</code> language codes. </p> <ul> <li> <p> <code>de-DE</code> - German, Germany </p> </li> <li> <p> <code>en-GB</code> - English, United Kingdom </p> </li> <li> <p> <code>en-US</code> - English, United States </p> </li> <li> <p> <code>es-ES</code> - Spanish, Spain </p> </li> <li> <p> <code>fr-FR</code> - French, France </p> </li> <li> <p> <code>it-IT</code> - Italian, Italy </p> </li> <li> <p> <code>ja-JP</code> - Japanese, Japan </p> </li> <li> <p> <code>ko-KR</code> - Korean, Republic of Korea </p> </li> <li> <p> <code>pt-BR</code> - Portugese, Brazil </p> </li> <li> <p> <code>zh-CN</code> - Chinese, China </p> </li> <li> <p> <code>zh-TW</code> - Chinese, Taiwan </p> </li> </ul>
    try {
      GetRecommendationsResponse result = apiInstance.getRecommendations(endTime, profilingGroupName, startTime, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecommendations");
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
| **endTime** | **OffsetDateTime**|  The start time of the profile to get analysis data about. You must specify &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.  | |
| **profilingGroupName** | **String**|  The name of the profiling group to get analysis data about.  | |
| **startTime** | **OffsetDateTime**|  The end time of the profile to get analysis data about. You must specify &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **locale** | **String**| &lt;p&gt; The language used to provide analysis. Specify using a string that is one of the following &lt;code&gt;BCP 47&lt;/code&gt; language codes. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;de-DE&lt;/code&gt; - German, Germany &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;en-GB&lt;/code&gt; - English, United Kingdom &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;en-US&lt;/code&gt; - English, United States &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;es-ES&lt;/code&gt; - Spanish, Spain &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;fr-FR&lt;/code&gt; - French, France &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;it-IT&lt;/code&gt; - Italian, Italy &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ja-JP&lt;/code&gt; - Japanese, Japan &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ko-KR&lt;/code&gt; - Korean, Republic of Korea &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pt-BR&lt;/code&gt; - Portugese, Brazil &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;zh-CN&lt;/code&gt; - Chinese, China &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;zh-TW&lt;/code&gt; - Chinese, Taiwan &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] |

### Return type

[**GetRecommendationsResponse**](GetRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="listFindingsReports"></a>
# **listFindingsReports**
> ListFindingsReportsResponse listFindingsReports(endTime, profilingGroupName, startTime, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, dailyReportsOnly, maxResults, nextToken)



List the available reports for a given profiling group and time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime |  The end time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group from which to search for analysis data.
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime |  The start time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean dailyReportsOnly = true; // Boolean | A <code>Boolean</code> value indicating whether to only return reports from daily profiles. If set to <code>True</code>, only analysis data from daily profiles is returned. If set to <code>False</code>, analysis data is returned from smaller time windows (for example, one hour).
    Integer maxResults = 56; // Integer | The maximum number of report results returned by <code>ListFindingsReports</code> in paginated output. When this parameter is used, <code>ListFindingsReports</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListFindingsReports</code> request with the returned <code>nextToken</code> value.
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>ListFindingsReportsRequest</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
    try {
      ListFindingsReportsResponse result = apiInstance.listFindingsReports(endTime, profilingGroupName, startTime, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, dailyReportsOnly, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFindingsReports");
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
| **endTime** | **OffsetDateTime**|  The end time of the profile to get analysis data about. You must specify &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.  | |
| **profilingGroupName** | **String**| The name of the profiling group from which to search for analysis data. | |
| **startTime** | **OffsetDateTime**|  The start time of the profile to get analysis data about. You must specify &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **dailyReportsOnly** | **Boolean**| A &lt;code&gt;Boolean&lt;/code&gt; value indicating whether to only return reports from daily profiles. If set to &lt;code&gt;True&lt;/code&gt;, only analysis data from daily profiles is returned. If set to &lt;code&gt;False&lt;/code&gt;, analysis data is returned from smaller time windows (for example, one hour). | [optional] |
| **maxResults** | **Integer**| The maximum number of report results returned by &lt;code&gt;ListFindingsReports&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListFindingsReports&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListFindingsReports&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListFindingsReportsRequest&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

[**ListFindingsReportsResponse**](ListFindingsReportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="listProfileTimes"></a>
# **listProfileTimes**
> ListProfileTimesResponse listProfileTimes(endTime, period, profilingGroupName, startTime, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, orderBy)



Lists the start times of the available aggregated profiles of a profiling group for an aggregation period within the specified time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | The end time of the time range from which to list the profiles.
    String period = "PT5M"; // String | <p> The aggregation period. This specifies the period during which an aggregation profile collects posted agent profiles for a profiling group. There are 3 valid values. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group.
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | The start time of the time range from which to list the profiles.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of profile time results returned by <code>ListProfileTimes</code> in paginated output. When this parameter is used, <code>ListProfileTimes</code> only returns <code>maxResults</code> results in a single page with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListProfileTimes</code> request with the returned <code>nextToken</code> value. 
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>ListProfileTimes</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
    String orderBy = "TimestampDescending"; // String | The order (ascending or descending by start time of the profile) to use when listing profiles. Defaults to <code>TIMESTAMP_DESCENDING</code>. 
    try {
      ListProfileTimesResponse result = apiInstance.listProfileTimes(endTime, period, profilingGroupName, startTime, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listProfileTimes");
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
| **endTime** | **OffsetDateTime**| The end time of the time range from which to list the profiles. | |
| **period** | **String**| &lt;p&gt; The aggregation period. This specifies the period during which an aggregation profile collects posted agent profiles for a profiling group. There are 3 valid values. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;P1D&lt;/code&gt; — 1 day &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PT1H&lt;/code&gt; — 1 hour &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PT5M&lt;/code&gt; — 5 minutes &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [enum: PT5M, PT1H, P1D] |
| **profilingGroupName** | **String**| The name of the profiling group. | |
| **startTime** | **OffsetDateTime**| The start time of the time range from which to list the profiles. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of profile time results returned by &lt;code&gt;ListProfileTimes&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListProfileTimes&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListProfileTimes&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value.  | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListProfileTimes&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |
| **orderBy** | **String**| The order (ascending or descending by start time of the profile) to use when listing profiles. Defaults to &lt;code&gt;TIMESTAMP_DESCENDING&lt;/code&gt;.  | [optional] [enum: TimestampDescending, TimestampAscending] |

### Return type

[**ListProfileTimesResponse**](ListProfileTimesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="listProfilingGroups"></a>
# **listProfilingGroups**
> ListProfilingGroupsResponse listProfilingGroups(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, includeDescription, maxResults, nextToken)



 Returns a list of profiling groups. The profiling groups are returned as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\&quot;&gt; &lt;code&gt;ProfilingGroupDescription&lt;/code&gt; &lt;/a&gt; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Boolean includeDescription = true; // Boolean | A <code>Boolean</code> value indicating whether to include a description. If <code>true</code>, then a list of <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\"> <code>ProfilingGroupDescription</code> </a> objects that contain detailed information about profiling groups is returned. If <code>false</code>, then a list of profiling group names is returned.
    Integer maxResults = 56; // Integer | The maximum number of profiling groups results returned by <code>ListProfilingGroups</code> in paginated output. When this parameter is used, <code>ListProfilingGroups</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListProfilingGroups</code> request with the returned <code>nextToken</code> value. 
    String nextToken = "nextToken_example"; // String | <p>The <code>nextToken</code> value returned from a previous paginated <code>ListProfilingGroups</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
    try {
      ListProfilingGroupsResponse result = apiInstance.listProfilingGroups(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, includeDescription, maxResults, nextToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listProfilingGroups");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **includeDescription** | **Boolean**| A &lt;code&gt;Boolean&lt;/code&gt; value indicating whether to include a description. If &lt;code&gt;true&lt;/code&gt;, then a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\&quot;&gt; &lt;code&gt;ProfilingGroupDescription&lt;/code&gt; &lt;/a&gt; objects that contain detailed information about profiling groups is returned. If &lt;code&gt;false&lt;/code&gt;, then a list of profiling group names is returned. | [optional] |
| **maxResults** | **Integer**| The maximum number of profiling groups results returned by &lt;code&gt;ListProfilingGroups&lt;/code&gt; in paginated output. When this parameter is used, &lt;code&gt;ListProfilingGroups&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListProfilingGroups&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value.  | [optional] |
| **nextToken** | **String**| &lt;p&gt;The &lt;code&gt;nextToken&lt;/code&gt; value returned from a previous paginated &lt;code&gt;ListProfilingGroups&lt;/code&gt; request where &lt;code&gt;maxResults&lt;/code&gt; was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the &lt;code&gt;nextToken&lt;/code&gt; value. &lt;/p&gt; &lt;note&gt; &lt;p&gt;This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

[**ListProfilingGroupsResponse**](ListProfilingGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ThrottlingException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Returns a list of the tags that are assigned to a specified resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String |  The Amazon Resource Name (ARN) of the resource that contains the tags to return. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
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
| **resourceArn** | **String**|  The Amazon Resource Name (ARN) of the resource that contains the tags to return.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |

<a id="postAgentProfile"></a>
# **postAgentProfile**
> Object postAgentProfile(contentType, profilingGroupName, postAgentProfileRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, profileToken)



 Submits profiling data to an aggregated profile of a profiling group. To get an aggregated profile that is created with this profiling data, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetProfile.html\&quot;&gt; &lt;code&gt;GetProfile&lt;/code&gt; &lt;/a&gt;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String contentType = "contentType_example"; // String | <p> The format of the submitted profiling data. The format maps to the <code>Accept</code> and <code>Content-Type</code> headers of the HTTP request. You can specify one of the following: or the default . </p> <pre><code> &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;application/json&lt;/code&gt; — standard JSON format &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;application/x-amzn-ion&lt;/code&gt; — the Amazon Ion data format. For more information, see &lt;a href=&quot;http://amzn.github.io/ion-docs/&quot;&gt;Amazon Ion&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; </code></pre>
    String profilingGroupName = "profilingGroupName_example"; // String |  The name of the profiling group with the aggregated profile that receives the submitted profiling data. 
    PostAgentProfileRequest postAgentProfileRequest = new PostAgentProfileRequest(); // PostAgentProfileRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String profileToken = "profileToken_example"; // String |  Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental submission of duplicate profiling data if there are failures and retries. 
    try {
      Object result = apiInstance.postAgentProfile(contentType, profilingGroupName, postAgentProfileRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, profileToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postAgentProfile");
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
| **contentType** | **String**| &lt;p&gt; The format of the submitted profiling data. The format maps to the &lt;code&gt;Accept&lt;/code&gt; and &lt;code&gt;Content-Type&lt;/code&gt; headers of the HTTP request. You can specify one of the following: or the default . &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;code&amp;gt;application/json&amp;lt;/code&amp;gt; — standard JSON format &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;code&amp;gt;application/x-amzn-ion&amp;lt;/code&amp;gt; — the Amazon Ion data format. For more information, see &amp;lt;a href&#x3D;&amp;quot;http://amzn.github.io/ion-docs/&amp;quot;&amp;gt;Amazon Ion&amp;lt;/a&amp;gt;. &amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ul&amp;gt; &lt;/code&gt;&lt;/pre&gt; | |
| **profilingGroupName** | **String**|  The name of the profiling group with the aggregated profile that receives the submitted profiling data.  | |
| **postAgentProfileRequest** | [**PostAgentProfileRequest**](PostAgentProfileRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **profileToken** | **String**|  Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental submission of duplicate profiling data if there are failures and retries.  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="putPermission"></a>
# **putPermission**
> PutPermissionResponse putPermission(actionGroup, profilingGroupName, putPermissionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Adds permissions to a profiling group&#39;s resource-based policy that are provided using an action group. If a profiling group doesn&#39;t have a resource-based policy, one is created for it using the permissions in the action group and the roles and users in the &lt;code&gt;principals&lt;/code&gt; parameter. &lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;p&amp;gt; The one supported action group that can be added is &amp;lt;code&amp;gt;agentPermission&amp;lt;/code&amp;gt; which grants &amp;lt;code&amp;gt;ConfigureAgent&amp;lt;/code&amp;gt; and &amp;lt;code&amp;gt;PostAgent&amp;lt;/code&amp;gt; permissions. For more information, see &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html&amp;quot;&amp;gt;Resource-based policies in CodeGuru Profiler&amp;lt;/a&amp;gt; in the &amp;lt;i&amp;gt;Amazon CodeGuru Profiler User Guide&amp;lt;/i&amp;gt;, &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html&amp;quot;&amp;gt; &amp;lt;code&amp;gt;ConfigureAgent&amp;lt;/code&amp;gt; &amp;lt;/a&amp;gt;, and &amp;lt;a href&#x3D;&amp;quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html&amp;quot;&amp;gt; &amp;lt;code&amp;gt;PostAgentProfile&amp;lt;/code&amp;gt; &amp;lt;/a&amp;gt;. &amp;lt;/p&amp;gt; &amp;lt;p&amp;gt; The first time you call &amp;lt;code&amp;gt;PutPermission&amp;lt;/code&amp;gt; on a profiling group, do not specify a &amp;lt;code&amp;gt;revisionId&amp;lt;/code&amp;gt; because it doesn&#39;t have a resource-based policy. Subsequent calls must provide a &amp;lt;code&amp;gt;revisionId&amp;lt;/code&amp;gt; to specify which revision of the resource-based policy to add the permissions to. &amp;lt;/p&amp;gt; &amp;lt;p&amp;gt; The response contains the profiling group&#39;s JSON-formatted resource policy. &amp;lt;/p&amp;gt; &lt;/code&gt;&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String actionGroup = "agentPermissions"; // String |  Specifies an action group that contains permissions to add to a profiling group resource. One action group is supported, <code>agentPermissions</code>, which grants permission to perform actions required by the profiling agent, <code>ConfigureAgent</code> and <code>PostAgentProfile</code> permissions. 
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group to grant access to.
    PutPermissionRequest putPermissionRequest = new PutPermissionRequest(); // PutPermissionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutPermissionResponse result = apiInstance.putPermission(actionGroup, profilingGroupName, putPermissionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putPermission");
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
| **actionGroup** | **String**|  Specifies an action group that contains permissions to add to a profiling group resource. One action group is supported, &lt;code&gt;agentPermissions&lt;/code&gt;, which grants permission to perform actions required by the profiling agent, &lt;code&gt;ConfigureAgent&lt;/code&gt; and &lt;code&gt;PostAgentProfile&lt;/code&gt; permissions.  | [enum: agentPermissions] |
| **profilingGroupName** | **String**| The name of the profiling group to grant access to. | |
| **putPermissionRequest** | [**PutPermissionRequest**](PutPermissionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutPermissionResponse**](PutPermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ConflictException |  -  |
| **482** | ValidationException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ResourceNotFoundException |  -  |

<a id="removeNotificationChannel"></a>
# **removeNotificationChannel**
> RemoveNotificationChannelResponse removeNotificationChannel(channelId, profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Remove one anomaly notifications channel for a profiling group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelId = "channelId_example"; // String | The id of the channel that we want to stop receiving notifications.
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group we want to change notification configuration for.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RemoveNotificationChannelResponse result = apiInstance.removeNotificationChannel(channelId, profilingGroupName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeNotificationChannel");
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
| **channelId** | **String**| The id of the channel that we want to stop receiving notifications. | |
| **profilingGroupName** | **String**| The name of the profiling group we want to change notification configuration for. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RemoveNotificationChannelResponse**](RemoveNotificationChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="removePermission"></a>
# **removePermission**
> RemovePermissionResponse removePermission(actionGroup, profilingGroupName, revisionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Removes permissions from a profiling group&#39;s resource-based policy that are provided using an action group. The one supported action group that can be removed is &lt;code&gt;agentPermission&lt;/code&gt; which grants &lt;code&gt;ConfigureAgent&lt;/code&gt; and &lt;code&gt;PostAgent&lt;/code&gt; permissions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html\&quot;&gt;Resource-based policies in CodeGuru Profiler&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Profiler User Guide&lt;/i&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html\&quot;&gt; &lt;code&gt;ConfigureAgent&lt;/code&gt; &lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html\&quot;&gt; &lt;code&gt;PostAgentProfile&lt;/code&gt; &lt;/a&gt;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String actionGroup = "agentPermissions"; // String |  Specifies an action group that contains the permissions to remove from a profiling group's resource-based policy. One action group is supported, <code>agentPermissions</code>, which grants <code>ConfigureAgent</code> and <code>PostAgentProfile</code> permissions. 
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group.
    String revisionId = "revisionId_example"; // String |  A universally unique identifier (UUID) for the revision of the resource-based policy from which you want to remove permissions. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RemovePermissionResponse result = apiInstance.removePermission(actionGroup, profilingGroupName, revisionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removePermission");
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
| **actionGroup** | **String**|  Specifies an action group that contains the permissions to remove from a profiling group&#39;s resource-based policy. One action group is supported, &lt;code&gt;agentPermissions&lt;/code&gt;, which grants &lt;code&gt;ConfigureAgent&lt;/code&gt; and &lt;code&gt;PostAgentProfile&lt;/code&gt; permissions.  | [enum: agentPermissions] |
| **profilingGroupName** | **String**| The name of the profiling group. | |
| **revisionId** | **String**|  A universally unique identifier (UUID) for the revision of the resource-based policy from which you want to remove permissions.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RemovePermissionResponse**](RemovePermissionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ConflictException |  -  |
| **482** | ValidationException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ResourceNotFoundException |  -  |

<a id="submitFeedback"></a>
# **submitFeedback**
> Object submitFeedback(anomalyInstanceId, profilingGroupName, submitFeedbackRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Sends feedback to CodeGuru Profiler about whether the anomaly detected by the analysis is useful or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String anomalyInstanceId = "anomalyInstanceId_example"; // String | The universally unique identifier (UUID) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AnomalyInstance.html\"> <code>AnomalyInstance</code> </a> object that is included in the analysis data.
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group that is associated with the analysis data.
    SubmitFeedbackRequest submitFeedbackRequest = new SubmitFeedbackRequest(); // SubmitFeedbackRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.submitFeedback(anomalyInstanceId, profilingGroupName, submitFeedbackRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#submitFeedback");
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
| **anomalyInstanceId** | **String**| The universally unique identifier (UUID) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AnomalyInstance.html\&quot;&gt; &lt;code&gt;AnomalyInstance&lt;/code&gt; &lt;/a&gt; object that is included in the analysis data. | |
| **profilingGroupName** | **String**| The name of the profiling group that is associated with the analysis data. | |
| **submitFeedbackRequest** | [**SubmitFeedbackRequest**](SubmitFeedbackRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | ResourceNotFoundException |  -  |

<a id="tagResource"></a>
# **tagResource**
> Object tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Use to assign one or more tags to a resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String |  The Amazon Resource Name (ARN) of the resource that the tags are added to. 
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
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
| **resourceArn** | **String**|  The Amazon Resource Name (ARN) of the resource that the tags are added to.  | |
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |

<a id="untagResource"></a>
# **untagResource**
> Object untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Use to remove one or more tags from a resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceArn = "resourceArn_example"; // String |  The Amazon Resource Name (ARN) of the resource that contains the tags to remove. 
    List<String> tagKeys = Arrays.asList(); // List<String> |  A list of tag keys. Existing tags of resources with keys in this list are removed from the specified resource. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
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
| **resourceArn** | **String**|  The Amazon Resource Name (ARN) of the resource that contains the tags to remove.  | |
| **tagKeys** | [**List&lt;String&gt;**](String.md)|  A list of tag keys. Existing tags of resources with keys in this list are removed from the specified resource.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ValidationException |  -  |
| **482** | ResourceNotFoundException |  -  |

<a id="updateProfilingGroup"></a>
# **updateProfilingGroup**
> UpdateProfilingGroupResponse updateProfilingGroup(profilingGroupName, updateProfilingGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates a profiling group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://codeguru-profiler.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String profilingGroupName = "profilingGroupName_example"; // String | The name of the profiling group to update.
    UpdateProfilingGroupRequest updateProfilingGroupRequest = new UpdateProfilingGroupRequest(); // UpdateProfilingGroupRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateProfilingGroupResponse result = apiInstance.updateProfilingGroup(profilingGroupName, updateProfilingGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateProfilingGroup");
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
| **profilingGroupName** | **String**| The name of the profiling group to update. | |
| **updateProfilingGroupRequest** | [**UpdateProfilingGroupRequest**](UpdateProfilingGroupRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateProfilingGroupResponse**](UpdateProfilingGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalServerException |  -  |
| **481** | ConflictException |  -  |
| **482** | ValidationException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | ResourceNotFoundException |  -  |

