# SeriesApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllSeries**](SeriesApi.md#fetchAllSeries) | **GET** /series | Find all series |
| [**fetchOneSeries**](SeriesApi.md#fetchOneSeries) | **GET** /series/{series_id} | Get one series by ID |


<a id="fetchAllSeries"></a>
# **fetchAllSeries**
> List&lt;SeriesEntity&gt; fetchAllSeries(label, fromDate, toDate, type, sort, pageSize, acceptLanguage)

Find all series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    String label = "label_example"; // String | Find only the venues whose label contains this value.
    LocalDate fromDate = LocalDate.now(); // LocalDate | Find only the series starting after this date.
    LocalDate toDate = LocalDate.now(); // LocalDate | Find only the series ending before this date.
    String type = "TOU"; // String | Find only the series whose type is equal to this value.
    String sort = "label"; // String | Sort the series in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<SeriesEntity> result = apiInstance.fetchAllSeries(label, fromDate, toDate, type, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#fetchAllSeries");
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
| **label** | **String**| Find only the venues whose label contains this value. | [optional] |
| **fromDate** | **LocalDate**| Find only the series starting after this date. | [optional] |
| **toDate** | **LocalDate**| Find only the series ending before this date. | [optional] |
| **type** | **String**| Find only the series whose type is equal to this value. | [optional] [enum: TOU, LGS] |
| **sort** | **String**| Sort the series in the corresponding order. | [optional] [default to first_date] [enum: label, -label, first_date, -first_date, last_date, -last_date] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;SeriesEntity&gt;**](SeriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of series |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneSeries"></a>
# **fetchOneSeries**
> SeriesEntity fetchOneSeries(seriesId, acceptLanguage)

Get one series by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    SeriesApi apiInstance = new SeriesApi(defaultClient);
    Integer seriesId = 56; // Integer | ID of the targeted series.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      SeriesEntity result = apiInstance.fetchOneSeries(seriesId, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesApi#fetchOneSeries");
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
| **seriesId** | **Integer**| ID of the targeted series. | |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**SeriesEntity**](SeriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one series |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

