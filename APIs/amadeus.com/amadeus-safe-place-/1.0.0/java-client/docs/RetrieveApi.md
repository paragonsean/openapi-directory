# RetrieveApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLocationSafetyRanking**](RetrieveApi.md#getLocationSafetyRanking) | **GET** /safety/safety-rated-locations/{safety-rated-locationId} | Retieve safety information of a location by its Id. |


<a id="getLocationSafetyRanking"></a>
# **getLocationSafetyRanking**
> Success1 getLocationSafetyRanking(safetyRatedLocationId)

Retieve safety information of a location by its Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetrieveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    RetrieveApi apiInstance = new RetrieveApi(defaultClient);
    String safetyRatedLocationId = "safetyRatedLocationId_example"; // String | identifier of the location
    try {
      Success1 result = apiInstance.getLocationSafetyRanking(safetyRatedLocationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetrieveApi#getLocationSafetyRanking");
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
| **safetyRatedLocationId** | **String**| identifier of the location | |

### Return type

[**Success1**](Success1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 4926    | INVALID DATA RECEIVED                32171   | MANDATORY DATA MISSING         |  -  |
| **404** | Not Found |  -  |
| **0** | Unexpected Error |  -  |

