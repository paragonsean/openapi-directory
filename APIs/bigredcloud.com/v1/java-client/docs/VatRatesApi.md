# VatRatesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vatRatesGet**](VatRatesApi.md#vatRatesGet) | **GET** /v1/vatRates | Returns a list of company&#39;s Vat Rates. Supports OData querying protocol.  Filtering is allowed by \&quot;vatCategoryId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields. |


<a id="vatRatesGet"></a>
# **vatRatesGet**
> PageResultVatRateDto vatRatesGet()

Returns a list of company&#39;s Vat Rates. Supports OData querying protocol.  Filtering is allowed by \&quot;vatCategoryId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VatRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    VatRatesApi apiInstance = new VatRatesApi(defaultClient);
    try {
      PageResultVatRateDto result = apiInstance.vatRatesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VatRatesApi#vatRatesGet");
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

[**PageResultVatRateDto**](PageResultVatRateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

