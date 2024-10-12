# LicensesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2LicensesIDGet**](LicensesApi.md#apiV2LicensesIDGet) | **GET** /api/v2/Licenses/{ID} | Get a license. |
| [**licensesGet**](LicensesApi.md#licensesGet) | **GET** /api/v2/Licenses | Gets a list of licenses with the specified criteria. |


<a id="apiV2LicensesIDGet"></a>
# **apiV2LicensesIDGet**
> DealerDBModelsLicense apiV2LicensesIDGet(ID)

Get a license.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String ID = "ID_example"; // String | The ID of the license to get.
    try {
      DealerDBModelsLicense result = apiInstance.apiV2LicensesIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#apiV2LicensesIDGet");
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
| **ID** | **String**| The ID of the license to get. | |

### Return type

[**DealerDBModelsLicense**](DealerDBModelsLicense.md)

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

<a id="licensesGet"></a>
# **licensesGet**
> APIPagedResponseDealerDBModelsLicense licensesGet(voucherCode, dealerCode, status, limit, offset)

Gets a list of licenses with the specified criteria.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    LicensesApi apiInstance = new LicensesApi(defaultClient);
    String voucherCode = "voucherCode_example"; // String | Optional. Filter by VoucherCode
    String dealerCode = "dealerCode_example"; // String | Optional. Filter by DealerCode
    String status = "Active"; // String | Optional. Filter by Status.  By default only active licenses will be returned.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseDealerDBModelsLicense result = apiInstance.licensesGet(voucherCode, dealerCode, status, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensesApi#licensesGet");
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
| **voucherCode** | **String**| Optional. Filter by VoucherCode | [optional] |
| **dealerCode** | **String**| Optional. Filter by DealerCode | [optional] |
| **status** | **String**| Optional. Filter by Status.  By default only active licenses will be returned. | [optional] [enum: Active, Inactive, All] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseDealerDBModelsLicense**](APIPagedResponseDealerDBModelsLicense.md)

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

