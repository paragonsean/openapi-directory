# RateIssuedApi

All URIs are relative to *http://api.mastercard.com/mcapi/settlement/currencyrate*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**isRateIssuedUsingGET**](RateIssuedApi.md#isRateIssuedUsingGET) | **GET** /conversion-rate-issued | Determine if the settlement rate has been issued. |


<a id="isRateIssuedUsingGET"></a>
# **isRateIssuedUsingGET**
> SettlementRateIssuedRequest isRateIssuedUsingGET(date)

Determine if the settlement rate has been issued.

Determine if the settlement rate has been issued.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RateIssuedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.mastercard.com/mcapi/settlement/currencyrate");

    RateIssuedApi apiInstance = new RateIssuedApi(defaultClient);
    String date = "date_example"; // String | The date by which the rate would have been issued.
    try {
      SettlementRateIssuedRequest result = apiInstance.isRateIssuedUsingGET(date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RateIssuedApi#isRateIssuedUsingGET");
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
| **date** | **String**| The date by which the rate would have been issued. | [optional] |

### Return type

[**SettlementRateIssuedRequest**](SettlementRateIssuedRequest.md)

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

