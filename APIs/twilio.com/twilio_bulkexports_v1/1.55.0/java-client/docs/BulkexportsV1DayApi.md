# BulkexportsV1DayApi

All URIs are relative to *https://bulkexports.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchDay**](BulkexportsV1DayApi.md#fetchDay) | **GET** /v1/Exports/{ResourceType}/Days/{Day} |  |
| [**listDay**](BulkexportsV1DayApi.md#listDay) | **GET** /v1/Exports/{ResourceType}/Days |  |


<a id="fetchDay"></a>
# **fetchDay**
> fetchDay(resourceType, day)



Fetch a specific Day.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1DayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1DayApi apiInstance = new BulkexportsV1DayApi(defaultClient);
    String resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
    String day = "day_example"; // String | The ISO 8601 format date of the resources in the file, for a UTC day
    try {
      apiInstance.fetchDay(resourceType, day);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1DayApi#fetchDay");
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
| **resourceType** | **String**| The type of communication – Messages, Calls, Conferences, and Participants | |
| **day** | **String**| The ISO 8601 format date of the resources in the file, for a UTC day | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **307** | Temporary Redirect |  -  |

<a id="listDay"></a>
# **listDay**
> ListDayResponse listDay(resourceType, pageSize, page, pageToken)



Retrieve a list of all Days for a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1DayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1DayApi apiInstance = new BulkexportsV1DayApi(defaultClient);
    String resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDayResponse result = apiInstance.listDay(resourceType, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1DayApi#listDay");
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
| **resourceType** | **String**| The type of communication – Messages, Calls, Conferences, and Participants | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDayResponse**](ListDayResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

