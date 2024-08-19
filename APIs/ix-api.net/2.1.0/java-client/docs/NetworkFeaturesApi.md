# NetworkFeaturesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networkFeaturesList**](NetworkFeaturesApi.md#networkFeaturesList) | **GET** /network-features |  |
| [**networkFeaturesRead**](NetworkFeaturesApi.md#networkFeaturesRead) | **GET** /network-features/{id} |  |


<a id="networkFeaturesList"></a>
# **networkFeaturesList**
> List&lt;NetworkFeature&gt; networkFeaturesList(id, type, required, networkService, name)



List available network features.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkFeaturesApi apiInstance = new NetworkFeaturesApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String type = "route_server"; // String | Filter by type
    String required = "required_example"; // String | Filter by required
    String networkService = "networkService_example"; // String | Filter by network_service
    String name = "name_example"; // String | Filter by name
    try {
      List<NetworkFeature> result = apiInstance.networkFeaturesList(id, type, required, networkService, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFeaturesApi#networkFeaturesList");
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
| **type** | **String**| Filter by type | [optional] [enum: route_server] |
| **required** | **String**| Filter by required | [optional] |
| **networkService** | **String**| Filter by network_service | [optional] |
| **name** | **String**| Filter by name | [optional] |

### Return type

[**List&lt;NetworkFeature&gt;**](NetworkFeature.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Polymorphic Network Feature |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="networkFeaturesRead"></a>
# **networkFeaturesRead**
> NetworkFeature networkFeaturesRead(id)



Get a single network feature by it&#39;s id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkFeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    NetworkFeaturesApi apiInstance = new NetworkFeaturesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      NetworkFeature result = apiInstance.networkFeaturesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkFeaturesApi#networkFeaturesRead");
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

[**NetworkFeature**](NetworkFeature.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Network Feature |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

