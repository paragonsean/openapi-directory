# YodleeCoreApis.VerificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVerificationStatus**](VerificationApi.md#getVerificationStatus) | **GET** /verification | Get Verification Status
[**initiateMatchingOrChallengeDepositeVerification**](VerificationApi.md#initiateMatchingOrChallengeDepositeVerification) | **POST** /verification | Initiaite Matching Service and Challenge Deposit
[**verifyChallengeDeposit**](VerificationApi.md#verifyChallengeDeposit) | **PUT** /verification | Verify Challenge Deposit



## getVerificationStatus

> VerificationStatusResponse getVerificationStatus(opts)

Get Verification Status

The get verification status service is used to retrieve the verification status of all accounts for which the MS or CDV process has been initiated.&lt;br&gt;For the MS process, the account details object returns the aggregated information of the verified accounts. For the CDV process, the account details object returns the user provided account information.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.VerificationApi();
let opts = {
  'accountId': "accountId_example", // String | Comma separated accountId
  'providerAccountId': "providerAccountId_example", // String | Comma separated providerAccountId
  'verificationType': "verificationType_example" // String | verificationType
};
apiInstance.getVerificationStatus(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| Comma separated accountId | [optional] 
 **providerAccountId** | **String**| Comma separated providerAccountId | [optional] 
 **verificationType** | **String**| verificationType | [optional] 

### Return type

[**VerificationStatusResponse**](VerificationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## initiateMatchingOrChallengeDepositeVerification

> VerificationResponse initiateMatchingOrChallengeDepositeVerification(verificationRequest)

Initiaite Matching Service and Challenge Deposit

The post verification service is used to initiate the matching service (MS) and the challenge deposit account verification (CDV) process to verify account ownership.&lt;br&gt;The MS and CDV process can verify ownership of only bank accounts (i.e., checking and savings).&lt;br&gt;The MS verification can be initiated only for an already aggregated account or a providerAccount.&lt;br&gt;The prerequisite for the MS verification process is to request the ACCT_PROFILE dataset with the HOLDER_NAME attribute.&lt;br&gt;In the MS verification process, a string-match of the account holder name with the registered user name is performed instantaneously. You can contact the Yodlee CustomerCare to configure the full name or only the last name match.&lt;br&gt;Once the CDV process is initiated Yodlee will post the microtransaction (i.e., credit and debit) in the user&#39;s account. The CDV process takes 2 to 3 days to complete as it requires the user to provide the microtransaction details.&lt;br&gt;The CDV process is currently supported only in the United States.&lt;br&gt;The verificationId in the response can be used to track the verification request.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;This endpoint cannot be used to test the CDV functionality in the developer sandbox or test environment. You will need a money transmitter license to implement the CDV functionality and also require the Yodlee Professional Services team&#39;s assistance to set up a dedicated environment.

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.VerificationApi();
let verificationRequest = new YodleeCoreApis.VerificationRequest(); // VerificationRequest | verification information
apiInstance.initiateMatchingOrChallengeDepositeVerification(verificationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verificationRequest** | [**VerificationRequest**](VerificationRequest.md)| verification information | 

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## verifyChallengeDeposit

> VerificationResponse verifyChallengeDeposit(updateVerificationRequest)

Verify Challenge Deposit

The put verification service is used to complete the challenge deposit verification (CDV) process.&lt;br&gt;This service is used only by the customer of CDV flow.&lt;br&gt;In the CDV process, the user-provided microtransaction details (i.e., credit and debit) is matched against the microtransactions posted by Yodlee. For a successful verification of the account&#39;s ownership both the microtransaction details should match.&lt;br&gt;The CDV process is currently supported only in the United States.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;This endpoint cannot be used to test the CDV functionality in the developer sandbox or test environment. You will need a money transmitter license to implement the CDV functionality and also require the Yodlee Professional Services team&#39;s assistance to set up a dedicated environment.&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.VerificationApi();
let updateVerificationRequest = new YodleeCoreApis.UpdateVerificationRequest(); // UpdateVerificationRequest | verification information
apiInstance.verifyChallengeDeposit(updateVerificationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateVerificationRequest** | [**UpdateVerificationRequest**](UpdateVerificationRequest.md)| verification information | 

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8

