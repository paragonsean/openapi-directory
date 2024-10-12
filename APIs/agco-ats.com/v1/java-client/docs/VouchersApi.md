# VouchersApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2VouchersVoucherCodeGet**](VouchersApi.md#apiV2VouchersVoucherCodeGet) | **GET** /api/v2/Vouchers/{VoucherCode} | Get a voucher |
| [**vouchersDelete**](VouchersApi.md#vouchersDelete) | **DELETE** /api/v2/Vouchers/{VoucherCode} | Delete a voucher |
| [**vouchersGet**](VouchersApi.md#vouchersGet) | **GET** /api/v2/Vouchers | Gets a list of vouchers |
| [**vouchersGetVoucherHistory**](VouchersApi.md#vouchersGetVoucherHistory) | **GET** /api/v2/Vouchers/{VoucherCode}/VoucherHistory | Get a voucher&#39;s history. |
| [**vouchersPost**](VouchersApi.md#vouchersPost) | **POST** /api/v2/Vouchers | Create a voucher |
| [**vouchersPut**](VouchersApi.md#vouchersPut) | **PUT** /api/v2/Vouchers/{VoucherCode} | Update a voucher |


<a id="apiV2VouchersVoucherCodeGet"></a>
# **apiV2VouchersVoucherCodeGet**
> DealerDBModelsVoucher apiV2VouchersVoucherCodeGet(voucherCode, deleted)

Get a voucher

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VouchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    VouchersApi apiInstance = new VouchersApi(defaultClient);
    String voucherCode = "voucherCode_example"; // String | The voucher code of the voucher to get.
    String deleted = "NotDeleted"; // String | Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.
    try {
      DealerDBModelsVoucher result = apiInstance.apiV2VouchersVoucherCodeGet(voucherCode, deleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VouchersApi#apiV2VouchersVoucherCodeGet");
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
| **voucherCode** | **String**| The voucher code of the voucher to get. | |
| **deleted** | **String**| Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned. | [optional] [enum: NotDeleted, Deleted, All] |

### Return type

[**DealerDBModelsVoucher**](DealerDBModelsVoucher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vouchersDelete"></a>
# **vouchersDelete**
> vouchersDelete(voucherCode)

Delete a voucher

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VouchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    VouchersApi apiInstance = new VouchersApi(defaultClient);
    String voucherCode = "voucherCode_example"; // String | The voucher code of the voucher to delete.
    try {
      apiInstance.vouchersDelete(voucherCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling VouchersApi#vouchersDelete");
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
| **voucherCode** | **String**| The voucher code of the voucher to delete. | |

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
| **204** | No Content |  -  |

<a id="vouchersGet"></a>
# **vouchersGet**
> APIPagedResponseDealerDBModelsVoucher vouchersGet(type, dealerCode, licenseTo, purpose, orderNumber, email, modifiedBy, createdAfter, createdBefore, punchedAfter, punchedBefore, punched, expirationAfter, expirationBefore, deleted, limit, offset)

Gets a list of vouchers

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VouchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    VouchersApi apiInstance = new VouchersApi(defaultClient);
    String type = "Commercial"; // String | Optional. Filter vouchers by Type
    String dealerCode = "dealerCode_example"; // String | Optional. Filter vouchers by DealerCode
    String licenseTo = "licenseTo_example"; // String | Optional. Filter vouchers by LicenseTo. Wildcard supported (*).
    String purpose = "purpose_example"; // String | Optional. Filter vouchers by Purpose. Wildcard supported (*).
    String orderNumber = "orderNumber_example"; // String | Optional. Filter vouchers by OrderNumber
    String email = "email_example"; // String | Optional. Filter vouchers by Email. Wildcard supported (*).
    String modifiedBy = "modifiedBy_example"; // String | Optional. Filter vouchers by ModifiedBy
    OffsetDateTime createdAfter = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter vouchers by CreatedDate
    OffsetDateTime createdBefore = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter vouchers by CreatedDate
    OffsetDateTime punchedAfter = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter vouchers by PunchedDate
    OffsetDateTime punchedBefore = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter vouchers by PunchedDate
    Boolean punched = true; // Boolean | Optional. Filter vouchers by Punched status
    OffsetDateTime expirationAfter = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter vouchers by ExpirationDate
    OffsetDateTime expirationBefore = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter vouchers by ExpirationDate
    String deleted = "NotDeleted"; // String | Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseDealerDBModelsVoucher result = apiInstance.vouchersGet(type, dealerCode, licenseTo, purpose, orderNumber, email, modifiedBy, createdAfter, createdBefore, punchedAfter, punchedBefore, punched, expirationAfter, expirationBefore, deleted, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VouchersApi#vouchersGet");
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
| **type** | **String**| Optional. Filter vouchers by Type | [optional] [enum: Commercial, Internal, Temporary, RightToRepair] |
| **dealerCode** | **String**| Optional. Filter vouchers by DealerCode | [optional] |
| **licenseTo** | **String**| Optional. Filter vouchers by LicenseTo. Wildcard supported (*). | [optional] |
| **purpose** | **String**| Optional. Filter vouchers by Purpose. Wildcard supported (*). | [optional] |
| **orderNumber** | **String**| Optional. Filter vouchers by OrderNumber | [optional] |
| **email** | **String**| Optional. Filter vouchers by Email. Wildcard supported (*). | [optional] |
| **modifiedBy** | **String**| Optional. Filter vouchers by ModifiedBy | [optional] |
| **createdAfter** | **OffsetDateTime**| Optional. Filter vouchers by CreatedDate | [optional] |
| **createdBefore** | **OffsetDateTime**| Optional. Filter vouchers by CreatedDate | [optional] |
| **punchedAfter** | **OffsetDateTime**| Optional. Filter vouchers by PunchedDate | [optional] |
| **punchedBefore** | **OffsetDateTime**| Optional. Filter vouchers by PunchedDate | [optional] |
| **punched** | **Boolean**| Optional. Filter vouchers by Punched status | [optional] |
| **expirationAfter** | **OffsetDateTime**| Optional. Filter vouchers by ExpirationDate | [optional] |
| **expirationBefore** | **OffsetDateTime**| Optional. Filter vouchers by ExpirationDate | [optional] |
| **deleted** | **String**| Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned. | [optional] [enum: NotDeleted, Deleted, All] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseDealerDBModelsVoucher**](APIPagedResponseDealerDBModelsVoucher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vouchersGetVoucherHistory"></a>
# **vouchersGetVoucherHistory**
> APIPagedResponseDealerDBModelsVoucherHistory vouchersGetVoucherHistory(voucherCode, limit, offset)

Get a voucher&#39;s history.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VouchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    VouchersApi apiInstance = new VouchersApi(defaultClient);
    String voucherCode = "voucherCode_example"; // String | The voucher code to get history for.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseDealerDBModelsVoucherHistory result = apiInstance.vouchersGetVoucherHistory(voucherCode, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VouchersApi#vouchersGetVoucherHistory");
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
| **voucherCode** | **String**| The voucher code to get history for. | |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseDealerDBModelsVoucherHistory**](APIPagedResponseDealerDBModelsVoucherHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vouchersPost"></a>
# **vouchersPost**
> String vouchersPost(dealerDBModelsVoucher)

Create a voucher

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VouchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    VouchersApi apiInstance = new VouchersApi(defaultClient);
    DealerDBModelsVoucher dealerDBModelsVoucher = new DealerDBModelsVoucher(); // DealerDBModelsVoucher | The voucher to add.
    try {
      String result = apiInstance.vouchersPost(dealerDBModelsVoucher);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VouchersApi#vouchersPost");
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
| **dealerDBModelsVoucher** | [**DealerDBModelsVoucher**](DealerDBModelsVoucher.md)| The voucher to add. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vouchersPut"></a>
# **vouchersPut**
> vouchersPut(voucherCode, dealerDBModelsVoucher)

Update a voucher

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VouchersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    VouchersApi apiInstance = new VouchersApi(defaultClient);
    String voucherCode = "voucherCode_example"; // String | The voucher code of the voucher to update.
    DealerDBModelsVoucher dealerDBModelsVoucher = new DealerDBModelsVoucher(); // DealerDBModelsVoucher | The updated voucher.
    try {
      apiInstance.vouchersPut(voucherCode, dealerDBModelsVoucher);
    } catch (ApiException e) {
      System.err.println("Exception when calling VouchersApi#vouchersPut");
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
| **voucherCode** | **String**| The voucher code of the voucher to update. | |
| **dealerDBModelsVoucher** | [**DealerDBModelsVoucher**](DealerDBModelsVoucher.md)| The updated voucher. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

