# TaxClassesTaxClassIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxTaxClassRepositoryV1DeleteByIdDelete**](TaxClassesTaxClassIdApi.md#taxTaxClassRepositoryV1DeleteByIdDelete) | **DELETE** /V1/taxClasses/{taxClassId} | taxClasses/{taxClassId} |
| [**taxTaxClassRepositoryV1GetGet**](TaxClassesTaxClassIdApi.md#taxTaxClassRepositoryV1GetGet) | **GET** /V1/taxClasses/{taxClassId} | taxClasses/{taxClassId} |


<a id="taxTaxClassRepositoryV1DeleteByIdDelete"></a>
# **taxTaxClassRepositoryV1DeleteByIdDelete**
> Boolean taxTaxClassRepositoryV1DeleteByIdDelete(taxClassId)

taxClasses/{taxClassId}

Delete a tax class with the given tax class id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxClassesTaxClassIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxClassesTaxClassIdApi apiInstance = new TaxClassesTaxClassIdApi(defaultClient);
    Integer taxClassId = 56; // Integer | 
    try {
      Boolean result = apiInstance.taxTaxClassRepositoryV1DeleteByIdDelete(taxClassId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxClassesTaxClassIdApi#taxTaxClassRepositoryV1DeleteByIdDelete");
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
| **taxClassId** | **Integer**|  | |

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
| **0** | Unexpected error |  -  |

<a id="taxTaxClassRepositoryV1GetGet"></a>
# **taxTaxClassRepositoryV1GetGet**
> TaxDataTaxClassInterface taxTaxClassRepositoryV1GetGet(taxClassId)

taxClasses/{taxClassId}

Get a tax class with the given tax class id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxClassesTaxClassIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TaxClassesTaxClassIdApi apiInstance = new TaxClassesTaxClassIdApi(defaultClient);
    Integer taxClassId = 56; // Integer | 
    try {
      TaxDataTaxClassInterface result = apiInstance.taxTaxClassRepositoryV1GetGet(taxClassId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxClassesTaxClassIdApi#taxTaxClassRepositoryV1GetGet");
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
| **taxClassId** | **Integer**|  | |

### Return type

[**TaxDataTaxClassInterface**](TaxDataTaxClassInterface.md)

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

