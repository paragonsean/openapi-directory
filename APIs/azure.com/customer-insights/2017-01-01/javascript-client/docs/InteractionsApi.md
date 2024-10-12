# CustomerInsightsManagementClient.InteractionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**interactionsCreateOrUpdate**](InteractionsApi.md#interactionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/interactions/{interactionName} | 
[**interactionsGet**](InteractionsApi.md#interactionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/interactions/{interactionName} | 
[**interactionsListByHub**](InteractionsApi.md#interactionsListByHub) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/interactions | 
[**interactionsSuggestRelationshipLinks**](InteractionsApi.md#interactionsSuggestRelationshipLinks) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/interactions/{interactionName}/suggestRelationshipLinks | 



## interactionsCreateOrUpdate

> InteractionResourceFormat interactionsCreateOrUpdate(resourceGroupName, hubName, interactionName, apiVersion, subscriptionId, parameters)



Creates an interaction or updates an existing interaction within a hub.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.InteractionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let interactionName = "interactionName_example"; // String | The name of the interaction.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new CustomerInsightsManagementClient.InteractionResourceFormat(); // InteractionResourceFormat | Parameters supplied to the CreateOrUpdate Interaction operation.
apiInstance.interactionsCreateOrUpdate(resourceGroupName, hubName, interactionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **interactionName** | **String**| The name of the interaction. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**InteractionResourceFormat**](InteractionResourceFormat.md)| Parameters supplied to the CreateOrUpdate Interaction operation. | 

### Return type

[**InteractionResourceFormat**](InteractionResourceFormat.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## interactionsGet

> InteractionResourceFormat interactionsGet(resourceGroupName, hubName, interactionName, apiVersion, subscriptionId, opts)



Gets information about the specified interaction.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.InteractionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let interactionName = "interactionName_example"; // String | The name of the interaction.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'localeCode': "'en-us'" // String | Locale of interaction to retrieve, default is en-us.
};
apiInstance.interactionsGet(resourceGroupName, hubName, interactionName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **interactionName** | **String**| The name of the interaction. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **localeCode** | **String**| Locale of interaction to retrieve, default is en-us. | [optional] [default to &#39;en-us&#39;]

### Return type

[**InteractionResourceFormat**](InteractionResourceFormat.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## interactionsListByHub

> InteractionListResult interactionsListByHub(resourceGroupName, hubName, apiVersion, subscriptionId, opts)



Gets all interactions in the hub.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.InteractionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'localeCode': "'en-us'" // String | Locale of interaction to retrieve, default is en-us.
};
apiInstance.interactionsListByHub(resourceGroupName, hubName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **localeCode** | **String**| Locale of interaction to retrieve, default is en-us. | [optional] [default to &#39;en-us&#39;]

### Return type

[**InteractionListResult**](InteractionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## interactionsSuggestRelationshipLinks

> SuggestRelationshipLinksResponse interactionsSuggestRelationshipLinks(resourceGroupName, hubName, interactionName, apiVersion, subscriptionId)



Suggests relationships to create relationship links.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.InteractionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let interactionName = "interactionName_example"; // String | The name of the interaction.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.interactionsSuggestRelationshipLinks(resourceGroupName, hubName, interactionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **interactionName** | **String**| The name of the interaction. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SuggestRelationshipLinksResponse**](SuggestRelationshipLinksResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

