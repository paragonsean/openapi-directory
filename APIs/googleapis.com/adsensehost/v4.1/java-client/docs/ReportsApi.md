# ReportsApi

All URIs are relative to *https://www.googleapis.com/adsensehost/v4.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adsensehostReportsGenerate**](ReportsApi.md#adsensehostReportsGenerate) | **GET** /reports |  |


<a id="adsensehostReportsGenerate"></a>
# **adsensehostReportsGenerate**
> Report adsensehostReportsGenerate(startDate, endDate, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, dimension, filter, locale, maxResults, metric, sort, startIndex)



Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify \&quot;alt&#x3D;csv\&quot; as a query parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/adsensehost/v4.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String startDate = "startDate_example"; // String | Start of the date range to report on in \"YYYY-MM-DD\" format, inclusive.
    String endDate = "endDate_example"; // String | End of the date range to report on in \"YYYY-MM-DD\" format, inclusive.
    String alt = "csv"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    List<String> dimension = Arrays.asList(); // List<String> | Dimensions to base the report on.
    List<String> filter = Arrays.asList(); // List<String> | Filters to be run on the report.
    String locale = "locale_example"; // String | Optional locale to use for translating report output to a local language. Defaults to \"en_US\" if not specified.
    Integer maxResults = 56; // Integer | The maximum number of rows of report data to return.
    List<String> metric = Arrays.asList(); // List<String> | Numeric columns to include in the report.
    List<String> sort = Arrays.asList(); // List<String> | The name of a dimension or metric to sort the resulting report on, optionally prefixed with \"+\" to sort ascending or \"-\" to sort descending. If no prefix is specified, the column is sorted ascending.
    Integer startIndex = 56; // Integer | Index of the first row of report data to return.
    try {
      Report result = apiInstance.adsensehostReportsGenerate(startDate, endDate, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, dimension, filter, locale, maxResults, metric, sort, startIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#adsensehostReportsGenerate");
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
| **startDate** | **String**| Start of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive. | |
| **endDate** | **String**| End of the date range to report on in \&quot;YYYY-MM-DD\&quot; format, inclusive. | |
| **alt** | **String**| Data format for the response. | [optional] [enum: csv, json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **dimension** | [**List&lt;String&gt;**](String.md)| Dimensions to base the report on. | [optional] |
| **filter** | [**List&lt;String&gt;**](String.md)| Filters to be run on the report. | [optional] |
| **locale** | **String**| Optional locale to use for translating report output to a local language. Defaults to \&quot;en_US\&quot; if not specified. | [optional] |
| **maxResults** | **Integer**| The maximum number of rows of report data to return. | [optional] |
| **metric** | [**List&lt;String&gt;**](String.md)| Numeric columns to include in the report. | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The name of a dimension or metric to sort the resulting report on, optionally prefixed with \&quot;+\&quot; to sort ascending or \&quot;-\&quot; to sort descending. If no prefix is specified, the column is sorted ascending. | [optional] |
| **startIndex** | **Integer**| Index of the first row of report data to return. | [optional] |

### Return type

[**Report**](Report.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

