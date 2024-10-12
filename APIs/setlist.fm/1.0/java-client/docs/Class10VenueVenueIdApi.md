# Class10VenueVenueIdApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10VenueVenueIdGetVenueGET**](Class10VenueVenueIdApi.md#resource10VenueVenueIdGetVenueGET) | **GET** /1.0/venue/{venueId} | Get a venue by its unique id. |


<a id="resource10VenueVenueIdGetVenueGET"></a>
# **resource10VenueVenueIdGetVenueGET**
> JsonVenue resource10VenueVenueIdGetVenueGET(venueId)

Get a venue by its unique id.

Get a venue by its unique id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10VenueVenueIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10VenueVenueIdApi apiInstance = new Class10VenueVenueIdApi(defaultClient);
    String venueId = "venueId_example"; // String | the venue's id
    try {
      JsonVenue result = apiInstance.resource10VenueVenueIdGetVenueGET(venueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10VenueVenueIdApi#resource10VenueVenueIdGetVenueGET");
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
| **venueId** | **String**| the venue&#39;s id | |

### Return type

[**JsonVenue**](JsonVenue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

