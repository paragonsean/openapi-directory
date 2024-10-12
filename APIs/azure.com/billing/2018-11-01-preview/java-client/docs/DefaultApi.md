# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingSubscriptionsTransfer**](DefaultApi.md#billingSubscriptionsTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/billingSubscriptions/{billingSubscriptionName}/transfer |  |
| [**billingSubscriptionsValidateTransfer**](DefaultApi.md#billingSubscriptionsValidateTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/billingSubscriptions/{billingSubscriptionName}/validateTransferEligibility |  |
| [**productsValidateTransfer**](DefaultApi.md#productsValidateTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products/{productName}/validateTransferEligibility |  |


<a id="billingSubscriptionsTransfer"></a>
# **billingSubscriptionsTransfer**
> TransferBillingSubscriptionResult billingSubscriptionsTransfer(billingAccountName, invoiceSectionName, billingSubscriptionName, parameters)



Transfers the subscription from one invoice section to another within a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
    TransferBillingSubscriptionRequestProperties parameters = new TransferBillingSubscriptionRequestProperties(); // TransferBillingSubscriptionRequestProperties | Parameters supplied to the Transfer Billing Subscription operation.
    try {
      TransferBillingSubscriptionResult result = apiInstance.billingSubscriptionsTransfer(billingAccountName, invoiceSectionName, billingSubscriptionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#billingSubscriptionsTransfer");
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
| **billingAccountName** | **String**| Billing Account Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **billingSubscriptionName** | **String**| Billing Subscription Id. | |
| **parameters** | [**TransferBillingSubscriptionRequestProperties**](TransferBillingSubscriptionRequestProperties.md)| Parameters supplied to the Transfer Billing Subscription operation. | |

### Return type

[**TransferBillingSubscriptionResult**](TransferBillingSubscriptionResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. Billing Subscription transfer is in progress. |  * Retry-After - Recommends the retryable time after receiving this. <br>  * Azure-AsyncOperation - URI to poll for the operation status <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Unexpected error. |  -  |

<a id="billingSubscriptionsValidateTransfer"></a>
# **billingSubscriptionsValidateTransfer**
> ValidateSubscriptionTransferEligibilityResult billingSubscriptionsValidateTransfer(billingAccountName, invoiceSectionName, billingSubscriptionName, parameters)



Validates the transfer of billing subscriptions across invoice sections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
    TransferBillingSubscriptionRequestProperties parameters = new TransferBillingSubscriptionRequestProperties(); // TransferBillingSubscriptionRequestProperties | Parameters supplied to the Transfer Billing Subscription operation.
    try {
      ValidateSubscriptionTransferEligibilityResult result = apiInstance.billingSubscriptionsValidateTransfer(billingAccountName, invoiceSectionName, billingSubscriptionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#billingSubscriptionsValidateTransfer");
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
| **billingAccountName** | **String**| Billing Account Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **billingSubscriptionName** | **String**| Billing Subscription Id. | |
| **parameters** | [**TransferBillingSubscriptionRequestProperties**](TransferBillingSubscriptionRequestProperties.md)| Parameters supplied to the Transfer Billing Subscription operation. | |

### Return type

[**ValidateSubscriptionTransferEligibilityResult**](ValidateSubscriptionTransferEligibilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productsValidateTransfer"></a>
# **productsValidateTransfer**
> ValidateProductTransferEligibilityResult productsValidateTransfer(billingAccountName, invoiceSectionName, productName, parameters)



Validates the transfer of products across invoice sections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String productName = "productName_example"; // String | Invoice Id.
    TransferProductRequestProperties parameters = new TransferProductRequestProperties(); // TransferProductRequestProperties | Parameters supplied to the Transfer Products operation.
    try {
      ValidateProductTransferEligibilityResult result = apiInstance.productsValidateTransfer(billingAccountName, invoiceSectionName, productName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#productsValidateTransfer");
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
| **billingAccountName** | **String**| Billing Account Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **productName** | **String**| Invoice Id. | |
| **parameters** | [**TransferProductRequestProperties**](TransferProductRequestProperties.md)| Parameters supplied to the Transfer Products operation. | |

### Return type

[**ValidateProductTransferEligibilityResult**](ValidateProductTransferEligibilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

