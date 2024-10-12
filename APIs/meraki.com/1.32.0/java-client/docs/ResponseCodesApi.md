# ResponseCodesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationApiRequestsOverviewResponseCodesByInterval_3**](ResponseCodesApi.md#getOrganizationApiRequestsOverviewResponseCodesByInterval_3) | **GET** /organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval | Tracks organizations&#39; API requests by response code across a given time period |


<a id="getOrganizationApiRequestsOverviewResponseCodesByInterval_3"></a>
# **getOrganizationApiRequestsOverviewResponseCodesByInterval_3**
> List&lt;GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner&gt; getOrganizationApiRequestsOverviewResponseCodesByInterval_3(organizationId, t0, t1, timespan, interval, version, operationIds, sourceIps, adminIds, userAgent)

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
import org.openapitools.client.api.ResponseCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ResponseCodesApi apiInstance = new ResponseCodesApi(defaultClient);
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
      List<GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner> result = apiInstance.getOrganizationApiRequestsOverviewResponseCodesByInterval_3(organizationId, t0, t1, timespan, interval, version, operationIds, sourceIps, adminIds, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseCodesApi#getOrganizationApiRequestsOverviewResponseCodesByInterval_3");
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

