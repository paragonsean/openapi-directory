# AtmLocationsApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**atmsV1AtmGet**](AtmLocationsApi.md#atmsV1AtmGet) | **GET** /atms/v1/atm | Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features. |


<a id="atmsV1AtmGet"></a>
# **atmsV1AtmGet**
> AtmsResponse atmsV1AtmGet(pageOffset, pageLength, addressLine1, addressLine2, city, countrySubdivision, postalCode, country, latitude, longitude, distanceUnit, radius, supportEMV, internationalMaestroAccepted)

Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features.

Returns detailed information about an ATM location.  This information can be used to display ATMs on a map, provide driving directions, or show special ATM features. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AtmLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    AtmLocationsApi apiInstance = new AtmLocationsApi(defaultClient);
    Integer pageOffset = 0; // Integer | Zero-based offset where the response will start. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests.
    Integer pageLength = 5; // Integer | Maximum number of items to retrieve within the current \"page\" of results.
    String addressLine1 = "114 Fifth Avenue"; // String | Line 1 of the street address for the merchant location.  Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
    String addressLine2 = "Apartment 1"; // String | Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter.
    String city = "New York City"; // String | The name of the city for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    String countrySubdivision = "NY"; // String | The state or province for a merchant location (only supported for US and Canada locations).  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    String postalCode = "11101"; // String | The zip code or postal code for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter.
    String country = "USA"; // String | Any three digit country code for an ATM location.  Valid values are Three digit alpha country code as defined in ISO 3166-1.  This parameter is ignored if latitude and longitude are provided. This parameter is required if any other address information is provided including AddressLine1 AddressLine2 City PostalCode or CountrySubdivision.
    Double latitude = 38.76006576913497D; // Double | The latitude of a merchant location.  If latitude is provided longitude must also be provided.
    Double longitude = -90.74615107952418D; // Double | The longitude of a merchant location.  If longitude is provided latitude must also be provided.
    String distanceUnit = "MILE"; // String | Indicates the unit for the radius as well as the units of the distance of each location from the basepoint in the response.
    Integer radius = 25; // Integer | This is the radius from the search point in the distance unit you set.  For example if you want to search for locations within 50 miles of a certain point you would set DistanceUnit=mile and Radius=50.  This parameter is ignored in non-geocoded countries.
    Integer supportEMV = 1; // Integer | This indicates whether the ATM should have the ability to read chip cards or not.
    Integer internationalMaestroAccepted = 1; // Integer | This field will provide ATM Terminals which can still process Maestro transactions but are not yet EMV chip reader enabled. Information available only for USA and Argentina till October 2014.
    try {
      AtmsResponse result = apiInstance.atmsV1AtmGet(pageOffset, pageLength, addressLine1, addressLine2, city, countrySubdivision, postalCode, country, latitude, longitude, distanceUnit, radius, supportEMV, internationalMaestroAccepted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AtmLocationsApi#atmsV1AtmGet");
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
| **pageOffset** | **Integer**| Zero-based offset where the response will start. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests. | |
| **pageLength** | **Integer**| Maximum number of items to retrieve within the current \&quot;page\&quot; of results. | |
| **addressLine1** | **String**| Line 1 of the street address for the merchant location.  Usually includes the street number and name. This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter. | [optional] |
| **addressLine2** | **String**| Line 2 of the street address usually an apartment number or suite number. This parameter is used rarely and is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter and either City parameter or PostalCode parameter. | [optional] |
| **city** | **String**| The name of the city for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] |
| **countrySubdivision** | **String**| The state or province for a merchant location (only supported for US and Canada locations).  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] |
| **postalCode** | **String**| The zip code or postal code for a merchant location.  This parameter is ignored if latitude and longitude are provided. If you provide this parameter you must also provide the Country parameter. | [optional] |
| **country** | **String**| Any three digit country code for an ATM location.  Valid values are Three digit alpha country code as defined in ISO 3166-1.  This parameter is ignored if latitude and longitude are provided. This parameter is required if any other address information is provided including AddressLine1 AddressLine2 City PostalCode or CountrySubdivision. | [optional] |
| **latitude** | **Double**| The latitude of a merchant location.  If latitude is provided longitude must also be provided. | [optional] |
| **longitude** | **Double**| The longitude of a merchant location.  If longitude is provided latitude must also be provided. | [optional] |
| **distanceUnit** | **String**| Indicates the unit for the radius as well as the units of the distance of each location from the basepoint in the response. | [optional] |
| **radius** | **Integer**| This is the radius from the search point in the distance unit you set.  For example if you want to search for locations within 50 miles of a certain point you would set DistanceUnit&#x3D;mile and Radius&#x3D;50.  This parameter is ignored in non-geocoded countries. | [optional] |
| **supportEMV** | **Integer**| This indicates whether the ATM should have the ability to read chip cards or not. | [optional] |
| **internationalMaestroAccepted** | **Integer**| This field will provide ATM Terminals which can still process Maestro transactions but are not yet EMV chip reader enabled. Information available only for USA and Argentina till October 2014. | [optional] |

### Return type

[**AtmsResponse**](AtmsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of ATM locations |  -  |
| **0** | Unexpected error |  -  |

