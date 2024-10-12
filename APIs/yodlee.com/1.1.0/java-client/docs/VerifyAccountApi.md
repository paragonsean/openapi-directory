# VerifyAccountApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**initiateAccountVerification**](VerifyAccountApi.md#initiateAccountVerification) | **POST** /verifyAccount/{providerAccountId} | Verify Accounts Using Transactions |


<a id="initiateAccountVerification"></a>
# **initiateAccountVerification**
> VerifyAccountResponse initiateAccountVerification(providerAccountId, verifyAccountRequest)

Verify Accounts Using Transactions

The verify account service is used to verify the account&#39;s ownership by  matching the transaction details with the accounts aggregated for the user.&lt;br&gt;&lt;ul&gt;&lt;li&gt;If a match is identified, the service returns details of all the accounts along with the matched transaction&#39;s details.&lt;li&gt;If no transaction match is found, an empty response will be returned.&lt;li&gt;A maximum of 5 transactionCriteria can be passed in a request.&lt;li&gt;The baseType, date, and amount parameters should mandatorily be passed.&lt;li&gt;The optional dateVariance parameter cannot be more than 7 days. For example, +7, -4, or +/-2.&lt;li&gt;Pass the container or accountId parameters for better performance.&lt;li&gt;This service supports the localization feature and accepts locale as a header parameter.&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VerifyAccountApi apiInstance = new VerifyAccountApi(defaultClient);
    String providerAccountId = "providerAccountId_example"; // String | providerAccountId
    VerifyAccountRequest verifyAccountRequest = new VerifyAccountRequest(); // VerifyAccountRequest | verificationParam
    try {
      VerifyAccountResponse result = apiInstance.initiateAccountVerification(providerAccountId, verifyAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyAccountApi#initiateAccountVerification");
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
| **providerAccountId** | **String**| providerAccountId | |
| **verifyAccountRequest** | [**VerifyAccountRequest**](VerifyAccountRequest.md)| verificationParam | |

### Return type

[**VerifyAccountResponse**](VerifyAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for container&lt;br&gt;Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for amount&lt;br&gt;Y800 : Invalid value for dateVariance&lt;br&gt;Y801 : Invalid length for keyword&lt;br&gt;Y804 : Permitted values of dateVariance between 1 - 7&lt;br&gt;Y806 : Invalid input&lt;br&gt;Y807 : Resource not found&lt;br&gt;Y809 : Invalid date range&lt;br&gt;Y812 : Required field/value - transactionCriteria missing in the input&lt;br&gt;Y812 : Required field/value - amount missing in the transactionCriteria&lt;br&gt;Y812 : Required field/value - amount date in the transactionCriteria&lt;br&gt;Y812 : Required field/value - baseType missing in the transactionCriteria&lt;br&gt;Y823 : Transaction not applicable for container &lt;br&gt;Y824 : The maximum number of transactionCriteria permitted is 5&lt;br&gt;Y857 : Transactions are not refreshed in the past 24 hours&lt;br&gt;Y858 : Only active accounts can be verified&lt;br&gt;Y901 : Service not supported&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

