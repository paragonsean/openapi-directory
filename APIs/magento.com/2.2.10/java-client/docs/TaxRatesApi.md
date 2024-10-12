# TaxRatesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxTaxRateRepositoryV1SavePost**](TaxRatesApi.md#taxTaxRateRepositoryV1SavePost) | **POST** /V1/taxRates | taxRates |
| [**taxTaxRateRepositoryV1SavePut**](TaxRatesApi.md#taxTaxRateRepositoryV1SavePut) | **PUT** /V1/taxRates | taxRates |


<a id="taxTaxRateRepositoryV1SavePost"></a>
# **taxTaxRateRepositoryV1SavePost**
> TaxDataTaxRateInterface taxTaxRateRepositoryV1SavePost(taxTaxRateRepositoryV1SavePutRequest)

taxRates

Create or update tax rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxRatesApi apiInstance = new TaxRatesApi(defaultClient);
    TaxTaxRateRepositoryV1SavePutRequest taxTaxRateRepositoryV1SavePutRequest = new TaxTaxRateRepositoryV1SavePutRequest(); // TaxTaxRateRepositoryV1SavePutRequest | 
    try {
      TaxDataTaxRateInterface result = apiInstance.taxTaxRateRepositoryV1SavePost(taxTaxRateRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxRatesApi#taxTaxRateRepositoryV1SavePost");
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
| **taxTaxRateRepositoryV1SavePutRequest** | [**TaxTaxRateRepositoryV1SavePutRequest**](TaxTaxRateRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**TaxDataTaxRateInterface**](TaxDataTaxRateInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="taxTaxRateRepositoryV1SavePut"></a>
# **taxTaxRateRepositoryV1SavePut**
> TaxDataTaxRateInterface taxTaxRateRepositoryV1SavePut(taxTaxRateRepositoryV1SavePutRequest)

taxRates

Create or update tax rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxRatesApi apiInstance = new TaxRatesApi(defaultClient);
    TaxTaxRateRepositoryV1SavePutRequest taxTaxRateRepositoryV1SavePutRequest = new TaxTaxRateRepositoryV1SavePutRequest(); // TaxTaxRateRepositoryV1SavePutRequest | 
    try {
      TaxDataTaxRateInterface result = apiInstance.taxTaxRateRepositoryV1SavePut(taxTaxRateRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxRatesApi#taxTaxRateRepositoryV1SavePut");
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
| **taxTaxRateRepositoryV1SavePutRequest** | [**TaxTaxRateRepositoryV1SavePutRequest**](TaxTaxRateRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**TaxDataTaxRateInterface**](TaxDataTaxRateInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

