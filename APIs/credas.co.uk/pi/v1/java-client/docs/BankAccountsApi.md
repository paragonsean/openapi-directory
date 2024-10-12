# BankAccountsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**verify**](BankAccountsApi.md#verify) | **POST** /api/bank-accounts/verify | Verifies bank account details. |


<a id="verify"></a>
# **verify**
> CredasApiModelsBankAccountsAccountVerificationResponse verify(apikey, credasApiModelsBankAccountsAccountVerificationRequest)

Verifies bank account details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    BankAccountsApi apiInstance = new BankAccountsApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsBankAccountsAccountVerificationRequest credasApiModelsBankAccountsAccountVerificationRequest = new CredasApiModelsBankAccountsAccountVerificationRequest(); // CredasApiModelsBankAccountsAccountVerificationRequest | Object containing data required to perform bank account verification.
    try {
      CredasApiModelsBankAccountsAccountVerificationResponse result = apiInstance.verify(apikey, credasApiModelsBankAccountsAccountVerificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BankAccountsApi#verify");
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
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsBankAccountsAccountVerificationRequest** | [**CredasApiModelsBankAccountsAccountVerificationRequest**](CredasApiModelsBankAccountsAccountVerificationRequest.md)| Object containing data required to perform bank account verification. | [optional] |

### Return type

[**CredasApiModelsBankAccountsAccountVerificationResponse**](CredasApiModelsBankAccountsAccountVerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **402** | Error code meaning that the operation was aborted due to insufficient credits. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

