# CabwiseApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cabwiseGet**](CabwiseApi.md#cabwiseGet) | **GET** /Cabwise/search | Gets taxis and minicabs contact information |


<a id="cabwiseGet"></a>
# **cabwiseGet**
> Object cabwiseGet(lat, lon, optype, wc, radius, name, maxResults, legacyFormat, forceXml, twentyFourSevenOnly)

Gets taxis and minicabs contact information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CabwiseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    CabwiseApi apiInstance = new CabwiseApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude
    Double lon = 3.4D; // Double | Longitude
    String optype = "optype_example"; // String | Operator Type e.g Minicab, Executive, Limousine
    String wc = "wc_example"; // String | Wheelchair accessible
    Double radius = 3.4D; // Double | The radius of the bounding circle in metres
    String name = "name_example"; // String | Trading name of operating company
    Integer maxResults = 56; // Integer | An optional parameter to limit the number of results return. Default and maximum is 20.
    Boolean legacyFormat = true; // Boolean | Legacy Format
    Boolean forceXml = true; // Boolean | Force Xml
    Boolean twentyFourSevenOnly = true; // Boolean | Twenty Four Seven Only
    try {
      Object result = apiInstance.cabwiseGet(lat, lon, optype, wc, radius, name, maxResults, legacyFormat, forceXml, twentyFourSevenOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CabwiseApi#cabwiseGet");
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
| **lat** | **Double**| Latitude | |
| **lon** | **Double**| Longitude | |
| **optype** | **String**| Operator Type e.g Minicab, Executive, Limousine | [optional] |
| **wc** | **String**| Wheelchair accessible | [optional] |
| **radius** | **Double**| The radius of the bounding circle in metres | [optional] |
| **name** | **String**| Trading name of operating company | [optional] |
| **maxResults** | **Integer**| An optional parameter to limit the number of results return. Default and maximum is 20. | [optional] |
| **legacyFormat** | **Boolean**| Legacy Format | [optional] |
| **forceXml** | **Boolean**| Force Xml | [optional] |
| **twentyFourSevenOnly** | **Boolean**| Twenty Four Seven Only | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

