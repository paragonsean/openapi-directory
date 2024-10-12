# OperationsApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsFlightstatusArrivalsByAirportCodeAndFromDateTimeGet**](OperationsApi.md#operationsFlightstatusArrivalsByAirportCodeAndFromDateTimeGet) | **GET** /operations/flightstatus/arrivals/{airportCode}/{fromDateTime} | Flight Status at Arrival Airport |
| [**operationsFlightstatusByFlightNumberAndDateGet**](OperationsApi.md#operationsFlightstatusByFlightNumberAndDateGet) | **GET** /operations/flightstatus/{flightNumber}/{date} | Flight Status |
| [**operationsFlightstatusDeparturesByAirportCodeAndFromDateTimeGet**](OperationsApi.md#operationsFlightstatusDeparturesByAirportCodeAndFromDateTimeGet) | **GET** /operations/flightstatus/departures/{airportCode}/{fromDateTime} | Flight Status at Departure Airport |
| [**operationsFlightstatusRouteDateByOriginAndDestinationGet**](OperationsApi.md#operationsFlightstatusRouteDateByOriginAndDestinationGet) | **GET** /operations/flightstatus/route/{origin}/{destination}/{date} | Flight Status by Route |
| [**operationsSchedulesFromDateTimeByOriginAndDestinationGet**](OperationsApi.md#operationsSchedulesFromDateTimeByOriginAndDestinationGet) | **GET** /operations/schedules/{origin}/{destination}/{fromDateTime} | Flight Schedules |


<a id="operationsFlightstatusArrivalsByAirportCodeAndFromDateTimeGet"></a>
# **operationsFlightstatusArrivalsByAirportCodeAndFromDateTimeGet**
> Object operationsFlightstatusArrivalsByAirportCodeAndFromDateTimeGet(airportCode, fromDateTime, accept, limit, offset)

Flight Status at Arrival Airport

Status of all arrivals at a given airport up to 4 hours from the provided date time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String airportCode = "airportCode_example"; // String | 3-letter IATA aiport code (e.g. 'ZRH')
    String fromDateTime = "fromDateTime_example"; // String | Start of time range in local time of arrival airport (YYYY-MM-DDTHH:mm)
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String limit = "limit_example"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "offset_example"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.operationsFlightstatusArrivalsByAirportCodeAndFromDateTimeGet(airportCode, fromDateTime, accept, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsFlightstatusArrivalsByAirportCodeAndFromDateTimeGet");
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
| **airportCode** | **String**| 3-letter IATA aiport code (e.g. &#39;ZRH&#39;) | |
| **fromDateTime** | **String**| Start of time range in local time of arrival airport (YYYY-MM-DDTHH:mm) | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="operationsFlightstatusByFlightNumberAndDateGet"></a>
# **operationsFlightstatusByFlightNumberAndDateGet**
> Object operationsFlightstatusByFlightNumberAndDateGet(flightNumber, date, accept, limit, offset)

Flight Status

Status of a particular flight (boarding, delayed, etc.).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String flightNumber = "flightNumber_example"; // String | Flight number including carrier code and any suffix (e.g. 'LH400')
    String date = "date_example"; // String | The departure date (YYYY-MM-DD) in the local time of the departure airport
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String limit = "limit_example"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "offset_example"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.operationsFlightstatusByFlightNumberAndDateGet(flightNumber, date, accept, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsFlightstatusByFlightNumberAndDateGet");
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
| **flightNumber** | **String**| Flight number including carrier code and any suffix (e.g. &#39;LH400&#39;) | |
| **date** | **String**| The departure date (YYYY-MM-DD) in the local time of the departure airport | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="operationsFlightstatusDeparturesByAirportCodeAndFromDateTimeGet"></a>
# **operationsFlightstatusDeparturesByAirportCodeAndFromDateTimeGet**
> Object operationsFlightstatusDeparturesByAirportCodeAndFromDateTimeGet(airportCode, fromDateTime, accept, limit, offset)

Flight Status at Departure Airport

Status of all departures from a given airport up to 4 hours from the provided date time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String airportCode = "airportCode_example"; // String | Departure airport. 3-letter IATA airport code (e.g. 'HAM')
    String fromDateTime = "fromDateTime_example"; // String | Start of time range in local time of departure airport (YYYY-MM-DDTHH:mm)
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String limit = "limit_example"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "offset_example"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.operationsFlightstatusDeparturesByAirportCodeAndFromDateTimeGet(airportCode, fromDateTime, accept, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsFlightstatusDeparturesByAirportCodeAndFromDateTimeGet");
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
| **airportCode** | **String**| Departure airport. 3-letter IATA airport code (e.g. &#39;HAM&#39;) | |
| **fromDateTime** | **String**| Start of time range in local time of departure airport (YYYY-MM-DDTHH:mm) | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="operationsFlightstatusRouteDateByOriginAndDestinationGet"></a>
# **operationsFlightstatusRouteDateByOriginAndDestinationGet**
> Object operationsFlightstatusRouteDateByOriginAndDestinationGet(origin, destination, date, accept, limit, offset)

Flight Status by Route

Status of flights between a given origin and destination on a given date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String origin = "origin_example"; // String | 3-letter IATA airport (e.g. 'FRA')
    String destination = "destination_example"; // String | 3-letter IATA airport code (e.g. 'JFK')
    String date = "date_example"; // String | Departure date (YYYY-MM-DD) in local time of departure airport
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String limit = "limit_example"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "offset_example"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.operationsFlightstatusRouteDateByOriginAndDestinationGet(origin, destination, date, accept, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsFlightstatusRouteDateByOriginAndDestinationGet");
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
| **origin** | **String**| 3-letter IATA airport (e.g. &#39;FRA&#39;) | |
| **destination** | **String**| 3-letter IATA airport code (e.g. &#39;JFK&#39;) | |
| **date** | **String**| Departure date (YYYY-MM-DD) in local time of departure airport | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="operationsSchedulesFromDateTimeByOriginAndDestinationGet"></a>
# **operationsSchedulesFromDateTimeByOriginAndDestinationGet**
> Object operationsSchedulesFromDateTimeByOriginAndDestinationGet(origin, destination, fromDateTime, accept, directFlights, limit, offset)

Flight Schedules

Scheduled flights between given airports on a given date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String origin = "origin_example"; // String | Departure airport. 3-letter IATA airport code (e.g. 'ZRH')
    String destination = "destination_example"; // String | Destination airport. 3-letter IATA airport code (e.g. 'FRA')
    String fromDateTime = "fromDateTime_example"; // String | Local departure date and optionally departure time (YYYY-MM-DD or YYYY-MM-DDTHH:mm). When not provided, time is assumed to be 00:01
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    Boolean directFlights = true; // Boolean | Show only direct flights (false=0, true=1). Default is false
    String limit = "limit_example"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "offset_example"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.operationsSchedulesFromDateTimeByOriginAndDestinationGet(origin, destination, fromDateTime, accept, directFlights, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsSchedulesFromDateTimeByOriginAndDestinationGet");
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
| **origin** | **String**| Departure airport. 3-letter IATA airport code (e.g. &#39;ZRH&#39;) | |
| **destination** | **String**| Destination airport. 3-letter IATA airport code (e.g. &#39;FRA&#39;) | |
| **fromDateTime** | **String**| Local departure date and optionally departure time (YYYY-MM-DD or YYYY-MM-DDTHH:mm). When not provided, time is assumed to be 00:01 | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **directFlights** | **Boolean**| Show only direct flights (false&#x3D;0, true&#x3D;1). Default is false | [optional] |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

