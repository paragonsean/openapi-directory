# AtmCountrySubdivisionsApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**atmsV1CountrysubdivisionGet**](AtmCountrySubdivisionsApi.md#atmsV1CountrysubdivisionGet) | **GET** /atms/v1/countrysubdivision | Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada. |


<a id="atmsV1CountrysubdivisionGet"></a>
# **atmsV1CountrysubdivisionGet**
> CountrySubdivisionResponse atmsV1CountrysubdivisionGet(country)

Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada.

Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AtmCountrySubdivisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    AtmCountrySubdivisionsApi apiInstance = new AtmCountrySubdivisionsApi(defaultClient);
    String country = "USA"; // String | Any three digit country code as defined in ISO 3166-1.  \"USA\" or \"CAN\"
    try {
      CountrySubdivisionResponse result = apiInstance.atmsV1CountrysubdivisionGet(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AtmCountrySubdivisionsApi#atmsV1CountrysubdivisionGet");
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
| **country** | **String**| Any three digit country code as defined in ISO 3166-1.  \&quot;USA\&quot; or \&quot;CAN\&quot; | |

### Return type

[**CountrySubdivisionResponse**](CountrySubdivisionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all the CountrySubdivisions |  -  |
| **0** | Unexpected error |  -  |

