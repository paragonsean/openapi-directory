# GetPaymentAccountReferenceApi

All URIs are relative to *https://sandbox.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**parPaymentaccountreference10GetPaymentAccountReferencePost**](GetPaymentAccountReferenceApi.md#parPaymentaccountreference10GetPaymentAccountReferencePost) | **POST** /par/paymentaccountreference/1/0/getPaymentAccountReference | Submit an encrypted PAN to obtain the PAR linked to the account. |


<a id="parPaymentaccountreference10GetPaymentAccountReferencePost"></a>
# **parPaymentaccountreference10GetPaymentAccountReferencePost**
> GetPaymentAccountReferenceResponseSchema parPaymentaccountreference10GetPaymentAccountReferencePost(getPaymentAccountReferenceRequestSchema)

Submit an encrypted PAN to obtain the PAR linked to the account.

The API performs a PAR query into the PAR Vault with the supplied PAN. When a PAR is returned from the PAR vault the API will encrypt it using the wrapped encryption method with the  Mastercard Customer?s Encryption Public Key and include it in the API response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetPaymentAccountReferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.mastercard.com");

    GetPaymentAccountReferenceApi apiInstance = new GetPaymentAccountReferenceApi(defaultClient);
    GetPaymentAccountReferenceRequestSchema getPaymentAccountReferenceRequestSchema = new GetPaymentAccountReferenceRequestSchema(); // GetPaymentAccountReferenceRequestSchema | Contains the details of the get PAR API request message.
    try {
      GetPaymentAccountReferenceResponseSchema result = apiInstance.parPaymentaccountreference10GetPaymentAccountReferencePost(getPaymentAccountReferenceRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetPaymentAccountReferenceApi#parPaymentaccountreference10GetPaymentAccountReferencePost");
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
| **getPaymentAccountReferenceRequestSchema** | [**GetPaymentAccountReferenceRequestSchema**](GetPaymentAccountReferenceRequestSchema.md)| Contains the details of the get PAR API request message. | [optional] |

### Return type

[**GetPaymentAccountReferenceResponseSchema**](GetPaymentAccountReferenceResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains the details of the get PAR API response message. |  -  |

