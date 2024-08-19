# ConversionRateApi

All URIs are relative to *http://api.mastercard.com/mcapi/settlement/currencyrate*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConversionDetailUsingGET**](ConversionRateApi.md#getConversionDetailUsingGET) | **GET** /conversion-rate | Get the currency conversion rate details. |


<a id="getConversionDetailUsingGET"></a>
# **getConversionDetailUsingGET**
> ConversionRateRequest getConversionDetailUsingGET(fxDate, transCurr, crdhldBillCurr, transAmt, bankFee)

Get the currency conversion rate details.

Get the currency conversion rate details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversionRateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.mastercard.com/mcapi/settlement/currencyrate");

    ConversionRateApi apiInstance = new ConversionRateApi(defaultClient);
    String fxDate = "fxDate_example"; // String | Date of the requested FX rates.
    String transCurr = "transCurr_example"; // String | Currency of the transaction.
    String crdhldBillCurr = "crdhldBillCurr_example"; // String | Cardholder billing currency.
    Double transAmt = 3.4D; // Double | Amount in the transaction currency.
    Double bankFee = 3.4D; // Double | Additional fees imposed by the bank.
    try {
      ConversionRateRequest result = apiInstance.getConversionDetailUsingGET(fxDate, transCurr, crdhldBillCurr, transAmt, bankFee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversionRateApi#getConversionDetailUsingGET");
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
| **fxDate** | **String**| Date of the requested FX rates. | |
| **transCurr** | **String**| Currency of the transaction. | |
| **crdhldBillCurr** | **String**| Cardholder billing currency. | |
| **transAmt** | **Double**| Amount in the transaction currency. | |
| **bankFee** | **Double**| Additional fees imposed by the bank. | [optional] |

### Return type

[**ConversionRateRequest**](ConversionRateRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

