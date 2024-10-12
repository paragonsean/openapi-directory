# DistrictsInRegionApi

All URIs are relative to *https://mtaa-api.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**districtsInARegion**](DistrictsInRegionApi.md#districtsInARegion) | **GET** /{country}/{region} | Returns all districts in region |


<a id="districtsInARegion"></a>
# **districtsInARegion**
> districtsInARegion(country, region)

Returns all districts in region

Returns a post code and all districts in a specified region

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DistrictsInRegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mtaa-api.herokuapp.com/api");

    DistrictsInRegionApi apiInstance = new DistrictsInRegionApi(defaultClient);
    String country = "country_example"; // String | Country name in lowercase eg( tanzania)
    String region = "region_example"; // String | Name of the region eg (Mbeya)
    try {
      apiInstance.districtsInARegion(country, region);
    } catch (ApiException e) {
      System.err.println("Exception when calling DistrictsInRegionApi#districtsInARegion");
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

