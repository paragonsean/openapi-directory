# WardsInADistrictApi

All URIs are relative to *https://mtaa-api.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**wardsInADistrict**](WardsInADistrictApi.md#wardsInADistrict) | **GET** /{country}/{region}/{district} | Returns all wards in a district |


<a id="wardsInADistrict"></a>
# **wardsInADistrict**
> wardsInADistrict(country, region, district)

Returns all wards in a district

Returns all wards in a  specified district and district postcode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WardsInADistrictApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mtaa-api.herokuapp.com/api");

    WardsInADistrictApi apiInstance = new WardsInADistrictApi(defaultClient);
    String country = "country_example"; // String | Country name in lowercase eg( tanzania)
    String region = "region_example"; // String | Name of the region eg (Mbeya)
    String district = "district_example"; // String | Name of the District eg (Rungwe)
    try {
      apiInstance.wardsInADistrict(country, region, district);
    } catch (ApiException e) {
      System.err.println("Exception when calling WardsInADistrictApi#wardsInADistrict");
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

