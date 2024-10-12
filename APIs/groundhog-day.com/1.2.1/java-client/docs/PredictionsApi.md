# PredictionsApi

All URIs are relative to *https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**predictions**](PredictionsApi.md#predictions) | **GET** /api/v1/predictions | Get predictions for a given year |


<a id="predictions"></a>
# **predictions**
> Predictions200Response predictions(year)

Get predictions for a given year

Get all predictions for a given year.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PredictionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1");

    PredictionsApi apiInstance = new PredictionsApi(defaultClient);
    Integer year = 56; // Integer | A calendar year
    try {
      Predictions200Response result = apiInstance.predictions(year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PredictionsApi#predictions");
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
| **year** | **Integer**| A calendar year | [optional] |

### Return type

[**Predictions200Response**](Predictions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **302** | Found |  * location - /api/v1/predictions?year&#x3D;2022 <br>  |
| **400** | Bad Request |  -  |

