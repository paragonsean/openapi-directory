# VerificationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVerificationStatus**](VerificationApi.md#getVerificationStatus) | **GET** /verification | Get Verification Status |
| [**initiateMatchingOrChallengeDepositeVerification**](VerificationApi.md#initiateMatchingOrChallengeDepositeVerification) | **POST** /verification | Initiaite Matching Service and Challenge Deposit |
| [**verifyChallengeDeposit**](VerificationApi.md#verifyChallengeDeposit) | **PUT** /verification | Verify Challenge Deposit |


<a id="getVerificationStatus"></a>
# **getVerificationStatus**
> VerificationStatusResponse getVerificationStatus(accountId, providerAccountId, verificationType)

Get Verification Status

The get verification status service is used to retrieve the verification status of all accounts for which the MS or CDV process has been initiated.&lt;br&gt;For the MS process, the account details object returns the aggregated information of the verified accounts. For the CDV process, the account details object returns the user provided account information.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    String accountId = "accountId_example"; // String | Comma separated accountId
    String providerAccountId = "providerAccountId_example"; // String | Comma separated providerAccountId
    String verificationType = "verificationType_example"; // String | verificationType
    try {
      VerificationStatusResponse result = apiInstance.getVerificationStatus(accountId, providerAccountId, verificationType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#getVerificationStatus");
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
| **accountId** | **String**| Comma separated accountId | [optional] |
| **providerAccountId** | **String**| Comma separated providerAccountId | [optional] |
| **verificationType** | **String**| verificationType | [optional] |

### Return type

[**VerificationStatusResponse**](VerificationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y901 : Service not supported&lt;br&gt;Y813 : Either of accountId or providerAccountId should be provided&lt;br&gt;Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for verification.verificationType&lt;br&gt;Y800 : Invalid value for providerAccountId&lt;br&gt;Y835 : Account(s) not eligible for Matching verification&lt;br&gt;Y836 : No verification initiated |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="initiateMatchingOrChallengeDepositeVerification"></a>
# **initiateMatchingOrChallengeDepositeVerification**
> VerificationResponse initiateMatchingOrChallengeDepositeVerification(verificationRequest)

Initiaite Matching Service and Challenge Deposit

The post verification service is used to initiate the matching service (MS) and the challenge deposit account verification (CDV) process to verify account ownership.&lt;br&gt;The MS and CDV process can verify ownership of only bank accounts (i.e., checking and savings).&lt;br&gt;The MS verification can be initiated only for an already aggregated account or a providerAccount.&lt;br&gt;The prerequisite for the MS verification process is to request the ACCT_PROFILE dataset with the HOLDER_NAME attribute.&lt;br&gt;In the MS verification process, a string-match of the account holder name with the registered user name is performed instantaneously. You can contact the Yodlee CustomerCare to configure the full name or only the last name match.&lt;br&gt;Once the CDV process is initiated Yodlee will post the microtransaction (i.e., credit and debit) in the user&#39;s account. The CDV process takes 2 to 3 days to complete as it requires the user to provide the microtransaction details.&lt;br&gt;The CDV process is currently supported only in the United States.&lt;br&gt;The verificationId in the response can be used to track the verification request.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;This endpoint cannot be used to test the CDV functionality in the developer sandbox or test environment. You will need a money transmitter license to implement the CDV functionality and also require the Yodlee Professional Services team&#39;s assistance to set up a dedicated environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    VerificationRequest verificationRequest = new VerificationRequest(); // VerificationRequest | verification information
    try {
      VerificationResponse result = apiInstance.initiateMatchingOrChallengeDepositeVerification(verificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#initiateMatchingOrChallengeDepositeVerification");
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
| **verificationRequest** | [**VerificationRequest**](VerificationRequest.md)| verification information | |

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y901 : Service not supported&lt;br&gt;Y812 : Required field/value - verification.verificationType missing in the verificationParam&lt;br&gt;Y812 : Required field/value - accountNumber missing in the verificationParam&lt;br&gt;Y812 : Required field/value - accountType missing in the verificationParam&lt;br&gt;Y812 : Required field/value - bankTransferCode missing in the verificationParam&lt;br&gt;Y812 : Required field/value - bankTransferCode.id missing in the verificationParam&lt;br&gt;Y812 : Required field/value - bankTransferCode.type missing in the verificationParam&lt;br&gt;Y800 : Invalid value for verification.verificationType&lt;br&gt;Y800 : Invalid value for verificationParam&lt;br&gt;Y800 : Invalid value for bankTransferCode.type&lt;br&gt;Y800 : Invalid value for bankTransferCode.id&lt;br&gt;Y800 : Invalid value for accountType&lt;br&gt;Y800 : Invalid value for accountId&lt;br&gt;Y813 : Account details should be provided&lt;br&gt;Y801 : Invalid length for accountNumber&lt;br&gt;Y835 : Account(s) not eligible for Challenge Deposit verification&lt;br&gt;Y806 : Invalid Input&lt;br&gt;Y840 : Verification has been initiated already&lt;br&gt;Y837 : Account has been verified already |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="verifyChallengeDeposit"></a>
# **verifyChallengeDeposit**
> VerificationResponse verifyChallengeDeposit(updateVerificationRequest)

Verify Challenge Deposit

The put verification service is used to complete the challenge deposit verification (CDV) process.&lt;br&gt;This service is used only by the customer of CDV flow.&lt;br&gt;In the CDV process, the user-provided microtransaction details (i.e., credit and debit) is matched against the microtransactions posted by Yodlee. For a successful verification of the account&#39;s ownership both the microtransaction details should match.&lt;br&gt;The CDV process is currently supported only in the United States.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;This endpoint cannot be used to test the CDV functionality in the developer sandbox or test environment. You will need a money transmitter license to implement the CDV functionality and also require the Yodlee Professional Services team&#39;s assistance to set up a dedicated environment.&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    UpdateVerificationRequest updateVerificationRequest = new UpdateVerificationRequest(); // UpdateVerificationRequest | verification information
    try {
      VerificationResponse result = apiInstance.verifyChallengeDeposit(updateVerificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#verifyChallengeDeposit");
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
| **updateVerificationRequest** | [**UpdateVerificationRequest**](UpdateVerificationRequest.md)| verification information | |

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y901 : Service not supported&lt;br&gt;Y812 : Required field/value - verification.verificationType missing in the verificationParam&lt;br&gt;Y812 : Required field/value - amount.amount missing in the verificationParam&lt;br&gt;Y812 : Required field/value - baseType missing in the verificationParam&lt;br&gt;Y812 : Required field/value - currency missing in the verificationParam&lt;br&gt;Y812 : Required field/value - providerAccountId missing in the verificationParam&lt;br&gt;Y812 : Required field/value - accountId missing in the verificationParam&lt;br&gt;Y800 : Invalid value for verificationParam&lt;br&gt;Y800 : Invalid value for verification.verificationType&lt;br&gt;Y800 : Invalid value for baseType&lt;br&gt;Y800 : Invalid value for providerAccountId&lt;br&gt;Y800 : Invalid value for accountId&lt;br&gt;Y813 : Transaction should be provided&lt;br&gt;Y801 : Invalid length for accountNumber&lt;br&gt;Y801 : Invalid length for amount&lt;br&gt;Y835 : Account(s) not eligible for Challenge Deposit verification&lt;br&gt;Y806 : Invalid Input&lt;br&gt;Y840 : Verification has been initiated already&lt;br&gt;Y837 : Account has been verified already&lt;br&gt;Y838 : The currency code provided does not match with the currency of the transaction executed on the target account&lt;br&gt;Y846 : The number of financial transactions made on the target account does not match with the number of transactions entered by the user.&lt;br&gt;Y842 : Number of retries exceeded the maximum Challenge Deposit verification limit&lt;br&gt;Y844 : Financial Instructions were not executed successfully on the target account&lt;br&gt;Y845 : Verification time expired. Please try initiating challenge deposit again&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

