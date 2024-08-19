# FundingApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFunding**](FundingApi.md#createFunding) | **POST** /send/v1/partners/{partnerId}/transfers/funding | The Funding Transaction enables the &#39;pull&#39; of money from the sender&#39;s card to the Transaction Originator who is providing the Person to Merchant service. The amount that is debited from the Funding Account (sending consumer&#39;s account) will be the amount &#39;pushed&#39; to the recipient via a payment transfer request.  Funds can be transferred from Mastercard® or Maestro® debit card accounts. To initiate the funding transaction, users can provide the sending consumer&#39;s Primary Account Number (PAN) or a unique identifier previously mapped to the sending consumer&#39;s account. |


<a id="createFunding"></a>
# **createFunding**
> Transfer129Wrapper createFunding(partnerId, fundingTransfer)

The Funding Transaction enables the &#39;pull&#39; of money from the sender&#39;s card to the Transaction Originator who is providing the Person to Merchant service. The amount that is debited from the Funding Account (sending consumer&#39;s account) will be the amount &#39;pushed&#39; to the recipient via a payment transfer request.  Funds can be transferred from Mastercard® or Maestro® debit card accounts. To initiate the funding transaction, users can provide the sending consumer&#39;s Primary Account Number (PAN) or a unique identifier previously mapped to the sending consumer&#39;s account.

The Funding Transaction enables the &#39;pull&#39; of money from the sender&#39;s card to the Transaction Originator who is providing the Person to Merchant service. The amount that is debited from the Funding Account (sending consumer&#39;s account) will be the amount &#39;pushed&#39; to the recipient via a payment transfer request.  Funds can be transferred from Mastercard® or Maestro® debit card accounts. To initiate the funding transaction, users can provide the sending consumer&#39;s Primary Account Number (PAN) or a unique identifier previously mapped to the sending consumer&#39;s account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FundingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    FundingApi apiInstance = new FundingApi(defaultClient);
    String partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Details - string, 32
    FundingTransfer118Wrapper fundingTransfer = new FundingTransfer118Wrapper(); // FundingTransfer118Wrapper | Contains the details of the request message.
    try {
      Transfer129Wrapper result = apiInstance.createFunding(partnerId, fundingTransfer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FundingApi#createFunding");
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
| **fundingTransfer** | [**FundingTransfer118Wrapper**](FundingTransfer118Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**Transfer129Wrapper**](Transfer129Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details |  -  |

