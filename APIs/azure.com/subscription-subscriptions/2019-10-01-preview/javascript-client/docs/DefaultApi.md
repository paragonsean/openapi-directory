# SubscriptionClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Subscription/operations | 
[**subscriptionCancel**](DefaultApi.md#subscriptionCancel) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/cancel | 
[**subscriptionCreateCspSubscription**](DefaultApi.md#subscriptionCreateCspSubscription) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/providers/Microsoft.Subscription/createSubscription | 
[**subscriptionCreateSubscription**](DefaultApi.md#subscriptionCreateSubscription) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Subscription/createSubscription | 
[**subscriptionCreateSubscriptionInEnrollmentAccount**](DefaultApi.md#subscriptionCreateSubscriptionInEnrollmentAccount) | **POST** /providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountName}/providers/Microsoft.Subscription/createSubscription | 
[**subscriptionEnable**](DefaultApi.md#subscriptionEnable) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/enable | 
[**subscriptionOperationGet**](DefaultApi.md#subscriptionOperationGet) | **GET** /providers/Microsoft.Subscription/subscriptionOperations/{operationId} | 
[**subscriptionRename**](DefaultApi.md#subscriptionRename) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Subscription/rename | 



## operationsList

> OperationListResult operationsList(apiVersion)



Lists all of the available Microsoft.Subscription API operations.

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionCancel

> CanceledSubscriptionId subscriptionCancel(subscriptionId, apiVersion)



The operation to cancel a subscription

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
apiInstance.subscriptionCancel(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | 

### Return type

[**CanceledSubscriptionId**](CanceledSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionCreateCspSubscription

> SubscriptionCreationResult subscriptionCreateCspSubscription(billingAccountName, customerName, apiVersion, body)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
let body = new SubscriptionClient.ModernCspSubscriptionCreationParameters(); // ModernCspSubscriptionCreationParameters | The subscription creation parameters.
apiInstance.subscriptionCreateCspSubscription(billingAccountName, customerName, apiVersion, body, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | 
 **body** | [**ModernCspSubscriptionCreationParameters**](ModernCspSubscriptionCreationParameters.md)| The subscription creation parameters. | 

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionCreateSubscription

> SubscriptionCreationResult subscriptionCreateSubscription(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, body)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
let body = new SubscriptionClient.ModernSubscriptionCreationParameters(); // ModernSubscriptionCreationParameters | The subscription creation parameters.
apiInstance.subscriptionCreateSubscription(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, body, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | 
 **body** | [**ModernSubscriptionCreationParameters**](ModernSubscriptionCreationParameters.md)| The subscription creation parameters. | 

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionCreateSubscriptionInEnrollmentAccount

> SubscriptionCreationResult subscriptionCreateSubscriptionInEnrollmentAccount(enrollmentAccountName, apiVersion, body)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
let body = new SubscriptionClient.SubscriptionCreationParameters(); // SubscriptionCreationParameters | The subscription creation parameters.
apiInstance.subscriptionCreateSubscriptionInEnrollmentAccount(enrollmentAccountName, apiVersion, body, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | 
 **body** | [**SubscriptionCreationParameters**](SubscriptionCreationParameters.md)| The subscription creation parameters. | 

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionEnable

> EnabledSubscriptionId subscriptionEnable(subscriptionId, apiVersion)



The operation to enable a subscription

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
apiInstance.subscriptionEnable(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | 

### Return type

[**EnabledSubscriptionId**](EnabledSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | 

### Return type

[**SubscriptionCreationResult**](SubscriptionCreationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionRename

> RenamedSubscriptionId subscriptionRename(subscriptionId, apiVersion, body)



The operation to rename a subscription

### Example

```javascript
import SubscriptionClient from 'subscription_client';
let defaultClient = SubscriptionClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2019-10-01-preview
let body = new SubscriptionClient.SubscriptionName(); // SubscriptionName | Subscription Name
apiInstance.subscriptionRename(subscriptionId, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2019-10-01-preview | 
 **body** | [**SubscriptionName**](SubscriptionName.md)| Subscription Name | 

### Return type

[**RenamedSubscriptionId**](RenamedSubscriptionId.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

