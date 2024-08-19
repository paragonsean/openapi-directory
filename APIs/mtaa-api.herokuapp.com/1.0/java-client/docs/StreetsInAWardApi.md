# StreetsInAWardApi

All URIs are relative to *https://mtaa-api.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**streetsInAWard**](StreetsInAWardApi.md#streetsInAWard) | **GET** /{country}/{region}/{district}/{ward} | Returns all streets in a ward |


<a id="streetsInAWard"></a>
# **streetsInAWard**
> streetsInAWard(country, region, district, ward)

Returns all streets in a ward

Returns all streets in a specified ward and ward postcode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreetsInAWardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mtaa-api.herokuapp.com/api");

    StreetsInAWardApi apiInstance = new StreetsInAWardApi(defaultClient);
    String country = "country_example"; // String | Country name in lowercase eg( tanzania)
    String region = "region_example"; // String | Name of the region eg (Mbeya)
    String district = "district_example"; // String | Name of the District eg (Rungwe)
    String ward = "ward_example"; // String | Name of the Ward eg (Kiwira)
    try {
      apiInstance.streetsInAWard(country, region, district, ward);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreetsInAWardApi#streetsInAWard");
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
| **country** | **String**| Country name in lowercase eg( tanzania) | |
| **region** | **String**| Name of the region eg (Mbeya) | |
| **district** | **String**| Name of the District eg (Rungwe) | |
| **ward** | **String**| Name of the Ward eg (Kiwira) | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **404** | Resource not Found |  -  |

