# TaxRatesRateIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxTaxRateRepositoryV1DeleteByIdDelete**](TaxRatesRateIdApi.md#taxTaxRateRepositoryV1DeleteByIdDelete) | **DELETE** /V1/taxRates/{rateId} | taxRates/{rateId} |
| [**taxTaxRateRepositoryV1GetGet**](TaxRatesRateIdApi.md#taxTaxRateRepositoryV1GetGet) | **GET** /V1/taxRates/{rateId} | taxRates/{rateId} |


<a id="taxTaxRateRepositoryV1DeleteByIdDelete"></a>
# **taxTaxRateRepositoryV1DeleteByIdDelete**
> Boolean taxTaxRateRepositoryV1DeleteByIdDelete(rateId)

taxRates/{rateId}

Delete tax rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxRatesRateIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxRatesRateIdApi apiInstance = new TaxRatesRateIdApi(defaultClient);
    Integer rateId = 56; // Integer | 
    try {
      Boolean result = apiInstance.taxTaxRateRepositoryV1DeleteByIdDelete(rateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxRatesRateIdApi#taxTaxRateRepositoryV1DeleteByIdDelete");
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
| **rateId** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="taxTaxRateRepositoryV1GetGet"></a>
# **taxTaxRateRepositoryV1GetGet**
> TaxDataTaxRateInterface taxTaxRateRepositoryV1GetGet(rateId)

taxRates/{rateId}

Get tax rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxRatesRateIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxRatesRateIdApi apiInstance = new TaxRatesRateIdApi(defaultClient);
    Integer rateId = 56; // Integer | 
    try {
      TaxDataTaxRateInterface result = apiInstance.taxTaxRateRepositoryV1GetGet(rateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxRatesRateIdApi#taxTaxRateRepositoryV1GetGet");
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
| **rateId** | **Integer**|  | |

### Return type

[**TaxDataTaxRateInterface**](TaxDataTaxRateInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

