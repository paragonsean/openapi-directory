# AcquirerContactRequestApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fraudMerchantV3CommonContactDetailsPost**](AcquirerContactRequestApi.md#fraudMerchantV3CommonContactDetailsPost) | **POST** /fraud/merchant/v3/common/contact-details | Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH. |


<a id="fraudMerchantV3CommonContactDetailsPost"></a>
# **fraudMerchantV3CommonContactDetailsPost**
> ContactResponseSchema fraudMerchantV3CommonContactDetailsPost(contactRequest)

Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH.

Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AcquirerContactRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    AcquirerContactRequestApi apiInstance = new AcquirerContactRequestApi(defaultClient);
    ContactRequestSchema contactRequest = new ContactRequestSchema(); // ContactRequestSchema | The contact request object
    try {
      ContactResponseSchema result = apiInstance.fraudMerchantV3CommonContactDetailsPost(contactRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AcquirerContactRequestApi#fraudMerchantV3CommonContactDetailsPost");
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
| **contactRequest** | [**ContactRequestSchema**](ContactRequestSchema.md)| The contact request object | |

### Return type

[**ContactResponseSchema**](ContactResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The acquirer contact response object. |  -  |
| **400** | Bad request |  -  |
| **0** | Unexpected error |  -  |

