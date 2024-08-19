# AccountHolderMessagingApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountholdermessagingPost**](AccountHolderMessagingApi.md#accountholdermessagingPost) | **POST** /accountholdermessaging |  |


<a id="accountholdermessagingPost"></a>
# **accountholdermessagingPost**
> AccountHolderMessagingResponseSchema accountholdermessagingPost(accountholderMessagingRequestSchema)



Allows issuers to display customized messages per token within the Apple Pay wallet, below the digitized image of the card. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountHolderMessagingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    AccountHolderMessagingApi apiInstance = new AccountHolderMessagingApi(defaultClient);
    AccountHolderMessagingRequest accountholderMessagingRequestSchema = new AccountHolderMessagingRequest(); // AccountHolderMessagingRequest | Contains the details of the request message.
    try {
      AccountHolderMessagingResponseSchema result = apiInstance.accountholdermessagingPost(accountholderMessagingRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountHolderMessagingApi#accountholdermessagingPost");
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
| **accountholderMessagingRequestSchema** | [**AccountHolderMessagingRequest**](AccountHolderMessagingRequest.md)| Contains the details of the request message. | [optional] |

### Return type

[**AccountHolderMessagingResponseSchema**](AccountHolderMessagingResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains the details of the response |  -  |
| **0** | unexpected error |  -  |

