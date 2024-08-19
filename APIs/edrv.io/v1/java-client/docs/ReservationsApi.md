# ReservationsApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReservation**](ReservationsApi.md#getReservation) | **GET** /v1/reservations/{id} |  |
| [**getReservations**](ReservationsApi.md#getReservations) | **GET** /v1/reservations |  |
| [**updatereservation**](ReservationsApi.md#updatereservation) | **PATCH** /v1/reservations/{id} |  |


<a id="getReservation"></a>
# **getReservation**
> getReservation(id, includeChargestation, includeOrganization)



Get one reservation data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    String id = "id_example"; // String | ID of the reservation that needs to be fetched
    Boolean includeChargestation = true; // Boolean | Populate chargestation
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getReservation(id, includeChargestation, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#getReservation");
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
| **id** | **String**| ID of the reservation that needs to be fetched | |
| **includeChargestation** | **Boolean**| Populate chargestation | [optional] |
| **includeOrganization** | **Boolean**| Populate organization | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getReservations"></a>
# **getReservations**
> getReservations(paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeChargestation, includeOrganization)



Get Reservations data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    Integer paginateLimit = 20; // Integer | Number of results per page
    String paginatePage = "paginatePage_example"; // String | The queried page index
    Boolean paginateEnabled = true; // Boolean | Enable pagination
    String sortBy = "createdAt"; // String | Sort data by this key
    String sortOrder = "desc"; // String | asc to sort ascending (default is desc - descending)
    OffsetDateTime createdAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime createdAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    Boolean includeChargestation = true; // Boolean | Populate chargestation
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getReservations(paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeChargestation, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#getReservations");
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
| **paginateLimit** | **Integer**| Number of results per page | [optional] [default to 20] |
| **paginatePage** | **String**| The queried page index | [optional] |
| **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true] |
| **sortBy** | **String**| Sort data by this key | [optional] [default to createdAt] |
| **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to desc] [enum: desc, asc] |
| **createdAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **createdAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **includeChargestation** | **Boolean**| Populate chargestation | [optional] |
| **includeOrganization** | **Boolean**| Populate organization | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updatereservation"></a>
# **updatereservation**
> PatchChargeStation200Response updatereservation(id, updatereservationRequest)



Use to request a update an existing reservation. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReservationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReservationsApi apiInstance = new ReservationsApi(defaultClient);
    String id = "id_example"; // String | ID of the reservation that needs to be fetched
    UpdatereservationRequest updatereservationRequest = new UpdatereservationRequest(); // UpdatereservationRequest | 
    try {
      PatchChargeStation200Response result = apiInstance.updatereservation(id, updatereservationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReservationsApi#updatereservation");
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
| **id** | **String**| ID of the reservation that needs to be fetched | |
| **updatereservationRequest** | [**UpdatereservationRequest**](UpdatereservationRequest.md)|  | |

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

