# DefaultApi

All URIs are relative to *https://api.deutschebahn.com/fasta/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findFacilities**](DefaultApi.md#findFacilities) | **GET** /facilities |  |
| [**findStationByStationNumber**](DefaultApi.md#findStationByStationNumber) | **GET** /stations/{stationnumber} |  |
| [**getFacilityByEquipmentNumber**](DefaultApi.md#getFacilityByEquipmentNumber) | **GET** /facilities/{equipmentnumber} |  |


<a id="findFacilities"></a>
# **findFacilities**
> List&lt;Facility&gt; findFacilities(type, state, equipmentnumbers, stationnumber, area)



Access to public facilities (escalators and elevators) in railway stations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/fasta/v2");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Set<String> type = Arrays.asList(); // Set<String> | Type of the facility.
    Set<String> state = Arrays.asList(); // Set<String> | Operational state of the facility.
    Set<Long> equipmentnumbers = Arrays.asList(); // Set<Long> | List of equipmentnumbers to select.
    Long stationnumber = 56L; // Long | Number of the station the facilities belong to.
    List<String> area = Arrays.asList(); // List<String> | Geo coordinate rectangle in WGS84-format to filter facilities by geographical position. Parameters must be 4 numbers exactly as follows: longitudeWest, latitudeSouth, longitudeEast, latitudeNorth.
    try {
      List<Facility> result = apiInstance.findFacilities(type, state, equipmentnumbers, stationnumber, area);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findFacilities");
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
| **type** | [**Set&lt;String&gt;**](String.md)| Type of the facility. | [optional] [enum: ESCALATOR, ELEVATOR] |
| **state** | [**Set&lt;String&gt;**](String.md)| Operational state of the facility. | [optional] [enum: ACTIVE, INACTIVE, UNKNOWN] |
| **equipmentnumbers** | [**Set&lt;Long&gt;**](Long.md)| List of equipmentnumbers to select. | [optional] |
| **stationnumber** | **Long**| Number of the station the facilities belong to. | [optional] |
| **area** | [**List&lt;String&gt;**](String.md)| Geo coordinate rectangle in WGS84-format to filter facilities by geographical position. Parameters must be 4 numbers exactly as follows: longitudeWest, latitudeSouth, longitudeEast, latitudeNorth. | [optional] |

### Return type

[**List&lt;Facility&gt;**](Facility.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | facility data |  -  |
| **400** | The given filters contained invalid values. |  -  |
| **406** | The requested representation format is not available. |  -  |
| **500** | A processing error has occurred. |  -  |
| **503** | The service has been disabled temporarily. |  -  |

<a id="findStationByStationNumber"></a>
# **findStationByStationNumber**
> Station findStationByStationNumber(stationnumber)



Returns information about a station (and its corresponding facilities) identified by a stationnumber.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/fasta/v2");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long stationnumber = 56L; // Long | Number of the station to fetch.
    try {
      Station result = apiInstance.findStationByStationNumber(stationnumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findStationByStationNumber");
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
| **stationnumber** | **Long**| Number of the station to fetch. | |

### Return type

[**Station**](Station.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | station data |  -  |
| **404** | The requested station could not be found. |  -  |
| **406** | Requested representation format is not available. |  -  |
| **500** | A processing error has occurred. |  -  |
| **503** | The service has been disabled temporarily. |  -  |

<a id="getFacilityByEquipmentNumber"></a>
# **getFacilityByEquipmentNumber**
> Facility getFacilityByEquipmentNumber(equipmentnumber)



Returns the facility identified by its equipmentnumber.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/fasta/v2");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long equipmentnumber = 56L; // Long | Equipmentnumber of the facility to fetch.
    try {
      Facility result = apiInstance.getFacilityByEquipmentNumber(equipmentnumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFacilityByEquipmentNumber");
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
| **equipmentnumber** | **Long**| Equipmentnumber of the facility to fetch. | |

### Return type

[**Facility**](Facility.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Facility data |  -  |
| **404** | The requested facility could not be found. |  -  |
| **406** | The requested representation format is not available. |  -  |
| **500** | A processing error has occurred. |  -  |
| **503** | The service has been disabled temporarily. |  -  |

