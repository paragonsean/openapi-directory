# CountriesApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countriesGet**](CountriesApi.md#countriesGet) | **GET** /countries | List of countries |
| [**countriesIdGet**](CountriesApi.md#countriesIdGet) | **GET** /countries/{id} | Country by ID |


<a id="countriesGet"></a>
# **countriesGet**
> CountriesResponse countriesGet(pageNumber, pageSize, filterRegion, filterSubRegion, sort)

List of countries

Returns all available countries. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    Set<String> filterRegion = Arrays.asList(); // Set<String> | Filtration by region.
    Set<String> filterSubRegion = Arrays.asList(); // Set<String> | Filtration by sub region.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | area | -area | | population | -population | | region | -region | | sub_region | -sub_region | 
    try {
      CountriesResponse result = apiInstance.countriesGet(pageNumber, pageSize, filterRegion, filterSubRegion, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#countriesGet");
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
| **pageNumber** | **Integer**| Current page number. | [optional] |
| **pageSize** | **Integer**| Page size.&lt;br&gt;*Default value: 100*  | [optional] |
| **filterRegion** | [**Set&lt;String&gt;**](String.md)| Filtration by region. | [optional] [enum: africa, americas, asia, europe, oceania, polar] |
| **filterSubRegion** | [**Set&lt;String&gt;**](String.md)| Filtration by sub region. | [optional] [enum: northern_africa, southern_africa, western_africa, eastern_africa, middle_africa, northern_america, south_america, central_america, caribbean, southern_asia, western_asia, eastern_asia, south_eastern_asia, central_asia, northern_europe, southern_europe, western_europe, eastern_europe, polynesia, australia_and_new_zealand, micronesia, melanesia] |
| **sort** | [**Set&lt;String&gt;**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | area | -area | | population | -population | | region | -region | | sub_region | -sub_region |  | [optional] [enum: name, -name, area, -area, population, -population, region, -region, sub_region, -sub_region] |

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of countries. |  -  |

<a id="countriesIdGet"></a>
# **countriesIdGet**
> CountryResponse countriesIdGet(id)

Country by ID

Returns country with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      CountryResponse result = apiInstance.countriesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#countriesIdGet");
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
| **id** | **String**| Unique ID. | |

### Return type

[**CountryResponse**](CountryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Country informatiion. |  -  |
| **404** | Country ID is not valid. |  -  |

