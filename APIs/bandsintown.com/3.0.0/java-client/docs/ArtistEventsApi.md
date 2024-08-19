# ArtistEventsApi

All URIs are relative to *https://rest.bandsintown.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artistEvents**](ArtistEventsApi.md#artistEvents) | **GET** /artists/{artistname}/events | Get upcoming, past, or all artist events, or events within a date range |


<a id="artistEvents"></a>
# **artistEvents**
> List&lt;EventData&gt; artistEvents(artistname, appId, date)

Get upcoming, past, or all artist events, or events within a date range

artist events 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtistEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.bandsintown.com");

    ArtistEventsApi apiInstance = new ArtistEventsApi(defaultClient);
    String artistname = "artistname_example"; // String | The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \" use %27C
    String appId = "appId_example"; // String | The application ID assigned to you by Bandsintown
    String date = "date_example"; // String | Can be one of the following values: \"upcoming\", \"past\", \"all\", or a date range e.g. \"2015-05-05,2017-05-05\". If not specified, only upcoming shows are returned
    try {
      List<EventData> result = apiInstance.artistEvents(artistname, appId, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtistEventsApi#artistEvents");
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
| **artistname** | **String**| The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \&quot; use %27C | |
| **appId** | **String**| The application ID assigned to you by Bandsintown | |
| **date** | **String**| Can be one of the following values: \&quot;upcoming\&quot;, \&quot;past\&quot;, \&quot;all\&quot;, or a date range e.g. \&quot;2015-05-05,2017-05-05\&quot;. If not specified, only upcoming shows are returned | [optional] |

### Return type

[**List&lt;EventData&gt;**](EventData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Shows within a date range for the selected artist |  -  |

