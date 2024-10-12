# AccidentStatsApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accidentStatsGet**](AccidentStatsApi.md#accidentStatsGet) | **GET** /AccidentStats/{year} | Gets all accident details for accidents occuring in the specified year |


<a id="accidentStatsGet"></a>
# **accidentStatsGet**
> List&lt;TflApiPresentationEntitiesAccidentStatsAccidentDetail&gt; accidentStatsGet(year)

Gets all accident details for accidents occuring in the specified year

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccidentStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    AccidentStatsApi apiInstance = new AccidentStatsApi(defaultClient);
    Integer year = 56; // Integer | The year for which to filter the accidents on.
    try {
      List<TflApiPresentationEntitiesAccidentStatsAccidentDetail> result = apiInstance.accidentStatsGet(year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccidentStatsApi#accidentStatsGet");
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
| **year** | **Integer**| The year for which to filter the accidents on. | |

### Return type

[**List&lt;TflApiPresentationEntitiesAccidentStatsAccidentDetail&gt;**](TflApiPresentationEntitiesAccidentStatsAccidentDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

