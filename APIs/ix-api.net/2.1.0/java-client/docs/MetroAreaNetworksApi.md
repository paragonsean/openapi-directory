# MetroAreaNetworksApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metroAreaNetworksList**](MetroAreaNetworksApi.md#metroAreaNetworksList) | **GET** /metro-area-networks |  |
| [**metroAreaNetworksRead**](MetroAreaNetworksApi.md#metroAreaNetworksRead) | **GET** /metro-area-networks/{id} |  |


<a id="metroAreaNetworksList"></a>
# **metroAreaNetworksList**
> List&lt;MetroAreaNetwork&gt; metroAreaNetworksList(id, name, metroArea, serviceProvider)



List all MetroAreaNetworks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetroAreaNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MetroAreaNetworksApi apiInstance = new MetroAreaNetworksApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String name = "name_example"; // String | Filter by name
    String metroArea = "metroArea_example"; // String | Filter by metro_area
    String serviceProvider = "serviceProvider_example"; // String | Filter by service_provider
    try {
      List<MetroAreaNetwork> result = apiInstance.metroAreaNetworksList(id, name, metroArea, serviceProvider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetroAreaNetworksApi#metroAreaNetworksList");
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
| **metroArea** | **String**| Filter by metro_area | [optional] |
| **serviceProvider** | **String**| Filter by service_provider | [optional] |

### Return type

[**List&lt;MetroAreaNetwork&gt;**](MetroAreaNetwork.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: MetroAreaNetwork |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="metroAreaNetworksRead"></a>
# **metroAreaNetworksRead**
> MetroAreaNetwork metroAreaNetworksRead(id)



Retrieve a MetroAreaNetwork

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetroAreaNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MetroAreaNetworksApi apiInstance = new MetroAreaNetworksApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      MetroAreaNetwork result = apiInstance.metroAreaNetworksRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetroAreaNetworksApi#metroAreaNetworksRead");
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

[**MetroAreaNetwork**](MetroAreaNetwork.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MetroAreaNetwork |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

