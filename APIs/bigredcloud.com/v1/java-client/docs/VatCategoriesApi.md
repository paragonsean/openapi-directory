# VatCategoriesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vatCategoriesGet**](VatCategoriesApi.md#vatCategoriesGet) | **GET** /v1/vatCategories | Returns a list of global Vat Categories. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field. |
| [**vatCategoriesProcessVatRates**](VatCategoriesApi.md#vatCategoriesProcessVatRates) | **POST** /v1/vatCategories/vatRates | Process Vat Rates |


<a id="vatCategoriesGet"></a>
# **vatCategoriesGet**
> PageResultVatCategoryDto vatCategoriesGet()

Returns a list of global Vat Categories. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VatCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    VatCategoriesApi apiInstance = new VatCategoriesApi(defaultClient);
    try {
      PageResultVatCategoryDto result = apiInstance.vatCategoriesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VatCategoriesApi#vatCategoriesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PageResultVatCategoryDto**](PageResultVatCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vatCategoriesProcessVatRates"></a>
# **vatCategoriesProcessVatRates**
> Object vatCategoriesProcessVatRates(vatRatesByVatCategoryDto)

Process Vat Rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VatCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    VatCategoriesApi apiInstance = new VatCategoriesApi(defaultClient);
    List<VatRatesByVatCategoryDto> vatRatesByVatCategoryDto = Arrays.asList(); // List<VatRatesByVatCategoryDto> | Array of Vat Rates.
    try {
      Object result = apiInstance.vatCategoriesProcessVatRates(vatRatesByVatCategoryDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VatCategoriesApi#vatCategoriesProcessVatRates");
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
| **vatRatesByVatCategoryDto** | [**List&lt;VatRatesByVatCategoryDto&gt;**](VatRatesByVatCategoryDto.md)| Array of Vat Rates. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

