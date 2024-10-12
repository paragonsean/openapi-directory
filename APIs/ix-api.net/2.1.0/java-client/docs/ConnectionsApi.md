# ConnectionsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectionsList**](ConnectionsApi.md#connectionsList) | **GET** /connections |  |
| [**connectionsRead**](ConnectionsApi.md#connectionsRead) | **GET** /connections/{id} |  |


<a id="connectionsList"></a>
# **connectionsList**
> List&lt;Connection&gt; connectionsList(id, state, stateIsNot, mode, modeIsNot, name, metroAreaNetwork, pop, facility, externalRef)



List all &#x60;connection&#x60;s.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String state = "state_example"; // String | Filter by state
    String stateIsNot = "stateIsNot_example"; // String | Filter by state__is_not
    String mode = "mode_example"; // String | Filter by mode
    String modeIsNot = "modeIsNot_example"; // String | Filter by mode__is_not
    String name = "name_example"; // String | Filter by name
    String metroAreaNetwork = "metroAreaNetwork_example"; // String | Filter by metro_area_network
    String pop = "pop_example"; // String | Filter by pop
    String facility = "facility_example"; // String | Filter by facility
    String externalRef = "externalRef_example"; // String | Filter by external_ref
    try {
      List<Connection> result = apiInstance.connectionsList(id, state, stateIsNot, mode, modeIsNot, name, metroAreaNetwork, pop, facility, externalRef);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsList");
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
| **mode** | **String**| Filter by mode | [optional] |
| **modeIsNot** | **String**| Filter by mode__is_not | [optional] |
| **name** | **String**| Filter by name | [optional] |
| **metroAreaNetwork** | **String**| Filter by metro_area_network | [optional] |
| **pop** | **String**| Filter by pop | [optional] |
| **facility** | **String**| Filter by facility | [optional] |
| **externalRef** | **String**| Filter by external_ref | [optional] |

### Return type

[**List&lt;Connection&gt;**](Connection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Connection |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="connectionsRead"></a>
# **connectionsRead**
> Connection connectionsRead(id)



Read a &#x60;connection&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      Connection result = apiInstance.connectionsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsRead");
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

[**Connection**](Connection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connection |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

