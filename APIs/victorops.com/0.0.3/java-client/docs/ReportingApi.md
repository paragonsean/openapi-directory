# ReportingApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiReportingV1IncidentsGet**](ReportingApi.md#apiReportingV1IncidentsGet) | **GET** /api-reporting/v1/incidents | Get/search incident history |
| [**apiReportingV1TeamTeamOncallLogGet**](ReportingApi.md#apiReportingV1TeamTeamOncallLogGet) | **GET** /api-reporting/v1/team/{team}/oncall/log | A list of shift changes for a team |
| [**apiReportingV2IncidentsGet**](ReportingApi.md#apiReportingV2IncidentsGet) | **GET** /api-reporting/v2/incidents | Get/search incident history |


<a id="apiReportingV1IncidentsGet"></a>
# **apiReportingV1IncidentsGet**
> List&lt;IncidentList&gt; apiReportingV1IncidentsGet(xVOApiId, xVOApiKey, offset, limit, entityId, incidentNumber, startedAfter, startedBefore, host, service, currentPhase)

Get/search incident history

 __NOTE: This call is deprecated. Please use &#x60;GET /api-reporting/v2/incidents&#x60;.__  Retrieve incident history for your company, searching over date ranges and with filtering options.  This is historical data, and may be up to 15 minutes behind real-time incident data.  By default, only resolved incidents will be returned.  This API may be called a maximum of once a minute.  Incident requests are paginated with a offset and limit query string parameters.   The query for incidents is run and offset records are skipped, after which limit records will be returned.  The default offset is 0 and the default limit is 20. The maximum value allowed for limit is 100.  On return, the total number of records available for that query will be returned in the payload as &#39;total&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    BigDecimal offset = new BigDecimal("0.0"); // BigDecimal | The offset within the set of matching incidents
    BigDecimal limit = new BigDecimal("20.0"); // BigDecimal | The maximum number of matching incidents to return (100 max)
    String entityId = "entityId_example"; // String | The entity ID involved  This is the unique identifier for the entity causing the incident.
    String incidentNumber = "incidentNumber_example"; // String | The incident number as shown in VictorOps Multiple values and ranges are allowed: 4,5,20:50 
    String startedAfter = "startedAfter_example"; // String | Return incidents started after this timestamp Specify the timestamp in ISO8601 format
    String startedBefore = "startedBefore_example"; // String | Find incidents started before this timestamp  Specify the timestamp in ISO8601 format
    String host = "host_example"; // String | The host involved in the incident Multiple values can be separated with commas.
    String service = "service_example"; // String | The service involved in the incident (if any) Multiple values can be separated with commas.
    String currentPhase = "currentPhase_example"; // String | The current phase of the incident \"resolved\", \"triggered\" or \"acknowledged\". Multiple values can be separated with commas.
    try {
      List<IncidentList> result = apiInstance.apiReportingV1IncidentsGet(xVOApiId, xVOApiKey, offset, limit, entityId, incidentNumber, startedAfter, startedBefore, host, service, currentPhase);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#apiReportingV1IncidentsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **offset** | **BigDecimal**| The offset within the set of matching incidents | [optional] [default to 0.0] |
| **limit** | **BigDecimal**| The maximum number of matching incidents to return (100 max) | [optional] [default to 20.0] |
| **entityId** | **String**| The entity ID involved  This is the unique identifier for the entity causing the incident. | [optional] |
| **incidentNumber** | **String**| The incident number as shown in VictorOps Multiple values and ranges are allowed: 4,5,20:50  | [optional] |
| **startedAfter** | **String**| Return incidents started after this timestamp Specify the timestamp in ISO8601 format | [optional] |
| **startedBefore** | **String**| Find incidents started before this timestamp  Specify the timestamp in ISO8601 format | [optional] |
| **host** | **String**| The host involved in the incident Multiple values can be separated with commas. | [optional] |
| **service** | **String**| The service involved in the incident (if any) Multiple values can be separated with commas. | [optional] |
| **currentPhase** | **String**| The current phase of the incident \&quot;resolved\&quot;, \&quot;triggered\&quot; or \&quot;acknowledged\&quot;. Multiple values can be separated with commas. | [optional] |

### Return type

[**List&lt;IncidentList&gt;**](IncidentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of incidents matching the request filters |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiReportingV1TeamTeamOncallLogGet"></a>
# **apiReportingV1TeamTeamOncallLogGet**
> OnCallLog apiReportingV1TeamTeamOncallLogGet(xVOApiId, xVOApiKey, team, start, end, userName)

A list of shift changes for a team

Returns a log of user shift changes for the specified team. This is historical data, and may be up to 15 minutes behind real-time log data.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String team = "team_example"; // String | The VictorOps team 'slug'
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Return shift changes occurring after this timestamp. The default is the start of the day at midnight. Specify the timestamp in ISO8601 format
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Return shift changes occurring before this timestamp. The default is the end of the day at 11:59:59. Specify the timestamp in ISO8601 format
    String userName = "userName_example"; // String | The VictorOps user ID. Return shift changes occurring during the interval specified for this user. Without this parameter, all relevant users (with respect to the specified interval) are returned
    try {
      OnCallLog result = apiInstance.apiReportingV1TeamTeamOncallLogGet(xVOApiId, xVOApiKey, team, start, end, userName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#apiReportingV1TeamTeamOncallLogGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **team** | **String**| The VictorOps team &#39;slug&#39; | |
| **start** | **OffsetDateTime**| Return shift changes occurring after this timestamp. The default is the start of the day at midnight. Specify the timestamp in ISO8601 format | [optional] |
| **end** | **OffsetDateTime**| Return shift changes occurring before this timestamp. The default is the end of the day at 11:59:59. Specify the timestamp in ISO8601 format | [optional] |
| **userName** | **String**| The VictorOps user ID. Return shift changes occurring during the interval specified for this user. Without this parameter, all relevant users (with respect to the specified interval) are returned | [optional] |

### Return type

[**OnCallLog**](OnCallLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of the take request |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Team or user(s) not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiReportingV2IncidentsGet"></a>
# **apiReportingV2IncidentsGet**
> ActiveIncidentList apiReportingV2IncidentsGet(xVOApiId, xVOApiKey, offset, limit, entityId, incidentNumber, startedAfter, startedBefore, host, service, currentPhase, routingKey)

Get/search incident history

Retrieve incident history for your company, searching over date ranges and with filtering options.  This API may be called a maximum of once a minute.  Incident requests are paginated with a offset and limit query string parameters.   The query for incidents is run and offset records are skipped, after which limit records will be returned.  The default offset is 0 and the default limit is 20. The maximum value allowed for limit is 100.  Unless specified otherwise with the parameter currentPhase, the response will only contain resolved incidents.  On return, the total number of records available for that query will be returned in the payload as &#39;total&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    BigDecimal offset = new BigDecimal("0.0"); // BigDecimal | The offset within the set of matching incidents
    BigDecimal limit = new BigDecimal("20.0"); // BigDecimal | The maximum number of matching incidents to return (100 max)
    String entityId = "entityId_example"; // String | The entity ID involved  This is the unique identifier for the entity causing the incident.
    String incidentNumber = "incidentNumber_example"; // String | The incident number as shown in VictorOps Multiple values and ranges are allowed: 4,5,20:50 
    String startedAfter = "startedAfter_example"; // String | Return incidents started after this timestamp Specify the timestamp in ISO8601 format
    String startedBefore = "startedBefore_example"; // String | Find incidents started before this timestamp  Specify the timestamp in ISO8601 format
    String host = "host_example"; // String | The host involved in the incident Multiple values can be separated with commas.
    String service = "service_example"; // String | The service involved in the incident (if any) Multiple values can be separated with commas.
    String currentPhase = "currentPhase_example"; // String | The current phase of the incident \"resolved\", \"triggered\" or \"acknowledged\". Multiple values can be separated with commas. By default, response contains only \"resolved\" incidents
    String routingKey = "routingKey_example"; // String | The original routing of the incident
    try {
      ActiveIncidentList result = apiInstance.apiReportingV2IncidentsGet(xVOApiId, xVOApiKey, offset, limit, entityId, incidentNumber, startedAfter, startedBefore, host, service, currentPhase, routingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#apiReportingV2IncidentsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **offset** | **BigDecimal**| The offset within the set of matching incidents | [optional] [default to 0.0] |
| **limit** | **BigDecimal**| The maximum number of matching incidents to return (100 max) | [optional] [default to 20.0] |
| **entityId** | **String**| The entity ID involved  This is the unique identifier for the entity causing the incident. | [optional] |
| **incidentNumber** | **String**| The incident number as shown in VictorOps Multiple values and ranges are allowed: 4,5,20:50  | [optional] |
| **startedAfter** | **String**| Return incidents started after this timestamp Specify the timestamp in ISO8601 format | [optional] |
| **startedBefore** | **String**| Find incidents started before this timestamp  Specify the timestamp in ISO8601 format | [optional] |
| **host** | **String**| The host involved in the incident Multiple values can be separated with commas. | [optional] |
| **service** | **String**| The service involved in the incident (if any) Multiple values can be separated with commas. | [optional] |
| **currentPhase** | **String**| The current phase of the incident \&quot;resolved\&quot;, \&quot;triggered\&quot; or \&quot;acknowledged\&quot;. Multiple values can be separated with commas. By default, response contains only \&quot;resolved\&quot; incidents | [optional] |
| **routingKey** | **String**| The original routing of the incident | [optional] |

### Return type

[**ActiveIncidentList**](ActiveIncidentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of incidents matching the request filters |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | Path not found |  -  |
| **500** | Internal Server Error |  -  |

