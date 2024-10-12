# ModeApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**modeArrivals**](ModeApi.md#modeArrivals) | **GET** /Mode/{mode}/Arrivals | Gets the next arrival predictions for all stops of a given mode |
| [**modeGetActiveServiceTypes**](ModeApi.md#modeGetActiveServiceTypes) | **GET** /Mode/ActiveServiceTypes | Returns the service type active for a mode.              Currently only supports tube |


<a id="modeArrivals"></a>
# **modeArrivals**
> List&lt;TflApiPresentationEntitiesPrediction&gt; modeArrivals(mode, count)

Gets the next arrival predictions for all stops of a given mode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    ModeApi apiInstance = new ModeApi(defaultClient);
    String mode = "mode_example"; // String | A mode name e.g. tube, dlr
    Integer count = 56; // Integer | A number of arrivals to return for each stop, -1 to return all available.
    try {
      List<TflApiPresentationEntitiesPrediction> result = apiInstance.modeArrivals(mode, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModeApi#modeArrivals");
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
| **mode** | **String**| A mode name e.g. tube, dlr | |
| **count** | **Integer**| A number of arrivals to return for each stop, -1 to return all available. | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesPrediction&gt;**](TflApiPresentationEntitiesPrediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="modeGetActiveServiceTypes"></a>
# **modeGetActiveServiceTypes**
> List&lt;TflApiPresentationEntitiesActiveServiceType&gt; modeGetActiveServiceTypes()

Returns the service type active for a mode.              Currently only supports tube

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    ModeApi apiInstance = new ModeApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesActiveServiceType> result = apiInstance.modeGetActiveServiceTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModeApi#modeGetActiveServiceTypes");
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

[**List&lt;TflApiPresentationEntitiesActiveServiceType&gt;**](TflApiPresentationEntitiesActiveServiceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

