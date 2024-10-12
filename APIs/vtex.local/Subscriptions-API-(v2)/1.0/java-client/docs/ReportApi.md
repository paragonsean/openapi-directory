# ReportApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getreportstatusbyID**](ReportApi.md#getreportstatusbyID) | **GET** /report/reportStatus/{reportId} | Get report status by ID |
| [**requestreportbyStatus**](ReportApi.md#requestreportbyStatus) | **GET** /report/subscriptionsByStatus | Retrieve Subscription report by Status |
| [**requestreportbydate**](ReportApi.md#requestreportbydate) | **GET** /report/subscriptionsByDate | Retrieve Subscription report by date |
| [**requestreportbyorderdate**](ReportApi.md#requestreportbyorderdate) | **GET** /report/subscriptionsOrderByDate | Retrieve Subscription report by order date |
| [**requestreportbyschedule**](ReportApi.md#requestreportbyschedule) | **GET** /report/subscriptionsScheduled | Retrieve Subscription report by schedule |
| [**requestreportbyupdate**](ReportApi.md#requestreportbyupdate) | **GET** /report/subscriptionsUpdated | Request report by update |


<a id="getreportstatusbyID"></a>
# **getreportstatusbyID**
> getreportstatusbyID(contentType, accept, reportId)

Get report status by ID

Retrieves the Subscription&#39;s report status, filtering by its reportId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportApi apiInstance = new ReportApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String reportId = "reportId_example"; // String | Report ID.
    try {
      apiInstance.getreportstatusbyID(contentType, accept, reportId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#getreportstatusbyID");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **reportId** | **String**| Report ID. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="requestreportbyStatus"></a>
# **requestreportbyStatus**
> requestreportbyStatus(requesterEmail, status, contentType, accept)

Retrieve Subscription report by Status

Retrieves Subscriptions&#39; reports, filtering by status. The report will be sent by email, to the address inserted in the API&#39;s path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportApi apiInstance = new ReportApi(defaultClient);
    String requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
    Integer status = 1; // Integer | Binary OR of the following status: 1 - ACTIVE; 2 - PAUSED; 4 - CANCELED; 8 - EXPIRED
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.requestreportbyStatus(requesterEmail, status, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#requestreportbyStatus");
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
| **requesterEmail** | **String**| Email that the report will be sent to | |
| **status** | **Integer**| Binary OR of the following status: 1 - ACTIVE; 2 - PAUSED; 4 - CANCELED; 8 - EXPIRED | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="requestreportbydate"></a>
# **requestreportbydate**
> requestreportbydate(requesterEmail, beginDate, endDate, contentType, accept)

Retrieve Subscription report by date

Retrieves a report with the subscriptions created at the date interval requested

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportApi apiInstance = new ReportApi(defaultClient);
    String requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
    Integer beginDate = 20190101; // Integer | begin date of report interval, use format yyyyMMdd
    Integer endDate = 20190701; // Integer | end date of report interval, use format yyyyMMdd
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.requestreportbydate(requesterEmail, beginDate, endDate, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#requestreportbydate");
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
| **requesterEmail** | **String**| Email that the report will be sent to | |
| **beginDate** | **Integer**| begin date of report interval, use format yyyyMMdd | |
| **endDate** | **Integer**| end date of report interval, use format yyyyMMdd | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="requestreportbyorderdate"></a>
# **requestreportbyorderdate**
> requestreportbyorderdate(requesterEmail, beginDate, endDate, contentType, accept)

Retrieve Subscription report by order date

Retrieves a report regarding the Subscriptions created during the date interval of orders.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportApi apiInstance = new ReportApi(defaultClient);
    String requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
    Integer beginDate = 20190101; // Integer | begin date of report interval, use format yyyyMMdd
    Integer endDate = 20190701; // Integer | end date of report interval, use format yyyyMMdd
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.requestreportbyorderdate(requesterEmail, beginDate, endDate, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#requestreportbyorderdate");
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
| **requesterEmail** | **String**| Email that the report will be sent to | |
| **beginDate** | **Integer**| begin date of report interval, use format yyyyMMdd | |
| **endDate** | **Integer**| end date of report interval, use format yyyyMMdd | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="requestreportbyschedule"></a>
# **requestreportbyschedule**
> requestreportbyschedule(requesterEmail, beginDate, endDate, contentType, accept)

Retrieve Subscription report by schedule

Retrieves a report regarding the Subscriptions scheduled to execute at the date interval requested

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportApi apiInstance = new ReportApi(defaultClient);
    String requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
    Integer beginDate = 20190101; // Integer | begin date of report interval, use format yyyyMMdd
    Integer endDate = 20190701; // Integer | end date of report interval, use format yyyyMMdd
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.requestreportbyschedule(requesterEmail, beginDate, endDate, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#requestreportbyschedule");
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
| **requesterEmail** | **String**| Email that the report will be sent to | |
| **beginDate** | **Integer**| begin date of report interval, use format yyyyMMdd | |
| **endDate** | **Integer**| end date of report interval, use format yyyyMMdd | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="requestreportbyupdate"></a>
# **requestreportbyupdate**
> requestreportbyupdate(requesterEmail, beginDate, endDate, contentType, accept)

Request report by update

Retrieves a report regarding Subscriptions updated in the date interval chosen. The report will be sent by email, to the address inserted in the API&#39;s path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportApi apiInstance = new ReportApi(defaultClient);
    String requesterEmail = "user@vtex.com.br"; // String | Email that the report will be sent to
    Integer beginDate = 20190101; // Integer | begin date of report interval, use format yyyyMMdd
    Integer endDate = 20190701; // Integer | end date of report interval, use format yyyyMMdd
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.requestreportbyupdate(requesterEmail, beginDate, endDate, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportApi#requestreportbyupdate");
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
| **requesterEmail** | **String**| Email that the report will be sent to | |
| **beginDate** | **Integer**| begin date of report interval, use format yyyyMMdd | |
| **endDate** | **Integer**| end date of report interval, use format yyyyMMdd | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

