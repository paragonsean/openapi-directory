# ReportsApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReport**](ReportsApi.md#getReport) | **GET** /reports/{reportId} | fetch a specific report |
| [**getReports**](ReportsApi.md#getReports) | **GET** /reports | fetch all reports |
| [**messagesReport**](ReportsApi.md#messagesReport) | **POST** /reports/messages | submit a request for a messages report |


<a id="getReport"></a>
# **getReport**
> GetReport200Response getReport(contentLanguage, authorization, accept, acceptCharset, contentType, reportId, telstraApiVersion)

fetch a specific report

Fetch a download link for a report generated with POST /reports/{reportId} using the **reportId** returned in the response. Once ready, your report will be available for download for one week. 

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
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    UUID reportId = UUID.randomUUID(); // UUID | Use the reportId returned in the POST /reports/{reportType} response. 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      GetReport200Response result = apiInstance.getReport(contentLanguage, authorization, accept, acceptCharset, contentType, reportId, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getReport");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **reportId** | **UUID**| Use the reportId returned in the POST /reports/{reportType} response.  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**GetReport200Response**](GetReport200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 OK response means the call has been successful. Your download link (reportUrl) will be returned in the response.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the [API status page](https://dev.telstra.com/api/status) to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the [API status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the [API status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="getReports"></a>
# **getReports**
> GetReports200Response getReports(contentLanguage, authorization, accept, acceptCharset, contentType, telstraApiVersion)

fetch all reports

Fetch details of all reports recently generated for your account. Use it to check the status of a report, plus fetch the report ID, status, report type and expiry date. 

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
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      GetReports200Response result = apiInstance.getReports(contentLanguage, authorization, accept, acceptCharset, contentType, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getReports");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**GetReports200Response**](GetReports200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 OK response means the call has been successful. Details of any report(s) generated for your account will be returned in the response.  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the [API status page](https://dev.telstra.com/api/status) to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the [API status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the [API status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="messagesReport"></a>
# **messagesReport**
> MessagesReport201Response messagesReport(contentLanguage, authorization, accept, acceptCharset, contentType, messagesReportRequest, telstraApiVersion)

submit a request for a messages report

Request a CSV report of messages (both incoming and outgoing) that have been sent to/from your account within the last three months. You can request details for a specific timeframe, and filter your messages by tags, recipient number or Virtual Number.  A 201 Created means your report has been queued for generation. Make a note of the reportId returned in the response. You&#39;ll need this to check the status of your report and fetch your download link with GET reports/{reportId}. If you supplied a reportCallbackUrl in the request we&#39;ll also notify it when your report is ready for download.  Once your report is generated, it will be available for download for one week. The expiry date is returned in the response. 

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
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    MessagesReportRequest messagesReportRequest = new MessagesReportRequest(); // MessagesReportRequest | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      MessagesReport201Response result = apiInstance.messagesReport(contentLanguage, authorization, accept, acceptCharset, contentType, messagesReportRequest, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#messagesReport");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **messagesReportRequest** | [**MessagesReportRequest**](MessagesReportRequest.md)|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**MessagesReport201Response**](MessagesReport201Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A 201 Created response means the call has been successful. Your report is in the queue to be generated.  |  * Content-Language -  <br>  * Location -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_LENGTH_ERR | Check the field is within character limits. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the [API status page](https://dev.telstra.com/api/status) to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is POST. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the [API status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the [API status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

