# AmazonBillingAddressAmazonOrderReferenceIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**amazonPaymentAddressManagementV1GetBillingAddressPut**](AmazonBillingAddressAmazonOrderReferenceIdApi.md#amazonPaymentAddressManagementV1GetBillingAddressPut) | **PUT** /V1/amazon-billing-address/{amazonOrderReferenceId} | amazon-billing-address/{amazonOrderReferenceId} |


<a id="amazonPaymentAddressManagementV1GetBillingAddressPut"></a>
# **amazonPaymentAddressManagementV1GetBillingAddressPut**
> String amazonPaymentAddressManagementV1GetBillingAddressPut(amazonOrderReferenceId, amazonPaymentAddressManagementV1GetBillingAddressPutRequest)

amazon-billing-address/{amazonOrderReferenceId}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AmazonBillingAddressAmazonOrderReferenceIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    AmazonBillingAddressAmazonOrderReferenceIdApi apiInstance = new AmazonBillingAddressAmazonOrderReferenceIdApi(defaultClient);
    String amazonOrderReferenceId = "amazonOrderReferenceId_example"; // String | 
    AmazonPaymentAddressManagementV1GetBillingAddressPutRequest amazonPaymentAddressManagementV1GetBillingAddressPutRequest = new AmazonPaymentAddressManagementV1GetBillingAddressPutRequest(); // AmazonPaymentAddressManagementV1GetBillingAddressPutRequest | 
    try {
      String result = apiInstance.amazonPaymentAddressManagementV1GetBillingAddressPut(amazonOrderReferenceId, amazonPaymentAddressManagementV1GetBillingAddressPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AmazonBillingAddressAmazonOrderReferenceIdApi#amazonPaymentAddressManagementV1GetBillingAddressPut");
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
| **amazonOrderReferenceId** | **String**|  | |
| **amazonPaymentAddressManagementV1GetBillingAddressPutRequest** | [**AmazonPaymentAddressManagementV1GetBillingAddressPutRequest**](AmazonPaymentAddressManagementV1GetBillingAddressPutRequest.md)|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **0** | Unexpected error |  -  |

