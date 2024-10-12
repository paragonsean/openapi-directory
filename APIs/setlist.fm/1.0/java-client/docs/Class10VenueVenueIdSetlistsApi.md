# Class10VenueVenueIdSetlistsApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10VenueVenueIdSetlistsGetVenueSetlistsGET**](Class10VenueVenueIdSetlistsApi.md#resource10VenueVenueIdSetlistsGetVenueSetlistsGET) | **GET** /1.0/venue/{venueId}/setlists | . |


<a id="resource10VenueVenueIdSetlistsGetVenueSetlistsGET"></a>
# **resource10VenueVenueIdSetlistsGetVenueSetlistsGET**
> JsonSetlists resource10VenueVenueIdSetlistsGetVenueSetlistsGET(venueId, p)

.

&lt;p&gt; Get setlists for a specific venue. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10VenueVenueIdSetlistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10VenueVenueIdSetlistsApi apiInstance = new Class10VenueVenueIdSetlistsApi(defaultClient);
    String venueId = "venueId_example"; // String | the id of the venue
    Integer p = 1; // Integer | the number of the result page
    try {
      JsonSetlists result = apiInstance.resource10VenueVenueIdSetlistsGetVenueSetlistsGET(venueId, p);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10VenueVenueIdSetlistsApi#resource10VenueVenueIdSetlistsGetVenueSetlistsGET");
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
| **venueId** | **String**| the id of the venue | |
| **p** | **Integer**| the number of the result page | [optional] [default to 1] |

### Return type

[**JsonSetlists**](JsonSetlists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

