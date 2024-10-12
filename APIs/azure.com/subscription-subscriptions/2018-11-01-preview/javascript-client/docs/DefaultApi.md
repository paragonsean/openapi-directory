# SubscriptionClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionFactoryCreateCspSubscription**](DefaultApi.md#subscriptionFactoryCreateCspSubscription) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/providers/Microsoft.Subscription/createSubscription | 
[**subscriptionFactoryCreateSubscription**](DefaultApi.md#subscriptionFactoryCreateSubscription) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Subscription/createSubscription | 
[**subscriptionOperationGet**](DefaultApi.md#subscriptionOperationGet) | **GET** /providers/Microsoft.Subscription/subscriptionOperations/{operationId} | 



## subscriptionFactoryCreateCspSubscription

> SubscriptionCreationResult subscriptionFactoryCreateCspSubscription(billingAccountName, customerName, apiVersion, body)



The operation to create a new CSP subscription.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let billingAccountName = "billingAccountName_example"; // String | The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.
let customerName = "customerName_example"; // String | The name of the customer.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2018-11-01-preview
let body = new SubscriptionClient.ModernCspSubscriptionCreationParameters(); // ModernCspSubscriptionCreationParameters | The subscription creation parameters.
apiInstance.subscriptionFactoryCreateCspSubscription(billingAccountName, customerName, apiVersion, body, (error, data, response) => {
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
 **billingAccountName** | **String**| The name of the Microsoft Customer Agreement billing account for which you want to create the subscription. | 
 **customerName** | **String**| The name of the customer. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2018-11-01-preview | 
 **body** | [**ModernCspSubscriptionCreationParameters**](ModernCspSubscriptionCreationParameters.md)| The subscription creation parameters. | 

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionFactoryCreateSubscription

> SubscriptionCreationResult subscriptionFactoryCreateSubscription(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, body)



The operation to create a new WebDirect or EA Azure subscription.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let billingAccountName = "billingAccountName_example"; // String | The name of the Microsoft Customer Agreement billing account for which you want to create the subscription.
let billingProfileName = "billingProfileName_example"; // String | The name of the billing profile in the billing account for which you want to create the subscription.
let invoiceSectionName = "invoiceSectionName_example"; // String | The name of the invoice section in the billing account for which you want to create the subscription.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2018-11-01-preview
let body = new SubscriptionClient.ModernSubscriptionCreationParameters(); // ModernSubscriptionCreationParameters | The subscription creation parameters.
apiInstance.subscriptionFactoryCreateSubscription(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, body, (error, data, response) => {
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
 **billingAccountName** | **String**| The name of the Microsoft Customer Agreement billing account for which you want to create the subscription. | 
 **billingProfileName** | **String**| The name of the billing profile in the billing account for which you want to create the subscription. | 
 **invoiceSectionName** | **String**| The name of the invoice section in the billing account for which you want to create the subscription. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2018-11-01-preview | 
 **body** | [**ModernSubscriptionCreationParameters**](ModernSubscriptionCreationParameters.md)| The subscription creation parameters. | 

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionOperationGet

> SubscriptionCreationResult subscriptionOperationGet(operationId, apiVersion)



Get the status of the pending Microsoft.Subscription API operations.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let operationId = "operationId_example"; // String | The operation ID, which can be found from the Location field in the generate recommendation response header.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2018-11-01-preview
apiInstance.subscriptionOperationGet(operationId, apiVersion, (error, data, response) => {
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
 **operationId** | **String**| The operation ID, which can be found from the Location field in the generate recommendation response header. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2018-11-01-preview | 

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

