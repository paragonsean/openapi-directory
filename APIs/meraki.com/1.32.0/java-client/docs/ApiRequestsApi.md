# ApiRequestsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationApiRequestsOverviewResponseCodesByInterval_1**](ApiRequestsApi.md#getOrganizationApiRequestsOverviewResponseCodesByInterval_1) | **GET** /organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval | Tracks organizations&#39; API requests by response code across a given time period |
| [**getOrganizationApiRequestsOverview_1**](ApiRequestsApi.md#getOrganizationApiRequestsOverview_1) | **GET** /organizations/{organizationId}/apiRequests/overview | Return an aggregated overview of API requests data |
| [**getOrganizationApiRequests_1**](ApiRequestsApi.md#getOrganizationApiRequests_1) | **GET** /organizations/{organizationId}/apiRequests | List the API requests made by an organization |


<a id="getOrganizationApiRequestsOverviewResponseCodesByInterval_1"></a>
# **getOrganizationApiRequestsOverviewResponseCodesByInterval_1**
> List&lt;GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner&gt; getOrganizationApiRequestsOverviewResponseCodesByInterval_1(organizationId, t0, t1, timespan, interval, version, operationIds, sourceIps, adminIds, userAgent)

Tracks organizations&#39; API requests by response code across a given time period

Tracks organizations&#39; API requests by response code across a given time period

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApiRequestsApi apiInstance = new ApiRequestsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
    Integer interval = 56; // Integer | The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
    Integer version = 0; // Integer | Filter by API version of the endpoint. Allowable values are: [0, 1]
    List<String> operationIds = Arrays.asList(); // List<String> | Filter by operation ID of the endpoint
    List<String> sourceIps = Arrays.asList(); // List<String> | Filter by source IP that made the API request
    List<String> adminIds = Arrays.asList(); // List<String> | Filter by admin ID of user that made the API request
    String userAgent = "userAgent_example"; // String | Filter by user agent string for API request. This will filter by a complete or partial match.
    try {
      List<GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner> result = apiInstance.getOrganizationApiRequestsOverviewResponseCodesByInterval_1(organizationId, t0, t1, timespan, interval, version, operationIds, sourceIps, adminIds, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiRequestsApi#getOrganizationApiRequestsOverviewResponseCodesByInterval_1");
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
| **organizationId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated. | [optional] |
| **interval** | **Integer**| The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided. | [optional] |
| **version** | **Integer**| Filter by API version of the endpoint. Allowable values are: [0, 1] | [optional] [enum: 0, 1] |
| **operationIds** | [**List&lt;String&gt;**](String.md)| Filter by operation ID of the endpoint | [optional] |
| **sourceIps** | [**List&lt;String&gt;**](String.md)| Filter by source IP that made the API request | [optional] |
| **adminIds** | [**List&lt;String&gt;**](String.md)| Filter by admin ID of user that made the API request | [optional] |
| **userAgent** | **String**| Filter by user agent string for API request. This will filter by a complete or partial match. | [optional] |

### Return type

[**List&lt;GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner&gt;**](GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationApiRequestsOverview_1"></a>
# **getOrganizationApiRequestsOverview_1**
> Object getOrganizationApiRequestsOverview_1(organizationId, t0, t1, timespan)

Return an aggregated overview of API requests data

Return an aggregated overview of API requests data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApiRequestsApi apiInstance = new ApiRequestsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    try {
      Object result = apiInstance.getOrganizationApiRequestsOverview_1(organizationId, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiRequestsApi#getOrganizationApiRequestsOverview_1");
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
| **organizationId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationApiRequests_1"></a>
# **getOrganizationApiRequests_1**
> List&lt;GetOrganizationApiRequests200ResponseInner&gt; getOrganizationApiRequests_1(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, adminId, path, method, responseCode, sourceIp, userAgent, version, operationIds)

List the API requests made by an organization

List the API requests made by an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ApiRequestsApi apiInstance = new ApiRequestsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String adminId = "adminId_example"; // String | Filter the results by the ID of the admin who made the API requests
    String path = "path_example"; // String | Filter the results by the path of the API requests
    String method = "DELETE"; // String | Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE')
    Integer responseCode = 56; // Integer | Filter the results by the response code of the API requests
    String sourceIp = "sourceIp_example"; // String | Filter the results by the IP address of the originating API request
    String userAgent = "userAgent_example"; // String | Filter the results by the user agent string of the API request
    Integer version = 0; // Integer | Filter the results by the API version of the API request
    List<String> operationIds = Arrays.asList(); // List<String> | Filter the results by one or more operation IDs for the API request
    try {
      List<GetOrganizationApiRequests200ResponseInner> result = apiInstance.getOrganizationApiRequests_1(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, adminId, path, method, responseCode, sourceIp, userAgent, version, operationIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiRequestsApi#getOrganizationApiRequests_1");
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
| **organizationId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **adminId** | **String**| Filter the results by the ID of the admin who made the API requests | [optional] |
| **path** | **String**| Filter the results by the path of the API requests | [optional] |
| **method** | **String**| Filter the results by the method of the API requests (must be &#39;GET&#39;, &#39;PUT&#39;, &#39;POST&#39; or &#39;DELETE&#39;) | [optional] [enum: DELETE, GET, POST, PUT] |
| **responseCode** | **Integer**| Filter the results by the response code of the API requests | [optional] |
| **sourceIp** | **String**| Filter the results by the IP address of the originating API request | [optional] |
| **userAgent** | **String**| Filter the results by the user agent string of the API request | [optional] |
| **version** | **Integer**| Filter the results by the API version of the API request | [optional] [enum: 0, 1] |
| **operationIds** | [**List&lt;String&gt;**](String.md)| Filter the results by one or more operation IDs for the API request | [optional] |

### Return type

[**List&lt;GetOrganizationApiRequests200ResponseInner&gt;**](GetOrganizationApiRequests200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

