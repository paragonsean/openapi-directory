# FeedContentAvailabilityApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**feedAvailabilityGet**](FeedContentAvailabilityApi.md#feedAvailabilityGet) | **GET** /feed/availability | Gets availability of featured feed content for the apps by wiki domain. |


<a id="feedAvailabilityGet"></a>
# **feedAvailabilityGet**
> Availability feedAvailabilityGet()

Gets availability of featured feed content for the apps by wiki domain.

Gets availability of featured feed content for the apps by wiki domain.  Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedContentAvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    FeedContentAvailabilityApi apiInstance = new FeedContentAvailabilityApi(defaultClient);
    try {
      Availability result = apiInstance.feedAvailabilityGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedContentAvailabilityApi#feedAvailabilityGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Availability**](Availability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8; profile=https://www.mediawiki.org/wiki/Specs/Availability/1.0.1, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JSON containing lists of wiki domains for which feed content is available. |  -  |
| **0** | Error |  -  |

