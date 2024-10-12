# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionFactoryCreateSubscriptionInEnrollmentAccount**](DefaultApi.md#subscriptionFactoryCreateSubscriptionInEnrollmentAccount) | **POST** /providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountName}/providers/Microsoft.Subscription/createSubscription |  |
| [**subscriptionOperationsList**](DefaultApi.md#subscriptionOperationsList) | **GET** /providers/Microsoft.Subscription/subscriptionOperations |  |


<a id="subscriptionFactoryCreateSubscriptionInEnrollmentAccount"></a>
# **subscriptionFactoryCreateSubscriptionInEnrollmentAccount**
> SubscriptionCreationResult subscriptionFactoryCreateSubscriptionInEnrollmentAccount(enrollmentAccountName, apiVersion, body)



Creates an Azure subscription

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
    String enrollmentAccountName = "enrollmentAccountName_example"; // String | The name of the enrollment account to which the subscription will be billed.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    SubscriptionCreationParameters body = new SubscriptionCreationParameters(); // SubscriptionCreationParameters | The subscription creation parameters.
    try {
      SubscriptionCreationResult result = apiInstance.subscriptionFactoryCreateSubscriptionInEnrollmentAccount(enrollmentAccountName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionFactoryCreateSubscriptionInEnrollmentAccount");
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
| **enrollmentAccountName** | **String**| The name of the enrollment account to which the subscription will be billed. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **body** | [**SubscriptionCreationParameters**](SubscriptionCreationParameters.md)| The subscription creation parameters. | |

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
| **202** | Accepted. Subscription creation is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - GET this URL to retrieve the status of the asynchronous operation. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="subscriptionOperationsList"></a>
# **subscriptionOperationsList**
> SubscriptionOperationListResult subscriptionOperationsList(apiVersion)



Lists all of the available pending Microsoft.Subscription API operations.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      SubscriptionOperationListResult result = apiInstance.subscriptionOperationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#subscriptionOperationsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**SubscriptionOperationListResult**](SubscriptionOperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

