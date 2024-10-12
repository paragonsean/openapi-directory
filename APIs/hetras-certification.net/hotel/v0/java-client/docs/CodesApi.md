# CodesApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**codesGetCode**](CodesApi.md#codesGetCode) | **GET** /api/hotel/v0/hotels/{hotelId}/codes/{id} | Get all the details for a specific code available for the hotel. |
| [**codesGetCodes**](CodesApi.md#codesGetCodes) | **GET** /api/hotel/v0/hotels/{hotelId}/codes | Get a list of codes for the specified hotel either filtered by type or code. |


<a id="codesGetCode"></a>
# **codesGetCode**
> CodeFullEntry codesGetCode(appId, appKey, hotelId, id)

Get all the details for a specific code available for the hotel.

Read the details about a specific code available for the defined hotel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    CodesApi apiInstance = new CodesApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id the code available for.
    String id = "id_example"; // String | The code identifier you want to see details for.
    try {
      CodeFullEntry result = apiInstance.codesGetCode(appId, appKey, hotelId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodesApi#codesGetCode");
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
| **hotelId** | **Integer**| The hotel id the code available for. | |
| **id** | **String**| The code identifier you want to see details for. | |

### Return type

[**CodeFullEntry**](CodeFullEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details for the given code and hotel. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI or the requested rateplan could not be found. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="codesGetCodes"></a>
# **codesGetCodes**
> CodesListResponse codesGetCodes(appId, appKey, hotelId, code, type)

Get a list of codes for the specified hotel either filtered by type or code.

With this call you can find codes for a hotel by type or code. By default and without any filter criteria              defined it will return you all available codes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    CodesApi apiInstance = new CodesApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | The hotel id you are trying to find codes for.
    String code = "code_example"; // String | Return all results matching the specified code. A code is unique in combination with the type              which means when you query for a code you could get multiple results each for a different type
    String type = "GuestRequest"; // String | Return all codes for the specified type
    try {
      CodesListResponse result = apiInstance.codesGetCodes(appId, appKey, hotelId, code, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodesApi#codesGetCodes");
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
| **hotelId** | **Integer**| The hotel id you are trying to find codes for. | |
| **code** | **String**| Return all results matching the specified code. A code is unique in combination with the type              which means when you query for a code you could get multiple results each for a different type | [optional] |
| **type** | **String**| Return all codes for the specified type | [optional] [enum: GuestRequest, RequestDietary, VIPStatus, ReasonForRateChange, Regrets, MarketSegments, SourceOfBusiness, LoyaltyProgram, CancellationReason, AccountType, AccountRank, VIPLevel, Title, ContactFunction, Territory, CorrespondenceType, ExternalProgramType, RevenueBucket, AdditionalRevenueBucket, AdditionalStatisticsBuckets, MealPeriod, BillingCycle, ReminderCycle, MajorMarketSegments, DocumentType, ActivityType, ReservationLabels] |

### Return type

[**CodesListResponse**](CodesListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of codes for a requested hotel matching the filter criteria. |  -  |
| **204** | There are no codes found for the given filtering criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

