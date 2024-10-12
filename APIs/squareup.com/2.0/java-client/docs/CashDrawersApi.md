# CashDrawersApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listCashDrawerShiftEvents**](CashDrawersApi.md#listCashDrawerShiftEvents) | **GET** /v2/cash-drawers/shifts/{shift_id}/events | ListCashDrawerShiftEvents |
| [**listCashDrawerShifts**](CashDrawersApi.md#listCashDrawerShifts) | **GET** /v2/cash-drawers/shifts | ListCashDrawerShifts |
| [**retrieveCashDrawerShift**](CashDrawersApi.md#retrieveCashDrawerShift) | **GET** /v2/cash-drawers/shifts/{shift_id} | RetrieveCashDrawerShift |


<a id="listCashDrawerShiftEvents"></a>
# **listCashDrawerShiftEvents**
> ListCashDrawerShiftEventsResponse listCashDrawerShiftEvents(locationId, shiftId, limit, cursor)

ListCashDrawerShiftEvents

Provides a paginated list of events for a single cash drawer shift.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashDrawersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CashDrawersApi apiInstance = new CashDrawersApi(defaultClient);
    String locationId = "locationId_example"; // String | The ID of the location to list cash drawer shifts for.
    String shiftId = "shiftId_example"; // String | The shift ID.
    Integer limit = 56; // Integer | Number of resources to be returned in a page of results (200 by default, 1000 max).
    String cursor = "cursor_example"; // String | Opaque cursor for fetching the next page of results.
    try {
      ListCashDrawerShiftEventsResponse result = apiInstance.listCashDrawerShiftEvents(locationId, shiftId, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashDrawersApi#listCashDrawerShiftEvents");
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
| **locationId** | **String**| The ID of the location to list cash drawer shifts for. | |
| **shiftId** | **String**| The shift ID. | |
| **limit** | **Integer**| Number of resources to be returned in a page of results (200 by default, 1000 max). | [optional] |
| **cursor** | **String**| Opaque cursor for fetching the next page of results. | [optional] |

### Return type

[**ListCashDrawerShiftEventsResponse**](ListCashDrawerShiftEventsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listCashDrawerShifts"></a>
# **listCashDrawerShifts**
> ListCashDrawerShiftsResponse listCashDrawerShifts(locationId, sortOrder, beginTime, endTime, limit, cursor)

ListCashDrawerShifts

Provides the details for all of the cash drawer shifts for a location in a date range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashDrawersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CashDrawersApi apiInstance = new CashDrawersApi(defaultClient);
    String locationId = "locationId_example"; // String | The ID of the location to query for a list of cash drawer shifts.
    String sortOrder = "sortOrder_example"; // String | The order in which cash drawer shifts are listed in the response, based on their opened_at field. Default value: ASC
    String beginTime = "beginTime_example"; // String | The inclusive start time of the query on opened_at, in ISO 8601 format.
    String endTime = "endTime_example"; // String | The exclusive end date of the query on opened_at, in ISO 8601 format.
    Integer limit = 56; // Integer | Number of cash drawer shift events in a page of results (200 by default, 1000 max).
    String cursor = "cursor_example"; // String | Opaque cursor for fetching the next page of results.
    try {
      ListCashDrawerShiftsResponse result = apiInstance.listCashDrawerShifts(locationId, sortOrder, beginTime, endTime, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashDrawersApi#listCashDrawerShifts");
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
| **locationId** | **String**| The ID of the location to query for a list of cash drawer shifts. | |
| **sortOrder** | **String**| The order in which cash drawer shifts are listed in the response, based on their opened_at field. Default value: ASC | [optional] |
| **beginTime** | **String**| The inclusive start time of the query on opened_at, in ISO 8601 format. | [optional] |
| **endTime** | **String**| The exclusive end date of the query on opened_at, in ISO 8601 format. | [optional] |
| **limit** | **Integer**| Number of cash drawer shift events in a page of results (200 by default, 1000 max). | [optional] |
| **cursor** | **String**| Opaque cursor for fetching the next page of results. | [optional] |

### Return type

[**ListCashDrawerShiftsResponse**](ListCashDrawerShiftsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveCashDrawerShift"></a>
# **retrieveCashDrawerShift**
> RetrieveCashDrawerShiftResponse retrieveCashDrawerShift(locationId, shiftId)

RetrieveCashDrawerShift

Provides the summary details for a single cash drawer shift. See [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2021-08-18/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CashDrawersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CashDrawersApi apiInstance = new CashDrawersApi(defaultClient);
    String locationId = "locationId_example"; // String | The ID of the location to retrieve cash drawer shifts from.
    String shiftId = "shiftId_example"; // String | The shift ID.
    try {
      RetrieveCashDrawerShiftResponse result = apiInstance.retrieveCashDrawerShift(locationId, shiftId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CashDrawersApi#retrieveCashDrawerShift");
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
| **locationId** | **String**| The ID of the location to retrieve cash drawer shifts from. | |
| **shiftId** | **String**| The shift ID. | |

### Return type

[**RetrieveCashDrawerShiftResponse**](RetrieveCashDrawerShiftResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

