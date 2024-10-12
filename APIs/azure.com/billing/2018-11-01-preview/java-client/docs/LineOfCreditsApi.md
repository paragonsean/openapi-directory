# LineOfCreditsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lineOfCreditsGet**](LineOfCreditsApi.md#lineOfCreditsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Billing/billingAccounts/default/lineOfCredit/default |  |
| [**lineOfCreditsUpdate**](LineOfCreditsApi.md#lineOfCreditsUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Billing/billingAccounts/default/lineOfCredit/default |  |


<a id="lineOfCreditsGet"></a>
# **lineOfCreditsGet**
> LineOfCredit lineOfCreditsGet(apiVersion, subscriptionId)



Get the current line of credit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineOfCreditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LineOfCreditsApi apiInstance = new LineOfCreditsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id.
    try {
      LineOfCredit result = apiInstance.lineOfCreditsGet(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineOfCreditsApi#lineOfCreditsGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription Id. | |

### Return type

[**LineOfCredit**](LineOfCredit.md)

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

<a id="lineOfCreditsUpdate"></a>
# **lineOfCreditsUpdate**
> LineOfCredit lineOfCreditsUpdate(apiVersion, subscriptionId, parameters)



Increase the current line of credit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineOfCreditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LineOfCreditsApi apiInstance = new LineOfCreditsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id.
    LineOfCredit parameters = new LineOfCredit(); // LineOfCredit | Parameters supplied to the increase line of credit operation.
    try {
      LineOfCredit result = apiInstance.lineOfCreditsUpdate(apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineOfCreditsApi#lineOfCreditsUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **subscriptionId** | **String**| Azure Subscription Id. | |
| **parameters** | [**LineOfCredit**](LineOfCredit.md)| Parameters supplied to the increase line of credit operation. | |

### Return type

[**LineOfCredit**](LineOfCredit.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. Line of credit increase is in progress. |  * Retry-After - Recommends the retryable time after receiving this. <br>  * Azure-AsyncOperation - URI to poll for the operation status <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

