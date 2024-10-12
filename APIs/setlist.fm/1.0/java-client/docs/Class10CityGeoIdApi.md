# Class10CityGeoIdApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10CityGeoIdGetCityGET**](Class10CityGeoIdApi.md#resource10CityGeoIdGetCityGET) | **GET** /1.0/city/{geoId} | Get a city by its unique geoId. |


<a id="resource10CityGeoIdGetCityGET"></a>
# **resource10CityGeoIdGetCityGET**
> JsonCity resource10CityGeoIdGetCityGET(geoId)

Get a city by its unique geoId.

Get a city by its unique geoId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10CityGeoIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10CityGeoIdApi apiInstance = new Class10CityGeoIdApi(defaultClient);
    String geoId = "geoId_example"; // String | the city's geoId
    try {
      JsonCity result = apiInstance.resource10CityGeoIdGetCityGET(geoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10CityGeoIdApi#resource10CityGeoIdGetCityGET");
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
| **geoId** | **String**| the city&#39;s geoId | |

### Return type

[**JsonCity**](JsonCity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

