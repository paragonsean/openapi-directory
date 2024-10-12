# OrderMarginRequirementsApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsAccountOrderImpactPost**](OrderMarginRequirementsApi.md#accountsAccountOrderImpactPost) | **POST** /accounts/{account}/order_impact | Return margin impact info |


<a id="accountsAccountOrderImpactPost"></a>
# **accountsAccountOrderImpactPost**
> AccountsAccountOrderImpactPost200Response accountsAccountOrderImpactPost(account, accountsAccountOrderImpactPostRequest)

Return margin impact info

This endpoint allows the consumer to check the impact that an order would have on the account, including margin, NLV and estimated commission costs. To specify the contract, you provide a value for the ContractId field, OR Ticker/ListingExchange/InstrumentType&#x3D;STK for stocks OR Ticker/Currency/InstrumentType&#x3D;CASH for FX. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderMarginRequirementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    OrderMarginRequirementsApi apiInstance = new OrderMarginRequirementsApi(defaultClient);
    String account = "account_example"; // String | Account Number
    AccountsAccountOrderImpactPostRequest accountsAccountOrderImpactPostRequest = new AccountsAccountOrderImpactPostRequest(); // AccountsAccountOrderImpactPostRequest | Order Parameters
    try {
      AccountsAccountOrderImpactPost200Response result = apiInstance.accountsAccountOrderImpactPost(account, accountsAccountOrderImpactPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderMarginRequirementsApi#accountsAccountOrderImpactPost");
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
| **account** | **String**| Account Number | |
| **accountsAccountOrderImpactPostRequest** | [**AccountsAccountOrderImpactPostRequest**](AccountsAccountOrderImpactPostRequest.md)| Order Parameters | |

### Return type

[**AccountsAccountOrderImpactPost200Response**](AccountsAccountOrderImpactPost200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order impact info |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

