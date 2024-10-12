# StorageApi

All URIs are relative to *https://dweet.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStoredAlerts**](StorageApi.md#getStoredAlerts) | **GET** /get/stored/alerts/for/{thing} | Read all the saved alerts for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour. |
| [**getStoredDweetsForThingGet**](StorageApi.md#getStoredDweetsForThingGet) | **GET** /get/stored/dweets/for/{thing} | Read all the saved dweets for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour. |


<a id="getStoredAlerts"></a>
# **getStoredAlerts**
> getStoredAlerts(thing, key, date, hour, responseType)

Read all the saved alerts for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dweet.io");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String thing = "thing_example"; // String | A unique name of a thing.
    String key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
    String date = "date_example"; // String | The calendar date (YYYY-MM-DD) from which you'd like to start your query.  The response will be a maximum of one day.
    String hour = "hour_example"; // String | The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour.
    String responseType = "responseType_example"; // String | Current valid parameters for this are 'csv' and 'json'.  If this parameter is left blank, all responses default to hapi-json dweet-speak.
    try {
      apiInstance.getStoredAlerts(thing, key, date, hour, responseType);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#getStoredAlerts");
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
| **thing** | **String**| A unique name of a thing. | |
| **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | |
| **date** | **String**| The calendar date (YYYY-MM-DD) from which you&#39;d like to start your query.  The response will be a maximum of one day. | |
| **hour** | **String**| The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour. | [optional] |
| **responseType** | **String**| Current valid parameters for this are &#39;csv&#39; and &#39;json&#39;.  If this parameter is left blank, all responses default to hapi-json dweet-speak. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getStoredDweetsForThingGet"></a>
# **getStoredDweetsForThingGet**
> getStoredDweetsForThingGet(thing, key, date, hour, responseType)

Read all the saved dweets for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dweet.io");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String thing = "thing_example"; // String | A unique name of a thing.
    String key = "key_example"; // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
    String date = "date_example"; // String | The calendar date (YYYY-MM-DD) from which you'd like to start your query.  The response will be a maximum of one day.
    String hour = "hour_example"; // String | The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour.
    String responseType = "responseType_example"; // String | Current valid parameters for this are 'csv' and 'json'.  If this parameter is left blank, all responses default to hapi-json dweet-speak.
    try {
      apiInstance.getStoredDweetsForThingGet(thing, key, date, hour, responseType);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#getStoredDweetsForThingGet");
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
| **thing** | **String**| A unique name of a thing. | |
| **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | |
| **date** | **String**| The calendar date (YYYY-MM-DD) from which you&#39;d like to start your query.  The response will be a maximum of one day. | |
| **hour** | **String**| The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour. | [optional] |
| **responseType** | **String**| Current valid parameters for this are &#39;csv&#39; and &#39;json&#39;.  If this parameter is left blank, all responses default to hapi-json dweet-speak. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

