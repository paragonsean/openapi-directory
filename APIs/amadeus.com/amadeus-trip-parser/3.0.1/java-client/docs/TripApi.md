# TripApi

All URIs are relative to *https://test.api.amadeus.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postTripParserRequest**](TripApi.md#postTripParserRequest) | **POST** /travel/trip-parser | POST Trip Parser request |


<a id="postTripParserRequest"></a>
# **postTripParserRequest**
> PostTripParserRequest200Response postTripParserRequest(documentEnvelope)

POST Trip Parser request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TripApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v3");

    TripApi apiInstance = new TripApi(defaultClient);
    DocumentEnvelope documentEnvelope = new DocumentEnvelope(); // DocumentEnvelope | 
    try {
      PostTripParserRequest200Response result = apiInstance.postTripParserRequest(documentEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TripApi#postTripParserRequest");
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
| **documentEnvelope** | [**DocumentEnvelope**](DocumentEnvelope.md)|  | [optional] |

### Return type

[**PostTripParserRequest200Response**](PostTripParserRequest200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.amadeus+json
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Reply |  -  |
| **400** | Bad Request  code    | title                                  ------- | -------------------------------------  4926    | INVALID DATA RECEIVED                           32171   | MANDATORY DATA MISSING  |  -  |
| **500** | Internal Server Error  code    | title                                  ------- | -------------------------------------  141     | SYSTEM ERROR HAS OCCURRED |  -  |
| **501** | Not Implemented  code    | title                                  ------- | -------------------------------------  141     | UNABLE TO SUPPORT |  -  |

