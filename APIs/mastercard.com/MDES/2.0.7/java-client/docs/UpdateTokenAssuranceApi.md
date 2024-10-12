# UpdateTokenAssuranceApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updatetokenassurancePost**](UpdateTokenAssuranceApi.md#updatetokenassurancePost) | **POST** /updatetokenassurance |  |


<a id="updatetokenassurancePost"></a>
# **updatetokenassurancePost**
> UpdateTokenAssuranceResponseSchema updatetokenassurancePost(updateTokenAssuranceRequestSchema)



Used after an issuer has performed additional cardholder authentication to indicate an increased level of token assurance. It will only be applied to tokens that actually have a Token Assurance Level, and those that are in ACTIVE or SUSPENDED state. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateTokenAssuranceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    UpdateTokenAssuranceApi apiInstance = new UpdateTokenAssuranceApi(defaultClient);
    UpdateTokenAssuranceRequestSchema updateTokenAssuranceRequestSchema = new UpdateTokenAssuranceRequestSchema(); // UpdateTokenAssuranceRequestSchema | Contains the details of the request message.
    try {
      UpdateTokenAssuranceResponseSchema result = apiInstance.updatetokenassurancePost(updateTokenAssuranceRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateTokenAssuranceApi#updatetokenassurancePost");
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
| **updateTokenAssuranceRequestSchema** | [**UpdateTokenAssuranceRequestSchema**](UpdateTokenAssuranceRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**UpdateTokenAssuranceResponseSchema**](UpdateTokenAssuranceResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains the details of the response message. |  -  |
| **0** | unexpected error |  -  |

