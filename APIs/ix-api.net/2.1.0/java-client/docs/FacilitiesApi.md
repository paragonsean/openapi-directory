# FacilitiesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**facilitiesList**](FacilitiesApi.md#facilitiesList) | **GET** /facilities |  |
| [**facilitiesRead**](FacilitiesApi.md#facilitiesRead) | **GET** /facilities/{id} |  |


<a id="facilitiesList"></a>
# **facilitiesList**
> List&lt;Facility&gt; facilitiesList(id, capabilityMediaType, capabilitySpeed, capabilitySpeedLt, capabilitySpeedLte, capabilitySpeedGt, capabilitySpeedGte, organisationName, metroArea, metroAreaNetwork, addressCountry, addressLocality, postalCode)



Get a (filtered) list of &#x60;facilities&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String capabilityMediaType = "capabilityMediaType_example"; // String | Filter by capability_media_type
    Integer capabilitySpeed = 56; // Integer | Filter by capability_speed
    Integer capabilitySpeedLt = 56; // Integer | Filter by capability_speed__lt
    Integer capabilitySpeedLte = 56; // Integer | Filter by capability_speed__lte
    Integer capabilitySpeedGt = 56; // Integer | Filter by capability_speed__gt
    Integer capabilitySpeedGte = 56; // Integer | Filter by capability_speed__gte
    String organisationName = "organisationName_example"; // String | Filter by organisation_name
    String metroArea = "metroArea_example"; // String | Filter by metro_area
    String metroAreaNetwork = "metroAreaNetwork_example"; // String | Filter by metro_area_network
    String addressCountry = "addressCountry_example"; // String | Filter by address_country
    String addressLocality = "addressLocality_example"; // String | Filter by address_locality
    String postalCode = "postalCode_example"; // String | Filter by postal_code
    try {
      List<Facility> result = apiInstance.facilitiesList(id, capabilityMediaType, capabilitySpeed, capabilitySpeedLt, capabilitySpeedLte, capabilitySpeedGt, capabilitySpeedGte, organisationName, metroArea, metroAreaNetwork, addressCountry, addressLocality, postalCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#facilitiesList");
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
| **id** | [**List&lt;String&gt;**](String.md)| Filter by id | [optional] |
| **capabilityMediaType** | **String**| Filter by capability_media_type | [optional] |
| **capabilitySpeed** | **Integer**| Filter by capability_speed | [optional] |
| **capabilitySpeedLt** | **Integer**| Filter by capability_speed__lt | [optional] |
| **capabilitySpeedLte** | **Integer**| Filter by capability_speed__lte | [optional] |
| **capabilitySpeedGt** | **Integer**| Filter by capability_speed__gt | [optional] |
| **capabilitySpeedGte** | **Integer**| Filter by capability_speed__gte | [optional] |
| **organisationName** | **String**| Filter by organisation_name | [optional] |
| **metroArea** | **String**| Filter by metro_area | [optional] |
| **metroAreaNetwork** | **String**| Filter by metro_area_network | [optional] |
| **addressCountry** | **String**| Filter by address_country | [optional] |
| **addressLocality** | **String**| Filter by address_locality | [optional] |
| **postalCode** | **String**| Filter by postal_code | [optional] |

### Return type

[**List&lt;Facility&gt;**](Facility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Facility |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="facilitiesRead"></a>
# **facilitiesRead**
> List&lt;Facility&gt; facilitiesRead(id)



Retrieve a facility by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      List<Facility> result = apiInstance.facilitiesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#facilitiesRead");
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
| **id** | **String**| Get by id | |

### Return type

[**List&lt;Facility&gt;**](Facility.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Facility |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

