# DefaultApi

All URIs are relative to *https://api.nexmo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelReport**](DefaultApi.md#cancelReport) | **DELETE** /v2/reports/{report_id} | Cancel the execution of a report |
| [**createAsyncReport**](DefaultApi.md#createAsyncReport) | **POST** /v2/reports | Create an asynchronous report |
| [**downloadReport**](DefaultApi.md#downloadReport) | **GET** /v3/media/{file_id} | Get report data |
| [**getRecords**](DefaultApi.md#getRecords) | **GET** /v2/reports/records | Load records synchronously |
| [**getReport**](DefaultApi.md#getReport) | **GET** /v2/reports/{report_id} | Get status of report |
| [**listReports**](DefaultApi.md#listReports) | **GET** /v2/reports | List reports |


<a id="cancelReport"></a>
# **cancelReport**
> GetReport200Response cancelReport(reportId)

Cancel the execution of a report

Cancel the execution of a pending or processing report.

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String reportId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | UUID of the report
    try {
      GetReport200Response result = apiInstance.cancelReport(reportId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cancelReport");
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
| **reportId** | **String**| UUID of the report | |

### Return type

[**GetReport200Response**](GetReport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **409** | Invalid Abort Operation |  -  |

<a id="createAsyncReport"></a>
# **createAsyncReport**
> CreateAsyncReport200Response createAsyncReport(createAsyncReportRequest)

Create an asynchronous report

Request a report on your account activity

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAsyncReportRequest createAsyncReportRequest = new CreateAsyncReportRequest(); // CreateAsyncReportRequest | The parameters of the JSON body will be used to create and filter the report.<br> The value of the `product` field will define which product the report will be created for and which parameters are accepted. 
    try {
      CreateAsyncReport200Response result = apiInstance.createAsyncReport(createAsyncReportRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAsyncReport");
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
| **createAsyncReportRequest** | [**CreateAsyncReportRequest**](CreateAsyncReportRequest.md)| The parameters of the JSON body will be used to create and filter the report.&lt;br&gt; The value of the &#x60;product&#x60; field will define which product the report will be created for and which parameters are accepted.  | [optional] |

### Return type

[**CreateAsyncReport200Response**](CreateAsyncReport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |

<a id="downloadReport"></a>
# **downloadReport**
> DownloadReport200Response downloadReport(fileId)

Get report data

Download a zipped archive of the rendered report. The file is available for download for 72 hours.&lt;br&gt; The zip file will be named &#x60;&lt;PRODUCT&gt;_&lt;REPORT_ID&gt;.zip&#x60;&lt;br&gt; The csv file in the zip archive will be named as &#x60;report_&lt;PRODUCT&gt;_&lt;ACCOUNT_ID&gt;_&lt;DATE&gt;.csv&#x60; the date will be formatted as &#x60;yyyyMMdd&#x60;. 

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String fileId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | UUID of the file.
    try {
      DownloadReport200Response result = apiInstance.downloadReport(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#downloadReport");
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
| **fileId** | **String**| UUID of the file. | |

### Return type

[**DownloadReport200Response**](DownloadReport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Zip file containing CSV files |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="getRecords"></a>
# **getRecords**
> GetRecords200Response getRecords(accountId, product, direction, id, dateStart, dateEnd, includeMessage, showConcatenated, status)

Load records synchronously

Fetch usage data synchronously

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "abcd1234"; // String | The account for which the list of reports will be queried.
    String product = "SMS"; // String | The product to return records for
    String direction = "inbound"; // String | Direction of the communication, either `inbound` (received by our services), or `outbound` (originated from our services). Required for products `SMS` and `MESSAGES`. Optional for `VOICE-CALL`. Invalid for `IN-APP-VOICE`, `CONVERSATIONS`, `NUMBER-INSIGHT`, `VERIFY-API`.
    String id = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The UUID of the message or call to be searched for. You can specify a comma-separated list of UUIDs. If UUIDs are not found they are listed in the response in the `ids_not_found` field.  If you specify `id`, you must not specify `status`, `date_start` or `date_end`. 
    LocalDate dateStart = LocalDate.parse("2017-12-01T00:00:00+0000"); // LocalDate | ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format `yyyy-mm-ddThh:mm:ss[.sss]±hh:mm` or `yyyy-mm-ddThh:mm:ss[.sss]Z`) for when reports should begin.   It filters on the time the API call was received by Vonage and corresponds to the field `date_received` (`date_start` for Voice) in the report file. It is inclusive, i.e. the provided value is less than or equal to the value in the field `date_received` (`date_start` for Voice) in the CDR.  If you provide this, you must provide `date_end` and must not provide `id`. 
    LocalDate dateEnd = LocalDate.parse("2018-01-01T00:00:00+0000"); // LocalDate | **Must be no more than 24 hours later than `date_start`**  ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format `yyyy-mm-ddThh:mm:ss[.sss]±hh:mm` or `yyyy-mm-ddThh:mm:ss[.sss]Z`) for when report should end.  It is exclusive, i.e. the provided value is strictly greater than the value in the field `date_received` in the CDR.  If you provide this, you must provide `date_start` and must not provide `id`. 
    Boolean includeMessage = false; // Boolean | Include the message contents in the records. Only applicable for use with products `SMS` and `MESSAGES`, where it is optional.
    Boolean showConcatenated = false; // Boolean | Indicates whether the SMS was split up into multiple parts (due to its length).
    String status = "delivered"; // String | The SMS status to search for. Optional where product is `SMS`.
    try {
      GetRecords200Response result = apiInstance.getRecords(accountId, product, direction, id, dateStart, dateEnd, includeMessage, showConcatenated, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecords");
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
| **accountId** | **String**| The account for which the list of reports will be queried. | |
| **product** | **String**| The product to return records for | [enum: SMS, VOICE-CALL, VOICE-FAILED, IN-APP-VOICE, WEBSOCKET-CALL, VERIFY-API, NUMBER-INSIGHT, MESSAGES, ASR, CONVERSATIONS, REPORTS-USAGE] |
| **direction** | **String**| Direction of the communication, either &#x60;inbound&#x60; (received by our services), or &#x60;outbound&#x60; (originated from our services). Required for products &#x60;SMS&#x60; and &#x60;MESSAGES&#x60;. Optional for &#x60;VOICE-CALL&#x60;. Invalid for &#x60;IN-APP-VOICE&#x60;, &#x60;CONVERSATIONS&#x60;, &#x60;NUMBER-INSIGHT&#x60;, &#x60;VERIFY-API&#x60;. | [optional] [enum: inbound, outbound] |
| **id** | **String**| The UUID of the message or call to be searched for. You can specify a comma-separated list of UUIDs. If UUIDs are not found they are listed in the response in the &#x60;ids_not_found&#x60; field.  If you specify &#x60;id&#x60;, you must not specify &#x60;status&#x60;, &#x60;date_start&#x60; or &#x60;date_end&#x60;.  | [optional] |
| **dateStart** | **LocalDate**| ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;) for when reports should begin.   It filters on the time the API call was received by Vonage and corresponds to the field &#x60;date_received&#x60; (&#x60;date_start&#x60; for Voice) in the report file. It is inclusive, i.e. the provided value is less than or equal to the value in the field &#x60;date_received&#x60; (&#x60;date_start&#x60; for Voice) in the CDR.  If you provide this, you must provide &#x60;date_end&#x60; and must not provide &#x60;id&#x60;.  | [optional] |
| **dateEnd** | **LocalDate**| **Must be no more than 24 hours later than &#x60;date_start&#x60;**  ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;) for when report should end.  It is exclusive, i.e. the provided value is strictly greater than the value in the field &#x60;date_received&#x60; in the CDR.  If you provide this, you must provide &#x60;date_start&#x60; and must not provide &#x60;id&#x60;.  | [optional] |
| **includeMessage** | **Boolean**| Include the message contents in the records. Only applicable for use with products &#x60;SMS&#x60; and &#x60;MESSAGES&#x60;, where it is optional. | [optional] [default to false] |
| **showConcatenated** | **Boolean**| Indicates whether the SMS was split up into multiple parts (due to its length). | [optional] [default to false] |
| **status** | **String**| The SMS status to search for. Optional where product is &#x60;SMS&#x60;. | [optional] [default to none] [enum: delivered, expired, failed, rejected, accepted, buffered, unknown, deleted] |

### Return type

[**GetRecords200Response**](GetRecords200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Unprocessable entity |  -  |
| **422** | Unprocessable entity |  -  |

<a id="getReport"></a>
# **getReport**
> GetReport200Response getReport(reportId)

Get status of report

Retrieve status and metadata about a requested report.

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String reportId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | UUID of the report request (`request_id` in response).
    try {
      GetReport200Response result = apiInstance.getReport(reportId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReport");
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
| **reportId** | **String**| UUID of the report request (&#x60;request_id&#x60; in response). | |

### Return type

[**GetReport200Response**](GetReport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="listReports"></a>
# **listReports**
> ListReports200Response listReports(accountId, status, dateFrom, dateTo)

List reports

List reports created by the specified account based on filtered provided.

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "abcd1234"; // String | The account for which the list of reports will be queried.
    String status = "SUCCESS, FAILED"; // String | A comma-separated list of report status values. Reports with any of the statuses specified are returned. The values in the comma-seperated list specified for `status` can be any of `PENDING`, `PROCESSING`, `SUCCESS`, `ABORTED`, `FAILED`, `TRUNCATED`.
    LocalDate dateFrom = LocalDate.parse("2019-06-28T00:00:00-00:00"); // LocalDate | ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date from which the list of reports will be queried. Format `yyyy-mm-ddThh:mm:ss[.sss]±hh:mm` or `yyyy-mm-ddThh:mm:ss[.sss]Z`.
    LocalDate dateTo = LocalDate.parse("2019-06-28T23:59:59-00:00"); // LocalDate | ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date until which the list of reports will be queried. Format `yyyy-mm-ddThh:mm:ss[.sss]±hh:mm` or `yyyy-mm-ddThh:mm:ss[.sss]Z`.
    try {
      ListReports200Response result = apiInstance.listReports(accountId, status, dateFrom, dateTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listReports");
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
| **accountId** | **String**| The account for which the list of reports will be queried. | |
| **status** | **String**| A comma-separated list of report status values. Reports with any of the statuses specified are returned. The values in the comma-seperated list specified for &#x60;status&#x60; can be any of &#x60;PENDING&#x60;, &#x60;PROCESSING&#x60;, &#x60;SUCCESS&#x60;, &#x60;ABORTED&#x60;, &#x60;FAILED&#x60;, &#x60;TRUNCATED&#x60;. | |
| **dateFrom** | **LocalDate**| ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date from which the list of reports will be queried. Format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;. | [optional] |
| **dateTo** | **LocalDate**| ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date until which the list of reports will be queried. Format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;. | [optional] |

### Return type

[**ListReports200Response**](ListReports200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

