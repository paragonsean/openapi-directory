# StatementCreditActivationDetailApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statementcreditactivationdetailGet**](StatementCreditActivationDetailApi.md#statementcreditactivationdetailGet) | **GET** /statementcreditactivationdetail | Returns Information About Redeemable Postpaid Credit Offer |


<a id="statementcreditactivationdetailGet"></a>
# **statementcreditactivationdetailGet**
> StatementCreditActivationResponse statementcreditactivationdetailGet(fid, userToken, activationId)

Returns Information About Redeemable Postpaid Credit Offer

This resource returns extended information about the specified activated postpaid credit offer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatementCreditActivationDetailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/plo/v1");

    StatementCreditActivationDetailApi apiInstance = new StatementCreditActivationDetailApi(defaultClient);
    String fid = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    String userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
    String activationId = "TRU_1000136"; // String | Distinct identifier for the offer being available for redemption by the user as returned by Activate Statement Credit Offer or Redeemed Offers, not intended for end-user display.
    try {
      StatementCreditActivationResponse result = apiInstance.statementcreditactivationdetailGet(fid, userToken, activationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatementCreditActivationDetailApi#statementcreditactivationdetailGet");
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
| **fid** | **String**| Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation. | |
| **userToken** | **String**| Session identifier as returned by the UserToken resource. | |
| **activationId** | **String**| Distinct identifier for the offer being available for redemption by the user as returned by Activate Statement Credit Offer or Redeemed Offers, not intended for end-user display. | |

### Return type

[**StatementCreditActivationResponse**](StatementCreditActivationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This resource returns extended information about the specified activated postpaid credit offer. |  -  |
| **0** | Unexpected error |  -  |

