# PerformanceReportApi

All URIs are relative to *https://www.googleapis.com/adexchangebuyer/v1.3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adexchangebuyerPerformanceReportList**](PerformanceReportApi.md#adexchangebuyerPerformanceReportList) | **GET** /performancereport |  |


<a id="adexchangebuyerPerformanceReportList"></a>
# **adexchangebuyerPerformanceReportList**
> PerformanceReportList adexchangebuyerPerformanceReportList(accountId, endDateTime, startDateTime, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken)



Retrieves the authenticated user&#39;s list of performance metrics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerformanceReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adexchangebuyer/v1.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PerformanceReportApi apiInstance = new PerformanceReportApi(defaultClient);
    String accountId = "accountId_example"; // String | The account id to get the reports.
    String endDateTime = "endDateTime_example"; // String | The end time of the report in ISO 8601 timestamp format using UTC.
    String startDateTime = "startDateTime_example"; // String | The start time of the report in ISO 8601 timestamp format using UTC.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | Maximum number of entries returned on one result page. If not set, the default is 100. Optional.
    String pageToken = "pageToken_example"; // String | A continuation token, used to page through performance reports. To retrieve the next page, set this parameter to the value of \"nextPageToken\" from the previous response. Optional.
    try {
      PerformanceReportList result = apiInstance.adexchangebuyerPerformanceReportList(accountId, endDateTime, startDateTime, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerformanceReportApi#adexchangebuyerPerformanceReportList");
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
| **accountId** | **String**| The account id to get the reports. | |
| **endDateTime** | **String**| The end time of the report in ISO 8601 timestamp format using UTC. | |
| **startDateTime** | **String**| The start time of the report in ISO 8601 timestamp format using UTC. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| Maximum number of entries returned on one result page. If not set, the default is 100. Optional. | [optional] |
| **pageToken** | **String**| A continuation token, used to page through performance reports. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. Optional. | [optional] |

### Return type

[**PerformanceReportList**](PerformanceReportList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

