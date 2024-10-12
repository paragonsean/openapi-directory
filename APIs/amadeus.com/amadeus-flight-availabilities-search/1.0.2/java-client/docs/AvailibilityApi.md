# AvailibilityApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchFlightAvailabilities**](AvailibilityApi.md#searchFlightAvailabilities) | **POST** /shopping/availability/flight-availabilities | Return list of Flight Availabilities based on posted searching criteria. |


<a id="searchFlightAvailabilities"></a>
# **searchFlightAvailabilities**
> SuccessAvailability searchFlightAvailabilities(xHTTPMethodOverride, getFlightAvailabilitiesBody)

Return list of Flight Availabilities based on posted searching criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailibilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    AvailibilityApi apiInstance = new AvailibilityApi(defaultClient);
    String xHTTPMethodOverride = "GET"; // String | the HTTP method to apply
    GetFlightAvailabilitiesQuery getFlightAvailabilitiesBody = new GetFlightAvailabilitiesQuery(); // GetFlightAvailabilitiesQuery | list of criteria to retrieve a list of flight availabilities
    try {
      SuccessAvailability result = apiInstance.searchFlightAvailabilities(xHTTPMethodOverride, getFlightAvailabilitiesBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailibilityApi#searchFlightAvailabilities");
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
| **xHTTPMethodOverride** | **String**| the HTTP method to apply | [default to GET] |
| **getFlightAvailabilitiesBody** | [**GetFlightAvailabilitiesQuery**](GetFlightAvailabilitiesQuery.md)| list of criteria to retrieve a list of flight availabilities | |

### Return type

[**SuccessAvailability**](SuccessAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.amadeus+json
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  425     | INVALID DATE 477     | INVALID FORMAT 572     | INVALID OPTION 2668    | PARAMETER COMBINATION INVALID/RESTRICTED 2781    | INVALID LENGTH 4926    | INVALID DATA RECEIVED 9880    | SELECTED DATE IS TOO FAR IN THE FUTURE 10661   | MAXIMUM NUMBER OF OCCURRENCES EXCEEDED  32171   | MANDATORY DATA MISSING  |  -  |
| **0** | Unexpected error |  -  |

