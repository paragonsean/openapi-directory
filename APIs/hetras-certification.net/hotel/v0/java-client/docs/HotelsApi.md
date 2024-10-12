# HotelsApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hotelsGetHotel**](HotelsApi.md#hotelsGetHotel) | **GET** /api/hotel/v0/hotels/{hotelId} | Get the details of the hotel with the speccified hotel id. |
| [**hotelsGetHotels**](HotelsApi.md#hotelsGetHotels) | **GET** /api/hotel/v0/hotels | Get a list of all the hotels of a chain your application has access to. |


<a id="hotelsGetHotel"></a>
# **hotelsGetHotel**
> Hotel hotelsGetHotel(appId, appKey, hotelId)

Get the details of the hotel with the speccified hotel id.

Load the details about the specified hotel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HotelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    HotelsApi apiInstance = new HotelsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | 
    try {
      Hotel result = apiInstance.hotelsGetHotel(appId, appKey, hotelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HotelsApi#hotelsGetHotel");
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
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**|  | |

### Return type

[**Hotel**](Hotel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The details about the hotel. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="hotelsGetHotels"></a>
# **hotelsGetHotels**
> List&lt;Hotel&gt; hotelsGetHotels(appId, appKey)

Get a list of all the hotels of a chain your application has access to.

Load the details about all the hotels your application has access to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HotelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    HotelsApi apiInstance = new HotelsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    try {
      List<Hotel> result = apiInstance.hotelsGetHotels(appId, appKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HotelsApi#hotelsGetHotels");
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
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |

### Return type

[**List&lt;Hotel&gt;**](Hotel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of hotels. |  -  |
| **204** | You don´t have access to any hotels. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

