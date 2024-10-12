# AddTerminatedMerchantApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fraudMerchantV3AddMerchantPost**](AddTerminatedMerchantApi.md#fraudMerchantV3AddMerchantPost) | **POST** /fraud/merchant/v3/add-merchant | Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing. |


<a id="fraudMerchantV3AddMerchantPost"></a>
# **fraudMerchantV3AddMerchantPost**
> AddTerminatedMerchantResponseSchema fraudMerchantV3AddMerchantPost(addTerminatedMerchantRequestSchema)

Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing.

Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddTerminatedMerchantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    AddTerminatedMerchantApi apiInstance = new AddTerminatedMerchantApi(defaultClient);
    AddTerminatedMerchantRequestSchema addTerminatedMerchantRequestSchema = new AddTerminatedMerchantRequestSchema(); // AddTerminatedMerchantRequestSchema | Body of the Add Terminated Merchant Request
    try {
      AddTerminatedMerchantResponseSchema result = apiInstance.fraudMerchantV3AddMerchantPost(addTerminatedMerchantRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddTerminatedMerchantApi#fraudMerchantV3AddMerchantPost");
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
| **addTerminatedMerchantRequestSchema** | [**AddTerminatedMerchantRequestSchema**](AddTerminatedMerchantRequestSchema.md)| Body of the Add Terminated Merchant Request | |

### Return type

[**AddTerminatedMerchantResponseSchema**](AddTerminatedMerchantResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The add terminated merchant response object. |  -  |
| **0** | Unexpected error |  -  |

