# SchedulesApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeleteSchedules**](SchedulesApiApi.md#idDeleteSchedules) | **DELETE** /api/user/schedules/{id} | Handle DELETE reqeuest for Schedules |
| [**idGetSchedules**](SchedulesApiApi.md#idGetSchedules) | **GET** /api/user/schedules | Handle GET reqeuest for Schedules |
| [**idGetSingleSchedule**](SchedulesApiApi.md#idGetSingleSchedule) | **GET** /api/user/schedules/{id} | Handle GET reqeuest for Schedules |
| [**idPostSchedules**](SchedulesApiApi.md#idPostSchedules) | **POST** /api/user/schedules | Handle POST reqeuest for Schedules |


<a id="idDeleteSchedules"></a>
# **idDeleteSchedules**
> SchedulesAPIResponse idDeleteSchedules(id)

Handle DELETE reqeuest for Schedules

Deletes a schedule with the given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SchedulesApiApi apiInstance = new SchedulesApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      SchedulesAPIResponse result = apiInstance.idDeleteSchedules(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulesApiApi#idDeleteSchedules");
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
| **id** | **UUID**| id for a specific | |

### Return type

[**SchedulesAPIResponse**](SchedulesAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns List of saved schedules |  -  |

<a id="idGetSchedules"></a>
# **idGetSchedules**
> SchedulesAPIResponse idGetSchedules()

Handle GET reqeuest for Schedules

Returns the list of all the schedules saved by the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SchedulesApiApi apiInstance = new SchedulesApiApi(defaultClient);
    try {
      SchedulesAPIResponse result = apiInstance.idGetSchedules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulesApiApi#idGetSchedules");
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

[**SchedulesAPIResponse**](SchedulesAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns List of saved schedules |  -  |

<a id="idGetSingleSchedule"></a>
# **idGetSingleSchedule**
> Schedule idGetSingleSchedule(id)

Handle GET reqeuest for Schedules

Fetches and returns the schedule with the given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SchedulesApiApi apiInstance = new SchedulesApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      Schedule result = apiInstance.idGetSingleSchedule(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulesApiApi#idGetSingleSchedule");
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
| **id** | **UUID**| id for a specific | |

### Return type

[**Schedule**](Schedule.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single schedules |  -  |

<a id="idPostSchedules"></a>
# **idPostSchedules**
> Schedule idPostSchedules()

Handle POST reqeuest for Schedules

Save schedule using the current provider&#39;s persistence mechanism

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulesApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SchedulesApiApi apiInstance = new SchedulesApiApi(defaultClient);
    try {
      Schedule result = apiInstance.idPostSchedules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulesApiApi#idPostSchedules");
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

[**Schedule**](Schedule.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single schedules |  -  |

