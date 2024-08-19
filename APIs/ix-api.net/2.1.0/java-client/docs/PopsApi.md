# PopsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**popsList**](PopsApi.md#popsList) | **GET** /pops |  |
| [**popsRead**](PopsApi.md#popsRead) | **GET** /pops/{id} |  |


<a id="popsList"></a>
# **popsList**
> List&lt;PointOfPresence&gt; popsList(id, facility, metroAreaNetwork, capabilityMediaType, capabilitySpeed, capabilitySpeedLt, capabilitySpeedLte, capabilitySpeedGt, capabilitySpeedGte)



List all PoPs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    PopsApi apiInstance = new PopsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String facility = "facility_example"; // String | Filter by facility
    String metroAreaNetwork = "metroAreaNetwork_example"; // String | Filter by metro_area_network
    String capabilityMediaType = "capabilityMediaType_example"; // String | Filter by capability_media_type
    Integer capabilitySpeed = 56; // Integer | Filter by capability_speed
    Integer capabilitySpeedLt = 56; // Integer | Filter by capability_speed__lt
    Integer capabilitySpeedLte = 56; // Integer | Filter by capability_speed__lte
    Integer capabilitySpeedGt = 56; // Integer | Filter by capability_speed__gt
    Integer capabilitySpeedGte = 56; // Integer | Filter by capability_speed__gte
    try {
      List<PointOfPresence> result = apiInstance.popsList(id, facility, metroAreaNetwork, capabilityMediaType, capabilitySpeed, capabilitySpeedLt, capabilitySpeedLte, capabilitySpeedGt, capabilitySpeedGte);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PopsApi#popsList");
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
| **facility** | **String**| Filter by facility | [optional] |
| **metroAreaNetwork** | **String**| Filter by metro_area_network | [optional] |
| **capabilityMediaType** | **String**| Filter by capability_media_type | [optional] |
| **capabilitySpeed** | **Integer**| Filter by capability_speed | [optional] |
| **capabilitySpeedLt** | **Integer**| Filter by capability_speed__lt | [optional] |
| **capabilitySpeedLte** | **Integer**| Filter by capability_speed__lte | [optional] |
| **capabilitySpeedGt** | **Integer**| Filter by capability_speed__gt | [optional] |
| **capabilitySpeedGte** | **Integer**| Filter by capability_speed__gte | [optional] |

### Return type

[**List&lt;PointOfPresence&gt;**](PointOfPresence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Point Of Presence |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="popsRead"></a>
# **popsRead**
> PointOfPresence popsRead(id)



Get a single point of presence

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PopsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    PopsApi apiInstance = new PopsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      PointOfPresence result = apiInstance.popsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PopsApi#popsRead");
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

[**PointOfPresence**](PointOfPresence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Point Of Presence |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

