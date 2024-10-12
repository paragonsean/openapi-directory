# CreditsApi

All URIs are relative to *https://api.bulksms.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**creditTransferPost**](CreditsApi.md#creditTransferPost) | **POST** /credit/transfer | Transfer credits to another account |


<a id="creditTransferPost"></a>
# **creditTransferPost**
> creditTransferPost(transferEntry)

Transfer credits to another account

Before you can use the transfer credits endpoint, the _credit-transfer facility_ must be activated for your account.  You can request activation from &#x60;support@bulksms.com&#x60;.   The recipient must be an enabled account that uses the same currency as your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bulksms.com/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    CreditsApi apiInstance = new CreditsApi(defaultClient);
    TransferEntry transferEntry = new TransferEntry(); // TransferEntry | Contains details of the transfer request. 
    try {
      apiInstance.creditTransferPost(transferEntry);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditsApi#creditTransferPost");
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
| **transferEntry** | [**TransferEntry**](TransferEntry.md)| Contains details of the transfer request.  | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An empty body when the credits were transferred OK. |  -  |
| **400** | When the request fails validation checks. |  -  |
| **403** | When there are not enough credits in your account or the credit transfer facility is not activated. |  -  |

