# FacetsApi

All URIs are relative to *https://api.ideaconsult.net/enanomapper*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEndpointSummary_0**](FacetsApi.md#getEndpointSummary_0) | **GET** /enm/{db}/query/study | Search endpoint summary |


<a id="getEndpointSummary_0"></a>
# **getEndpointSummary_0**
> Facet getEndpointSummary_0(db, top, category)

Search endpoint summary

Returns endpoint summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/enanomapper");

    FacetsApi apiInstance = new FacetsApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String top = "P-CHEM"; // String | Top endpoint category
    String category = "category_example"; // String | Endpoint category (The value in the protocol.category.code field)
    try {
      Facet result = apiInstance.getEndpointSummary_0(db, top, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacetsApi#getEndpointSummary_0");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **top** | **String**| Top endpoint category | [optional] [enum: P-CHEM, ECOTOX, ENV FATE, TOX, EXPOSURE] |
| **category** | **String**| Endpoint category (The value in the protocol.category.code field) | [optional] |

### Return type

[**Facet**](Facet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **404** | Entries not found |  -  |

