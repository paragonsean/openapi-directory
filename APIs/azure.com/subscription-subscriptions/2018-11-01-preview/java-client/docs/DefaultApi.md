# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionFactoryCreateCspSubscription**](DefaultApi.md#subscriptionFactoryCreateCspSubscription) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/providers/Microsoft.Subscription/createSubscription |  |
| [**subscriptionFactoryCreateSubscription**](DefaultApi.md#subscriptionFactoryCreateSubscription) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Subscription/createSubscription |  |
| [**subscriptionOperationGet**](DefaultApi.md#subscriptionOperationGet) | **GET** /providers/Microsoft.Subscription/subscriptionOperations/{operationId} |  |


<a id="subscriptionFactoryCreateCspSubscription"></a>
# **subscriptionFactoryCreateCspSubscription**
> SubscriptionCreationResult subscriptionFactoryCreateCspSubscription(billingAccountName, customerName, apiVersion, body)



The operation to create a new CSP subscription.

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
    String billingAccountName = "billingAccountName_example"; // String | The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.
    String customerName = "customerName_example"; // String | The name of the customer.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2018-11-01-preview
    ModernCspSubscriptionCreationParameters body = new ModernCspSubscriptionCreationParameters(); // ModernCspSubscriptionCreationParameters | The subscription creation parameters.
    try {
      SubscriptionCreationResult result = apiInstance.subscriptionFactoryCreateCspSubscription(billingAccountName, customerName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionFactoryCreateCspSubscription");
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
| **billingAccountName** | **String**| The name of the Microsoft Customer Agreement billing account for which you want to create the subscription. | |
| **customerName** | **String**| The name of the customer. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2018-11-01-preview | |
| **body** | [**ModernCspSubscriptionCreationParameters**](ModernCspSubscriptionCreationParameters.md)| The subscription creation parameters. | |

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normal response for a successful query. The response body will contain the data that matches the filters specified in the query parameters. |  -  |
| **202** | Accepted. Subscription creation is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - The URL where the status of the asynchronous operation can be checked. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionFactoryCreateSubscription"></a>
# **subscriptionFactoryCreateSubscription**
> SubscriptionCreationResult subscriptionFactoryCreateSubscription(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, body)



The operation to create a new WebDirect or EA Azure subscription.

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
    String billingAccountName = "billingAccountName_example"; // String | The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.
    String billingProfileName = "billingProfileName_example"; // String | The name of the billing profile in the billing account for which you want to create the subscription.
    String invoiceSectionName = "invoiceSectionName_example"; // String | The name of the invoice section in the billing account for which you want to create the subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2018-11-01-preview
    ModernSubscriptionCreationParameters body = new ModernSubscriptionCreationParameters(); // ModernSubscriptionCreationParameters | The subscription creation parameters.
    try {
      SubscriptionCreationResult result = apiInstance.subscriptionFactoryCreateSubscription(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionFactoryCreateSubscription");
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
| **billingAccountName** | **String**| The name of the Microsoft Customer Agreement billing account for which you want to create the subscription. | |
| **billingProfileName** | **String**| The name of the billing profile in the billing account for which you want to create the subscription. | |
| **invoiceSectionName** | **String**| The name of the invoice section in the billing account for which you want to create the subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2018-11-01-preview | |
| **body** | [**ModernSubscriptionCreationParameters**](ModernSubscriptionCreationParameters.md)| The subscription creation parameters. | |

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normal response for a successful query. The response body will contain the data that matches the filters specified in the query parameters. |  -  |
| **202** | Accepted. Subscription creation is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - The URL where the status of the asynchronous operation can be checked. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionOperationGet"></a>
# **subscriptionOperationGet**
> SubscriptionCreationResult subscriptionOperationGet(operationId, apiVersion)



Get the status of the pending Microsoft.Subscription API operations.

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
    String operationId = "operationId_example"; // String | The operation ID, which can be found from the Location field in the generate recommendation response header.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2018-11-01-preview
    try {
      SubscriptionCreationResult result = apiInstance.subscriptionOperationGet(operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionOperationGet");
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
| **operationId** | **String**| The operation ID, which can be found from the Location field in the generate recommendation response header. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2018-11-01-preview | |

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful completion of the asynchronous operation |  -  |
| **202** | Accepted. Subscription update is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - The URL where the status of the asynchronous operation can be checked. <br>  |

