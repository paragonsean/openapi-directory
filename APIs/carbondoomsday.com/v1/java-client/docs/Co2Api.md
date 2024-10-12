# Co2Api

All URIs are relative to *https://api.carbondoomsday.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**co2List**](Co2Api.md#co2List) | **GET** /co2/ |  |
| [**co2Read**](Co2Api.md#co2Read) | **GET** /co2/{date}/ |  |


<a id="co2List"></a>
# **co2List**
> Co2List200Response co2List(ppm, date, dateRange, ordering, page, limit)



CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Co2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.carbondoomsday.com/api");
    
    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    Co2Api apiInstance = new Co2Api(defaultClient);
    BigDecimal ppm = new BigDecimal(78); // BigDecimal | 
    String date = "date_example"; // String | 
    String dateRange = "dateRange_example"; // String | Multiple values may be separated by commas.
    String ordering = "ordering_example"; // String | Which field to use when ordering the results.
    Integer page = 56; // Integer | A page number within the paginated result set.
    Integer limit = 56; // Integer | Number of results to return per page.
    try {
      Co2List200Response result = apiInstance.co2List(ppm, date, dateRange, ordering, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Co2Api#co2List");
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
| **ppm** | **BigDecimal**|  | [optional] |
| **date** | **String**|  | [optional] |
| **dateRange** | **String**| Multiple values may be separated by commas. | [optional] |
| **ordering** | **String**| Which field to use when ordering the results. | [optional] |
| **page** | **Integer**| A page number within the paginated result set. | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |

### Return type

[**Co2List200Response**](Co2List200Response.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="co2Read"></a>
# **co2Read**
> CO2 co2Read(date)



CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Co2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.carbondoomsday.com/api");
    
    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    Co2Api apiInstance = new Co2Api(defaultClient);
    LocalDate date = LocalDate.now(); // LocalDate | 
    try {
      CO2 result = apiInstance.co2Read(date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Co2Api#co2Read");
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
| **date** | **LocalDate**|  | |

### Return type

[**CO2**](CO2.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

