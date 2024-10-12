# DeparturesArrivalsApi

All URIs are relative to *https://api.departureboard.io/api/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getArrivalsAndDeparturesByCRS**](DeparturesArrivalsApi.md#getArrivalsAndDeparturesByCRS) | **GET** /getArrivalsAndDeparturesByCRS/{CRS} | getArrivalsAndDeparturesByCRS is used to get a list of services arriving to and departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place. |
| [**getArrivalsByCRS**](DeparturesArrivalsApi.md#getArrivalsByCRS) | **GET** /getArrivalsByCRS/{CRS} | getArrivalsByCRS is used to get a list of services arriving to a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place. |
| [**getDeparturesByCRS**](DeparturesArrivalsApi.md#getDeparturesByCRS) | **GET** /getDeparturesByCRS/{CRS} | getDeparturesByCRS is used to get a list of services departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place. |


<a id="getArrivalsAndDeparturesByCRS"></a>
# **getArrivalsAndDeparturesByCRS**
> getArrivalsAndDeparturesByCRS(CRS, apiKey, numServices, timeOffset, timeWindow, serviceDetails, filterStation, filterType)

getArrivalsAndDeparturesByCRS is used to get a list of services arriving to and departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeparturesArrivalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.departureboard.io/api/v2.0");

    DeparturesArrivalsApi apiInstance = new DeparturesArrivalsApi(defaultClient);
    String CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the Station you wish to get departure and arrival information for, e.g. KGX for London Kings Cross.
    String apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    Integer numServices = 10; // Integer | The number of arriving and departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services arriving to or departing from this station within the time window specified.
    Integer timeOffset = 0; // Integer | The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes.
    Integer timeWindow = 120; // Integer | The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes.
    Boolean serviceDetails = true; // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    String filterStation = "filterStation_example"; // String | The CRS (Computer Reservation System) code to filter the results by. When setting this you must also set the filterType parameter. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading) and filterType to from, will only show services arriving to London Paddington that stopped at Reading. Setting a filter for getArrivalsAndDeparturesByCRS is similar to performing a getArrivalsByCRS or getDeparturesByCRS lookup, with the appropriate filterStation parameter. However using the getArrivalsAndDeparturesByCRS endpoint shows more details for each of the returned services.
    String filterType = "filterType_example"; // String | Determines if the filterStation parameter should be applied for services arriving to, or leaving from the selected station. Required if filterStation is set.
    try {
      apiInstance.getArrivalsAndDeparturesByCRS(CRS, apiKey, numServices, timeOffset, timeWindow, serviceDetails, filterStation, filterType);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeparturesArrivalsApi#getArrivalsAndDeparturesByCRS");
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
| **CRS** | **String**| The CRS (Computer Reservation System) for the Station you wish to get departure and arrival information for, e.g. KGX for London Kings Cross. | |
| **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | |
| **numServices** | **Integer**| The number of arriving and departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services arriving to or departing from this station within the time window specified. | [optional] [default to 10] |
| **timeOffset** | **Integer**| The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes. | [optional] [default to 0] |
| **timeWindow** | **Integer**| The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes. | [optional] [default to 120] |
| **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true] |
| **filterStation** | **String**| The CRS (Computer Reservation System) code to filter the results by. When setting this you must also set the filterType parameter. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading) and filterType to from, will only show services arriving to London Paddington that stopped at Reading. Setting a filter for getArrivalsAndDeparturesByCRS is similar to performing a getArrivalsByCRS or getDeparturesByCRS lookup, with the appropriate filterStation parameter. However using the getArrivalsAndDeparturesByCRS endpoint shows more details for each of the returned services. | [optional] |
| **filterType** | **String**| Determines if the filterStation parameter should be applied for services arriving to, or leaving from the selected station. Required if filterStation is set. | [optional] |

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

<a id="getArrivalsByCRS"></a>
# **getArrivalsByCRS**
> getArrivalsByCRS(CRS, apiKey, numServices, timeOffset, timeWindow, serviceDetails, filterStation)

getArrivalsByCRS is used to get a list of services arriving to a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeparturesArrivalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.departureboard.io/api/v2.0");

    DeparturesArrivalsApi apiInstance = new DeparturesArrivalsApi(defaultClient);
    String CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the Station you wish to get arrival information for, e.g. KGX for London Kings Cross.
    String apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    Integer numServices = 10; // Integer | The number of arriving train services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running to this station within the time window specified.
    Integer timeOffset = 0; // Integer | The time window in minutes to offset the arrival information by. For example, a value of 20 will not show services arriving within the next 20 minutes.
    Integer timeWindow = 120; // Integer | The time window to show train services for in minutes. For example, a value of 60 will show services arriving to the station in the next 60 minutes.
    Boolean serviceDetails = true; // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    String filterStation = "filterStation_example"; // String | The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services arriving to Paddington that stopped at Reading.
    try {
      apiInstance.getArrivalsByCRS(CRS, apiKey, numServices, timeOffset, timeWindow, serviceDetails, filterStation);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeparturesArrivalsApi#getArrivalsByCRS");
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
| **CRS** | **String**| The CRS (Computer Reservation System) for the Station you wish to get arrival information for, e.g. KGX for London Kings Cross. | |
| **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | |
| **numServices** | **Integer**| The number of arriving train services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running to this station within the time window specified. | [optional] [default to 10] |
| **timeOffset** | **Integer**| The time window in minutes to offset the arrival information by. For example, a value of 20 will not show services arriving within the next 20 minutes. | [optional] [default to 0] |
| **timeWindow** | **Integer**| The time window to show train services for in minutes. For example, a value of 60 will show services arriving to the station in the next 60 minutes. | [optional] [default to 120] |
| **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true] |
| **filterStation** | **String**| The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services arriving to Paddington that stopped at Reading. | [optional] |

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

<a id="getDeparturesByCRS"></a>
# **getDeparturesByCRS**
> getDeparturesByCRS(CRS, apiKey, numServices, timeOffset, timeWindow, serviceDetails, filterStation)

getDeparturesByCRS is used to get a list of services departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeparturesArrivalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.departureboard.io/api/v2.0");

    DeparturesArrivalsApi apiInstance = new DeparturesArrivalsApi(defaultClient);
    String CRS = "CRS_example"; // String | The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
    String apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    Integer numServices = 10; // Integer | The number of departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running from the selected station within the time window specified.
    Integer timeOffset = 0; // Integer | The time window in minutes to offset the departure information by. For example, a value of 20 will not show services departing within the next 20 minutes.
    Integer timeWindow = 120; // Integer | The time window to show services for in minutes. For example, a value of 60 will show services departing the station in the next 60 minutes.
    Boolean serviceDetails = true; // Boolean | Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    String filterStation = "filterStation_example"; // String | The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services departing from Paddington that stop at Reading.
    try {
      apiInstance.getDeparturesByCRS(CRS, apiKey, numServices, timeOffset, timeWindow, serviceDetails, filterStation);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeparturesArrivalsApi#getDeparturesByCRS");
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
| **numServices** | **Integer**| The number of departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running from the selected station within the time window specified. | [optional] [default to 10] |
| **timeOffset** | **Integer**| The time window in minutes to offset the departure information by. For example, a value of 20 will not show services departing within the next 20 minutes. | [optional] [default to 0] |
| **timeWindow** | **Integer**| The time window to show services for in minutes. For example, a value of 60 will show services departing the station in the next 60 minutes. | [optional] [default to 120] |
| **serviceDetails** | **Boolean**| Should the response contain information on the calling points for each service? If set to false, calling points will not be returned. | [optional] [default to true] |
| **filterStation** | **String**| The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services departing from Paddington that stop at Reading. | [optional] |

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

