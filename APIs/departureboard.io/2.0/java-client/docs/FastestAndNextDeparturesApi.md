# FastestAndNextDeparturesApi

All URIs are relative to *https://api.departureboard.io/api/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFastestDeparturesByCRS**](FastestAndNextDeparturesApi.md#getFastestDeparturesByCRS) | **GET** /getFastestDeparturesByCRS/{CRS} | getFastestDeparturesByCRS is used to get the fastest next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place. |
| [**getNextDeparturesByCRS**](FastestAndNextDeparturesApi.md#getNextDeparturesByCRS) | **GET** /getNextDeparturesByCRS/{CRS} | getNextDeparturesByCRS is used to get the next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place. This will return the next departures for each of the filterList stations specified. It may not return the fastest next service. To get the fastest next service use the getFastestDeparturesByCRS endpoint. |


<a id="getFastestDeparturesByCRS"></a>
# **getFastestDeparturesByCRS**
> getFastestDeparturesByCRS(CRS, apiKey, filterList, timeOffset, timeWindow, serviceDetails)

getFastestDeparturesByCRS is used to get the fastest next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FastestAndNextDeparturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.departureboard.io/api/v2.0");

    FastestAndNextDeparturesApi apiInstance = new FastestAndNextDeparturesApi(defaultClient);
    String CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
    String apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    String filterList = "filterList_example"; // String | The CRS (Computer Reservation System) codes to show the fastest departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD.
    Integer timeOffset = 0; // Integer | The time window in minutes to offset the departure information by. For example, a value of 20 will show the fastest services departing after 20 minutes.
    Integer timeWindow = 120; // Integer | The time window to show train services for in minutes. For example, a value of 60 will show the fastest services departing the station in the next 60 minutes.
    Boolean serviceDetails = true; // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    try {
      apiInstance.getFastestDeparturesByCRS(CRS, apiKey, filterList, timeOffset, timeWindow, serviceDetails);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastestAndNextDeparturesApi#getFastestDeparturesByCRS");
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
| **CRS** | **String**| The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross. | |
| **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | |
| **filterList** | **String**| The CRS (Computer Reservation System) codes to show the fastest departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD. | |
| **timeOffset** | **Integer**| The time window in minutes to offset the departure information by. For example, a value of 20 will show the fastest services departing after 20 minutes. | [optional] [default to 0] |
| **timeWindow** | **Integer**| The time window to show train services for in minutes. For example, a value of 60 will show the fastest services departing the station in the next 60 minutes. | [optional] [default to 120] |
| **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true] |

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
| **200** | **OK**: The API Request was successful and returned data. |  -  |
| **400** | Your request was not valid. &lt;br&gt;&lt;br&gt;The departureboard.io API performs validation of queries to make sure they make sense and will return a valid response from National Rail. Bad queries made directly to the National Rail API return a generic &#x60;500 Internal Server Error&#x60; response which is difficult to troubleshoot.&lt;br&gt;&lt;br&gt;By validating requests the departureboard.io API can provide improved error messages to help with troubleshooting, and prevent bad queries from ever reaching National Rail. |  -  |
| **401** | **Unauthorized**: Your National Rail API key is wrong or your key has not been registered in the [departureboard.io API Portal](https://api-portal.departureboard.io) as detailed in the [registration](https://api.departureboard.io/docs/registration) section of the documentation.&lt;br&gt;&lt;br&gt;You should double check your API Key is valid and has been whitelisted. Newly generated API Keys can take up to 15 minutes to become active. |  -  |
| **429** | **Too Many Requests**: You have exceeded the rate limit. &lt;br&gt;&lt;br&gt;Get in touch to arrange an exception, or slow down your requests. |  -  |
| **500** | **Internal Server Error**: There was an unknown error returning the response.&lt;br&gt;&lt;br&gt;This error is served when an unknown error is encountered returning your response. This is often due to upstream problems with National Rail, for example them returning a bad response or malformed data. In rare circumstances it can be caused by a bad request that was not caught in the departureboard.io validation. |  -  |
| **503** | **Service Unavailable**: The National Rail upstream API is experiencing issues.&lt;br&gt;&lt;br&gt;This error is returned when the departureboard.io API detects issues with the upstream National Rail API. The departureboard.io API is functioning but cannot return a result as the National Rail API is down. |  -  |

<a id="getNextDeparturesByCRS"></a>
# **getNextDeparturesByCRS**
> getNextDeparturesByCRS(CRS, apiKey, filterList, timeOffset, timeWindow, serviceDetails)

getNextDeparturesByCRS is used to get the next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place. This will return the next departures for each of the filterList stations specified. It may not return the fastest next service. To get the fastest next service use the getFastestDeparturesByCRS endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FastestAndNextDeparturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.departureboard.io/api/v2.0");

    FastestAndNextDeparturesApi apiInstance = new FastestAndNextDeparturesApi(defaultClient);
    String CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
    String apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    String filterList = "filterList_example"; // String | The CRS (Computer Reservation System) codes to show departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD.
    Integer timeOffset = 0; // Integer | The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes.
    Integer timeWindow = 120; // Integer | The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes.
    Boolean serviceDetails = true; // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    try {
      apiInstance.getNextDeparturesByCRS(CRS, apiKey, filterList, timeOffset, timeWindow, serviceDetails);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastestAndNextDeparturesApi#getNextDeparturesByCRS");
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
| **CRS** | **String**| The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross. | |
| **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | |
| **filterList** | **String**| The CRS (Computer Reservation System) codes to show departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD. | |
| **timeOffset** | **Integer**| The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes. | [optional] [default to 0] |
| **timeWindow** | **Integer**| The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes. | [optional] [default to 120] |
| **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true] |

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
| **200** | **OK**: The API Request was successful and returned data. |  -  |
| **400** | Your request was not valid. &lt;br&gt;&lt;br&gt;The departureboard.io API performs validation of queries to make sure they make sense and will return a valid response from National Rail. Bad queries made directly to the National Rail API return a generic &#x60;500 Internal Server Error&#x60; response which is difficult to troubleshoot.&lt;br&gt;&lt;br&gt;By validating requests the departureboard.io API can provide improved error messages to help with troubleshooting, and prevent bad queries from ever reaching National Rail. |  -  |
| **401** | **Unauthorized**: Your National Rail API key is wrong or your key has not been registered in the [departureboard.io API Portal](https://api-portal.departureboard.io) as detailed in the [registration](https://api.departureboard.io/docs/registration) section of the documentation.&lt;br&gt;&lt;br&gt;You should double check your API Key is valid and has been whitelisted. Newly generated API Keys can take up to 15 minutes to become active. |  -  |
| **429** | **Too Many Requests**: You have exceeded the rate limit. &lt;br&gt;&lt;br&gt;Get in touch to arrange an exception, or slow down your requests. |  -  |
| **500** | **Internal Server Error**: There was an unknown error returning the response.&lt;br&gt;&lt;br&gt;This error is served when an unknown error is encountered returning your response. This is often due to upstream problems with National Rail, for example them returning a bad response or malformed data. In rare circumstances it can be caused by a bad request that was not caught in the departureboard.io validation. |  -  |
| **503** | **Service Unavailable**: The National Rail upstream API is experiencing issues.&lt;br&gt;&lt;br&gt;This error is returned when the departureboard.io API detects issues with the upstream National Rail API. The departureboard.io API is functioning but cannot return a result as the National Rail API is down. |  -  |

