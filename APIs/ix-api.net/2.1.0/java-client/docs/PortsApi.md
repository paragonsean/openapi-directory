# PortsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**portsList**](PortsApi.md#portsList) | **GET** /ports |  |
| [**portsRead**](PortsApi.md#portsRead) | **GET** /ports/{id} |  |


<a id="portsList"></a>
# **portsList**
> List&lt;Port&gt; portsList(id, state, stateIsNot, mediaType, pop, name, externalRef, device, speed, connection)



List all ports.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    PortsApi apiInstance = new PortsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String state = "state_example"; // String | Filter by state
    String stateIsNot = "stateIsNot_example"; // String | Filter by state__is_not
    String mediaType = "mediaType_example"; // String | Filter by media_type
    String pop = "pop_example"; // String | Filter by pop
    String name = "name_example"; // String | Filter by name
    String externalRef = "externalRef_example"; // String | Filter by external_ref
    String device = "device_example"; // String | Filter by device
    String speed = "speed_example"; // String | Filter by speed
    String connection = "connection_example"; // String | Filter by connection
    try {
      List<Port> result = apiInstance.portsList(id, state, stateIsNot, mediaType, pop, name, externalRef, device, speed, connection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortsApi#portsList");
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
| **state** | **String**| Filter by state | [optional] |
| **stateIsNot** | **String**| Filter by state__is_not | [optional] |
| **mediaType** | **String**| Filter by media_type | [optional] |
| **pop** | **String**| Filter by pop | [optional] |
| **name** | **String**| Filter by name | [optional] |
| **externalRef** | **String**| Filter by external_ref | [optional] |
| **device** | **String**| Filter by device | [optional] |
| **speed** | **String**| Filter by speed | [optional] |
| **connection** | **String**| Filter by connection | [optional] |

### Return type

[**List&lt;Port&gt;**](Port.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Port |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="portsRead"></a>
# **portsRead**
> Port portsRead(id)



Retrieve a port.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    PortsApi apiInstance = new PortsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      Port result = apiInstance.portsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortsApi#portsRead");
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

[**Port**](Port.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Port |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

