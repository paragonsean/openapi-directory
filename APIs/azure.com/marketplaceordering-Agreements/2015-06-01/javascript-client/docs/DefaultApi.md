# MarketplaceOrderingAgreements.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketplaceAgreementsCancel**](DefaultApi.md#marketplaceAgreementsCancel) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId}/cancel | 
[**marketplaceAgreementsCreate**](DefaultApi.md#marketplaceAgreementsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/offerTypes/{offerType}/publishers/{publisherId}/offers/{offerId}/plans/{planId}/agreements/current | 
[**marketplaceAgreementsGet**](DefaultApi.md#marketplaceAgreementsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/offerTypes/{offerType}/publishers/{publisherId}/offers/{offerId}/plans/{planId}/agreements/current | 
[**marketplaceAgreementsGetAgreement**](DefaultApi.md#marketplaceAgreementsGetAgreement) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId} | 
[**marketplaceAgreementsList**](DefaultApi.md#marketplaceAgreementsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements | 
[**marketplaceAgreementsSign**](DefaultApi.md#marketplaceAgreementsSign) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId}/sign | 



## marketplaceAgreementsCancel

> AgreementTerms marketplaceAgreementsCancel(apiVersion, subscriptionId, publisherId, offerId, planId)



Cancel marketplace terms.

### Example

```javascript
import MarketplaceOrderingAgreements from 'marketplace_ordering_agreements';
let defaultClient = MarketplaceOrderingAgreements.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketplaceOrderingAgreements.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
let offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
let planId = "planId_example"; // String | Plan identifier string of image being deployed.
apiInstance.marketplaceAgreementsCancel(apiVersion, subscriptionId, publisherId, offerId, planId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **publisherId** | **String**| Publisher identifier string of image being deployed. | 
 **offerId** | **String**| Offer identifier string of image being deployed. | 
 **planId** | **String**| Plan identifier string of image being deployed. | 

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketplaceAgreementsCreate

> AgreementTerms marketplaceAgreementsCreate(apiVersion, offerType, subscriptionId, publisherId, offerId, planId, parameters)



Save marketplace terms.

### Example

```javascript
import MarketplaceOrderingAgreements from 'marketplace_ordering_agreements';
let defaultClient = MarketplaceOrderingAgreements.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketplaceOrderingAgreements.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let offerType = "offerType_example"; // String | Offer Type, currently only virtualmachine type is supported.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
let offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
let planId = "planId_example"; // String | Plan identifier string of image being deployed.
let parameters = new MarketplaceOrderingAgreements.AgreementTerms(); // AgreementTerms | Parameters supplied to the Create Marketplace Terms operation.
apiInstance.marketplaceAgreementsCreate(apiVersion, offerType, subscriptionId, publisherId, offerId, planId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **offerType** | **String**| Offer Type, currently only virtualmachine type is supported. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **publisherId** | **String**| Publisher identifier string of image being deployed. | 
 **offerId** | **String**| Offer identifier string of image being deployed. | 
 **planId** | **String**| Plan identifier string of image being deployed. | 
 **parameters** | [**AgreementTerms**](AgreementTerms.md)| Parameters supplied to the Create Marketplace Terms operation. | 

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## marketplaceAgreementsGet

> AgreementTerms marketplaceAgreementsGet(apiVersion, subscriptionId, offerType, publisherId, offerId, planId)



Get marketplace terms.

### Example

```javascript
import MarketplaceOrderingAgreements from 'marketplace_ordering_agreements';
let defaultClient = MarketplaceOrderingAgreements.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketplaceOrderingAgreements.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let offerType = "offerType_example"; // String | Offer Type, currently only virtualmachine type is supported.
let publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
let offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
let planId = "planId_example"; // String | Plan identifier string of image being deployed.
apiInstance.marketplaceAgreementsGet(apiVersion, subscriptionId, offerType, publisherId, offerId, planId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **offerType** | **String**| Offer Type, currently only virtualmachine type is supported. | 
 **publisherId** | **String**| Publisher identifier string of image being deployed. | 
 **offerId** | **String**| Offer identifier string of image being deployed. | 
 **planId** | **String**| Plan identifier string of image being deployed. | 

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketplaceAgreementsGetAgreement

> AgreementTerms marketplaceAgreementsGetAgreement(apiVersion, subscriptionId, publisherId, offerId, planId)



Get marketplace agreement.

### Example

```javascript
import MarketplaceOrderingAgreements from 'marketplace_ordering_agreements';
let defaultClient = MarketplaceOrderingAgreements.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketplaceOrderingAgreements.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
let offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
let planId = "planId_example"; // String | Plan identifier string of image being deployed.
apiInstance.marketplaceAgreementsGetAgreement(apiVersion, subscriptionId, publisherId, offerId, planId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **publisherId** | **String**| Publisher identifier string of image being deployed. | 
 **offerId** | **String**| Offer identifier string of image being deployed. | 
 **planId** | **String**| Plan identifier string of image being deployed. | 

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketplaceAgreementsList

> [AgreementTerms] marketplaceAgreementsList(apiVersion, subscriptionId)



List marketplace agreements in the subscription.

### Example

```javascript
import MarketplaceOrderingAgreements from 'marketplace_ordering_agreements';
let defaultClient = MarketplaceOrderingAgreements.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketplaceOrderingAgreements.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
apiInstance.marketplaceAgreementsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 

### Return type

[**[AgreementTerms]**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketplaceAgreementsSign

> AgreementTerms marketplaceAgreementsSign(apiVersion, subscriptionId, publisherId, offerId, planId)



Sign marketplace terms.

### Example

```javascript
import MarketplaceOrderingAgreements from 'marketplace_ordering_agreements';
let defaultClient = MarketplaceOrderingAgreements.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketplaceOrderingAgreements.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
let offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
let planId = "planId_example"; // String | Plan identifier string of image being deployed.
apiInstance.marketplaceAgreementsSign(apiVersion, subscriptionId, publisherId, offerId, planId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **publisherId** | **String**| Publisher identifier string of image being deployed. | 
 **offerId** | **String**| Offer identifier string of image being deployed. | 
 **planId** | **String**| Plan identifier string of image being deployed. | 

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

