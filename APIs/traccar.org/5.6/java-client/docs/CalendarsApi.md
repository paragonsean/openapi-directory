# CalendarsApi

All URIs are relative to *https://demo.traccar.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calendarsGet**](CalendarsApi.md#calendarsGet) | **GET** /calendars | Fetch a list of Calendars |
| [**calendarsIdDelete**](CalendarsApi.md#calendarsIdDelete) | **DELETE** /calendars/{id} | Delete a Calendar |
| [**calendarsIdPut**](CalendarsApi.md#calendarsIdPut) | **PUT** /calendars/{id} | Update a Calendar |
| [**calendarsPost**](CalendarsApi.md#calendarsPost) | **POST** /calendars | Create a Calendar |


<a id="calendarsGet"></a>
# **calendarsGet**
> List&lt;Calendar&gt; calendarsGet(all, userId)

Fetch a list of Calendars

Without params, it returns a list of Calendars the user has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    Boolean all = true; // Boolean | Can only be used by admins or managers to fetch all entities
    Integer userId = 56; // Integer | Standard users can use this only with their own _userId_
    try {
      List<Calendar> result = apiInstance.calendarsGet(all, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsGet");
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
| **all** | **Boolean**| Can only be used by admins or managers to fetch all entities | [optional] |
| **userId** | **Integer**| Standard users can use this only with their own _userId_ | [optional] |

### Return type

[**List&lt;Calendar&gt;**](Calendar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="calendarsIdDelete"></a>
# **calendarsIdDelete**
> calendarsIdDelete(id)

Delete a Calendar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      apiInstance.calendarsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsIdDelete");
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
| **id** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="calendarsIdPut"></a>
# **calendarsIdPut**
> Calendar calendarsIdPut(id, body)

Update a Calendar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    Integer id = 56; // Integer | 
    Calendar body = new Calendar(); // Calendar | 
    try {
      Calendar result = apiInstance.calendarsIdPut(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsIdPut");
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
| **id** | **Integer**|  | |
| **body** | [**Calendar**](Calendar.md)|  | |

### Return type

[**Calendar**](Calendar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="calendarsPost"></a>
# **calendarsPost**
> Calendar calendarsPost(body)

Create a Calendar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CalendarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CalendarsApi apiInstance = new CalendarsApi(defaultClient);
    Calendar body = new Calendar(); // Calendar | 
    try {
      Calendar result = apiInstance.calendarsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CalendarsApi#calendarsPost");
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
| **body** | [**Calendar**](Calendar.md)|  | |

### Return type

[**Calendar**](Calendar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

