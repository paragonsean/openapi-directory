# DevicesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**devicesList**](DevicesApi.md#devicesList) | **GET** /devices |  |
| [**devicesRead**](DevicesApi.md#devicesRead) | **GET** /devices/{id} |  |


<a id="devicesList"></a>
# **devicesList**
> List&lt;Device&gt; devicesList(id, name, capabilityMediaType, capabilitySpeed, capabilitySpeedLt, capabilitySpeedLte, capabilitySpeedGt, capabilitySpeedGte, facility, pop, metroAreaNetwork)



List available devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String name = "name_example"; // String | Filter by name
    String capabilityMediaType = "capabilityMediaType_example"; // String | Filter by capability_media_type
    Integer capabilitySpeed = 56; // Integer | Filter by capability_speed
    Integer capabilitySpeedLt = 56; // Integer | Filter by capability_speed__lt
    Integer capabilitySpeedLte = 56; // Integer | Filter by capability_speed__lte
    Integer capabilitySpeedGt = 56; // Integer | Filter by capability_speed__gt
    Integer capabilitySpeedGte = 56; // Integer | Filter by capability_speed__gte
    String facility = "facility_example"; // String | Filter by facility
    String pop = "pop_example"; // String | Filter by pop
    String metroAreaNetwork = "metroAreaNetwork_example"; // String | Filter by metro_area_network
    try {
      List<Device> result = apiInstance.devicesList(id, name, capabilityMediaType, capabilitySpeed, capabilitySpeedLt, capabilitySpeedLte, capabilitySpeedGt, capabilitySpeedGte, facility, pop, metroAreaNetwork);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesList");
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
| **name** | **String**| Filter by name | [optional] |
| **capabilityMediaType** | **String**| Filter by capability_media_type | [optional] |
| **capabilitySpeed** | **Integer**| Filter by capability_speed | [optional] |
| **capabilitySpeedLt** | **Integer**| Filter by capability_speed__lt | [optional] |
| **capabilitySpeedLte** | **Integer**| Filter by capability_speed__lte | [optional] |
| **capabilitySpeedGt** | **Integer**| Filter by capability_speed__gt | [optional] |
| **capabilitySpeedGte** | **Integer**| Filter by capability_speed__gte | [optional] |
| **facility** | **String**| Filter by facility | [optional] |
| **pop** | **String**| Filter by pop | [optional] |
| **metroAreaNetwork** | **String**| Filter by metro_area_network | [optional] |

### Return type

[**List&lt;Device&gt;**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Device |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="devicesRead"></a>
# **devicesRead**
> Device devicesRead(id)



Get a specific device identified by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      Device result = apiInstance.devicesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesRead");
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

[**Device**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Device |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

