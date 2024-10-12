# Class10SearchCitiesApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10SearchCitiesGetCitiesGET**](Class10SearchCitiesApi.md#resource10SearchCitiesGetCitiesGET) | **GET** /1.0/search/cities | Search for a city. |


<a id="resource10SearchCitiesGetCitiesGET"></a>
# **resource10SearchCitiesGetCitiesGET**
> JsonCities resource10SearchCitiesGetCitiesGET(country, name, p, state, stateCode)

Search for a city.

Search for a city.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10SearchCitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10SearchCitiesApi apiInstance = new Class10SearchCitiesApi(defaultClient);
    String country = "country_example"; // String | the city's country
    String name = "name_example"; // String | name of the city
    Integer p = 1; // Integer | the number of the result page you'd like to have
    String state = "state_example"; // String | state the city lies in
    String stateCode = "stateCode_example"; // String | state code the city lies in
    try {
      JsonCities result = apiInstance.resource10SearchCitiesGetCitiesGET(country, name, p, state, stateCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10SearchCitiesApi#resource10SearchCitiesGetCitiesGET");
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
| **country** | **String**| the city&#39;s country | [optional] |
| **name** | **String**| name of the city | [optional] |
| **p** | **Integer**| the number of the result page you&#39;d like to have | [optional] [default to 1] |
| **state** | **String**| state the city lies in | [optional] |
| **stateCode** | **String**| state code the city lies in | [optional] |

### Return type

[**JsonCities**](JsonCities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

