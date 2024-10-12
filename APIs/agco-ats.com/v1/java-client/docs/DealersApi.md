# DealersApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dealersGetDealerbyDealerCode**](DealersApi.md#dealersGetDealerbyDealerCode) | **GET** /api/v2/Dealers/{DealerCode} | Lookup a dealer using a dealer code. |
| [**dealersGetDealers**](DealersApi.md#dealersGetDealers) | **GET** /api/v2/Dealers | Get a list of dealers. |


<a id="dealersGetDealerbyDealerCode"></a>
# **dealersGetDealerbyDealerCode**
> DealerDBModelsDealer dealersGetDealerbyDealerCode(dealerCode)

Lookup a dealer using a dealer code.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    DealersApi apiInstance = new DealersApi(defaultClient);
    String dealerCode = "dealerCode_example"; // String | The Dealer Code to Search for
    try {
      DealerDBModelsDealer result = apiInstance.dealersGetDealerbyDealerCode(dealerCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealersApi#dealersGetDealerbyDealerCode");
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
| **dealerCode** | **String**| The Dealer Code to Search for | |

### Return type

[**DealerDBModelsDealer**](DealerDBModelsDealer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="dealersGetDealers"></a>
# **dealersGetDealers**
> APIPagedResponseDealerDBModelsDealer dealersGetDealers(brand, shippingCountry, dealerName, limit, offset)

Get a list of dealers.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DealersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    DealersApi apiInstance = new DealersApi(defaultClient);
    String brand = "brand_example"; // String | The brand to filter by.
    String shippingCountry = "shippingCountry_example"; // String | The country to filter by.
    String dealerName = "dealerName_example"; // String | The partial Dealer Name to filter by. Wildcard supported (*).
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseDealerDBModelsDealer result = apiInstance.dealersGetDealers(brand, shippingCountry, dealerName, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DealersApi#dealersGetDealers");
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
| **brand** | **String**| The brand to filter by. | [optional] |
| **shippingCountry** | **String**| The country to filter by. | [optional] |
| **dealerName** | **String**| The partial Dealer Name to filter by. Wildcard supported (*). | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseDealerDBModelsDealer**](APIPagedResponseDealerDBModelsDealer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

