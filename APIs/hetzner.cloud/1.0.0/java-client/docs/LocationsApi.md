# LocationsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationsGet**](LocationsApi.md#locationsGet) | **GET** /locations | Get all Locations |
| [**locationsIdGet**](LocationsApi.md#locationsIdGet) | **GET** /locations/{id} | Get a Location |


<a id="locationsGet"></a>
# **locationsGet**
> LocationsGet200Response locationsGet(name)

Get all Locations

Returns all Location objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter Locations by their name. The response will only contain the Location matching the specified name.
    try {
      LocationsGet200Response result = apiInstance.locationsGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsGet");
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
| **name** | **String**| Can be used to filter Locations by their name. The response will only contain the Location matching the specified name. | [optional] |

### Return type

[**LocationsGet200Response**](LocationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;locations&#x60; key in the reply contains an array of Location objects with this structure |  -  |

<a id="locationsIdGet"></a>
# **locationsIdGet**
> LocationsIdGet200Response locationsIdGet(id)

Get a Location

Returns a specific Location object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    Integer id = 56; // Integer | ID of Location
    try {
      LocationsIdGet200Response result = apiInstance.locationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsIdGet");
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
| **id** | **Integer**| ID of Location | |

### Return type

[**LocationsIdGet200Response**](LocationsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;location&#x60; key in the reply contains a Location object with this structure |  -  |

