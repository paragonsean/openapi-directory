# DefaultApi

All URIs are relative to *https://api.nexmo.com/beta/audit*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEvent**](DefaultApi.md#getEvent) | **GET** /events/{id} | Retrieve individual audit event |
| [**getEvents**](DefaultApi.md#getEvents) | **GET** /events | Retrieve audit events |
| [**getEventsOptions**](DefaultApi.md#getEventsOptions) | **OPTIONS** /events | Retrieve audit event types |


<a id="getEvent"></a>
# **getEvent**
> AuditEvent getEvent(id)

Retrieve individual audit event

Get the specified audit event. 

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
    defaultClient.setBasePath("https://api.nexmo.com/beta/audit");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The UUID of the audit event to retrieve
    try {
      AuditEvent result = apiInstance.getEvent(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEvent");
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
| **id** | **String**| The UUID of the audit event to retrieve | |

### Return type

[**AuditEvent**](AuditEvent.md)

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
| **404** | Not Found |  -  |

<a id="getEvents"></a>
# **getEvents**
> AuditResp getEvents(eventType, dateFrom, dateTo, searchText, page, size)

Retrieve audit events

Get a series of audit events describing changes made to your Vonage API account over time. 

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
    defaultClient.setBasePath("https://api.nexmo.com/beta/audit");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    EventTypes eventType = EventTypes.fromValue("USER_STATUS"); // EventTypes | Filter results by this event type.
    String dateFrom = "dateFrom_example"; // String | Start of time range for audit events. DateTime in ISO-8601 format.
    String dateTo = "dateTo_example"; // String | End of time range for audit events. DateTime in ISO-8601 format.
    String searchText = "searchText_example"; // String | Return only audit events where the JSON object contains this search text. Must be legal text for a JSON attribute value, that is quotes and braces must be escaped.
    String page = "page_example"; // String | Page number starting with page 1.
    Integer size = 30; // Integer | Number of elements per page.
    try {
      AuditResp result = apiInstance.getEvents(eventType, dateFrom, dateTo, searchText, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEvents");
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
| **eventType** | [**EventTypes**](.md)| Filter results by this event type. | [optional] [enum: USER_STATUS, USER_UPDATE, USER_BILLING_UPDATE, USER_CREATE, USER_LOGIN, USER_LOGOUT, USER_PRODUCT_SEARCH, USER_API_KEYS_UPDATE, ACCOUNT_SECRET_DELETE, ACCOUNT_SECRET_CREATE, ACCOUNT_UPDATE_SPAMMER, ACCOUNT_UPDATE_SETTINGS_API, NUMBER_ASSIGN, NUMBER_UPDATED, NUMBER_RELEASE, NUMBER_LINKED, NUMBER_UNLINKED, APP_CREATE, APP_UPDATE, APP_DELETE, APP_DISABLE, APP_ENABLE, IP_WHITELIST_CREATE, IP_WHITELIST_DELETE, AUTORELOAD_ENABLE, AUTORELOAD_UPDATE, AUTORELOAD_DISABLE] |
| **dateFrom** | **String**| Start of time range for audit events. DateTime in ISO-8601 format. | [optional] |
| **dateTo** | **String**| End of time range for audit events. DateTime in ISO-8601 format. | [optional] |
| **searchText** | **String**| Return only audit events where the JSON object contains this search text. Must be legal text for a JSON attribute value, that is quotes and braces must be escaped. | [optional] |
| **page** | **String**| Page number starting with page 1. | [optional] |
| **size** | **Integer**| Number of elements per page. | [optional] [default to 30] |

### Return type

[**AuditResp**](AuditResp.md)

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
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getEventsOptions"></a>
# **getEventsOptions**
> AuditEventTypesResp getEventsOptions()

Retrieve audit event types

Get audit event types. 

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
    defaultClient.setBasePath("https://api.nexmo.com/beta/audit");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      AuditEventTypesResp result = apiInstance.getEventsOptions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEventsOptions");
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

[**AuditEventTypesResp**](AuditEventTypesResp.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

