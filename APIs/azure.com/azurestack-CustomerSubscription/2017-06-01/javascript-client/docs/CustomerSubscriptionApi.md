# AzureStackAzureBridgeClient.CustomerSubscriptionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerSubscriptionsCreate**](CustomerSubscriptionApi.md#customerSubscriptionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/customerSubscriptions/{customerSubscriptionName} | 
[**customerSubscriptionsDelete**](CustomerSubscriptionApi.md#customerSubscriptionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/customerSubscriptions/{customerSubscriptionName} | 
[**customerSubscriptionsGet**](CustomerSubscriptionApi.md#customerSubscriptionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/customerSubscriptions/{customerSubscriptionName} | 
[**customerSubscriptionsList**](CustomerSubscriptionApi.md#customerSubscriptionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/customerSubscriptions | 



## customerSubscriptionsCreate

> CustomerSubscription customerSubscriptionsCreate(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion, customerCreationParameters)



Creates a new customer subscription under a registration.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.CustomerSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let customerSubscriptionName = "customerSubscriptionName_example"; // String | Name of the product.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
let customerCreationParameters = new AzureStackAzureBridgeClient.CustomerSubscription(); // CustomerSubscription | Parameters use to create a customer subscription.
apiInstance.customerSubscriptionsCreate(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion, customerCreationParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **customerSubscriptionName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]
 **customerCreationParameters** | [**CustomerSubscription**](CustomerSubscription.md)| Parameters use to create a customer subscription. | 

### Return type

[**CustomerSubscription**](CustomerSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerSubscriptionsDelete

> customerSubscriptionsDelete(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion)



Deletes a customer subscription under a registration.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.CustomerSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let customerSubscriptionName = "customerSubscriptionName_example"; // String | Name of the product.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.customerSubscriptionsDelete(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **customerSubscriptionName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## customerSubscriptionsGet

> CustomerSubscription customerSubscriptionsGet(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion)



Returns the specified product.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.CustomerSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let customerSubscriptionName = "customerSubscriptionName_example"; // String | Name of the product.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.customerSubscriptionsGet(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **customerSubscriptionName** | **String**| Name of the product. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**CustomerSubscription**](CustomerSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerSubscriptionsList

> CustomerSubscriptionList customerSubscriptionsList(subscriptionId, resourceGroup, registrationName, apiVersion)



Returns a list of products.

### Example

```javascript
import AzureStackAzureBridgeClient from 'azure_stack_azure_bridge_client';
let defaultClient = AzureStackAzureBridgeClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureStackAzureBridgeClient.CustomerSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
let registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
let apiVersion = "'2017-06-01'"; // String | Client API Version.
apiInstance.customerSubscriptionsList(subscriptionId, resourceGroup, registrationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| Name of the resource group. | 
 **registrationName** | **String**| Name of the Azure Stack registration. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2017-06-01&#39;]

### Return type

[**CustomerSubscriptionList**](CustomerSubscriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

