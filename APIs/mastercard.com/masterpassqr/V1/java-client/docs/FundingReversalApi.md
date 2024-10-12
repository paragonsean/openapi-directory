# FundingReversalApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFundingReversal**](FundingReversalApi.md#createFundingReversal) | **POST** /send/v1/partners/{partner-id}/transfers/{transfer-id}/transactions/{transaction-id}/reversals | Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account. |


<a id="createFundingReversal"></a>
# **createFundingReversal**
> Transfer145Wrapper createFundingReversal(partnerId, transferId, transactionId, fundingReversal)

Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account.

Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingReversalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    FundingReversalApi apiInstance = new FundingReversalApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
    String transferId = "transferId_example"; // String | Valid transfer id
    String transactionId = "transactionId_example"; // String | Valid transaction id
    FundingReversal144Wrapper fundingReversal = new FundingReversal144Wrapper(); // FundingReversal144Wrapper | Contains the details of the request message.
    try {
      Transfer145Wrapper result = apiInstance.createFundingReversal(partnerId, transferId, transactionId, fundingReversal);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingReversalApi#createFundingReversal");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | |
| **transferId** | **String**| Valid transfer id | |
| **transactionId** | **String**| Valid transaction id | |
| **fundingReversal** | [**FundingReversal144Wrapper**](FundingReversal144Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**Transfer145Wrapper**](Transfer145Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details |  -  |

