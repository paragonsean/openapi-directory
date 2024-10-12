# SubscriptionsManagementClient.OfferDelegationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offerDelegationsCreateOrUpdate**](OfferDelegationsApi.md#offerDelegationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offerDelegationName} | 
[**offerDelegationsDelete**](OfferDelegationsApi.md#offerDelegationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offerDelegationName} | 
[**offerDelegationsGet**](OfferDelegationsApi.md#offerDelegationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offerDelegationName} | 
[**offerDelegationsList**](OfferDelegationsApi.md#offerDelegationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations | 



## offerDelegationsCreateOrUpdate

> OfferDelegation offerDelegationsCreateOrUpdate(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion, newOfferDelegation)



Create or update the offer delegation.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.OfferDelegationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let offer = "offer_example"; // String | Name of an offer.
let offerDelegationName = "offerDelegationName_example"; // String | Name of a offer delegation.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
let newOfferDelegation = new SubscriptionsManagementClient.OfferDelegation(); // OfferDelegation | New offer delegation parameter.
apiInstance.offerDelegationsCreateOrUpdate(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion, newOfferDelegation, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **offer** | **String**| Name of an offer. | 
 **offerDelegationName** | **String**| Name of a offer delegation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]
 **newOfferDelegation** | [**OfferDelegation**](OfferDelegation.md)| New offer delegation parameter. | 

### Return type

[**OfferDelegation**](OfferDelegation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offerDelegationsDelete

> offerDelegationsDelete(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion)



Delete the specified offer delegation.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.OfferDelegationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let offer = "offer_example"; // String | Name of an offer.
let offerDelegationName = "offerDelegationName_example"; // String | Name of a offer delegation.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.offerDelegationsDelete(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **offer** | **String**| Name of an offer. | 
 **offerDelegationName** | **String**| Name of a offer delegation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## offerDelegationsGet

> OfferDelegation offerDelegationsGet(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion)



Get the specified offer delegation.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.OfferDelegationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let offer = "offer_example"; // String | Name of an offer.
let offerDelegationName = "offerDelegationName_example"; // String | Name of a offer delegation.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.offerDelegationsGet(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **offer** | **String**| Name of an offer. | 
 **offerDelegationName** | **String**| Name of a offer delegation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**OfferDelegation**](OfferDelegation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offerDelegationsList

> OfferDelegationList offerDelegationsList(subscriptionId, resourceGroupName, offer, apiVersion)



Get the list of offer delegations.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.OfferDelegationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let offer = "offer_example"; // String | Name of an offer.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.offerDelegationsList(subscriptionId, resourceGroupName, offer, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **offer** | **String**| Name of an offer. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**OfferDelegationList**](OfferDelegationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

