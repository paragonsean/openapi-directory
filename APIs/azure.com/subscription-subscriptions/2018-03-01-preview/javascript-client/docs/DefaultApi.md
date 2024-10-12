# SubscriptionClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionFactoryCreateSubscriptionInEnrollmentAccount**](DefaultApi.md#subscriptionFactoryCreateSubscriptionInEnrollmentAccount) | **POST** /providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountName}/providers/Microsoft.Subscription/createSubscription | 
[**subscriptionOperationsList**](DefaultApi.md#subscriptionOperationsList) | **GET** /providers/Microsoft.Subscription/subscriptionOperations | 



## subscriptionFactoryCreateSubscriptionInEnrollmentAccount

> SubscriptionCreationResult subscriptionFactoryCreateSubscriptionInEnrollmentAccount(enrollmentAccountName, apiVersion, body)



Creates an Azure subscription

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let enrollmentAccountName = "enrollmentAccountName_example"; // String | The name of the enrollment account to which the subscription will be billed.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
let body = new SubscriptionClient.SubscriptionCreationParameters(); // SubscriptionCreationParameters | The subscription creation parameters.
apiInstance.subscriptionFactoryCreateSubscriptionInEnrollmentAccount(enrollmentAccountName, apiVersion, body, (error, data, response) => {
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
 **enrollmentAccountName** | **String**| The name of the enrollment account to which the subscription will be billed. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | 
 **body** | [**SubscriptionCreationParameters**](SubscriptionCreationParameters.md)| The subscription creation parameters. | 

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionOperationsList

> SubscriptionOperationListResult subscriptionOperationsList(apiVersion)



Lists all of the available pending Microsoft.Subscription API operations.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
apiInstance.subscriptionOperationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | 

### Return type

[**SubscriptionOperationListResult**](SubscriptionOperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

