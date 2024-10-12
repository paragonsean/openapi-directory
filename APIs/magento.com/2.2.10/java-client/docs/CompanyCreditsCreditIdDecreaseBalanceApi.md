# CompanyCreditsCreditIdDecreaseBalanceApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCreditCreditBalanceManagementV1DecreasePost**](CompanyCreditsCreditIdDecreaseBalanceApi.md#companyCreditCreditBalanceManagementV1DecreasePost) | **POST** /V1/companyCredits/{creditId}/decreaseBalance | companyCredits/{creditId}/decreaseBalance |


<a id="companyCreditCreditBalanceManagementV1DecreasePost"></a>
# **companyCreditCreditBalanceManagementV1DecreasePost**
> Boolean companyCreditCreditBalanceManagementV1DecreasePost(creditId, companyCreditCreditBalanceManagementV1DecreasePostRequest)

companyCredits/{creditId}/decreaseBalance

Decreases the company credit with an Update, Reimburse, or Purchase transaction. This transaction increases company&#39;s outstanding balance and decreases company&#39;s available credit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCreditsCreditIdDecreaseBalanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCreditsCreditIdDecreaseBalanceApi apiInstance = new CompanyCreditsCreditIdDecreaseBalanceApi(defaultClient);
    Integer creditId = 56; // Integer | 
    CompanyCreditCreditBalanceManagementV1DecreasePostRequest companyCreditCreditBalanceManagementV1DecreasePostRequest = new CompanyCreditCreditBalanceManagementV1DecreasePostRequest(); // CompanyCreditCreditBalanceManagementV1DecreasePostRequest | 
    try {
      Boolean result = apiInstance.companyCreditCreditBalanceManagementV1DecreasePost(creditId, companyCreditCreditBalanceManagementV1DecreasePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCreditsCreditIdDecreaseBalanceApi#companyCreditCreditBalanceManagementV1DecreasePost");
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

