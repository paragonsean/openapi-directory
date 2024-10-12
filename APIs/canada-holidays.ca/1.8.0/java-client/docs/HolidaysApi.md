# HolidaysApi

All URIs are relative to *https://canada-holidays.ca*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**holiday**](HolidaysApi.md#holiday) | **GET** /api/v1/holidays/{holidayId} | Get a holiday by id |
| [**holidays**](HolidaysApi.md#holidays) | **GET** /api/v1/holidays | Get all holidays |


<a id="holiday"></a>
# **holiday**
> Holiday200Response holiday(holidayId, year, optional)

Get a holiday by id

Returns one Canadian statutory holiday by integer id. Returns a 404 response for invalid ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://canada-holidays.ca");

    HolidaysApi apiInstance = new HolidaysApi(defaultClient);
    Integer holidayId = 2; // Integer | Primary key for a holiday
    Integer year = 2023; // Integer | A calendar year
    String optional = "1"; // String | A boolean parameter. If false or 0 (default), will return provinces for which this is a legislated holiday. If true or 1, will return provinces which optionally celebrate this holiday.
    try {
      Holiday200Response result = apiInstance.holiday(holidayId, year, optional);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaysApi#holiday");
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
| **holidayId** | **Integer**| Primary key for a holiday | |
| **year** | **Integer**| A calendar year | [optional] [default to 2023] |
| **optional** | **String**| A boolean parameter. If false or 0 (default), will return provinces for which this is a legislated holiday. If true or 1, will return provinces which optionally celebrate this holiday. | [optional] [default to false] [enum: 1, 0, true, false] |

### Return type

[**Holiday200Response**](Holiday200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="holidays"></a>
# **holidays**
> Holidays200Response holidays(year, federal, optional)

Get all holidays

Returns Canadian public holidays. Each holiday lists the regions that observe it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://canada-holidays.ca");

    HolidaysApi apiInstance = new HolidaysApi(defaultClient);
    Integer year = 2023; // Integer | A calendar year
    String federal = "1"; // String | A boolean parameter. If true or 1, will return only federal holidays. If false or 0, will return no federal holidays.
    String optional = "1"; // String | A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC.
    try {
      Holidays200Response result = apiInstance.holidays(year, federal, optional);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaysApi#holidays");
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
| **year** | **Integer**| A calendar year | [optional] [default to 2023] |
| **federal** | **String**| A boolean parameter. If true or 1, will return only federal holidays. If false or 0, will return no federal holidays. | [optional] [enum: 1, 0, true, false] |
| **optional** | **String**| A boolean parameter. If false or 0 (default), will return only legislated holidays. If true or 1, will return optional holidays from Alberta and BC. | [optional] [default to false] [enum: 1, 0, true, false] |

### Return type

[**Holidays200Response**](Holidays200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

