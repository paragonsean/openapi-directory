# AmazonShippingAddressAmazonOrderReferenceIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**amazonPaymentAddressManagementV1GetShippingAddressPut**](AmazonShippingAddressAmazonOrderReferenceIdApi.md#amazonPaymentAddressManagementV1GetShippingAddressPut) | **PUT** /V1/amazon-shipping-address/{amazonOrderReferenceId} | amazon-shipping-address/{amazonOrderReferenceId} |


<a id="amazonPaymentAddressManagementV1GetShippingAddressPut"></a>
# **amazonPaymentAddressManagementV1GetShippingAddressPut**
> String amazonPaymentAddressManagementV1GetShippingAddressPut(amazonOrderReferenceId, amazonPaymentAddressManagementV1GetBillingAddressPutRequest)

amazon-shipping-address/{amazonOrderReferenceId}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AmazonShippingAddressAmazonOrderReferenceIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    AmazonShippingAddressAmazonOrderReferenceIdApi apiInstance = new AmazonShippingAddressAmazonOrderReferenceIdApi(defaultClient);
    String amazonOrderReferenceId = "amazonOrderReferenceId_example"; // String | 
    AmazonPaymentAddressManagementV1GetBillingAddressPutRequest amazonPaymentAddressManagementV1GetBillingAddressPutRequest = new AmazonPaymentAddressManagementV1GetBillingAddressPutRequest(); // AmazonPaymentAddressManagementV1GetBillingAddressPutRequest | 
    try {
      String result = apiInstance.amazonPaymentAddressManagementV1GetShippingAddressPut(amazonOrderReferenceId, amazonPaymentAddressManagementV1GetBillingAddressPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AmazonShippingAddressAmazonOrderReferenceIdApi#amazonPaymentAddressManagementV1GetShippingAddressPut");
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

