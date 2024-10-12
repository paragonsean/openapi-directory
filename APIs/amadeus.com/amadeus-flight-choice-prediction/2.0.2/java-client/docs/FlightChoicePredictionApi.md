# FlightChoicePredictionApi

All URIs are relative to *https://test.api.amadeus.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFlightChoicePredict**](FlightChoicePredictionApi.md#getFlightChoicePredict) | **POST** /shopping/flight-offers/prediction | Predict the choice of flight offers. |


<a id="getFlightChoicePredict"></a>
# **getFlightChoicePredict**
> Success getFlightChoicePredict(xHTTPMethodOverride, body)

Predict the choice of flight offers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlightChoicePredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v2");

    FlightChoicePredictionApi apiInstance = new FlightChoicePredictionApi(defaultClient);
    String xHTTPMethodOverride = "GET"; // String | the HTTP method to apply
    FlightOffersSearchReply body = new FlightOffersSearchReply(); // FlightOffersSearchReply | 
    try {
      Success result = apiInstance.getFlightChoicePredict(xHTTPMethodOverride, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlightChoicePredictionApi#getFlightChoicePredict");
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
| **xHTTPMethodOverride** | **String**| the HTTP method to apply | [default to GET] |
| **body** | [**FlightOffersSearchReply**](FlightOffersSearchReply.md)|  | |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.amadeus+json, application/json
 - **Accept**: application/vnd.amadeus+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flight Offers Search Reply with prediction |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 32171   | MANDATORY DATA MISSING  |  -  |
| **500** | Unexpected error |  -  |

