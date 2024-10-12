# Class10SearchVenuesApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10SearchVenuesGetVenuesGET**](Class10SearchVenuesApi.md#resource10SearchVenuesGetVenuesGET) | **GET** /1.0/search/venues | Search for venues. |


<a id="resource10SearchVenuesGetVenuesGET"></a>
# **resource10SearchVenuesGetVenuesGET**
> JsonVenues resource10SearchVenuesGetVenuesGET(cityId, cityName, country, name, p, state, stateCode)

Search for venues.

Search for venues.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10SearchVenuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10SearchVenuesApi apiInstance = new Class10SearchVenuesApi(defaultClient);
    String cityId = "cityId_example"; // String | the city's geoId
    String cityName = "cityName_example"; // String | name of the city where the venue is located
    String country = "country_example"; // String | the city's country
    String name = "name_example"; // String | name of the venue
    Integer p = 1; // Integer | the number of the result page you'd like to have
    String state = "state_example"; // String | the city's state
    String stateCode = "stateCode_example"; // String | the city's state code
    try {
      JsonVenues result = apiInstance.resource10SearchVenuesGetVenuesGET(cityId, cityName, country, name, p, state, stateCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10SearchVenuesApi#resource10SearchVenuesGetVenuesGET");
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
| **cityId** | **String**| the city&#39;s geoId | [optional] |
| **cityName** | **String**| name of the city where the venue is located | [optional] |
| **country** | **String**| the city&#39;s country | [optional] |
| **name** | **String**| name of the venue | [optional] |
| **p** | **Integer**| the number of the result page you&#39;d like to have | [optional] [default to 1] |
| **state** | **String**| the city&#39;s state | [optional] |
| **stateCode** | **String**| the city&#39;s state code | [optional] |

### Return type

[**JsonVenues**](JsonVenues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

