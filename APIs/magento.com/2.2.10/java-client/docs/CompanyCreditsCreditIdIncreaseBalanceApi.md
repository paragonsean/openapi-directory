# CompanyCreditsCreditIdIncreaseBalanceApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCreditCreditBalanceManagementV1IncreasePost**](CompanyCreditsCreditIdIncreaseBalanceApi.md#companyCreditCreditBalanceManagementV1IncreasePost) | **POST** /V1/companyCredits/{creditId}/increaseBalance | companyCredits/{creditId}/increaseBalance |


<a id="companyCreditCreditBalanceManagementV1IncreasePost"></a>
# **companyCreditCreditBalanceManagementV1IncreasePost**
> Boolean companyCreditCreditBalanceManagementV1IncreasePost(creditId, companyCreditCreditBalanceManagementV1DecreasePostRequest)

companyCredits/{creditId}/increaseBalance

Increases the company credit with an Allocate, Update, Refund, Revert, or Reimburse transaction. This transaction decreases company&#39;s outstanding balance and increases company&#39;s available credit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCreditsCreditIdIncreaseBalanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCreditsCreditIdIncreaseBalanceApi apiInstance = new CompanyCreditsCreditIdIncreaseBalanceApi(defaultClient);
    Integer creditId = 56; // Integer | 
    CompanyCreditCreditBalanceManagementV1DecreasePostRequest companyCreditCreditBalanceManagementV1DecreasePostRequest = new CompanyCreditCreditBalanceManagementV1DecreasePostRequest(); // CompanyCreditCreditBalanceManagementV1DecreasePostRequest | 
    try {
      Boolean result = apiInstance.companyCreditCreditBalanceManagementV1IncreasePost(creditId, companyCreditCreditBalanceManagementV1DecreasePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCreditsCreditIdIncreaseBalanceApi#companyCreditCreditBalanceManagementV1IncreasePost");
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
| **creditId** | **Integer**|  | |
| **companyCreditCreditBalanceManagementV1DecreasePostRequest** | [**CompanyCreditCreditBalanceManagementV1DecreasePostRequest**](CompanyCreditCreditBalanceManagementV1DecreasePostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

